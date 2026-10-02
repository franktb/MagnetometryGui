from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QDoubleSpinBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

from figure_wrapper import TimeSeriesNavigationToolbar

from ui_elements.FloatListWidget import FloatListWidget
from ui_elements.ui_timeseries_window import Ui_MainWindow

from util.time_series_module import TimeSeriesManipulator

class TimeSeriesWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent = parent

        self.ui.actionDraw1D.triggered.connect(self.wrapper_1d_select)

        self.time_series_canvas = FigureCanvas(Figure())
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(TimeSeriesNavigationToolbar(self.time_series_canvas,self))
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(self.time_series_canvas)
        self.time_series_ax = self.time_series_canvas.figure.subplots()

        self.time_series_canvas_res = FigureCanvas(Figure())
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(NavigationToolbar(self.time_series_canvas_res))
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(self.time_series_canvas_res)
        self.time_series_ax_res = self.time_series_canvas_res.figure.subplots()

        self.time_series_canvas_depth = FigureCanvas(Figure())
        self.ui.verticalLayoutTimeSeriesCanvasDepth.addWidget(TimeSeriesNavigationToolbar(self.time_series_canvas_depth, self))
        self.ui.verticalLayoutTimeSeriesCanvasDepth.addWidget(self.time_series_canvas_depth)
        self.time_series_ax_depth = self.time_series_canvas_depth.figure.subplots()

        self.float_list = FloatListWidget()
        self.ui.verticalLayout_3.addWidget(self.float_list)

        self.ui.verticalLayout_3.addWidget(QLabel("Layer range:", self))
        self.lineEdit_depth_eps = QDoubleSpinBox()
        self.lineEdit_depth_eps.setDecimals(4)
        self.lineEdit_depth_eps.setRange(-1e9, 1e9)
        self.lineEdit_depth_eps.setSingleStep(0.1)
        self.lineEdit_depth_eps.setValue(1.0)
        self.ui.verticalLayout_3.addWidget(self.lineEdit_depth_eps)

        self.spinbox_neighbours = QDoubleSpinBox()
        self.spinbox_neighbours.setDecimals(0)
        self.spinbox_neighbours.setRange(0, 1e9)
        self.spinbox_neighbours.setSingleStep(1)
        self.spinbox_neighbours.setValue(10.0)

        self.ui.verticalLayout_3.addWidget(QLabel("Neighbours:", self))
        self.ui.verticalLayout_3.addWidget(self.spinbox_neighbours)

        self.clip_button = QPushButton("Clip layer")
        self.clip_button.clicked.connect(self.update_depths_layers)
        self.ui.verticalLayout_3.addWidget(self.clip_button)


    def wrapper_1d_select(self):
        self.draw_1d_selected()
        self.parent.draw_1d_selected()

    def draw_1d_selected(self):
        self.parent.TreeUtil.selected_df.sort_values(by='datetime')
        if not "Magnetic_Field_residual" in self.parent.TreeUtil.selected_df:
            self.parent.calc_residuals()


        self.time_series_ax.cla()
        self.time_series_ax.plot(self.parent.TreeUtil.selected_df["datetime"],
                                 self.parent.TreeUtil.selected_df["Magnetic_Field"],
                                 color="black")
        self.time_series_ax.set_ylabel("Total mag field $B$ [nT]")
        self.time_series_canvas.draw_idle()

        self.time_series_ax_res.cla()
        self.time_series_ax_res.plot(self.parent.TreeUtil.selected_df["datetime"],
                                     self.parent.TreeUtil.selected_df["Magnetic_Field_residual"],
                                     color="black")
        self.time_series_ax_res.set_ylabel(r"Res $B_0 - \bar{B}$ [nT]")
        self.time_series_canvas_res.draw_idle()


    def update_depths_layers(self):
        print("pushed")
        depths = self.float_list.values()
        layers = TimeSeriesManipulator.clip_depths_layers(self.parent.TreeUtil.selected_df ,depths , self.lineEdit_depth_eps.value())

        self.time_series_ax.cla()
        self.time_series_ax_depth.plot(self.parent.TreeUtil.selected_df["datetime"],
                                       self.parent.TreeUtil.selected_df["Depth (m)"],
                                       color="black")
        for layer in layers:
            print("layers:")
            print(layer)
            self.time_series_ax_depth.plot(layer["datetime"], layer["Depth (m)"])

        self.time_series_canvas_depth.draw_idle()
