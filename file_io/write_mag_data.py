import pandas as pd
import rasterio
from rasterio.transform import from_origin

class WriteMagCSV():
    def write_to_CSV(self, data_frame, columns):
        with rasterio.open(
            fp="output.tif",
            mode="w",
            driver='GTiff',

        )


    def write_to_GeoTiff(self, data_frame, columns):
        return 0

