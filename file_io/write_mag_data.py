import pandas as pd
import rasterio
from rasterio.transform import from_origin

class WriteMagCSV():
    def write_to_CSV(self, data_frame, columns):
        return 0
        #with rasterio.open(
          #  fp="output.tif",
          #  mode="w",
          #  driver='GTiff',
         #   count=1,
            #dtype=data.dtype,
          #  crs='EPSG:4326',  # Set to your coordinate system
            #transform=transform
        #)


    def write_to_GeoTiff(self, data_frame, columns):
        return 0

