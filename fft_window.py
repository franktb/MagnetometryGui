from multiprocessing import Queue

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QThreadPool, Slot, Signal, Qt, QTimer
from figure_wrapper import SlippyMapNavigationToolbar
from ui_elements.ui_fft_window import Ui_FFTWindow
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure

from util.filter import DownwardContinuation
from worker import PWorker
import numpy as np


class FFTWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FFTWindow()
        self.ui.setupUi(self)
        self.parent = parent


        self.downward_2D_canvas = FigureCanvas(Figure(figsize=(5,3)))

        self.ui.verticalLayout2DMappingCanvas.addWidget(SlippyMapNavigationToolbar(self.downward_2D_canvas,self,))
        self.ui.verticalLayout2DMappingCanvas.addWidget(self.downward_2D_canvas)
        self.downward_2D_ax = self.downward_2D_canvas.figure.subplots()

        self.depth = float(self.ui.lineEditDepth.text())
        self.ui.lineEditDepth.textEdited.connect(self.depthEdited)

        self.n_iterations = int(self.ui.lineEditIterations.text())
        self.ui.lineEditIterations.textEdited.connect(self.iterationsEdited)

        self.ui.pushButton_StartIteration.clicked.connect(self.downward_continuation)

        self.downward_field = None

        self.myDownward = DownwardContinuation()
        self.fft_queue = Queue()

    def depthEdited(self):
        self.depth = float(self.ui.lineEditDepth.text())

    def iterationsEdited(self):
        self.n_iterations = int(self.ui.lineEditIterations.text())


    def check_worker_result(self):
        if not self.fft_queue.empty():
            self.timer.stop()
            result = self.fft_queue.get()

            if isinstance(result, Exception):
                print("Worker failed:", result)
                return

            self.downward_field = result
            self.update_plot()

    def downward_continuation(self):
        print("lets do it")
        #self.myDownward.iterative_downward_finite(self.parent.grid_z,self.depth, self.n_iterations)

        myPworker = PWorker(self.myDownward.iterative_downward_finite,
                            np.nan_to_num(self.parent.grid_z),
                            self.depth,
                            #self.n_iterations,
                            result_queue=self.fft_queue)
        myPworker.start()
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_worker_result)
        self.timer.start(100)

    def update_plot(self):
        try:
            self.cbar.remove()
        except:
            pass

        self.downward_2D_ax.cla()

        x_min, x_max = np.min(self.parent.grid_x), np.max(self.parent.grid_x)
        y_min, y_max = np.min(self.parent.grid_y), np.max(self.parent.grid_y)

        self.downward_2D_ax.set_xlim([x_min - 0.1, x_max + 0.1])
        self.downward_2D_ax.set_ylim([y_min - 0.1, y_max + 0.1])

        masked_grid_z = np.ma.masked_invalid(self.downward_field)

        self.contourfplot = self.downward_2D_ax.pcolormesh(self.parent.grid_x,
                                                          self.parent.grid_y,
                                                          masked_grid_z,  # 250,
                                                          cmap='RdBu_r',
                                                          norm="symlog"
                                                          )

        self.cbar = self.downward_2D_canvas.figure.colorbar(self.contourfplot, ax=self.downward_2D_ax,
                                                           orientation="vertical")


        self.cbar.set_label('Anomaly [nT]')
        self.downward_2D_canvas.draw_idle()