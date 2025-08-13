# example on how to download data in zlflo

# import packages
import nlmod
import logging

import geopandas as gpd

from pathlib import Path

from zlflodata.get_paths import get_abs_data_path # zlflo data repository

import config # local module with model settings



# create a logger instance
logger = logging.getLogger(__name__)

# download data using nlmod
ahn = nlmod.read.ahn.download_ahn(extent=config.extent,
                                  cachedir=config.download_dir,
                                  cachename='ahn')

# read data from data repository (ZLFLO/data)
gdf_example_path = get_abs_data_path(name="example_dataset",
                                version="1.0.0",
                                location="get_from_env")
gdf = gpd.read_file(gdf_example_path / 'example_gdf.geojson')

# read data from external source via link in data repository

