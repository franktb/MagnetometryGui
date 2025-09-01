import sys
import os
import time
import util
import multiprocessing
from multiprocessing import Queue

import contextily as cx
import pandas as pd
import numpy as np

from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIntValidator
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.colors as colors
from matplotlib.colors import TwoSlopeNorm
from skimage import feature, measure



from figure_wrapper import SlippyMapNavigationToolbar
from TreeWidget import TreeUtil
from fft_window import FFTWindow
from file_io.tiff_io import WriteMag, Bathymetry
from file_io.txt_io import WriteMagCSV, ReadMagCSV
from timeseries_window import TimeSeriesWindow
from ui_elements.ui_main_window import Ui_MainWindow
from util.data_manipulation import DataManipulator
from util.gridding import grid
from util.filter import running_mean_uniform_filter1d, sobel
from ui_elements.dialogs import *
from util.time_series_module import TimeSeriesManipulator
from window_manager import WindowManager
from worker import Worker, PWorker



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.project = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionNew_Project.triggered.connect(self.create_new_project)
        self.ui.actionFrom_BOB_CSV.triggered.connect(self.select_BOB_CSV)
        self.ui.actionFrom_Sealink_Folder.triggered.connect(self.select_SeaLINKFolder)
        self.ui.actionFrom_Custom_CSV.triggered.connect(self.select_custom_CSV)
        self.ui.actionDraw1D.triggered.connect(self.wrapper_1d_selected)



        self.ui.actionDrawSelect.triggered.connect(self.draw_selection)
        self.ui.actionRemoveOutlier.triggered.connect(self.remove_outlier)

        self.ui.actioncalcResiduals.triggered.connect(self.calc_residuals)

        self.ui.actionCSV.triggered.connect(self.write_to_csv)

        self.ui.actionGeoTiff.triggered.connect(self.write_to_geotiff)

        self.ui.action_spawn_FFTWindow.triggered.connect(self.spawn_fft_window)
        self.ui.action_spawn_TimeSeriesWindow.triggered.connect(self.spawn_timeseries_window)

        self.ui.actionanomalyDetection.triggered.connect(self.detect_anomalies)

        self.mapping_2D_canvas = FigureCanvas(Figure())
        self.mapping_2D_canvas.setFocusPolicy(Qt.StrongFocus)
        self.mapping_2D_canvas.setFocus()
        # self.mapping_2D_canvas = MplCanvas(self, 5,3,150)

        self.ui.verticalLayout2DMappingCanvas.addWidget(SlippyMapNavigationToolbar(self.mapping_2D_canvas, self, ))
        self.ui.verticalLayout2DMappingCanvas.addWidget(self.mapping_2D_canvas)
        self.mapping_2D_ax = self.mapping_2D_canvas.figure.subplots()
        self.cbar = None
        self.contourfplot = None

        self.time_series_canvas = FigureCanvas(Figure())
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(NavigationToolbar(self.time_series_canvas))
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(self.time_series_canvas)
        self.time_series_ax = self.time_series_canvas.figure.subplots()

        self.time_series_canvas_res = FigureCanvas(Figure())
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(NavigationToolbar(self.time_series_canvas_res))
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(self.time_series_canvas_res)
        self.time_series_ax_res = self.time_series_canvas_res.figure.subplots()



        self.ui.comboBox_Scale_type.currentIndexChanged.connect(self.update_scale)
        self.color_scale_type = self.ui.comboBox_Scale_type.currentText()

        # self.ui.pushButton.clicked.connect(self.debugTree)

        # self.TreeUtil = TreeUtil(self.ui.treeWidget)

        self.selected_df = pd.DataFrame()
        self.TreeUtil = TreeUtil(self.ui.treeWidget, self.selected_df)
        self.ui.treeWidget.setEditTriggers(QTreeWidget.DoubleClicked | QTreeWidget.SelectedClicked)
        self.ui.treeWidget.itemChanged[QTreeWidgetItem, int].connect(self.update_selected_df)

        self.ui.actionExport_Survey.triggered.connect(self.TreeUtil.write_surveys_to_csv)

        firstlayer = QListWidgetItem("Context map")
        firstlayer.setCheckState(Qt.Checked)
        self.ui.layerWidget.addItem(firstlayer)

        secondlayer = QListWidgetItem("Anomaly map")
        secondlayer.setCheckState(Qt.Checked)
        self.ui.layerWidget.addItem(secondlayer)

        thirdlayer = QListWidgetItem("Anomaly annotation")
        thirdlayer.setCheckState(Qt.Unchecked)
        self.ui.layerWidget.addItem(thirdlayer)

        forthlayer = QListWidgetItem("Track Lines")
        forthlayer.setCheckState(Qt.Checked)
        self.ui.layerWidget.addItem(forthlayer)

        fifthlayer = QListWidgetItem("Clip region")
        fifthlayer.setCheckState(Qt.Checked)
        self.ui.layerWidget.addItem(fifthlayer)

        self.ui.layerWidget.itemChanged.connect(self.layer_update)

        self.data_manipulator = DataManipulator()
        self.data_coordinates = None
        self.track_lines = None

        self.validator_smooth = QIntValidator(0, 100000, self)
        self.ui.lineEdit_smoothingWindow.setValidator(self.validator_smooth)
        self.validator_ambient = QIntValidator(0, 1000000, self)
        self.ui.lineEdit_ambientWindow.setValidator(self.validator_ambient)

        self.validator_easting = QIntValidator(0, 5000, self)
        self.validator_northing = QIntValidator(0, 5000, self)
        self.ui.lineEdit_eastingsSampleRate.setValidator(self.validator_easting)
        self.ui.lineEdit_northingsSampleRate.setValidator(self.validator_northing)

        self.validator_nthSelect = QIntValidator(0, 10000, self)
        self.ui.lineEdit_nthSelectWindow.setValidator(self.validator_nthSelect)

        self.smoothing_window_length = int(self.ui.lineEdit_smoothingWindow.text())
        self.ambient_window_length = int(self.ui.lineEdit_ambientWindow.text())
        self.eastingsSampleRate = int(self.ui.lineEdit_eastingsSampleRate.text())
        self.northingsSampleRate = int(self.ui.lineEdit_northingsSampleRate.text())

        self.ui.lineEdit_ambientWindow.textEdited.connect(self.ambient_lineEdit_change)
        self.ui.lineEdit_smoothingWindow.textEdited.connect(self.smoothing_lineEdit_change)

        self.ui.lineEdit_northingsSampleRate.textEdited.connect(self.northings_lineEdit_change)
        self.ui.lineEdit_eastingsSampleRate.textEdited.connect(self.eastings_lineEdit_change)

        self.readCSV = ReadMagCSV()
        self.writeCSV = WriteMagCSV()
        self.writeTif = WriteMag()

        self.bath_IO = Bathymetry()
        # self.ui.treeWidget.setHeaderHidden(True)
        self.threadpool = QThreadPool()

        self.grid_queue = Queue()


    def spawn_fft_window(self):
        WindowManager.open_or_focus_window(self,
                                           "fft_window",
                                           FFTWindow,
                                           self.ui.action_spawn_FFTWindow)

    def spawn_timeseries_window(self):
        WindowManager.open_or_focus_window(self,
                                           "time_series_window",
                                           TimeSeriesWindow,
                                           self.ui.action_spawn_TimeSeriesWindow)

    def update_scale(self):
        self.color_scale_type = self.ui.comboBox_Scale_type.currentText()
        if self.grid_x is not None:
            self.update_plot()


    def detect_anomalies(self):
        print("I am here")
        magnitude = sobel(self.grid_z)
        threshold = np.percentile(magnitude, 98)  # or fixed value
        mask = magnitude >= threshold

        print(mask)
        # Step 4: Get coordinates
        y_indices, x_indices = np.where(mask)
        # magnitudes_filtered = magnitude[mask]

        x_coords = self.grid_x[y_indices, x_indices]
        y_coords = self.grid_y[y_indices, x_indices]
        self.anomalies = self.mapping_2D_ax.scatter(x_coords, y_coords)


        masked_grid_z = np.ma.masked_invalid(self.grid_z)
        edges = feature.canny(masked_grid_z)
        #self.anomalies = self.mapping_2D_ax.scatter(edges1)
        contours = measure.find_contours(edges, level=0.99)
        #print(type(contour))
        #print(contour.shape)

        for contour in contours:
            self.mapping_2D_ax.plot(contour[:, 1], contour[:, 0])

        #self.anomalies = self.mapping_2D_ax.scatter(x_coords, y_coords)

        self.mapping_2D_canvas.draw_idle()
        print("anno done")



    def write_to_csv(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save as text",
            "",
            ".csv (*.csv);;All Files (*)"
        )
        if not filename.lower().endswith(".csv"):
            filename += ".csv"
        print(np.column_stack((self.grid_x, self.grid_y, self.grid_z)).shape)
        flat_x = self.grid_x.ravel()
        flat_y = self.grid_y.ravel()
        flat_z = self.grid_z.ravel()
        df = pd.DataFrame({
            "UTM_Easting": flat_x,
            "UTM_Northing": flat_y,
            "Value": flat_z
        })
        df.to_csv(filename, index=False)

    def write_to_geotiff(self):
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Save as GeoTIFF",
            "",
            "GeoTIFF files (*.tif);;All Files (*)"
        )
        if filename:
            # Ensure the filename ends with .tif
            if not filename.lower().endswith(".tif"):
                filename += ".tif"

            if hasattr(self, 'mask_clip') and self.mask_clip is not None:
                print("I AM HERE")
                clipped_grid_z = np.ma.masked_where(~self.mask_clip, self.grid_z)
            else:
                clipped_grid_z = np.ma.masked_invalid(self.grid_z)



            self.writeTif.write_to_GeoTiff(filename, self.grid_x, self.grid_y, clipped_grid_z)

    def diurnal_correction(self):
        return 0

    def northings_lineEdit_change(self):
        state, text = self.lineEdit_validate(self.ui.lineEdit_northingsSampleRate)
        if state == QIntValidator.Acceptable:
            print("Valid integer:", text)
            self.northingsSampleRate = int(text)
        else:
            self.ui.lineEdit_northingsSampleRate.setText(str(self.northingsSampleRate))

    def eastings_lineEdit_change(self):
        state, text = self.lineEdit_validate(self.ui.lineEdit_eastingsSampleRate)
        if state == QIntValidator.Acceptable:
            print("Valid integer:", text)
            self.eastingsSampleRate = int(text)
        else:
            self.ui.lineEdit_eastingsSampleRate.setText(str(self.eastingsSampleRate))

    def ambient_lineEdit_change(self):
        state, text = self.lineEdit_validate(self.ui.lineEdit_ambientWindow)
        if state == QIntValidator.Acceptable:
            print("Valid integer:", text)
            self.ambient_window_length = int(text)
            self.validator_smooth.setRange(0, self.ambient_window_length)
        else:
            self.ui.lineEdit_ambientWindow.setText(str(self.ambient_window_length))

    def smoothing_lineEdit_change(self):
        state, text = self.lineEdit_validate(self.ui.lineEdit_smoothingWindow)
        if state == QIntValidator.Acceptable:
            print("Valid integer:", text)
            self.smoothing_window_length = int(text)
        else:
            self.ui.lineEdit_smoothingWindow.setText(str(self.smoothing_window_length))

    def lineEdit_validate(self, line_edit):
        state, text, _ = line_edit.validator().validate(line_edit.text(), 0)
        return state, text

    def layer_update(self):
        print("hello")
        for i in range(self.ui.layerWidget.count()):
            if self.ui.layerWidget.item(i).checkState() == Qt.Checked:
                print(self.ui.layerWidget.item(i).text())

        if self.ui.layerWidget.item(3).checkState() == Qt.Checked and self.track_lines != None:
            print("YES")

            self.track_lines.set_visible(True)
            self.mapping_2D_canvas.draw_idle()

        if self.ui.layerWidget.item(3).checkState() != Qt.Checked and self.track_lines != None:
            self.track_lines.set_visible(False)
            self.mapping_2D_canvas.draw_idle()

        self.update_plot()

    def update_selected_df(self):
        worker = Worker(self.TreeUtil.checked_items)
        self.threadpool.start(worker)

    def check_worker_result(self):
        if not self.grid_queue.empty():
            self.timer.stop()
            result = self.grid_queue.get()

            if isinstance(result, Exception):
                print("Worker failed:", result)
                return

            self.grid_x, self.grid_y, self.grid_z = result
            self.update_plot()

    def draw_selection(self):
        self.TreeUtil.selected_df = self.TreeUtil.selected_df.sort_values(by='datetime')


        if not "Magnetic_Field_residual" in self.TreeUtil.selected_df:
            self.calc_residuals()

        if self.TreeUtil.selected_df.isnull().values.any():
            self.TreeUtil.selected_df.dropna(inplace=True)
            QMessageBox.warning(self, "Nan rows", "Nan rows has been removed to continue processing", )


        nth_select = int(self.ui.lineEdit_nthSelectWindow.text())
        self.data_coordinates = np.array(
            (self.TreeUtil.selected_df["UTM_Easting"].iloc[::nth_select],
             self.TreeUtil.selected_df["UTM_Northing"].iloc[::nth_select]))

        x_min = np.min(self.TreeUtil.selected_df["UTM_Easting"])
        x_max = np.max(self.TreeUtil.selected_df["UTM_Easting"])

        y_min = np.min(self.TreeUtil.selected_df["UTM_Northing"])
        y_max = np.max(self.TreeUtil.selected_df["UTM_Northing"])

        myPworker = PWorker(util.gridding.grid,
                            self.TreeUtil.selected_df["Magnetic_Field_residual"].iloc[::nth_select],
                            self.data_coordinates,
                            x_min,
                            x_max,
                            complex(0, self.eastingsSampleRate),
                            y_max,
                            y_min,
                            complex(0, self.northingsSampleRate), "linear", result_queue=self.grid_queue, )

        myPworker.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_worker_result)
        self.timer.start(100)

    def update_plot(self, ):

        try:
            self.cbar.remove()
        except:
            pass

        self.mapping_2D_ax.cla()

        # self.grid_x, self.grid_y, self.grid_z = result
        x_min, x_max = np.min(self.grid_x), np.max(self.grid_x)
        y_min, y_max = np.min(self.grid_y), np.max(self.grid_y)

        # Compute ranges
        x_range = x_max - x_min
        y_range = y_max - y_min

        # Apply 5% padding
        x_pad = 0.05 * x_range
        y_pad = 0.05 * y_range

        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min , x_max, y_min, y_max ))
        self.mapping_2D_ax.set_xlim([x_min - x_pad, x_max + x_pad])
        self.mapping_2D_ax.set_ylim([y_min - y_pad, y_max + y_pad])

        # Mask invalid Z values
        masked_grid_z = np.ma.masked_invalid(self.grid_z)

        self.mapping_2D_ax.set_xlabel("Eastings [m]")
        self.mapping_2D_ax.set_ylabel("Northings [m]")
        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min, x_max, y_min, y_max))

        bounds = np.array([-300, -200, -100, -50, -20, -10., -5, 0, 5, 10, 20, 50, 100, 200, 300])
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
        # self.contourfplot = self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', extent=(x_min, x_max, y_min, y_max),
        #           cmap='RdBu_r' )

        start = time.time()

        # norm = colors.SymLogNorm(linthresh=1e-3, linscale=1.0, vmin=grid_z.min(), vmax=grid_z.max())
        #masked_grid_z = np.ma.masked_invalid(self.grid_z)

        if hasattr(self, 'mask_clip') and self.mask_clip is not None:
            print("I AM HERE")
            clipped_grid_z = np.ma.masked_where(~self.mask_clip, self.grid_z)
        else:
            clipped_grid_z = np.ma.masked_invalid(self.grid_z)



        if self.color_scale_type == "Linear scale":
            norm = TwoSlopeNorm(vmin=np.nanmin(clipped_grid_z), vcenter=0, vmax=np.nanmax(clipped_grid_z))
            self.contourfplot = self.mapping_2D_ax.pcolormesh(self.grid_x,
                                                              self.grid_y,
                                                              clipped_grid_z,
                                                              cmap='RdBu_r',
                                                              norm=norm)

        elif self.color_scale_type == "Logarithmic scale":
            self.contourfplot = self.mapping_2D_ax.pcolormesh(self.grid_x,
                                                              self.grid_y,
                                                              clipped_grid_z,  # 250,
                                                              # origin='lower',
                                                              # extent=(x_min, x_max, y_min, y_max),
                                                              # cmap='RdBu_r', norm=norm)
                                                              cmap='RdBu_r',
                                                              norm="symlog"
                                                              )

        end = time.time()
        print(end - start)

        cx.add_basemap(self.mapping_2D_ax,
                       crs="EPSG:32629",
                       source=cx.providers.OpenStreetMap.Mapnik,
                       )

        # self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', levels=10,
        #                            norm=colors.SymLogNorm(linthresh=10, linscale=1,
        #                                                   vmin=np.nanmin(grid_z), vmax=np.nanmax(grid_z), base=10))

        try:
            self.track_lines.remove()
        except:
            pass


        if hasattr(self, 'masked_tracklines') and self.masked_tracklines is not None:
            self.track_lines = self.mapping_2D_ax.scatter(self.masked_tracklines[0, :],
                                                          self.masked_tracklines[1, :], color="black", s=1)
        else:
            self.track_lines = self.mapping_2D_ax.scatter(self.data_coordinates[0, :],
                                                          self.data_coordinates[1, :], color="black", s=1)

        if self.ui.layerWidget.item(3).checkState() == Qt.Checked:
            self.track_lines.set_visible(True)
        else:
            self.track_lines.set_visible(False)

        self.cbar = self.mapping_2D_canvas.figure.colorbar(self.contourfplot, ax=self.mapping_2D_ax,
                                                           orientation="vertical")
        self.cbar.set_label('Anomaly [nT]')

        #self.mapping_2D_ax.scatter(489426, 5693316)
        #self.mapping_2D_ax.scatter(514400,5705500)

        self.mapping_2D_canvas.draw_idle()
        # print("Number of collections:", len(self.contourfplot.collections))

    def create_new_project(self):
        project_name, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter project name:')
        if ok:
            self.setWindowTitle(project_name)
            # self.project = TreeModel(project_name)
            self.ui.treeWidget = QTreeWidget(self.ui.centralwidget)
        return ok

    def select_BOB_CSV(self):
        # if self.project != None:
        selected_survey = QFileDialog.getOpenFileName(filter="All Files(*);;Text files(*.csv *.txt)")
        if selected_survey[0].endswith((".txt", ".csv")):
            worker = Worker(self.readCSV.read_from_BOBCSV,
                            selected_survey[0],
                            delimiter=",",
                            skiprows=5,
                            project=self.TreeUtil
                            )

            # worker.start()
            self.threadpool.start(worker)
        else:
            QMessageBox.critical(self, "File IO Error", "No text file selected!", )

    def select_SeaLINKFolder(self):
        selected_folder = QFileDialog.getExistingDirectory(parent=self,
                                                           caption="Select directory",
                                                           options=QFileDialog.Option.ShowDirsOnly)

        valid_folder = False
        print(selected_folder)

        folder_content = os.listdir(selected_folder)
        # The raw data of acquired with Sealink is stored in CVXX_YY and a "Raw" subfolder
        if str(os.listdir(selected_folder)[0]) == "Raw":
            selected_folder = os.path.join(selected_folder, os.listdir(selected_folder)[0])
            valid_folder = True

        for file in folder_content:
            if file.endswith(".XYZ"):
                valid_folder = True
                break

        if valid_folder:
            worker = Worker(self.readCSV.read_from_SeaLINKFolderXYZ,
                            selected_folder,
                            project=self.TreeUtil,
                            )

            self.threadpool.start(worker)
        else:
            QMessageBox.critical(self, "File IO Error", r"No .XYZ or Raw folder containing them has been found!", )

    def select_custom_CSV(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            print(inputs)

            print(inputs[-1])
            print(inputs[1:-1])
            worker = Worker(self.readCSV.read_from_customCSV,
                            inputs[0],
                            delimiter=",",
                            skiprows=int(inputs[-1]),
                            usecols=[int(x) - 1 for x in inputs[1:-1]],
                            project=self.TreeUtil
                            )

            self.threadpool.start(worker)

        dlg = ColumnSelectDlg(self)
        dlg.data_signal.connect(retrieve_user_input)
        dlg.exec()

    def calc_residuals(self):
        TimeSeriesManipulator.smoothing_and_residual_calculation(self.TreeUtil.selected_df,
                                                                 self.smoothing_window_length,
                                                                 self.ambient_window_length)



    def wrapper_1d_selected(self):
        self.TreeUtil.selected_df = self.TreeUtil.selected_df.sort_values(by='datetime')
        if not "Magnetic_Field_residual" in self.TreeUtil.selected_df:
            self.calc_residuals()

        window = getattr(self, "time_series_window", None)
        if window is not None:
            window.draw_1d_selected()

        self.draw_1d_selected()

    def draw_1d_selected(self):
        self.time_series_ax.cla()
        self.time_series_ax.plot(self.TreeUtil.selected_df["datetime"], self.TreeUtil.selected_df["Magnetic_Field"],
                                 color="black")
        self.time_series_ax.set_ylabel("Total mag field $B$ [nT]")
        self.time_series_canvas.draw_idle()

        self.time_series_ax_res.cla()
        self.time_series_ax_res.plot(self.TreeUtil.selected_df["datetime"],
                                     self.TreeUtil.selected_df["Magnetic_Field_residual"],
                                     color="black")
        self.time_series_ax_res.set_ylabel(r"Res $B_0 - \bar{B}$ [nT]")
        self.time_series_canvas_res.draw_idle()

    def remove_outlier(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            print(inputs)
            # print(type(self.TreeUtil.selected_df["UTM_Easting"][0]))
            print(inputs[-1])

            try:
                max_mag, min_mag, max_long, min_long, max_lat, min_lat = [float(i) for i in inputs[:-1]]
                if inputs[-1] == "Remove entry":
                    print(("Here"))

                    worker = Worker(self.TreeUtil.dropna_outlier,
                                    max_mag, min_mag, max_long, min_long, max_lat, min_lat
                                    )
                    self.threadpool.start(worker)
                elif inputs[-1] == "Use last value":
                    worker = Worker(self.TreeUtil.ffill_outlier,
                                    max_mag, min_mag, max_long, min_long, max_lat, min_lat
                                    )
                    self.threadpool.start(worker)

                elif inputs[-1] == "Interpolate neighbours":
                    raise ("not implemented")


            except ValueError:
                QMessageBox.critical(self, "Input Error", "Please specify a valid number.", )

        dlg = RemoveOutlierDlg(self)
        dlg.data_signal.connect(retrieve_user_input)
        dlg.exec()


if __name__ == "__main__":
    # pd.set_option('display.max_columns', None)
    pd.options.mode.copy_on_write = True  # becomes default in Pandas 3.0
    if getattr(sys, 'frozen', False):
        # For PyInstaller bundled app
        os.environ['PROJ_DATA'] = os.path.join(sys._MEIPASS, 'pyproj', 'proj')

    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
