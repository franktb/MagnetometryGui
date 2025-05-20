from scipy.interpolate import griddata
import numpy as np
from multiprocessing import Pool
from itertools import repeat
from scipy.interpolate import LinearNDInterpolator
from scipy.spatial import Delaunay
import time

class Gridder():
    @staticmethod
    def interpolate_chunk(args):
        chunk, coordinates, scatter_data = args
        return griddata(coordinates, scatter_data, chunk, method='linear')

    @staticmethod
    def interpolate_chunk_v2(args):
        chunk, interp = args
        return interp(chunk)

    @staticmethod
    def split_into_chunks(data, n_chunks):
        return np.array_split(data, n_chunks)

    @staticmethod
    def grid(scatter_data, coordinates, xwest, xeast, sample_x, ynorth, ysouth, sample_y,method):
        grid_x, grid_y = np.mgrid[xwest:xeast:sample_x, ysouth:ynorth:sample_y]
        grid_points = np.column_stack((grid_x.ravel(), grid_y.ravel()))
        n_cores = 8
        grid_chunks = Gridder.split_into_chunks(grid_points, n_cores)

        #args = zip(grid_chunks, repeat(coordinates.T), repeat(scatter_data))

        triangulation = Delaunay(coordinates.T)
        interpolator = LinearNDInterpolator(triangulation, scatter_data)
        args = zip(grid_chunks, repeat(interpolator ))

        start = time.time()
        with Pool(processes=n_cores) as pool:
            #args = zip(grid_chunks, repeat(coordinates.T), repeat(scatter_data))
            #results = pool.map(Gridder.interpolate_chunk, args)
            results = pool.map(Gridder.interpolate_chunk_v2, args )

        grid_z = np.concatenate(results).reshape(grid_x.shape)
        end = time.time()
        print("funktion", end-start)
        #grid_z = griddata(coordinates.T, scatter_data, (grid_x, grid_y), method=method)
        return grid_x, grid_y, grid_z