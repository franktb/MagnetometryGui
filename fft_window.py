from multiprocessing import Queue

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QThreadPool, Slot, Signal, Qt, QTimer
from figure_wrapper import SlippyMapNavigationToolbar
from file_io.tiff_io import Bathymetry, WriteMag
from ui_elements.ui_fft_window import Ui_FFTWindow
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtGui import QIntValidator

from util.filter import DownwardContinuation
from util.interpolation_module import MagCube
from worker import PWorker
import numpy as np


class FFTWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FFTWindow()
        self.ui.setupUi(self)
        self.parent = parent

        self.downward_2D_canvas = FigureCanvas(Figure(figsize=(5, 3)))

        self.ui.verticalLayout2DMappingCanvas.addWidget(SlippyMapNavigationToolbar(self.downward_2D_canvas, self, ))
        self.ui.verticalLayout2DMappingCanvas.addWidget(self.downward_2D_canvas)
        self.downward_2D_ax = self.downward_2D_canvas.figure.subplots()

        self.depth = float(self.ui.lineEditDepth.text())
        self.ui.lineEditDepth.textEdited.connect(self.depthEdited)

        self.n_iterations = int(self.ui.lineEditIterations.text())
        self.ui.lineEditIterations.textEdited.connect(self.iterationsEdited)

        self.ui.pushButton_StartIteration.clicked.connect(self.start_selected_downward)
        self.ui.pushButton_layer.clicked.connect(self.downward_cube)

        self.validator_layer = QIntValidator(0, 10, self)
        self.ui.lineEditLayers.setValidator(self.validator_layer)
        self.ui.lineEditLayers.textEdited.connect(self.lineEditLayers_changed)
        self.lineEditLayers_changed()  # set up the comboBoxDisplayedLayer as well


        self.ui.comboBoxDisplayedLayer.currentIndexChanged.connect(self.comboBoxDisplayedLayer_changed)
        self.downward_field = None
        self.cube = None

        self.myDownward = DownwardContinuation()
        self.fft_queue = Queue()

        self.myMagCube = MagCube()
        self.myBathymetry = Bathymetry()
        self.tiffWriter = WriteMag()

    def lineEdit_validate(self, line_edit):
        state, text, _ = line_edit.validator().validate(line_edit.text(), 0)
        return state, text

    def lineEditLayers_changed(self):
        state, text = self.lineEdit_validate(self.ui.lineEditLayers)
        if state == QIntValidator.Acceptable:
            self.layer_count = int(text)
            self.ui.comboBoxDisplayedLayer.clear()
            items = [str(i) for i in range(1, self.layer_count + 1)]
            print(items)
            self.ui.comboBoxDisplayedLayer.addItems(items)
        else:
            self.ui.lineEditLayers.setText(str(self.layer_count))

    def comboBoxDisplayedLayer_changed(self):
        if self.cube is not None:
            print("hello")
            print(self.ui.comboBoxDisplayedLayer.currentIndex())
            self.update_plot(self.cube[self.ui.comboBoxDisplayedLayer.currentIndex(),:,:])



    def closeEvent(self, event):
        self.parent.ui.action_spawn_FFTWindow.setChecked(False)
        self.parent.fft_window = None
        super().closeEvent(event)

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
            self.update_plot(result)

    def start_selected_downward(self):
        if self.ui.comboBox_display.currentIndex() == 0:
            self.downward_continuation()
        if self.ui.comboBox_display.currentIndex() == 1:
            self.downward_cube(10,30)
        if self.ui.comboBox_display.currentIndex() == 2:
            print(self.ui.comboBox_display.currentText(),2)
            self.downward_bathymetry()


    def downward_continuation(self):
        print("lets do it")
        # self.myDownward.iterative_downward_finite(self.parent.grid_z,self.depth, self.n_iterations)

        print("do it depth", self.depth)
        myPworker = PWorker(self.myDownward.iterative_downward_finite,
                            np.nan_to_num(self.parent.grid_z),
                            self.depth,
                            # self.n_iterations,
                            result_queue=self.fft_queue)
        myPworker.start()
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_worker_result)
        self.timer.start(100)

    def downward_cube(self, min_depth, max_depth):
        cube, layer_heights = self.myMagCube.compute_cube(min_depth=min_depth,
                                                          max_depth=max_depth,
                                                          grid_z=np.nan_to_num(self.parent.grid_z),
                                                          layer_count=self.layer_count)
        self.cube = np.nan_to_num(cube)

        # cube, layer_depths = self.myMagCube.sample_cube_at_height(cube, layer_heights, depth_grid)
        # self.tiffWriter.write_to_GeoTiff("depth.tif", self.parent.grid_x, self.parent.grid_y, maglayer)

    def downward_bathymetry(self):
        filenames = ["/home/frank/UCC/MagnetometryGui/data/BathTiffs/BY_CV16_01_CelticSea_5m_U29N.tif",
                     "/home/frank/UCC/MagnetometryGui/data/BathTiffs/BY_CV16_02_Cork_5m_U29N.tif"]

        depth_grid = self.myBathymetry.read_from_TiffFolder(filenames,
                                                            self.parent.grid_x,
                                                            self.parent.grid_y)
        print(depth_grid)
        np.savetxt("debugBAthGrid", depth_grid)
        min_depth = np.nanmin(depth_grid)
        max_depth = np.nanmax(depth_grid)
        cube, layer_heights = self.myMagCube.compute_cube(min_depth=min_depth,
                                                          max_depth=max_depth,
                                                          grid_z=np.nan_to_num(self.parent.grid_z),
                                                          layer_count=self.layer_count)
        cube = np.nan_to_num(cube)

        maglayer = self.myMagCube.sample_cube_at_height(cube, layer_heights, depth_grid)
        self.update_plot(maglayer)
        self.tiffWriter.write_to_GeoTiff("depth.tif", self.parent.grid_x, self.parent.grid_y, maglayer)

    def update_plot(self, downward_field):
        try:
            self.cbar.remove()
        except:
            pass

        self.downward_2D_ax.cla()

        x_min, x_max = np.min(self.parent.grid_x), np.max(self.parent.grid_x)
        y_min, y_max = np.min(self.parent.grid_y), np.max(self.parent.grid_y)

        self.downward_2D_ax.set_xlim([x_min - 0.1, x_max + 0.1])
        self.downward_2D_ax.set_ylim([y_min - 0.1, y_max + 0.1])

        masked_grid_z = np.ma.masked_invalid(downward_field)

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
