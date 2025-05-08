from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import contextily as cx
from PySide6.QtGui import QIcon

class SlippyMapNavigationToolbar(NavigationToolbar):
    def __init__(self, canvas, parent=None):
        super(SlippyMapNavigationToolbar, self).__init__(canvas, parent)
        self.custom_action = self.addAction(
            QIcon.fromTheme("face-smile"),  # Use a theme icon or load your own with QIcon("path.png")
            "Custom Tool",
            self.select_lasso
        )


    def release_pan(self, *args):
        #EPSG:4326,EPSG:3857
        super().release_pan(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)


    def release_zoom(self, *args):
        super().release_zoom(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)


    def select_lasso(self):
        print("hello")