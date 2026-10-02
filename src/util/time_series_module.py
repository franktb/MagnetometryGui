import scipy.ndimage as ndi
import pandas as pd
import numpy as np
from numpy.typing import ArrayLike


class TimeSeriesManipulator():
    @staticmethod
    def running_mean_1d(x: ArrayLike,
                        N: int) -> np.ndarray:
        """
        Computes the running mean of a 1D array
        See https://stackoverflow.com/questions/13728392/moving-average-or-running-mean/43200476#43200476 for details

        Args:
            x: the input array
            N: the window size

        Returns: the running mean of the input array

        """
        return ndi.uniform_filter1d(x, N, mode='reflect', )

    @staticmethod
    def smoothing_and_residual_calculation(df: pd.DataFrame,
                                           smooth_window_size: int,
                                           ambient_win_size: int):
        """
        Smooths the input array using a running mean and estimates the residual by calculating the difference between the actual field and the ambient field.

        The ambient field is estimated using a slower running mean to capture the underlying background trend.
        Args:
            df: The input dataframe
            smooth_window_size: The window size to smooth the trajectory
            ambient_win_size: The window size to estimate ambient field, i.e. the background trend

        Returns:

        """
        df.sort_values(by='datetime', inplace=True)
        df.loc[:, "Magnetic_Field_Smoothed"] = TimeSeriesManipulator.running_mean_1d(df.loc[:, "Magnetic_Field"],
                                                                                     smooth_window_size)
        df.loc[:, "Magnetic_Field_Ambient"] = TimeSeriesManipulator.running_mean_1d(df.loc[:, "Magnetic_Field"],
                                                                                    ambient_win_size)
        df.loc[:, "Magnetic_Field_residual"] = df.loc[:, "Magnetic_Field_Smoothed"] - df.loc[:,
        "Magnetic_Field_Ambient"]

    @staticmethod
    def clip_depths_layers(df: pd.DataFrame,
                           depths: list[float],
                           eps: float,
                           neighbors: int = 20) -> list[pd.DataFrame]:
        """

        Args:
            df: The dataframe the is to be separated into different layers
            depths: A list of depths that define the layers
            eps: The epsilon value to define a range that is used for clipping
            neighbors: The minimal number of neighbors required in positive and negative time direction for a point be considered part of a layer

        Returns: A list of layers where each layer is a pandas DataFrame

        """
        layers = []

        for depth in depths:
            mask = df["Depth (m)"].between(
                depth - eps,
                depth + eps
            )

            # A point must have `neighbors` valid points
            # immediately before AND after it.
            valid = (
                    mask
                    .rolling(2 * neighbors + 1, center=True)
                    .sum()
                    == 2 * neighbors + 1
            )

            layer = df.loc[mask & valid].copy()

            if not layer.empty:
                layers.append(layer)

        return layers
