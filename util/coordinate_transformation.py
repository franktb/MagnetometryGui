import geopandas as gpd

class CoordinateTransformation():
    @staticmethod
    def longlat_to_eastnorth(long_series, lat_series):
        """
        Converts a series of coordinates given as latitude and longitude to projected eastings and northings
        :param long_series: 1D array of longitude values
        :param lat_series: 1D array of latitude values
        :return: 1D array of eastings, 1D arry of northings
        """
        geo_series_latlong = gpd.GeoSeries(gpd.points_from_xy(long_series,lat_series), crs="EPSG:4326")
        geo_series_leastnorth = geo_series_latlong.to_crs(epsg=32629)
        return geo_series_leastnorth.x, geo_series_leastnorth.y

    @staticmethod
    def eastnorth_to_latlong(df):
        return 0