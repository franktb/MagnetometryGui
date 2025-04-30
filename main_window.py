import sys

from TreeWidget import TreeUtil
from ui_elements.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog, QTreeWidget, \
    QTreeWidgetItem, QDialog, QListWidgetItem
from PySide6.QtCore import QThreadPool, Slot, Signal, Qt
import contextily as cx

from matplotlib.backends.backend_qtagg import FigureCanvas
from slippy_map_util import slippyMapNavigationToolbar
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

from file_io.read_mag_data import ReadMagCSV
import pandas as pd
pd.options.mode.copy_on_write = True
import numpy as np

import matplotlib.colors as colors

from worker import Worker

from util.gridding import grid
from util.filter import running_mean_uniform_filter1d
from ui_elements.dialogs import *


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
        self.ui.verticalLayout2DMappingCanvas.addWidget(slippyMapNavigationToolbar(self.mapping_2D_canvas, self))
        self.ui.verticalLayout2DMappingCanvas.addWidget(self.mapping_2D_canvas)
        self.mapping_2D_ax = self.mapping_2D_canvas.figure.subplots()

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

        self.magCSV = ReadMagCSV()
        # self.ui.treeWidget.setHeaderHidden(True)
        self.threadpool = QThreadPool()

    def update_selected_df(self):
        worker = Worker(self.TreeUtil.checked_items)
        self.threadpool.start(worker)

    def draw_selection(self):
        survey_combined = self.TreeUtil.selected_df
        print(survey_combined)
        survey_combined.astype({"Magnetic_Field": "float32"})
        survey_combined = survey_combined.sort_values(by='datetime')
        #survey_combined.loc[survey_combined["Longitude"].astype(float) < -8.6, "Longitude"] = np.nan
        #survey_combined.loc[survey_combined["Magnetic_Field"].astype(float) < 45000., "Magnetic_Field"] = np.nan
        #survey_combined.loc[survey_combined["Magnetic_Field"].astype(float) > 49500., "Magnetic_Field"] = np.nan
        #survey_combined.ffill(inplace=True)

        self.time_series_ax.plot(survey_combined["datetime"], survey_combined["Magnetic_Field"].astype(float))
        self.time_series_ax.set_ylabel("Total anomaly [nT]")
        self.time_series_canvas.draw_idle()

        data_coordinates = np.array(
            (survey_combined["Longitude"].astype(float), survey_combined["Latitude"].astype(float)))

        x_min = -8.7
        x_max = -7.3
        y_min = 51.3
        y_max = 51.99

        # aspect = ((x_max - x_min) / 2000) / ((y_max - y_min) / 2000)

        survey_combined.loc[:, "Magnetic_Field_Smoothed"] = running_mean_uniform_filter1d(
            survey_combined.loc[:, "Magnetic_Field"].astype(float), 20)
        survey_combined.loc[:, "Magnetic_Field_Ambient"] = running_mean_uniform_filter1d(
            survey_combined.loc[:, "Magnetic_Field"].astype(float), 500)
        survey_combined.loc[:, "Magnetic_Field_residual"] = survey_combined.loc[:,
                                                            "Magnetic_Field_Smoothed"] - survey_combined.loc[:,
                                                                                         "Magnetic_Field_Ambient"]

        grid_x, grid_y, grid_z = grid(survey_combined["Magnetic_Field_residual"].astype(float), data_coordinates,
                                      x_min,
                                      x_max,
                                      2000j,
                                      y_max,
                                      y_min,
                                      2000j, "linear")

        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min , x_max, y_min, y_max ))
        self.mapping_2D_ax.set_xlim([x_min, x_max])
        self.mapping_2D_ax.set_ylim([y_min, y_max])

        cx.add_basemap(self.mapping_2D_ax, crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)
        self.mapping_2D_ax.set_xlabel("Long [°]")
        self.mapping_2D_ax.set_ylabel("Lat [°]")
        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min, x_max, y_min, y_max))

        bounds = np.array([-300, -200, -100, -50, -20, -10., -5, 0, 5, 10, 20, 50, 100, 200, 300])
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
        # self.contourf = self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', extent=(x_min, x_max, y_min, y_max),
        #           cmap='RdBu_r' )

        self.contourf = self.mapping_2D_ax.contourf(grid_x, grid_y, grid_z, 250, origin='lower',
                                                    extent=(x_min, x_max, y_min, y_max),
                                                    # cmap='RdBu_r', norm=norm)
                                                    cmap='RdBu_r', norm="symlog")

        # self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', levels=10,
        #                            norm=colors.SymLogNorm(linthresh=10, linscale=1,
        #                                                   vmin=np.nanmin(grid_z), vmax=np.nanmax(grid_z), base=10))
        cbar = self.mapping_2D_canvas.figure.colorbar(self.contourf, ax=self.mapping_2D_ax, orientation="vertical")
        cbar.set_label('Anomaly [nT]')
        self.mapping_2D_canvas.draw_idle()

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
            # survey_combined.ffill(inplace=True)

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
        checked_items = self.TreeUtil.selected_df
        checked_items = checked_items.sort_values(by='datetime')


        checked_items .loc[:, "Magnetic_Field_Smoothed"] = running_mean_uniform_filter1d(
            checked_items.loc[:, "Magnetic_Field"].astype(float), 20)
        checked_items .loc[:, "Magnetic_Field_Ambient"] = running_mean_uniform_filter1d(
            checked_items.loc[:, "Magnetic_Field"].astype(float), 500)
        checked_items.loc[:, "Magnetic_Field_residual"] = checked_items.loc[:,
                                                            "Magnetic_Field_Smoothed"] - checked_items .loc[:,
                                                                                         "Magnetic_Field_Ambient"]

        self.time_series_ax.cla()
        self.time_series_ax.plot(checked_items["datetime"], checked_items["Magnetic_Field"])
        self.time_series_ax.set_ylabel("Total mag field $B$ [nT]")
        self.time_series_canvas.draw_idle()

        self.time_series_ax_res.cla()
        self.time_series_ax_res.plot(checked_items["datetime"], checked_items["Magnetic_Field_residual"])
        self.time_series_ax_res.set_ylabel(r"Res $B_0 - \bar{B}$ [nT]")
        self.time_series_canvas_res.draw_idle()

    def remove_outlier(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            print(inputs)
            #print(type(self.TreeUtil.selected_df["Longitude"][0]))
            print(inputs[-1])
            try:
                inputs = [float(i) for i in inputs[:-1]]
                max_mag, min_mag, max_long, min_long, max_lat, min_lat = inputs


                if inputs[-1] == "Remove entry":
                    raise ("not implemnted")
                elif inputs[-1]  == "Use last value":
                    self.TreeUtil.selected_df.sort_values(by='datetime')
                    self.TreeUtil.selected_df.loc[
                        self.TreeUtil.selected_df["Magnetic_Field"] > max_mag, "Magnetic_Field"] = np.nan
                    self.TreeUtil.selected_df.loc[
                        self.TreeUtil.selected_df["Magnetic_Field"] < min_mag, "Magnetic_Field"] = np.nan
                    self.TreeUtil.selected_df.loc[
                        self.TreeUtil.selected_df["Magnetic_Field"] > max_mag, "Magnetic_Field"] = np.nan
                    self.TreeUtil.selected_df.loc[
                        self.TreeUtil.selected_df["Magnetic_Field"] < min_mag, "Magnetic_Field"] = np.nan
                    self.TreeUtil.selected_df.loc[
                        self.TreeUtil.selected_df["Longitude"] > max_long, "Longitude"] = np.nan
                    self.TreeUtil.selected_df.loc[
                        self.TreeUtil.selected_df["Longitude"] < min_long, "Longitude"] = np.nan
                    self.TreeUtil.selected_df.loc[self.TreeUtil.selected_df["Latitude"] > max_lat, "Latitude"] = np.nan
                    self.TreeUtil.selected_df.loc[self.TreeUtil.selected_df["Latitude"] < min_lat, "Latitude"] = np.nan
                    self.TreeUtil.selected_df.ffill(inplace=True)
                elif  inputs[-1]  == "Interpolate neighbours":
                    raise("not implemnted")


            except ValueError:
                QMessageBox.critical(self, "Input Error", "Please specify a valid number.", )

        dlg = RemoveOutlierDlg(self)
        dlg.data_signal.connect(retrieve_user_input)
        dlg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
