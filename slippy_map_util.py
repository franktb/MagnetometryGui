from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import contextily as cx
from PySide6.QtGui import QIcon

class SlippyMapNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent=None):
        super(SlippyMapNavigationToolbar, self).__init__(canvas, parent)

        # Find the index of the stretchable spacer (usually last)
        spacer_index = self._find_spacer_index()

        self.lasso_action = self.addAction(
            QIcon(r"./ui_elements/icons/cut-scissor-icon.png"),
            #fromTheme("face-smile"),  # Use a theme icon or load your own with QIcon("path.png")
            "Custom Tool",
            self.select_lasso
        )
        self.insertAction(self.actions()[spacer_index], self.lasso_action)

    def _find_spacer_index(self):
        # Typically the last action is the spacer that pushes widgets to the right
        for i, action in enumerate(self.actions()):
            if action.isSeparator():
                continue
            if action.iconText() == "":  # crude check for spacer
                return i
        return len(self.actions())

    def release_pan(self, *args):
        #EPSG:4326,EPSG:3857
        super().release_pan(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)


    def release_zoom(self, *args):
        super().release_zoom(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)


    def select_lasso(self):
        print("hello")