from scipy.interpolate import griddata
import numpy as np


def grid(scatter_data, coordinates, xwest, xeast, sample_x, ynorth, ysouth, sample_y,method):
    grid_x, grid_y = np.mgrid[xwest:xeast:sample_x, ysouth:ynorth:sample_y]
    grid_z = griddata(coordinates.T, scatter_data, (grid_x, grid_y), method=method)
    return grid_x, grid_y, grid_z