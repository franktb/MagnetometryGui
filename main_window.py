import sys
import os

from TreeWidget import TreeUtil
from ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog, QTreeWidget, \
    QTreeWidgetItem, QDialog
from PySide6.QtGui import QAction, QStandardItemModel, QStandardItem, QColor, QFont
from PySide6.QtCore import Qt, QRunnable, QThreadPool, Slot, QObject, Signal
import contextily as cx

from matplotlib.backends.backend_qtagg import FigureCanvas
from slippy_map_util import slippyMapNavigationToolbar
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

from file_io.read_mag_data import MagCSV
import pandas as pd
import numpy as np


from select_column_dialog import  Ui_ColumnSelectDialog
import matplotlib.colors as colors

from worker import Worker
import time

from util.gridding import grid
from util.filter import running_mean_uniform_filter1d




class ColumnselectDlg(QDialog):
    data_signal = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ColumnSelectDialog()
        self.ui.setupUi(self)


        self.ui.selectFileButton.clicked.connect(self.open_file_dialog)

        self.ui.submitButton.clicked.connect(self.send_data)


    def open_file_dialog(self):
        selected_survey = QFileDialog.getOpenFileName(filter="All Files(*);;Text files(*.csv *.txt)")
        if selected_survey[0].endswith((".txt", ".csv")):
            self.ui.lineEdit_file_path.setText(selected_survey[0])

    def send_data(self):
        inputs = [
            self.ui.lineEdit_file_path.text(),
            self.ui.lineEdit_day.text(),
            self.ui.lineEdit_time.text(),
            self.ui.lineEdit_mag_field.text(),
            self.ui.lineEdit_Gps_lat.text(),
            self.ui.lineEdit_Gps_long.text(),
            self.ui.lineEdit_Gps_easting.text(),
            self.ui.lineEdit_Gps_northing.text()
        ]

        self.data_signal.emit(inputs)
        self.accept()



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

        self.ui.pushButton.clicked.connect(self.debugTree)

        # self.TreeUtil = TreeUtil(self.ui.treeWidget)

        self.selected_df = pd.DataFrame()
        self.TreeUtil = TreeUtil(self.ui.treeWidget, self.selected_df)
        self.ui.treeWidget.itemChanged[QTreeWidgetItem, int].connect(self.update_selected_df)

        self.magCSV = MagCSV()
        # self.ui.treeWidget.setHeaderHidden(True)
        self.threadpool = QThreadPool()

    def update_selected_df(self):
        worker = Worker(self.TreeUtil.checked_items)
        self.threadpool.start(worker)

    def draw_selection(self):
        survey_combined = self.selected_df
        survey_combined.astype({"Magnetic_Field": "float32"})
        survey_combined = survey_combined.sort_values(by='datetime')
        survey_combined.loc[survey_combined["Longitude"].astype(float) < -8.6, "Longitude"] = np.nan
        survey_combined.loc[survey_combined["Magnetic_Field"].astype(float) < 45000., "Magnetic_Field"] = np.nan

        survey_combined.ffill(inplace=True)

        self.time_series_ax.plot(survey_combined["datetime"], survey_combined["Magnetic_Field"].astype(float))
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
        # self.mapping_2D_ax.imshow(grid_z.T, origin='lower', extent=(x_min, x_max, y_min, y_max))

        bounds = np.array([-200, -100, -50, -20, -10., -5, 0, 5, 10, 20, 50, 100, 200])
        norm = colors.BoundaryNorm(boundaries=bounds, ncolors=256)
        # self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', extent=(x_min, x_max, y_min, y_max),
        #           cmap='RdBu_r', )

        self.contourf = self.mapping_2D_ax.contourf(grid_x, grid_y, grid_z, 200, origin='lower',
                                                    extent=(x_min, x_max, y_min, y_max),
                                                    cmap='RdBu_r', norm="symlog")

        # self.mapping_2D_ax.contourf(grid_x,grid_y,grid_z, origin='lower', levels=10,
        #                            norm=colors.SymLogNorm(linthresh=10, linscale=1,
        #                                                   vmin=np.nanmin(grid_z), vmax=np.nanmax(grid_z), base=10))
        self.mapping_2D_canvas.figure.colorbar(self.contourf, ax=self.mapping_2D_ax, orientation="vertical")
        self.mapping_2D_canvas.draw_idle()

    def debugTree(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            print(inputs)

        dlg = ColumnselectDlg(self)
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
                            project=self.ui.treeWidget
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
                        project=self.ui.treeWidget,
                        )

        self.threadpool.start(worker)

    def select_custom_CSV(self):
        @Slot(list)
        def retrieve_user_input(inputs):
            print(inputs)

        dlg = ColumnselectDlg(self)
        dlg.data_signal.connect(retrieve_user_input)
        dlg.exec()


    def draw_1d_selected(self):
        checked_items = self.TreeUtil.checked_items()

        survey_combined = pd.DataFrame()
        for item in checked_items:
            print(item.text(0))
            survey_combined = pd.concat([survey_combined, item.data_frame])

    def remove_outlier(self):
        return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
