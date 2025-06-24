from multiprocessing.queues import Queue

import pandas as pd
import rasterio
from rasterio.transform import from_origin, rowcol
from rasterio.enums import Resampling
import numpy as np
from scipy.ndimage import map_coordinates

from worker import PWorker

class WriteMag():
    def write_to_GeoTiff(self,filename, grid_x, grid_y, grid_z):
        data = np.ma.masked_invalid(grid_z).filled(np.nan).astype(np.float32)
        print(data)
        height= grid_y.shape[0]
        width = grid_x.shape[0]


        x_min = np.min(grid_x)
        x_max = np.max(grid_x)

        y_max = np.max(grid_y)
        y_min = np.min(grid_y)

        pixel_width = (x_max - x_min) / (grid_x.shape[0] - 1)
        pixel_height = (y_max - y_min) / (grid_y.shape[0] - 1)


        transform = from_origin(x_min, y_min, pixel_width, -pixel_height)
        with rasterio.open(
                    fp=filename,
                    mode="w",
                    driver='GTiff',
                    height=height,
                    width=width,
                    count=1,
                    dtype=data.dtype,
                    crs='+proj=latlong',
                    #crs='EPSG:4326',  # Set to your coordinate system
                    transform=transform,
                    nodata=np.nan
                    ) as dst:
            dst.write(data.T, 1)


class ReadBathymetry():
    def read_from_GeoTiff(self, filename, grid_x, grid_y):
        queue = Queue()

        def quickwrapper(filename):
            with rasterio.open(filename) as dataset:
                data = dataset.read(1)
                transform = dataset.transform

                # Convert spatial coordinates to pixel row,col
                rows, cols = rowcol(transform, grid_x.ravel(), grid_y.ravel(), op=float)

                # Interpolate values at floating point pixel coords
                coords = np.vstack([rows, cols])  # shape (2, N)
                values = map_coordinates(data, coords, order=1, mode='nearest')
            return values


        myPworker = PWorker(quickwrapper,
                            result_queue=queue,
                            filename=filename)
        myPworker.start()
        raw_tiff = queue.get()
        myPworker.join()
        return raw_tiff