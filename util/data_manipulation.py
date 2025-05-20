from unittest.mock import inplace

import pandas as pd
import numpy as np


class DataManipulator():
    @staticmethod
    def ffill_outlier_from_df(df, max_mag, min_mag, max_long, min_long, max_lat, min_lat):

        print("huhu")
        df.sort_values(by='datetime')
        df.loc[df["Magnetic_Field"] > max_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Magnetic_Field"] < min_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Magnetic_Field"] > max_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Magnetic_Field"] < min_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Longitude"] > max_long, "Longitude"] = np.nan
        df.loc[df["Longitude"] < min_long, "Longitude"] = np.nan
        df.loc[df["Latitude"] > max_lat, "Latitude"] = np.nan
        df.loc[df["Latitude"] < min_lat, "Latitude"] = np.nan
        df.ffill(inplace=True)
        print(df.shape)

    @staticmethod
    def dropna_outlier_from_df(df, max_mag, min_mag, max_long, min_long, max_lat, min_lat):
        df.sort_values(by='datetime')
        df.loc[df["Magnetic_Field"] > max_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Magnetic_Field"] < min_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Magnetic_Field"] > max_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Magnetic_Field"] < min_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Longitude"] > max_long, "Longitude"] = np.nan
        df.loc[df["Longitude"] < min_long, "Longitude"] = np.nan
        df.loc[df["Latitude"] > max_lat, "Latitude"] = np.nan
        df.loc[df["Latitude"] < min_lat, "Latitude"] = np.nan
        df.dropna(inplace=True)

    @staticmethod
    def drop_from_lasso_select(df, selected_lat_long, tol=1e-5):
        mask_long = df['Longitude'].apply(
            lambda x: any(np.isclose(x, val, atol=tol) for val in selected_lat_long[:,0]))
        mask_lat = df['Latitude'].apply(
            lambda x: any(np.isclose(x, val, atol=tol) for val in selected_lat_long[:,1]))
        mask =  ~(mask_long & mask_lat)
        df.drop(df[~mask].index, inplace=True)
