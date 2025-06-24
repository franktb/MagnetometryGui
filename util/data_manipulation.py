import pandas as pd
import numpy as np
from util.bin.fastmask import compute_mask, compute_pairwise_mask
import os
os.environ["OMP_NUM_THREADS"] = "12"
import cupy as cp


class DataManipulator():
    @staticmethod
    def ffill_outlier_from_df(df, max_mag, min_mag, max_long, min_long, max_lat, min_lat):

        print("huhu")
        df.sort_values(by='datetime', inplace=True)
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
        print(df.shape)
        df.sort_values(by='datetime', inplace=True)
        df.loc[df["Magnetic_Field"] > max_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Magnetic_Field"] < min_mag, "Magnetic_Field"] = np.nan
        df.loc[df["Longitude"] > max_long, "Longitude"] = np.nan
        df.loc[df["Longitude"] < min_long, "Longitude"] = np.nan
        df.loc[df["Latitude"] > max_lat, "Latitude"] = np.nan
        df.loc[df["Latitude"] < min_lat, "Latitude"] = np.nan
        df.dropna(inplace=True)
        print(df.shape)

    @staticmethod
    def drop_from_lasso_select(df, selected_lat_long, tol=1e-8):
        df.sort_values(by='datetime', inplace=True)
        lat_array = df['UTM_Northing'].to_numpy().astype(np.float64)
        long_array = df['UTM_Easting'].to_numpy().astype(np.float64)
        coord_array = np.stack((long_array, lat_array), axis=1)  # Shape: (N, 2)
        selected_coords = selected_lat_long.data.astype(np.float64)  # Shape: (M, 2)

        #def pairwise_match(coords, selected, tol):
        #    mask = np.zeros(coords.shape[0], dtype=bool)
        #    for i in range(coords.shape[0]):
        #        dists = np.linalg.norm(selected - coords[i], axis=1)
        #        if np.any(dists <= tol):
        #            mask[i] = True
        #    return mask

        mask = compute_pairwise_mask(coord_array, selected_coords, tol)

        print(f"Selected pairs: {selected_coords.shape[0]}")
        print(f"Matching rows: {np.sum(mask)} of {len(df)}")
        df.drop(df[mask].index, inplace=True)
        print("DONE!!!")
        print(df.shape)