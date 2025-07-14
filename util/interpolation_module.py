import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import interpn
from util.filter import DownwardContinuation


class MagCube():
    def __init__(self):
        self.dc = DownwardContinuation()

    def compute_cube(self, grid_merge, grid_z,layer_count = 5):
        layers = []
        min_hight = np.nanmin(grid_merge)
        max_high = np.nanmax(grid_merge)

        layer_heights = np.linspace(min_hight, max_high, layer_count)

        for hight in layer_heights:
            print("Hight", hight)
            mylayer = self.dc.iterative_downward_finite(grid_z, np.abs(hight))
            layers.append(mylayer)

        cube = np.stack(layers, axis=0)  # shape: (layer_count, Ny, Nx)
        return cube, layer_heights

    def sample_cube_at_height(self,cube, layer_heights, grid_merge):
        print("cube.shape", cube.shape)
        print("grid_merge", grid_merge.shape)
        print("layer hights", layer_heights.shape)

        L, Y, X = cube.shape

        # Grid of layer heights (z), y and x coordinates
        grid = (layer_heights, np.arange(Y), np.arange(X))

        # Points where to sample: (N, 3) = (z, y, x)
        points = np.stack([
            grid_merge.ravel(),  # z (height at each point)
            np.repeat(np.arange(Y), X),  # y indices
            np.tile(np.arange(X), Y)  # x indices
        ], axis=-1)

        values_flat = interpn(
            points=grid,
            values=cube,
            xi=points,
            bounds_error=False,
            fill_value=0
        )

        values = values_flat.reshape(Y, X)
        return values