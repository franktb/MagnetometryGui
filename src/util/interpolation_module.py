import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import interpn
from util.filter import DownwardContinuation


class MagCube():
    def __init__(self):
        self.dc = DownwardContinuation()

    def compute_cube(self,
                     min_depth: float,
                     max_depth: float,
                     grid_z,
                     layer_count: int = 5):
        """
        Estimates the magnetic field for a volume (cube) below the surface, sampled at a given size of layers.

        Args:
            min_depth: depth of upper layer of the magnetic field cube
            max_depth: depth of lower layer of the magnetic field cube
            grid_z: the magnetic field at the surface
            layer_count: the amount how often the cube should be sampled

        Returns: the magnetic (volume) field as a cube, sampled at a given amount of layers

        """
        layers = []
        layer_depths = np.linspace(min_depth, max_depth, layer_count)

        for depth in layer_depths:
            print("Depth", depth)
            layer = self.dc.iterative_downward_finite(grid_z, np.abs(depth))
            layers.append(layer)

        cube = np.stack(layers, axis=0)  # shape: (layer_count, Ny, Nx)
        return cube, layer_depths

    def sample_cube_at_height(self, cube, layer_heights, grid_merge):
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
