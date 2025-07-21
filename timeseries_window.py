from ui_elements.ui_timeseries_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar

class TimeSeriesWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parent = parent

        self.time_series_canvas = FigureCanvas(Figure())
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(NavigationToolbar(self.time_series_canvas))
        self.ui.verticalLayoutTimeSeriesCanvas.addWidget(self.time_series_canvas)
        self.time_series_ax = self.time_series_canvas.figure.subplots()

        self.time_series_canvas_res = FigureCanvas(Figure())
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(NavigationToolbar(self.time_series_canvas_res))
        self.ui.verticalLayoutTimeSeriesCanvas_2.addWidget(self.time_series_canvas_res)
        self.time_series_ax_res = self.time_series_canvas_res.figure.subplots()

    def draw_1D_seelcted(self):
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