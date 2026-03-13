from scipy.interpolate import griddata
import numpy as np


def grid(scatter_data, coordinates, xwest, xeast, sample_x, ynorth, ysouth, sample_y,method):
    grid_x, grid_y = np.mgrid[xwest:xeast:sample_x, ysouth:ynorth:sample_y]
    grid_z = griddata(coordinates.T, scatter_data, (grid_x, grid_y), method=method)
    return grid_x, grid_y, grid_z

def clip_grid(grid_x, grid_y, grid_z, mask_clip):
    rows, cols = np.where(mask_clip)
    rmin, rmax = rows.min(), rows.max()
    cmin, cmax = cols.min(), cols.max()

    clipped_grid_x = grid_x[rmin:rmax + 1, cmin:cmax + 1]
    clipped_grid_y = grid_y[rmin:rmax + 1, cmin:cmax + 1]
    clipped_grid_z = grid_z[rmin:rmax + 1, cmin:cmax + 1]
    mask_sub = mask_clip[rmin:rmax + 1, cmin:cmax + 1]

    clipped_grid_z = np.where(mask_sub, clipped_grid_z, np.nan)

    return clipped_grid_x, clipped_grid_y, clipped_grid_z