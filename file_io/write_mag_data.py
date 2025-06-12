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
        masked_grid_z = np.ma.masked_invalid(grid_z)
        data = masked_grid_z.filled(np.nan)

        # Assumes grid_x and grid_y are increasing along axis=1 and axis=0 respectively
        x_res = (grid_x[0, 1] - grid_x[0, 0])
        y_res = (grid_y[0, 0] - grid_y[1, 0])  # y decreases down rows

        # Upper-left corner
        x_min = grid_x[0, 0]
        y_max = grid_y[0, 0]

        transform = from_origin(x_min, y_max, x_res, y_res)
        with rasterio.open(
                    fp=filename,
                    mode="w",
                    driver='GTiff',
                    count=1,
                    dtype=data.dtype,
                    crs='EPSG:4326',  # Set to your coordinate system
                    transform=transform
                    ) as dst:
            dst.write(data, 1)

