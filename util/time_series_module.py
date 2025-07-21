import scipy.ndimage as ndi
import numpy as np


class TimeSeriesManipulator():
    @staticmethod
    def running_mean_1d(x, N):
        return ndi.uniform_filter1d(x, N, mode='reflect', )

    @staticmethod
    def smoothing_and_residual_calculation(df, smooth_window_size, ambient_win_size):
        df.sort_values(by='datetime', inplace=True)
        df.loc[:, "Magnetic_Field_Smoothed"] = TimeSeriesManipulator.running_mean_1d(df.loc[:, "Magnetic_Field"],
                                                                                     smooth_window_size)
        df.loc[:, "Magnetic_Field_Ambient"] = TimeSeriesManipulator.running_mean_1d(df.loc[:, "Magnetic_Field"],
                                                                                    ambient_win_size)
        df.loc[:, "Magnetic_Field_residual"] = df.loc[:, "Magnetic_Field_Smoothed"] - df.loc[:,
                                                                                      "Magnetic_Field_Ambient"]
