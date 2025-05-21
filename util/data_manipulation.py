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
    def drop_from_lasso_select(df, selected_lat_long, tol=1e-8):
        """
        df.sort_values(by='datetime')
        print("")
        print("")
        long_array = df['Longitude'].to_numpy().astype(np.float64)
        target_longs = selected_lat_long[:, 0].data.astype(np.float64) #selected_lat_long is a masked array
        #target_longs.sort()
        mask_long = compute_mask(long_array, target_longs, tol)
        #np.savetxt("longInputs.txt", long_array)
        #np.savetxt("debugTargetsLong.txt", mask_long.T)

        lat_array = df['Latitude'].to_numpy().astype(np.float64)
        target_lats = selected_lat_long[:, 1].data.astype(np.float64) #selected_lat_long is a masked array
        #target_lats.sort()
        mask_lat = compute_mask(lat_array, target_lats, tol)
        np.savetxt("debugInputsLat.txt", lat_array)
        np.savetxt("debugTargetsLat.txt", target_lats.T)
        np.savetxt("debugMaskLat.txt", mask_lat.T)

        mask =  ~(mask_long & mask_lat)
        print("lat bool", np.sum(mask_lat))
        print("long bool", np.sum(mask_long))
        print("mask bool", np.sum(mask))

        print(selected_lat_long.shape)
        print(df.shape)
        print(mask.shape)
        df.drop(df[~mask].index, inplace=True)
        print("")
        print("")
        print("DONE!!!")
        print(df.shape)
        """

        df.sort_values(by='datetime', inplace=True)
        print(df)
        #pd.set_option('display.max_rows', None)
        lat_array = df['Latitude'].to_numpy().astype(np.float64)
        long_array = df['Longitude'].to_numpy().astype(np.float64)
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