from PySide6.QtWidgets import QMainWindow
from ui_elements.ui_fft_window import Ui_FFTWindow

class FFTWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FFTWindow()
        self.ui.setupUi(self)