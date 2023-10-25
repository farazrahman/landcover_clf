# LAND COVER CLASSIFICATION AND BIOMASS ESTIMATION

This project conducts land cover classification using Landsat imagery using the Google Earth Engine platform, detects change in land cover from 2020 to 2022 and then estimates the biomass for the location of interest.

### ENVIRONMENT SETUP
To execute the project follow the steps below: NOTE: Pycharm is used as IDE:

1. Clone the repository
2. Set up a virtual environment in the project's root directory and install required packages and libraries.
3. Libraries used:
   1. pandas, geopandas, numpy, scipy, matplotlib
   2. Google earth engine, geemap
   
### PROJECT EXECUTION:
1. Main analysis is in the jupyter notebook: "1_landcover_classification(single).ipynb"
2. Polygons used: "boundary_clipped.geojson"
3. Biomass data: "roi_biomass.geojson"
