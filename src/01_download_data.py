# example on how to download data in zlflo

# import packages
import logging

import geopandas as gpd
import nlmod

import settings  # local module with model settings
from zlflodata import get_abs_data_path  # local module for data path handling

# create a logger instance
logger = logging.getLogger(__name__)

# download data using nlmod
ahn = nlmod.read.ahn.download_ahn(
    extent=settings.extent, cachedir=settings.paths["download"], cachename="ahn"
)

# read data from data repository (ZLFLO/data)
gdf_example_path = get_abs_data_path(
    name="example_dataset", version="1.0.0", location="get_from_env"
)
gdf = gpd.read_file(gdf_example_path / "example_gdf.geojson")

# read data from external source via link in data repository
