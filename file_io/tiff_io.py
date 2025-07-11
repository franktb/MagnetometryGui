from multiprocessing import Queue

import pandas as pd
import rasterio
from rasterio.transform import from_origin, rowcol
from rasterio.enums import Resampling
import numpy as np
from scipy.ndimage import map_coordinates

from worker import PWorker
from scipy.interpolate import RegularGridInterpolator

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


class Bathymetry():
    def read_and_interpolate_geotiff(self, filename, grid_x, grid_y, upscale_factor=0.25):
        file = rasterio.open(filename)
        data = file.read(1, out_shape=(
            file.count,
            int(file.height * upscale_factor),
            int(file.width * upscale_factor)
        ), resampling=Resampling.bilinear)

        # scale image transform
        transform = file.transform * file.transform.scale(
            (file.width / data.shape[-1]),
            (file.height / data.shape[-2])
        )

        data = data.astype(float)
        mask = np.isclose(data, file.nodata, atol=1e-8)
        data[mask] = np.nan

        # Generate 1D row and column indices
        rows = np.arange(data.shape[0])
        cols = np.arange(data.shape[1])

        a, b, c, d, e, f = transform.a, transform.b, transform.c, transform.d, transform.e, transform.f

        xs = c + cols * a  # b should be 0 due to regular grid
        ys = f + rows * e  # d should be 0 due to regular grid

        # Get TIFF bounds
        xmin, ymin, xmax, ymax = file.bounds

        # Mask: where grid points fall within the TIFF bounds
        inside_mask = (
                (grid_x >= xmin) & (grid_x <= xmax) &
                (grid_y >= ymin) & (grid_y <= ymax)
        )

        interp = RegularGridInterpolator(
            (ys, xs), data,
            bounds_error=False, fill_value=np.nan
        )

        # Only interpolate points inside the TIFF area
        points = np.stack([grid_y[inside_mask], grid_x[inside_mask]], axis=-1)
        interpolated_values = interp(points)

        # Prepare output array filled with NaNs
        interpolated = np.full_like(grid_x, np.nan, dtype=float)
        interpolated[inside_mask] = interpolated_values

        return interpolated


    def merge_TiffFolder(self,filenames, grid_x, grid_y, upscale_factor=0.25):
        merged = np.full_like(grid_x, np.nan, dtype=float)
        for fname in filenames:
            interpolated = self.read_and_interpolate_geotiff(fname, grid_x, grid_y, upscale_factor)
            merged = np.where(~np.isnan(interpolated), interpolated, merged)

        return merged


    def read_from_TiffFolder(self, filenames, grid_x, grid_y):
        queue = Queue()
        myPworker = PWorker(self.merge_TiffFolder,
                            result_queue=queue,
                            filenames= filenames,
                            grid_x=grid_x,
                            grid_y=grid_y,
        )
        myPworker.start()
        bathymetry_map = queue.get()
        myPworker.join()
        return bathymetry_map