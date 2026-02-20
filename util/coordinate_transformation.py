import geopandas as gpd


class CoordinateTransformation():
    @staticmethod
    def longlat_to_eastnorth(long_series, lat_series):
        """Converts a series of coordinates given as longitude and latitude (in xy order) to projected eastings and northings


        Args:
            long_series: 1D array of longitude values
            lat_series: 1D array of latitude values

        Returns: 1D array of easting values, 1D array of northing values

        """
        geo_series_longlat = gpd.GeoSeries(gpd.points_from_xy(long_series, lat_series), crs="EPSG:4326")
        geo_series_eastnorth = geo_series_longlat.to_crs(epsg=32629)
        return geo_series_eastnorth.x, geo_series_eastnorth.y

    @staticmethod
    def eastnorth_to_latlong(east_series, north_series, crs="EPSG:32629"):
        """
        
        Args:
            east_series: 1D array of easting values
            north_series: 1D array of northing values
            crs: the coordinate reference system. Defaults to EPSG:32629 the WGS 84 / UTM zone 29N zone containing Ireland

        Returns: 1D array of longitude values, 1D array of latitude values

        """
        geo_series_easthnorth = gpd.GeoSeries(gpd.points_from_xy(east_series, north_series), crs=crs)
        geo_series_longlat = geo_series_easthnorth.to_crs(epsg=4326)
        return geo_series_longlat.x, geo_series_longlat.y
