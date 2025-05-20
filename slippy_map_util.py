from PySide6.QtWidgets import QMessageBox
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import contextily as cx
from PySide6.QtGui import QIcon
from matplotlib.widgets import LassoSelector
import numpy as np
from matplotlib.path import Path
from threading import Thread

class SlippyMapNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent=None):
        super(SlippyMapNavigationToolbar, self).__init__(canvas, parent)
        self.parent = parent
        self.selected_points = None

        self.lasso_selector = None
        self.lasso_active = False

        # Store references to zoom and pan actions
        self.zoom_action = self._actions['zoom']
        self.pan_action = self._actions['pan']


        # Find the index of the stretchable spacer (usually last)
        spacer_index = self._find_spacer_index()


        self.lasso_action = self.addAction(
            QIcon(r"./ui_elements/icons/cut-scissor-icon.png"),
            #fromTheme("face-smile"),  # Use a theme icon or load your own with QIcon("path.png")
            "Custom Tool",
            self.toggle_lasso
        )
        self.lasso_action.setToolTip("Lasso removal")
        self.lasso_action.setCheckable(True)
        self.insertAction(self.actions()[spacer_index], self.lasso_action)

    def _find_spacer_index(self):
        # Typically the last action is the spacer that pushes widgets to the right
        for i, action in enumerate(self.actions()):
            if action.isSeparator():
                continue
            if action.iconText() == "":  # crude check for spacer
                return i
        return len(self.actions())

    def toggle_lasso(self):
        if self.lasso_active:
            self.deactivate_lasso()
        else:
            self.activate_lasso()

    def activate_lasso(self):
        self.lasso_active = True
        self.lasso_action.setChecked(True)

        # Disable pan/zoom actions to prevent user activation
        self.zoom_action.setEnabled(False)
        self.pan_action.setEnabled(False)

        # Deactivate if already active
        if self.zoom_action.isChecked():
            self.zoom()
        if self.pan_action.isChecked():
            self.pan()

        # Initialize LassoSelector
        ax = self.canvas.figure.get_axes()[0]
        self.lasso_selector = LassoSelector(ax, onselect=self.on_select)


    def deactivate_lasso(self):
        self.lasso_active = False
        self.lasso_action.setChecked(False)

        # Re-enable pan/zoom
        self.zoom_action.setEnabled(True)
        self.pan_action.setEnabled(True)

        if self.lasso_selector:
            self.lasso_selector.disconnect_events()
            self.lasso_selector = None

        self.canvas.draw_idle()

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Conformation")
        dlg.setText("Remove marked track line points?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            #print("Yes!")
            #print(self.selected_points)
            #if self.selected_points !=None:

            thread = Thread(target=self.parent.data_manipulator.drop_from_lasso_select,
                                args=(self.parent.TreeUtil.selected_df,
                                      self.selected_points))
            thread.start()
        else:
            print("No!")





    def on_select(self, verts):
        ax = self.canvas.figure.axes[0]
        path = Path(verts)
        line = self.parent.track_lines.get_offsets()

        x, y = line[:,0], line[:,1]
        points = np.column_stack((x, y))
        # Respect zoomed view
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
        visible = (x >= xlim[0]) & (x <= xlim[1]) & (y >= ylim[0]) & (y <= ylim[1])
        visible_points = points[visible]

        selected = path.contains_points(visible_points)
        self.selected_points = visible_points[selected]

        print("Selected points:", self.selected_points)


    def release_pan(self, *args):
        #EPSG:4326,EPSG:3857
        super().release_pan(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)


    def release_zoom(self, *args):
        super().release_zoom(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)

