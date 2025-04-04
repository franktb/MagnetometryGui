from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
import contextily as cx

class slippyMapNavigationToolbar(NavigationToolbar):
    def release_pan(self, *args):

        #EPSG:4326,EPSG:3857
        super().release_pan(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)

        #self.canvas.draw_idle()

    def release_zoom(self, *args):
        super().release_zoom(*args)
        cx.add_basemap(self.canvas.figure.get_axes()[0], crs="EPSG:4326", source=cx.providers.OpenStreetMap.Mapnik)

        #self.canvas.draw_idle()