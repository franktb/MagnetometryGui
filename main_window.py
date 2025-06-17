import sys
import os
import multiprocessing
from multiprocessing import Queue

from TreeWidget import TreeUtil
from fft_window import FFTWindow
from file_io.write_mag_data import WriteMagCSV
from ui_elements.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog, QTreeWidget, \
    QTreeWidgetItem, QDialog, QListWidgetItem
from PySide6.QtCore import QThreadPool, Slot, Signal, Qt, QTimer
import contextily as cx
from PySide6.QtGui import QIntValidator
from matplotlib.backends.backend_qtagg import FigureCanvas
from slippy_map_util import SlippyMapNavigationToolbar
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

from file_io.read_mag_data import ReadMagCSV
import pandas as pd

from util.data_manipulation import DataManipulator

pd.options.mode.copy_on_write = True
import numpy as np

import matplotlib.colors as colors

from worker import Worker, PWorker

from util.gridding import grid
from util.filter import running_mean_uniform_filter1d
from ui_elements.dialogs import *
import time
import util


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=3, dpi=150):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)


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
        self.ui.actionDraw1D.triggered.connect(self.draw_1d_selected)

        self.ui.actionDrawSelect.triggered.connect(self.draw_selection)
        self.ui.actionRemoveOutlier.triggered.connect(self.remove_outlier)

        self.ui.actioncalcResiduals.triggered.connect(self.calc_residuals)

        self.ui.actionCSV.triggered.connect(self.write_to_csv)

        self.ui.actionGeoTiff.triggered.connect(self.write_to_geotiff)
        self.ui.actionDownward_continuation.triggered.connect(self.spawn_fft_window)


        self.mapping_2D_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        # self.mapping_2D_canvas = MplCanvas(self, 5,3,150)

        self.ui.verticalLayout2DMappingCanvas.addWidget(SlippyMapNavigationToolbar(self.mapping_2D_canvas, self, ))
        self.ui.verticalLayout2DMappingCanvas.addWidget(self.mapping_2D_canvas)
        self.mapping_2D_ax = self.mapping_2D_canvas.figure.subplots()
        self.cbar = None
        self.contourfplot = None

        self.time_series_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(NavigationToolbar(self.time_series_canvas))
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(self.time_series_canvas)
        self.time_series_ax = self.time_series_canvas.figure.subplots()

        self.time_series_canvas_res = FigureCanvas(Figure(figsize=(5, 3)))
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(NavigationToolbar(self.time_series_canvas_res))
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(self.time_series_canvas_res)
        self.time_series_ax_res = self.time_series_canvas_res.figure.subplots()

        # self.ui.pushButton.clicked.connect(self.debugTree)

        # self.TreeUtil = TreeUtil(self.ui.treeWidget)

        self.selected_df = pd.DataFrame()
        self.TreeUtil = TreeUtil(self.ui.treeWidget, self.selected_df)
        self.ui.treeWidget.itemChanged[QTreeWidgetItem, int].connect(self.update_selected_df)

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
        # self.ui.treeWidget.setHeaderHidden(True)
        self.threadpool = QThreadPool()

        self.grid_queue = Queue()



    def spawn_fft_window(self):
        widgetFFT = FFTWindow(parent=self)
        widgetFFT.show()

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
            "Longitude": flat_x,
            "Latitude": flat_y,
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
            self.writeCSV.write_to_GeoTiff(filename, self.grid_x.rave, self.grid_y, self.grid_z)

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
        nth_select = int(self.ui.lineEdit_nthSelectWindow.text())
        self.data_coordinates = np.array(
            (self.TreeUtil.selected_df["Longitude"].iloc[::nth_select],
             self.TreeUtil.selected_df["Latitude"].iloc[::nth_select]))

        x_min = np.min(self.TreeUtil.selected_df["Longitude"])
        x_max = np.max(self.TreeUtil.selected_df["Longitude"])

        y_min = np.min(self.TreeUtil.selected_df["Latitude"])
        y_max = np.max(self.TreeUtil.selected_df["Latitude"])

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

        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min , x_max, y_min, y_max ))
        self.mapping_2D_ax.set_xlim([x_min - 0.1, x_max + 0.1])
        self.mapping_2D_ax.set_ylim([y_min - 0.1, y_max + 0.1])

        cx.add_basemap(self.mapping_2D_ax, crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)
        self.mapping_2D_ax.set_xlabel("Long [°]")
        self.mapping_2D_ax.set_ylabel("Lat [°]")
        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min, x_max, y_min, y_max))

        bounds = np.array([-300, -200, -100, -50, -20, -10., -5, 0, 5, 10, 20, 50, 100, 200, 300])
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
        # self.contourfplot = self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', extent=(x_min, x_max, y_min, y_max),
        #           cmap='RdBu_r' )

        start = time.time()

        # norm = colors.SymLogNorm(linthresh=1e-3, linscale=1.0, vmin=grid_z.min(), vmax=grid_z.max())
        masked_grid_z = np.ma.masked_invalid(self.grid_z)
        self.contourfplot = self.mapping_2D_ax.pcolormesh(self.grid_x, self.grid_y, masked_grid_z,  # 250,
                                                          # origin='lower',
                                                          # extent=(x_min, x_max, y_min, y_max),
                                                          # cmap='RdBu_r', norm=norm)
                                                          cmap='RdBu_r',
                                                          norm="symlog"
                                                          )

        end = time.time()
        print(end - start)

        # self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', levels=10,
        #                            norm=colors.SymLogNorm(linthresh=10, linscale=1,
        #                                                   vmin=np.nanmin(grid_z), vmax=np.nanmax(grid_z), base=10))

        try:
            self.track_lines.remove()
        except:
            pass

        self.track_lines = self.mapping_2D_ax.scatter(self.data_coordinates[0, :],
                                                      self.data_coordinates[1, :], color="black", s=1)
        if self.ui.layerWidget.item(3).checkState() == Qt.Checked:
            self.track_lines.set_visible(True)
        else:
            self.track_lines.set_visible(False)

        self.cbar = self.mapping_2D_canvas.figure.colorbar(self.contourfplot, ax=self.mapping_2D_ax,
                                                           orientation="vertical")
        self.cbar.set_label('Anomaly [nT]')
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
        print(selected_folder)
        worker = Worker(self.readCSV.read_from_SeaLINKFolderXYZ,
                        selected_folder,
                        project=self.TreeUtil,
                        )

        self.threadpool.start(worker)

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
        self.TreeUtil.selected_df = self.TreeUtil.selected_df.sort_values(by='datetime')
        self.TreeUtil.selected_df.loc[:, "Magnetic_Field_Smoothed"] = running_mean_uniform_filter1d(
            self.TreeUtil.selected_df.loc[:, "Magnetic_Field"], self.smoothing_window_length)
        self.TreeUtil.selected_df.loc[:, "Magnetic_Field_Ambient"] = running_mean_uniform_filter1d(
            self.TreeUtil.selected_df.loc[:, "Magnetic_Field"], self.ambient_window_length)
        self.TreeUtil.selected_df.loc[:, "Magnetic_Field_residual"] = self.TreeUtil.selected_df.loc[:,
                                                                      "Magnetic_Field_Smoothed"] - self.TreeUtil.selected_df.loc[
                                                                                                   :,
                                                                                                   "Magnetic_Field_Ambient"]

    def draw_1d_selected(self):
        self.TreeUtil.selected_df = self.TreeUtil.selected_df.sort_values(by='datetime')
        self.time_series_ax.cla()
        self.time_series_ax.plot(self.TreeUtil.selected_df["datetime"], self.TreeUtil.selected_df["Magnetic_Field"])
        self.time_series_ax.set_ylabel("Total mag field $B$ [nT]")
        self.time_series_canvas.draw_idle()

        self.time_series_ax_res.cla()
        self.time_series_ax_res.plot(self.TreeUtil.selected_df["datetime"],
                                     self.TreeUtil.selected_df["Magnetic_Field_residual"])
        self.time_series_ax_res.set_ylabel(r"Res $B_0 - \bar{B}$ [nT]")
        self.time_series_canvas_res.draw_idle()

    def remove_outlier(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            print(inputs)
            # print(type(self.TreeUtil.selected_df["Longitude"][0]))
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
    if getattr(sys, 'frozen', False):
        # For PyInstaller bundled app
        os.environ['PROJ_DATA'] = os.path.join(sys._MEIPASS, 'pyproj', 'proj')

    multiprocessing.freeze_support()

    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
