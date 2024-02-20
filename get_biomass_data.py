import ee
import rasterio
import random
import pyproj
import geopandas as gpd
from rasterio.plot import show
import pandas as pd
import geemap

tif_file = 'roi_biomass.tif'
# Define the desired CRS (e.g., EPSG:4326 for WGS 84, which is commonly used for lat/lon)
desired_crs = 'EPSG:4326'

with rasterio.open(tif_file) as src:
    # Define the number of sample points
    num_samples = 1000
    sample_geodata = []

    # Create a transformer to convert from the source CRS to the desired CRS
    transformer = pyproj.Transformer.from_crs(src.crs, desired_crs, always_xy=True)

    while len(sample_geodata) < num_samples:
        # Generate random pixel coordinates within the raster shape
        x_pixel = random.randint(0, src.width - 1)
        y_pixel = random.randint(0, src.height - 1)

        # Get the pixel value
        value = src.read(1, window=((y_pixel, y_pixel + 1), (x_pixel, x_pixel + 1)))[0]

        # Check if the value is not equal to -9999
        if value != -9999:
            # Convert pixel coordinates to map coordinates
            x, y = src.xy(y_pixel, x_pixel)

            # Reproject to the desired CRS (lat/lon)
            lon, lat = transformer.transform(x, y)

            # Create a GeoDataFrame with point geometries
            sample_geodata.append({'geometry': gpd.points_from_xy([lon], [lat])[0], 'Value': float(value)})

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(sample_geodata, crs=desired_crs)

# Save the GeoDataFrame to a GeoJSON file
gdf.to_file('roi_biomass.geojson', driver='GeoJSON')



