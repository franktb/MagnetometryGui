import pandas as pd
import rasterio
from rasterio.transform import from_origin
import numpy as np

class WriteMagCSV():
    def write_to_CSV(self, filename, data_frame, columns,sep=","):
        data_frame.to_csv(path_or_buf=filename,
                          sep=sep)



    def write_to_GeoTiff(self,filename, grid_x, grid_y, grid_z):
        print("huhuGEoTiff")

        print("grid_z type:", type(grid_z))
        print("grid_z shape:", grid_z.shape)
        print("grid_x shape:", grid_x.shape)
        print("grid_y shape:", grid_y.shape)




        data = np.ma.masked_invalid(grid_z).filled(np.nan).astype(np.float32)
        print(data)
        height= grid_y.shape[0]
        width = grid_x.shape[0]

        print("width:", width)
        print("height:", height)
        print("dtype:", data.dtype)


        x_min = np.min(grid_x)
        x_max = np.max(grid_x)

        y_max = np.max(grid_y)
        y_min = np.min(grid_y)

        pixel_width = (x_max - x_min) / (grid_x.shape[0] - 1)
        pixel_height = (y_max - y_min) / (grid_y.shape[0] - 1)




        transform = from_origin(x_min, y_max, pixel_width, -pixel_height)
        with rasterio.open(
                    fp=filename,
                    mode="w",
                    driver='GTiff',
                    height=height,
                    width=width,
                    count=1,
                    dtype=data.dtype,
                    crs='EPSG:4326',  # Set to your coordinate system
                    transform=transform,
                    nodata=np.nan
                    ) as dst:
            dst.write(data, 1)

