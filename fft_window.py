from PySide6.QtWidgets import QMainWindow

from figure_wrapper import SlippyMapNavigationToolbar
from ui_elements.ui_fft_window import Ui_FFTWindow
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

class FFTWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FFTWindow()
        self.ui.setupUi(self)


        self.downward_2D_canvas = FigureCanvas(Figure(figsize=(5,3)))

        self.ui.verticalLayoutWidget.addWidget(SlippyMapNavigationToolbar(self.downward_2D_canvas,self,))
        self.ui.verticalLayoutWidget.addWidget(self.downward_2D_canvas)