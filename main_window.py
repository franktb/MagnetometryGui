import sys


from TreeWidget import TreeUtil
from ui_elements.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog, QTreeWidget, \
    QTreeWidgetItem, QDialog, QListWidgetItem
from PySide6.QtCore import QThreadPool, Slot, Signal, Qt
import contextily as cx

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

from worker import Worker

from util.gridding import grid
from util.filter import running_mean_uniform_filter1d
from ui_elements.dialogs import *
import time


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

        self.mapping_2D_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        # self.mapping_2D_canvas = MplCanvas(self, 5,3,150)

        self.ui.verticalLayout2DMappingCanvas.addWidget(SlippyMapNavigationToolbar(self.mapping_2D_canvas, self,))
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

        self.magCSV = ReadMagCSV()
        # self.ui.treeWidget.setHeaderHidden(True)
        self.threadpool = QThreadPool()

    def layer_update(self):
        print("hello")
        for i in range(self.ui.layerWidget.count()):
            if self.ui.layerWidget.item(i).checkState() == Qt.Checked:
                print(self.ui.layerWidget.item(i).text())

        if self.ui.layerWidget.item(3).checkState() == Qt.Checked and self.track_lines !=None:
            print("YES")

            self.track_lines.set_visible(True)
            self.mapping_2D_canvas.draw_idle()

        if self.ui.layerWidget.item(3).checkState() != Qt.Checked and self.track_lines != None:
            self.track_lines.set_visible(False)
            self.mapping_2D_canvas.draw_idle()

    def update_selected_df(self):
        worker = Worker(self.TreeUtil.checked_items)
        self.threadpool.start(worker)

    def draw_selection(self):

        try:
            self.cbar.remove()
        except:
            pass

        self.mapping_2D_ax.cla()
        self.data_coordinates = np.array(
            (self.TreeUtil.selected_df["Longitude"],
             self.TreeUtil.selected_df["Latitude"]))

        x_min = np.min(self.TreeUtil.selected_df ["Longitude"])
        x_max = np.max(self.TreeUtil.selected_df ["Longitude"])

        y_min = np.min(self.TreeUtil.selected_df ["Latitude"])
        y_max = np.max(self.TreeUtil.selected_df ["Latitude"])



        start = time.time()
        grid_x, grid_y, grid_z = grid(self.TreeUtil.selected_df["Magnetic_Field_residual"],
                                      self.data_coordinates,
                                      x_min,
                                      x_max,
                                      2000j,
                                      y_max,
                                      y_min,
                                      2000j, "linear")

        end = time.time()
        print("I am here", end - start)

        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min , x_max, y_min, y_max ))
        self.mapping_2D_ax.set_xlim([x_min-0.1, x_max+0.1])
        self.mapping_2D_ax.set_ylim([y_min-0.1, y_max+0.1])

        cx.add_basemap(self.mapping_2D_ax, crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)
        self.mapping_2D_ax.set_xlabel("Long [°]")
        self.mapping_2D_ax.set_ylabel("Lat [°]")
        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min, x_max, y_min, y_max))

        bounds = np.array([-300, -200, -100, -50, -20, -10., -5, 0, 5, 10, 20, 50, 100, 200, 300])
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
        # self.contourfplot = self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', extent=(x_min, x_max, y_min, y_max),
        #           cmap='RdBu_r' )


        start = time.time()


        #norm = colors.SymLogNorm(linthresh=1e-3, linscale=1.0, vmin=grid_z.min(), vmax=grid_z.max())
        masked_grid_z = np.ma.masked_invalid(grid_z)
        self.contourfplot = self.mapping_2D_ax.pcolormesh(grid_x, grid_y, masked_grid_z, #250,
                                                    #origin='lower',
                                                    #extent=(x_min, x_max, y_min, y_max),
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




        self.cbar = self.mapping_2D_canvas.figure.colorbar(self.contourfplot, ax=self.mapping_2D_ax, orientation="vertical")
        self.cbar.set_label('Anomaly [nT]')
        self.mapping_2D_canvas.draw_idle()
        #print("Number of collections:", len(self.contourfplot.collections))


    def debugTree(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            max_mag, min_mag, max_long, min_long, max_lat, min_lat = inputs

            self.TreeUtil.selected_df.sort_values(by='datetime')
            self.TreeUtil.selected_df.loc[
                self.TreeUtil.selected_df["Magnetic_Field"] < max_mag, "Magnetic_Field"] = np.nan
            self.TreeUtil.selected_df.loc[
                self.TreeUtil.selected_df["Magnetic_Field"] > min_mag, "Magnetic_Field"] = np.nan
            self.TreeUtil.selected_df.loc[self.TreeUtil.selected_df["Longitude"] < -8.6, "Longitude"] = np.nan
            self.TreeUtil.selected_df.loc[self.TreeUtil.selected_df["Longitude"] < -8.6, "Longitude"] = np.nan
            # self.TreeUtil.selected_df.ffill(inplace=True)

        dlg = ColumnSelectDlg(self)
        dlg.data_signal.connect(retrieve_user_input)
        dlg.exec()

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
            worker = Worker(self.magCSV.read_from_BOBCSV,
                            selected_survey[0],
                            delimiter=",",
                            skiprows=5,
                            project=self.TreeUtil
                            )

            self.threadpool.start(worker)
        else:
            QMessageBox.critical(self, "File IO Error", "No text file selected!", )

    def select_SeaLINKFolder(self):
        selected_folder = QFileDialog.getExistingDirectory(parent=self,
                                                           caption="Select directory",
                                                           options=QFileDialog.Option.ShowDirsOnly)
        print(selected_folder)
        worker = Worker(self.magCSV.read_from_SeaLINKFolderXYZ,
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
            worker = Worker(self.magCSV.read_from_customCSV,
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

    def draw_1d_selected(self):
        self.TreeUtil.selected_df = self.TreeUtil.selected_df.sort_values(by='datetime')


        self.TreeUtil.selected_df.loc[:, "Magnetic_Field_Smoothed"] = running_mean_uniform_filter1d(
            self.TreeUtil.selected_df.loc[:, "Magnetic_Field"], 20)
        self.TreeUtil.selected_df.loc[:, "Magnetic_Field_Ambient"] = running_mean_uniform_filter1d(
            self.TreeUtil.selected_df.loc[:, "Magnetic_Field"], 500)
        self.TreeUtil.selected_df.loc[:, "Magnetic_Field_residual"] = self.TreeUtil.selected_df.loc[:,
                                                            "Magnetic_Field_Smoothed"] - self.TreeUtil.selected_df .loc[:,
                                                                                         "Magnetic_Field_Ambient"]

        self.time_series_ax.cla()
        self.time_series_ax.plot(self.TreeUtil.selected_df["datetime"], self.TreeUtil.selected_df["Magnetic_Field"])
        self.time_series_ax.set_ylabel("Total mag field $B$ [nT]")
        self.time_series_canvas.draw_idle()

        self.time_series_ax_res.cla()
        self.time_series_ax_res.plot(self.TreeUtil.selected_df["datetime"], self.TreeUtil.selected_df["Magnetic_Field_residual"])
        self.time_series_ax_res.set_ylabel(r"Res $B_0 - \bar{B}$ [nT]")
        self.time_series_canvas_res.draw_idle()

    def remove_outlier(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            print(inputs)
            #print(type(self.TreeUtil.selected_df["Longitude"][0]))
            print(inputs[-1])

            try:
                max_mag, min_mag, max_long, min_long, max_lat, min_lat = [float(i) for i in inputs[:-1]]
                if inputs[-1] == "Remove entry":
                    print(("Here"))
                    #print(self.TreeUtil.selected_df.shape)
                    worker = Worker(self.data_manipulator.dropna_outlier_from_df,
                                    self.TreeUtil.selected_df,
                                    max_mag, min_mag, max_long, min_long, max_lat, min_lat
                                    )
                    self.threadpool.start(worker)
                    self.TreeUtil.dropna_outlier(max_mag, min_mag, max_long, min_long, max_lat, min_lat)
                elif inputs[-1]  == "Use last value":
                    worker = Worker(self.data_manipulator.ffill_outlier_from_df,
                                    self.TreeUtil.selected_df,
                                    max_mag, min_mag, max_long, min_long, max_lat, min_lat
                                    )
                    self.threadpool.start(worker)
                    self.TreeUtil.ffill_outlier(max_mag, min_mag, max_long, min_long, max_lat, min_lat)

                elif  inputs[-1]  == "Interpolate neighbours":
                    raise("not implemnted")


            except ValueError:
                QMessageBox.critical(self, "Input Error", "Please specify a valid number.", )

        dlg = RemoveOutlierDlg(self)
        dlg.data_signal.connect(retrieve_user_input)
        dlg.exec()


if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
