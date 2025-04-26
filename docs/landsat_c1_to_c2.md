 
#  Landsat Collection 1 to Collection 2 migration 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Surface reflectance](https://developers.google.com/earth-engine/landsat_c1_to_c2#surface_reflectance)
  * [Top-of-atmosphere reflectance](https://developers.google.com/earth-engine/landsat_c1_to_c2#top-of-atmosphere_reflectance)
  * [Scaled radiance (DN)](https://developers.google.com/earth-engine/landsat_c1_to_c2#scaled_radiance_dn)
  * [Landsat Pre-Collection](https://developers.google.com/earth-engine/landsat_c1_to_c2#landsat_pre-collection)
  * [Temporal composites](https://developers.google.com/earth-engine/landsat_c1_to_c2#temporal_composites)


This guide provides instructions for switching from [Landsat](https://developers.google.com/earth-engine/datasets/catalog/landsat) Collection 1 to Collection 2 data. Collection 2 has been fully available in Earth Engine since 2022 and [no Collection 1 data has been produced by the USGS since December 31, 2021](https://www.usgs.gov/news/landsat-collection-1-forward-processing-cease-end-2021). Landsat Collection 1 is deprecated and all users are encouraged to migrate to Collection 2 as soon as possible.
Each [Landsat Collection](https://www.usgs.gov/landsat-missions/landsat-collections) represents a version of the image archive processed with consistent methods and routines. As systems and processing algorithms improve, new collections are generated. In 2020, the USGS began reprocessing the archive to [Collection 2](https://www.usgs.gov/landsat-missions/landsat-collection-2). See the article ["The 50-year Landsat collection 2 archive"](https://doi.org/10.1016/j.srs.2023.100103) in Remote Sensing of Environment to learn about the rationale behind the collections processing model and the contents and advancements provided by Collection 2.
The following sections describe the changes needed to migrate from Collection 1 to Collection 2 for each Landsat data product, including image and collection IDs, band names, new bands, band value scaling, and bitmask values. The content tabs within each section provide details for specific sensors.
## Surface reflectance
[OLI](https://developers.google.com/earth-engine/landsat_c1_to_c2#oli)[ETM+](https://developers.google.com/earth-engine/landsat_c1_to_c2#etm+)[TM](https://developers.google.com/earth-engine/landsat_c1_to_c2#tm) More
### Asset ID
Replace `C01` with `C02` and `SR` with `L2` in image and collection IDs. For example, [Landsat 8 OLI Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2) (Landsat 9 OLI-2 was not included in Collection 1):
Collection 1 | Collection 2  
---|---  
LANDSAT/LC08/**C01** /**T1_SR** | LANDSAT/LC08/**C02** /**T1_L2**  
### Band names
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Ultra blue | **B1** | **SR_B1**  
Blue | **B2** | **SR_B2**  
Green | **B3** | **SR_B3**  
Red | **B4** | **SR_B4**  
Near infrared | **B5** | **SR_B5**  
Shortwave infrared 1 | **B6** | **SR_B6**  
Shortwave infrared 2 | **B7** | **SR_B7**  
Brightness temperature 1 | **B10** |   
Brightness temperature 2 | **B11** |   
Aerosol attributes | **sr_aerosol** | **SR_QA_AEROSOL**  
Surface temperature |  | **ST_B10**  
Atmospheric transmittance |  | **ST_ATRAN**  
Pixel distance to cloud |  | **ST_CDIST**  
Downwelled radiance |  | **ST_DRAD**  
Emissivity |  | **ST_EMIS**  
Emissivity standard deviation |  | **ST_EMSD**  
Surface temperature uncertainty |  | **ST_QA**  
Thermal radiance |  | **ST_TRAD**  
Upwelled radiance |  | **ST_URAD**  
Pixel quality attributes (CFMask) | **pixel_qa** | **QA_PIXEL**  
Radiometric saturation QA | **radsat_qa** | **QA_RADSAT**  
Update code that selects bands whose names have changed, for example, the near-infrared band:
Collection 1 | Collection 2  
---|---  
`image.select('B5')` | `image.select('SR_B5')`  
### Value scaling
Reflectance bands have new scaling factors. Collection 1 used a `0.0001` scale factor. Collection 2 uses a `2.75e-05` scale factor and `-0.2` offset. The thermal band also has new scale and offset factors. The following code block defines a function to apply Collection 2 surface reflectance and temperature band scaling factors and maps it over an image collection.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varapplyScaleFactors=function(image){
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBand=image.select('ST_B10').multiply(0.00341802).add(149.0);
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBand,null,true);
}
varsrColScaled=srCol.map(applyScaleFactors)
```
```
defapply_scale_factors(image):
 optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
 thermal_band = image.select('ST_B6').multiply(0.00341802).add(149.0)
 return image.addBands(optical_bands, None, True).addBands(
   thermal_band, None, True
 )
sr_col_scaled = sr_col.map(apply_scale_factors)
```

### QA masking
Bit codes have changed for the QA bitmask (CFMASK). See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2#bands)) and "Bitmask for pixel_qa" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_SR#bands)) sections in catalog entries for codes.
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0)
```

### Radiometric saturation
Bit codes have changed for the radiometric saturation bitmask. See the "Bitmask for QA_RADSAT" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2#bands)) and "Bitmask for radsat_qa" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_SR#bands)) sections in catalog entries for codes.
### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. Properties for solar geometry were altered. See the following property comparison table to determine whether you need to modify your code to accommodate missing, added, or altered properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2#image-properties) in the product's catalog page for Collection 2 property descriptions.
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
ALGORITHM_SOURCE_SURFACE_REFLECTANCE |   
| ALGORITHM_SOURCE_SURFACE_TEMPERATURE  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
| COLLECTION_CATEGORY  
| COLLECTION_NUMBER  
| DATA_SOURCE_AIR_TEMPERATURE  
| DATA_SOURCE_ELEVATION  
| DATA_SOURCE_OZONE  
| DATA_SOURCE_PRESSURE  
| DATA_SOURCE_REANALYSIS  
| DATA_SOURCE_TIRS_STRAY_LIGHT_CORRECTION  
| DATA_SOURCE_WATER_VAPOR  
| DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
| DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
| ELLIPSOID  
ESPA_VERSION |   
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
| GEOMETRIC_RMSE_VERIFY  
| GRID_CELL_SIZE_REFLECTIVE  
| GRID_CELL_SIZE_THERMAL  
| GROUND_CONTROL_POINTS_MODEL  
| GROUND_CONTROL_POINTS_VERIFY  
| GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY_OLI | IMAGE_QUALITY_OLI  
IMAGE_QUALITY_TIRS | IMAGE_QUALITY_TIRS  
| L1_DATE_PRODUCT_GENERATED  
| L1_LANDSAT_PRODUCT_ID  
| L1_PROCESSING_LEVEL  
| L1_PROCESSING_SOFTWARE_VERSION  
| L1_REQUEST_ID  
LANDSAT_ID |   
| LANDSAT_PRODUCT_ID  
| LANDSAT_SCENE_ID  
LEVEL1_PRODUCTION_DATE |   
| MAP_PROJECTION  
| NADIR_OFFNADIR  
| ORIENTATION  
PIXEL_QA_VERSION |   
| PROCESSING_LEVEL  
| PROCESSING_SOFTWARE_VERSION  
| REFLECTANCE_ADD_BAND_1  
| REFLECTANCE_ADD_BAND_2  
| REFLECTANCE_ADD_BAND_3  
| REFLECTANCE_ADD_BAND_4  
| REFLECTANCE_ADD_BAND_5  
| REFLECTANCE_ADD_BAND_6  
| REFLECTANCE_ADD_BAND_7  
| REFLECTANCE_MULT_BAND_1  
| REFLECTANCE_MULT_BAND_2  
| REFLECTANCE_MULT_BAND_3  
| REFLECTANCE_MULT_BAND_4  
| REFLECTANCE_MULT_BAND_5  
| REFLECTANCE_MULT_BAND_6  
| REFLECTANCE_MULT_BAND_7  
| REFLECTIVE_LINES  
| REFLECTIVE_SAMPLES  
| REQUEST_ID  
| ROLL_ANGLE  
SATELLITE |   
| SATURATION_BAND_1  
| SATURATION_BAND_2  
| SATURATION_BAND_3  
| SATURATION_BAND_4  
| SATURATION_BAND_5  
| SATURATION_BAND_6  
| SATURATION_BAND_7  
| SATURATION_BAND_8  
| SATURATION_BAND_9  
| SCENE_CENTER_TIME  
SENSING_TIME |   
| SENSOR_ID  
| SPACECRAFT_ID  
| STATION_ID  
**SOLAR_AZIMUTH_ANGLE** | **SUN_AZIMUTH**  
**SOLAR_ZENITH_ANGLE** | **SUN_ELEVATION** _(Collection 2 uses elevation instead of zenith angle. To calculate zenith angle, use`90 - elevation`.)_  
SR_APP_VERSION |   
| TARGET_WRS_PATH  
| TARGET_WRS_ROW  
| TEMPERATURE_ADD_BAND_ST_B10  
| TEMPERATURE_MAXIMUM_BAND_ST_B10  
| TEMPERATURE_MINIMUM_BAND_ST_B10  
| TEMPERATURE_MULT_BAND_ST_B10  
| THERMAL_LINES  
| THERMAL_SAMPLES  
| TIRS_SSM_MODEL  
| TIRS_SSM_POSITION_STATUS  
| TRUNCATION_OLI  
| UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
### Asset ID
Replace `C01` with `C02` and `SR` with `L2` in image and collection IDs. For example, [Landsat 7 ETM+ Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2):
Collection 1 | Collection 2  
---|---  
LANDSAT/LE07/**C01** /**T1_SR** | LANDSAT/LE07/**C02** /**T1_L2**  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Blue | **B1** | **SR_B1**  
Green | **B2** | **SR_B2**  
Red | **B3** | **SR_B3**  
Near infrared | **B4** | **SR_B4**  
Shortwave infrared 1 | **B5** | **SR_B5**  
TOA brightness temperature | **B6** |   
Shortwave infrared 2 | **B7** | **SR_B7**  
Atmospheric opacity | **sr_atmos_opacity** | **SR_ATMOS_OPACITY**  
Cloud quality assessment | **sr_cloud_qa** | **SR_CLOUD_QA**  
Surface temperature |  | **ST_B6**  
Atmospheric transmittance |  | **ST_ATRAN**  
Pixel distance to cloud |  | **ST_CDIST**  
Downwelled radiance |  | **ST_DRAD**  
Emissivity |  | **ST_EMIS**  
Emissivity standard deviation |  | **ST_EMSD**  
Surface temperature uncertainty |  | **ST_QA**  
Thermal radiance |  | **ST_TRAD**  
Upwelled radiance |  | **ST_URAD**  
Pixel quality attributes (CFMask) | **pixel_qa** | **QA_PIXEL**  
Radiometric saturation QA | **radsat_qa** | **QA_RADSAT**  
Update code that selects bands whose names have changed, for example, the near-infrared band:
Collection 1 | Collection 2  
---|---  
`image.select('B4')` | `image.select('SR_B4')`  
### Value scaling
Reflectance bands have new scaling factors. Collection 1 used a `0.0001` scale factor. Collection 2 uses a `2.75e-05` scale factor and `-0.2` offset. The thermal band also has new scale and offset factors. The following code block defines a function to apply Collection 2 surface reflectance and temperature band scaling factors and maps it over an image collection.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varapplyScaleFactors=function(image){
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBand=image.select('ST_B6').multiply(0.00341802).add(149.0);
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBand,null,true);
}
varsrColScaled=srCol.map(applyScaleFactors)
```
```
defapply_scale_factors(image):
 optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
 thermal_band = image.select('ST_B6').multiply(0.00341802).add(149.0)
 return image.addBands(optical_bands, None, True).addBands(
   thermal_band, None, True
 )
sr_col_scaled = sr_col.map(apply_scale_factors)
```

### QA masking
Bit codes have changed for the QA bitmask (CFMASK). See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2#bands)) and "Bitmask for pixel_qa" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1_SR#bands)) sections in catalog entries for codes.
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0)
```

### Radiometric saturation
Bit codes have changed for the radiometric saturation bitmask. See the "Bitmask for QA_RADSAT" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2#bands)) and "Bitmask for radsat_qa" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1_SR#bands)) sections in catalog entries for codes.
### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. Properties for solar geometry were altered. See the following property comparison table to determine whether you need to modify your code to accommodate missing, added, or altered properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2#image-properties) in the product's catalog page for Collection 2 property descriptions.
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
ALGORITHM_SOURCE_SURFACE_REFLECTANCE |   
| ALGORITHM_SOURCE_SURFACE_TEMPERATURE  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
| COLLECTION_CATEGORY  
| COLLECTION_NUMBER  
| CORRECTION_BIAS_BAND_1  
| CORRECTION_BIAS_BAND_2  
| CORRECTION_BIAS_BAND_3  
| CORRECTION_BIAS_BAND_4  
| CORRECTION_BIAS_BAND_5  
| CORRECTION_BIAS_BAND_6_VCID_1  
| CORRECTION_BIAS_BAND_6_VCID_2  
| CORRECTION_BIAS_BAND_7  
| CORRECTION_BIAS_BAND_8  
| CORRECTION_GAIN_BAND_1  
| CORRECTION_GAIN_BAND_2  
| CORRECTION_GAIN_BAND_3  
| CORRECTION_GAIN_BAND_4  
| CORRECTION_GAIN_BAND_5  
| CORRECTION_GAIN_BAND_6_VCID_1  
| CORRECTION_GAIN_BAND_6_VCID_2  
| CORRECTION_GAIN_BAND_7  
| CORRECTION_GAIN_BAND_8  
| DATA_SOURCE_AIR_TEMPERATURE  
| DATA_SOURCE_ELEVATION  
| DATA_SOURCE_OZONE  
| DATA_SOURCE_PRESSURE  
| DATA_SOURCE_REANALYSIS  
| DATA_SOURCE_WATER_VAPOR  
| DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
| DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
| ELLIPSOID  
| EPHEMERIS_TYPE  
ESPA_VERSION |   
| GAIN_BAND_1  
| GAIN_BAND_2  
| GAIN_BAND_3  
| GAIN_BAND_4  
| GAIN_BAND_5  
| GAIN_BAND_6_VCID_1  
| GAIN_BAND_6_VCID_2  
| GAIN_BAND_7  
| GAIN_BAND_8  
| GAIN_CHANGE_BAND_1  
| GAIN_CHANGE_BAND_2  
| GAIN_CHANGE_BAND_3  
| GAIN_CHANGE_BAND_4  
| GAIN_CHANGE_BAND_5  
| GAIN_CHANGE_BAND_6_VCID_1  
| GAIN_CHANGE_BAND_6_VCID_2  
| GAIN_CHANGE_BAND_7  
| GAIN_CHANGE_BAND_8  
| GAIN_CHANGE_SCAN_BAND_1  
| GAIN_CHANGE_SCAN_BAND_2  
| GAIN_CHANGE_SCAN_BAND_3  
| GAIN_CHANGE_SCAN_BAND_4  
| GAIN_CHANGE_SCAN_BAND_5  
| GAIN_CHANGE_SCAN_BAND_6_VCID_1  
| GAIN_CHANGE_SCAN_BAND_6_VCID_2  
| GAIN_CHANGE_SCAN_BAND_7  
| GAIN_CHANGE_SCAN_BAND_8  
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
| GRID_CELL_SIZE_REFLECTIVE  
| GRID_CELL_SIZE_THERMAL  
| GROUND_CONTROL_POINTS_MODEL  
| GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY | IMAGE_QUALITY  
| L1_DATE_PRODUCT_GENERATED  
| L1_LANDSAT_PRODUCT_ID  
| L1_PROCESSING_LEVEL  
| L1_PROCESSING_SOFTWARE_VERSION  
| L1_REQUEST_ID  
LANDSAT_ID |   
| LANDSAT_PRODUCT_ID  
| LANDSAT_SCENE_ID  
LEVEL1_PRODUCTION_DATE |   
| MAP_PROJECTION  
| ORIENTATION  
PIXEL_QA_VERSION |   
| PROCESSING_LEVEL  
| PROCESSING_SOFTWARE_VERSION  
| REFLECTANCE_ADD_BAND_1  
| REFLECTANCE_ADD_BAND_2  
| REFLECTANCE_ADD_BAND_3  
| REFLECTANCE_ADD_BAND_4  
| REFLECTANCE_ADD_BAND_5  
| REFLECTANCE_ADD_BAND_7  
| REFLECTANCE_MULT_BAND_1  
| REFLECTANCE_MULT_BAND_2  
| REFLECTANCE_MULT_BAND_3  
| REFLECTANCE_MULT_BAND_4  
| REFLECTANCE_MULT_BAND_5  
| REFLECTANCE_MULT_BAND_7  
| REFLECTIVE_LINES  
| REFLECTIVE_SAMPLES  
| REQUEST_ID  
SATELLITE |   
| SATURATION_BAND_1  
| SATURATION_BAND_2  
| SATURATION_BAND_3  
| SATURATION_BAND_4  
| SATURATION_BAND_5  
| SATURATION_BAND_6_VCID_1  
| SATURATION_BAND_6_VCID_2  
| SATURATION_BAND_7  
| SATURATION_BAND_8  
| SCENE_CENTER_TIME  
SENSING_TIME |   
| SENSOR_ANOMALIES  
| SENSOR_ID  
| SENSOR_MODE  
| SENSOR_MODE_SLC  
| SPACECRAFT_ID  
| STATION_ID  
**SOLAR_AZIMUTH_ANGLE** | **SUN_AZIMUTH**  
**SOLAR_ZENITH_ANGLE** | **SUN_ELEVATION** _(Collection 2 uses elevation instead of zenith angle. To calculate zenith angle, use`90 - elevation`.)_  
SR_APP_VERSION |   
| TEMPERATURE_ADD_BAND_ST_B6  
| TEMPERATURE_MAXIMUM_BAND_ST_B6  
| TEMPERATURE_MINIMUM_BAND_ST_B6  
| TEMPERATURE_MULT_BAND_ST_B6  
| THERMAL_LINES  
| THERMAL_SAMPLES  
| UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
### Asset ID
Replace `C01` with `C02` and `SR` with `L2` in image and collection IDs. For example, [Landsat 5 TM Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2):
Collection 1 | Collection 2  
---|---  
LANDSAT/LT05/**C01** /**T1_SR** | LANDSAT/LT05/**C02** /**T1_L2**  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Blue | **B1** | **SR_B1**  
Green | **B2** | **SR_B2**  
Red | **B3** | **SR_B3**  
Near infrared | **B4** | **SR_B4**  
Shortwave infrared 1 | **B5** | **SR_B5**  
TOA brightness temperature | **B6** |   
Shortwave infrared 2 | **B7** | **SR_B7**  
Atmospheric opacity | **sr_atmos_opacity** | **SR_ATMOS_OPACITY**  
Cloud quality assessment | **sr_cloud_qa** | **SR_CLOUD_QA**  
Surface temperature |  | **ST_B6**  
Atmospheric transmittance |  | **ST_ATRAN**  
Pixel distance to cloud |  | **ST_CDIST**  
Downwelled radiance |  | **ST_DRAD**  
Emissivity |  | **ST_EMIS**  
Emissivity standard deviation |  | **ST_EMSD**  
Surface temperature uncertainty |  | **ST_QA**  
Thermal radiance |  | **ST_TRAD**  
Upwelled radiance |  | **ST_URAD**  
Pixel quality attributes (CFMask) | **pixel_qa** | **QA_PIXEL**  
Radiometric saturation QA | **radsat_qa** | **QA_RADSAT**  
Update code that selects bands whose names have changed, for example, the near-infrared band:
Collection 1 | Collection 2  
---|---  
`image.select('B4')` | `image.select('SR_B4')`  
### Value scaling
Reflectance bands have new scaling factors. Collection 1 used a `0.0001` scale factor. Collection 2 uses a `2.75e-05` scale factor and `-0.2` offset. The thermal band also has new scale and offset factors. The following code block defines a function to apply Collection 2 surface reflectance and temperature band scaling factors and maps it over an image collection.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varapplyScaleFactors=function(image){
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBand=image.select('ST_B6').multiply(0.00341802).add(149.0);
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBand,null,true);
}
varsrColScaled=srCol.map(applyScaleFactors)
```
```
defapply_scale_factors(image):
 optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
 thermal_band = image.select('ST_B6').multiply(0.00341802).add(149.0)
 return image.addBands(optical_bands, None, True).addBands(
   thermal_band, None, True
 )
sr_col_scaled = sr_col.map(apply_scale_factors)
```

### QA masking
Bit codes have changed for the QA bitmask (CFMASK). See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2#bands)) and "Bitmask for pixel_qa" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1_SR#bands)) sections in catalog entries for codes (TM 5, for example).
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0)
```

### Radiometric saturation
Bit codes have changed for the radiometric saturation bitmask. See the "Bitmask for QA_RADSAT" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2#bands)) and "Bitmask for radsat_qa" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1_SR#bands)) sections in catalog entries for codes (TM 5, for example).
### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. Properties for solar geometry were altered. See the following property comparison table to determine whether you need to modify your code to accommodate missing, added, or altered properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2#image-properties) in the product's catalog page for Collection 2 property descriptions (TM 5, for example).
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
ALGORITHM_SOURCE_SURFACE_REFLECTANCE |   
| ALGORITHM_SOURCE_SURFACE_TEMPERATURE  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
| COLLECTION_CATEGORY  
| COLLECTION_NUMBER  
| CORRECTION_BIAS_BAND_1  
| CORRECTION_BIAS_BAND_2  
| CORRECTION_BIAS_BAND_3  
| CORRECTION_BIAS_BAND_4  
| CORRECTION_BIAS_BAND_5  
| CORRECTION_BIAS_BAND_6  
| CORRECTION_BIAS_BAND_7  
| CORRECTION_GAIN_BAND_1  
| CORRECTION_GAIN_BAND_2  
| CORRECTION_GAIN_BAND_3  
| CORRECTION_GAIN_BAND_4  
| CORRECTION_GAIN_BAND_5  
| CORRECTION_GAIN_BAND_6  
| CORRECTION_GAIN_BAND_7  
| DATA_SOURCE_AIR_TEMPERATURE  
| DATA_SOURCE_ELEVATION  
| DATA_SOURCE_OZONE  
| DATA_SOURCE_PRESSURE  
| DATA_SOURCE_REANALYSIS  
| DATA_SOURCE_WATER_VAPOR  
| DATA_TYPE_L0RP  
| DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
| DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
| ELLIPSOID  
| EPHEMERIS_TYPE  
ESPA_VERSION |   
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
| GEOMETRIC_RMSE_VERIFY  
| GEOMETRIC_RMSE_VERIFY_QUAD_LL  
| GEOMETRIC_RMSE_VERIFY_QUAD_LR  
| GEOMETRIC_RMSE_VERIFY_QUAD_UL  
| GEOMETRIC_RMSE_VERIFY_QUAD_UR  
| GRID_CELL_SIZE_REFLECTIVE  
| GRID_CELL_SIZE_THERMAL  
| GROUND_CONTROL_POINTS_MODEL  
| GROUND_CONTROL_POINTS_VERIFY  
| GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY | IMAGE_QUALITY  
| L1_DATE_PRODUCT_GENERATED  
| L1_LANDSAT_PRODUCT_ID  
| L1_PROCESSING_LEVEL  
| L1_PROCESSING_SOFTWARE_VERSION  
| L1_REQUEST_ID  
LANDSAT_ID |   
| LANDSAT_PRODUCT_ID  
| LANDSAT_SCENE_ID  
LEVEL1_PRODUCTION_DATE |   
| MAP_PROJECTION  
| ORIENTATION  
PIXEL_QA_VERSION |   
| PROCESSING_LEVEL  
| PROCESSING_SOFTWARE_VERSION  
| REFLECTANCE_ADD_BAND_1  
| REFLECTANCE_ADD_BAND_2  
| REFLECTANCE_ADD_BAND_3  
| REFLECTANCE_ADD_BAND_4  
| REFLECTANCE_ADD_BAND_5  
| REFLECTANCE_ADD_BAND_7  
| REFLECTANCE_MULT_BAND_1  
| REFLECTANCE_MULT_BAND_2  
| REFLECTANCE_MULT_BAND_3  
| REFLECTANCE_MULT_BAND_4  
| REFLECTANCE_MULT_BAND_5  
| REFLECTANCE_MULT_BAND_7  
| REFLECTIVE_LINES  
| REFLECTIVE_SAMPLES  
| REQUEST_ID  
SATELLITE |   
| SATURATION_BAND_1  
| SATURATION_BAND_2  
| SATURATION_BAND_3  
| SATURATION_BAND_4  
| SATURATION_BAND_5  
| SATURATION_BAND_6  
| SATURATION_BAND_7  
| SCENE_CENTER_TIME  
SENSING_TIME |   
| SENSOR_ANOMALIES  
| SENSOR_ID  
| SENSOR_MODE  
| SENSOR_MODE_SLC  
| SPACECRAFT_ID  
| STATION_ID  
**SOLAR_AZIMUTH_ANGLE** | **SUN_AZIMUTH**  
**SOLAR_ZENITH_ANGLE** | **SUN_ELEVATION** _(Collection 2 uses elevation instead of zenith angle. To calculate zenith angle, use`90 - elevation`.)_  
SR_APP_VERSION |   
| TEMPERATURE_ADD_BAND_ST_B6  
| TEMPERATURE_MAXIMUM_BAND_ST_B6  
| TEMPERATURE_MINIMUM_BAND_ST_B6  
| TEMPERATURE_MULT_BAND_ST_B6  
| THERMAL_LINES  
| THERMAL_SAMPLES  
| UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
## Top-of-atmosphere reflectance
[OLI](https://developers.google.com/earth-engine/landsat_c1_to_c2#oli)[ETM+](https://developers.google.com/earth-engine/landsat_c1_to_c2#etm+)[TM](https://developers.google.com/earth-engine/landsat_c1_to_c2#tm) More
### Asset ID
Replace `C01` with `C02` in image and collection IDs. For example, [Landsat 8 OLI Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_TOA) (Landsat 9 OLI-2 was not included in Collection 1):
Collection 1 | Collection 2  
---|---  
LANDSAT/LC08/**C01** /T1_TOA | LANDSAT/LC08/**C02** /T1_TOA  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Coastal aerosol | B1 | B1  
Blue | B2 | B2  
Green | B3 | B3  
Red | B4 | B4  
Near infrared | B5 | B5  
Shortwave infrared 1 | B6 | B6  
Shortwave infrared 2 | B7 | B7  
Panchromatic | B8 | B8  
Cirrus | B9 | B9  
Thermal infrared 1 | B10 | B10  
Thermal infrared 2 | B11 | B11  
QA bitmask | **BQA** | **QA_PIXEL**  
Radiometric saturation QA |  | **QA_RADSAT**  
Solar azimuth angle |  | **SAA**  
Solar zenith angle |  | **SZA**  
View azimuth angle |  | **VAA**  
View zenith angle |  | **VZA**  
Update code that selects bands whose names have changed, for example, the QA bitmask band:
Collection 1 | Collection 2  
---|---  
`image.select('BQA')` | `image.select('QA_PIXEL')`  
### Value scaling
No changes required. Collection 1 and Collection 2 have the same scaling for top-of-atmosphere reflectance and thermal values.
### QA masking
Bit codes have changed for the QA bitmask. See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_TOA#bands)) and "Bitmask for BQA" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_TOA#bands)) sections in catalog entries for codes.
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11010',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11010', 2)).eq(0)
```

### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. No property names were changed. See the following property comparison table to determine whether you need to modify your code to accommodate missing or added properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_TOA#image-properties) in the product's catalog page for Collection 2 property descriptions.
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
BPF_NAME_OLI |   
BPF_NAME_TIRS |   
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
COLLECTION_CATEGORY | COLLECTION_CATEGORY  
COLLECTION_NUMBER | COLLECTION_NUMBER  
CPF_NAME |   
| DATA_SOURCE_ELEVATION  
| DATA_SOURCE_TIRS_STRAY_LIGHT_CORRECTION  
DATA_TYPE |   
DATE_ACQUIRED | DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
DATUM | DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
ELEVATION_SOURCE |   
ELLIPSOID | ELLIPSOID  
FILE_DATE |   
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
GEOMETRIC_RMSE_VERIFY | GEOMETRIC_RMSE_VERIFY  
GRID_CELL_SIZE_PANCHROMATIC | GRID_CELL_SIZE_PANCHROMATIC  
GRID_CELL_SIZE_REFLECTIVE | GRID_CELL_SIZE_REFLECTIVE  
GRID_CELL_SIZE_THERMAL | GRID_CELL_SIZE_THERMAL  
GROUND_CONTROL_POINTS_MODEL | GROUND_CONTROL_POINTS_MODEL  
GROUND_CONTROL_POINTS_VERIFY | GROUND_CONTROL_POINTS_VERIFY  
GROUND_CONTROL_POINTS_VERSION | GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY_OLI | IMAGE_QUALITY_OLI  
IMAGE_QUALITY_TIRS | IMAGE_QUALITY_TIRS  
K1_CONSTANT_BAND_10 | K1_CONSTANT_BAND_10  
K1_CONSTANT_BAND_11 | K1_CONSTANT_BAND_11  
K2_CONSTANT_BAND_10 | K2_CONSTANT_BAND_10  
K2_CONSTANT_BAND_11 | K2_CONSTANT_BAND_11  
LANDSAT_PRODUCT_ID | LANDSAT_PRODUCT_ID  
LANDSAT_SCENE_ID | LANDSAT_SCENE_ID  
MAP_PROJECTION | MAP_PROJECTION  
NADIR_OFFNADIR | NADIR_OFFNADIR  
ORIENTATION | ORIENTATION  
PANCHROMATIC_LINES | PANCHROMATIC_LINES  
PANCHROMATIC_SAMPLES | PANCHROMATIC_SAMPLES  
| PROCESSING_LEVEL  
PROCESSING_SOFTWARE_VERSION | PROCESSING_SOFTWARE_VERSION  
RADIANCE_ADD_BAND_1 | RADIANCE_ADD_BAND_1  
RADIANCE_ADD_BAND_10 | RADIANCE_ADD_BAND_10  
RADIANCE_ADD_BAND_11 | RADIANCE_ADD_BAND_11  
RADIANCE_ADD_BAND_2 | RADIANCE_ADD_BAND_2  
RADIANCE_ADD_BAND_3 | RADIANCE_ADD_BAND_3  
RADIANCE_ADD_BAND_4 | RADIANCE_ADD_BAND_4  
RADIANCE_ADD_BAND_5 | RADIANCE_ADD_BAND_5  
RADIANCE_ADD_BAND_6 | RADIANCE_ADD_BAND_6  
RADIANCE_ADD_BAND_7 | RADIANCE_ADD_BAND_7  
RADIANCE_ADD_BAND_8 | RADIANCE_ADD_BAND_8  
RADIANCE_ADD_BAND_9 | RADIANCE_ADD_BAND_9  
RADIANCE_MULT_BAND_1 | RADIANCE_MULT_BAND_1  
RADIANCE_MULT_BAND_10 | RADIANCE_MULT_BAND_10  
RADIANCE_MULT_BAND_11 | RADIANCE_MULT_BAND_11  
RADIANCE_MULT_BAND_2 | RADIANCE_MULT_BAND_2  
RADIANCE_MULT_BAND_3 | RADIANCE_MULT_BAND_3  
RADIANCE_MULT_BAND_4 | RADIANCE_MULT_BAND_4  
RADIANCE_MULT_BAND_5 | RADIANCE_MULT_BAND_5  
RADIANCE_MULT_BAND_6 | RADIANCE_MULT_BAND_6  
RADIANCE_MULT_BAND_7 | RADIANCE_MULT_BAND_7  
RADIANCE_MULT_BAND_8 | RADIANCE_MULT_BAND_8  
RADIANCE_MULT_BAND_9 | RADIANCE_MULT_BAND_9  
REFLECTANCE_ADD_BAND_1 | REFLECTANCE_ADD_BAND_1  
REFLECTANCE_ADD_BAND_2 | REFLECTANCE_ADD_BAND_2  
REFLECTANCE_ADD_BAND_3 | REFLECTANCE_ADD_BAND_3  
REFLECTANCE_ADD_BAND_4 | REFLECTANCE_ADD_BAND_4  
REFLECTANCE_ADD_BAND_5 | REFLECTANCE_ADD_BAND_5  
REFLECTANCE_ADD_BAND_6 | REFLECTANCE_ADD_BAND_6  
REFLECTANCE_ADD_BAND_7 | REFLECTANCE_ADD_BAND_7  
REFLECTANCE_ADD_BAND_8 | REFLECTANCE_ADD_BAND_8  
REFLECTANCE_ADD_BAND_9 | REFLECTANCE_ADD_BAND_9  
REFLECTANCE_MULT_BAND_1 | REFLECTANCE_MULT_BAND_1  
REFLECTANCE_MULT_BAND_2 | REFLECTANCE_MULT_BAND_2  
REFLECTANCE_MULT_BAND_3 | REFLECTANCE_MULT_BAND_3  
REFLECTANCE_MULT_BAND_4 | REFLECTANCE_MULT_BAND_4  
REFLECTANCE_MULT_BAND_5 | REFLECTANCE_MULT_BAND_5  
REFLECTANCE_MULT_BAND_6 | REFLECTANCE_MULT_BAND_6  
REFLECTANCE_MULT_BAND_7 | REFLECTANCE_MULT_BAND_7  
REFLECTANCE_MULT_BAND_8 | REFLECTANCE_MULT_BAND_8  
REFLECTANCE_MULT_BAND_9 | REFLECTANCE_MULT_BAND_9  
REFLECTIVE_LINES | REFLECTIVE_LINES  
REFLECTIVE_SAMPLES | REFLECTIVE_SAMPLES  
REQUEST_ID | REQUEST_ID  
RESAMPLING_OPTION | RESAMPLING_OPTION  
RLUT_FILE_NAME |   
ROLL_ANGLE | ROLL_ANGLE  
SATURATION_BAND_1 | SATURATION_BAND_1  
SATURATION_BAND_2 | SATURATION_BAND_2  
SATURATION_BAND_3 | SATURATION_BAND_3  
SATURATION_BAND_4 | SATURATION_BAND_4  
SATURATION_BAND_5 | SATURATION_BAND_5  
SATURATION_BAND_6 | SATURATION_BAND_6  
SATURATION_BAND_7 | SATURATION_BAND_7  
SATURATION_BAND_8 | SATURATION_BAND_8  
SATURATION_BAND_9 | SATURATION_BAND_9  
SCENE_CENTER_TIME | SCENE_CENTER_TIME  
SENSOR_ID | SENSOR_ID  
SPACECRAFT_ID | SPACECRAFT_ID  
STATION_ID | STATION_ID  
SUN_AZIMUTH | SUN_AZIMUTH  
SUN_ELEVATION | SUN_ELEVATION  
TARGET_WRS_PATH | TARGET_WRS_PATH  
TARGET_WRS_ROW | TARGET_WRS_ROW  
THERMAL_LINES | THERMAL_LINES  
THERMAL_SAMPLES | THERMAL_SAMPLES  
TIRS_SSM_MODEL | TIRS_SSM_MODEL  
TIRS_SSM_POSITION_STATUS | TIRS_SSM_POSITION_STATUS  
TIRS_STRAY_LIGHT_CORRECTION_SOURCE |   
TRUNCATION_OLI | TRUNCATION_OLI  
UTM_ZONE | UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
google:registration_count |   
google:registration_offset_x |   
google:registration_offset_y |   
google:registration_ratio |   
### Asset ID
Replace `C01` with `C02` in image and collection IDs. For example, [Landsat 7 ETM+ Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_TOA):
Collection 1 | Collection 2  
---|---  
LANDSAT/LE07/**C01** /T1_TOA | LANDSAT/LE07/**C02** /T1_TOA  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Blue | B1 | B1  
Green | B2 | B2  
Red | B3 | B3  
Near infrared | B4 | B4  
Shortwave infrared 1 | B5 | B5  
Low-gain thermal infrared 1 | B6_VCID_1 | B6_VCID_1  
High-gain thermal infrared 1 | B6_VCID_2 | B6_VCID_2  
Shortwave infrared 2 | B7 | B7  
Panchromatic | B8 | B8  
QA bitmask | **BQA** | **QA_PIXEL**  
Radiometric saturation QA |  | **QA_RADSAT**  
Solar azimuth angle |  | **SAA**  
Solar zenith angle |  | **SZA**  
View azimuth angle |  | **VAA**  
View zenith angle |  | **VZA**  
Update code that selects bands whose names have changed, for example, the QA bitmask band:
Collection 1 | Collection 2  
---|---  
`image.select('BQA')` | `image.select('QA_PIXEL')`  
### Value scaling
No changes required. Collection 1 and Collection 2 have the same scaling for top-of-atmosphere reflectance and thermal values.
### QA masking
Bit codes have changed for the QA bitmask. See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_TOA#bands)) and "Bitmask for BQA" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1_TOA#bands)) sections in catalog entries for codes.
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11010',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11010', 2)).eq(0)
```

### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. No property names were changed. See the following property comparison table to determine whether you need to modify your code to accommodate missing or added properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_TOA#image-properties) in the product's catalog page for Collection 2 property descriptions.
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
COLLECTION_CATEGORY | COLLECTION_CATEGORY  
COLLECTION_NUMBER | COLLECTION_NUMBER  
CORRECTION_BIAS_BAND_1 | CORRECTION_BIAS_BAND_1  
CORRECTION_BIAS_BAND_2 | CORRECTION_BIAS_BAND_2  
CORRECTION_BIAS_BAND_3 | CORRECTION_BIAS_BAND_3  
CORRECTION_BIAS_BAND_4 | CORRECTION_BIAS_BAND_4  
CORRECTION_BIAS_BAND_5 | CORRECTION_BIAS_BAND_5  
CORRECTION_BIAS_BAND_6_VCID_1 | CORRECTION_BIAS_BAND_6_VCID_1  
CORRECTION_BIAS_BAND_6_VCID_2 | CORRECTION_BIAS_BAND_6_VCID_2  
CORRECTION_BIAS_BAND_7 | CORRECTION_BIAS_BAND_7  
CORRECTION_BIAS_BAND_8 | CORRECTION_BIAS_BAND_8  
CORRECTION_GAIN_BAND_1 | CORRECTION_GAIN_BAND_1  
CORRECTION_GAIN_BAND_2 | CORRECTION_GAIN_BAND_2  
CORRECTION_GAIN_BAND_3 | CORRECTION_GAIN_BAND_3  
CORRECTION_GAIN_BAND_4 | CORRECTION_GAIN_BAND_4  
CORRECTION_GAIN_BAND_5 | CORRECTION_GAIN_BAND_5  
CORRECTION_GAIN_BAND_6_VCID_1 | CORRECTION_GAIN_BAND_6_VCID_1  
CORRECTION_GAIN_BAND_6_VCID_2 | CORRECTION_GAIN_BAND_6_VCID_2  
CORRECTION_GAIN_BAND_7 | CORRECTION_GAIN_BAND_7  
CORRECTION_GAIN_BAND_8 | CORRECTION_GAIN_BAND_8  
CPF_NAME |   
DATA_CATEGORY |   
| DATA_SOURCE_ELEVATION  
DATA_TYPE |   
DATE_ACQUIRED | DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
DATUM | DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
ELEVATION_SOURCE |   
ELLIPSOID | ELLIPSOID  
EPHEMERIS_TYPE | EPHEMERIS_TYPE  
FILE_DATE |   
GAIN_BAND_1 | GAIN_BAND_1  
GAIN_BAND_2 | GAIN_BAND_2  
GAIN_BAND_3 | GAIN_BAND_3  
GAIN_BAND_4 | GAIN_BAND_4  
GAIN_BAND_5 | GAIN_BAND_5  
GAIN_BAND_6_VCID_1 | GAIN_BAND_6_VCID_1  
GAIN_BAND_6_VCID_2 | GAIN_BAND_6_VCID_2  
GAIN_BAND_7 | GAIN_BAND_7  
GAIN_BAND_8 | GAIN_BAND_8  
GAIN_CHANGE_BAND_1 | GAIN_CHANGE_BAND_1  
GAIN_CHANGE_BAND_2 | GAIN_CHANGE_BAND_2  
GAIN_CHANGE_BAND_3 | GAIN_CHANGE_BAND_3  
GAIN_CHANGE_BAND_4 | GAIN_CHANGE_BAND_4  
GAIN_CHANGE_BAND_5 | GAIN_CHANGE_BAND_5  
GAIN_CHANGE_BAND_6_VCID_1 | GAIN_CHANGE_BAND_6_VCID_1  
GAIN_CHANGE_BAND_6_VCID_2 | GAIN_CHANGE_BAND_6_VCID_2  
GAIN_CHANGE_BAND_7 | GAIN_CHANGE_BAND_7  
GAIN_CHANGE_BAND_8 | GAIN_CHANGE_BAND_8  
GAIN_CHANGE_SCAN_BAND_1 | GAIN_CHANGE_SCAN_BAND_1  
GAIN_CHANGE_SCAN_BAND_2 | GAIN_CHANGE_SCAN_BAND_2  
GAIN_CHANGE_SCAN_BAND_3 | GAIN_CHANGE_SCAN_BAND_3  
GAIN_CHANGE_SCAN_BAND_4 | GAIN_CHANGE_SCAN_BAND_4  
GAIN_CHANGE_SCAN_BAND_5 | GAIN_CHANGE_SCAN_BAND_5  
GAIN_CHANGE_SCAN_BAND_6_VCID_1 | GAIN_CHANGE_SCAN_BAND_6_VCID_1  
GAIN_CHANGE_SCAN_BAND_6_VCID_2 | GAIN_CHANGE_SCAN_BAND_6_VCID_2  
GAIN_CHANGE_SCAN_BAND_7 | GAIN_CHANGE_SCAN_BAND_7  
GAIN_CHANGE_SCAN_BAND_8 | GAIN_CHANGE_SCAN_BAND_8  
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
GRID_CELL_SIZE_PANCHROMATIC | GRID_CELL_SIZE_PANCHROMATIC  
GRID_CELL_SIZE_REFLECTIVE | GRID_CELL_SIZE_REFLECTIVE  
GRID_CELL_SIZE_THERMAL | GRID_CELL_SIZE_THERMAL  
GROUND_CONTROL_POINTS_MODEL | GROUND_CONTROL_POINTS_MODEL  
GROUND_CONTROL_POINTS_VERSION | GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY | IMAGE_QUALITY  
K1_CONSTANT_BAND_6_VCID_1 | K1_CONSTANT_BAND_6_VCID_1  
K1_CONSTANT_BAND_6_VCID_2 | K1_CONSTANT_BAND_6_VCID_2  
K2_CONSTANT_BAND_6_VCID_1 | K2_CONSTANT_BAND_6_VCID_1  
K2_CONSTANT_BAND_6_VCID_2 | K2_CONSTANT_BAND_6_VCID_2  
LANDSAT_PRODUCT_ID | LANDSAT_PRODUCT_ID  
LANDSAT_SCENE_ID | LANDSAT_SCENE_ID  
MAP_PROJECTION | MAP_PROJECTION  
ORIENTATION | ORIENTATION  
PANCHROMATIC_LINES | PANCHROMATIC_LINES  
PANCHROMATIC_SAMPLES | PANCHROMATIC_SAMPLES  
| PROCESSING_LEVEL  
PROCESSING_SOFTWARE_VERSION | PROCESSING_SOFTWARE_VERSION  
RADIANCE_ADD_BAND_1 | RADIANCE_ADD_BAND_1  
RADIANCE_ADD_BAND_2 | RADIANCE_ADD_BAND_2  
RADIANCE_ADD_BAND_3 | RADIANCE_ADD_BAND_3  
RADIANCE_ADD_BAND_4 | RADIANCE_ADD_BAND_4  
RADIANCE_ADD_BAND_5 | RADIANCE_ADD_BAND_5  
RADIANCE_ADD_BAND_6_VCID_1 | RADIANCE_ADD_BAND_6_VCID_1  
RADIANCE_ADD_BAND_6_VCID_2 | RADIANCE_ADD_BAND_6_VCID_2  
RADIANCE_ADD_BAND_7 | RADIANCE_ADD_BAND_7  
RADIANCE_ADD_BAND_8 | RADIANCE_ADD_BAND_8  
RADIANCE_MAXIMUM_BAND_1 |   
RADIANCE_MAXIMUM_BAND_2 |   
RADIANCE_MAXIMUM_BAND_3 |   
RADIANCE_MAXIMUM_BAND_4 |   
RADIANCE_MAXIMUM_BAND_5 |   
RADIANCE_MAXIMUM_BAND_6_VCID_1 |   
RADIANCE_MAXIMUM_BAND_6_VCID_2 |   
RADIANCE_MAXIMUM_BAND_7 |   
RADIANCE_MAXIMUM_BAND_8 |   
RADIANCE_MINIMUM_BAND_1 |   
RADIANCE_MINIMUM_BAND_2 |   
RADIANCE_MINIMUM_BAND_3 |   
RADIANCE_MINIMUM_BAND_4 |   
RADIANCE_MINIMUM_BAND_5 |   
RADIANCE_MINIMUM_BAND_6_VCID_1 |   
RADIANCE_MINIMUM_BAND_6_VCID_2 |   
RADIANCE_MINIMUM_BAND_7 |   
RADIANCE_MINIMUM_BAND_8 |   
RADIANCE_MULT_BAND_1 | RADIANCE_MULT_BAND_1  
RADIANCE_MULT_BAND_2 | RADIANCE_MULT_BAND_2  
RADIANCE_MULT_BAND_3 | RADIANCE_MULT_BAND_3  
RADIANCE_MULT_BAND_4 | RADIANCE_MULT_BAND_4  
RADIANCE_MULT_BAND_5 | RADIANCE_MULT_BAND_5  
RADIANCE_MULT_BAND_6_VCID_1 | RADIANCE_MULT_BAND_6_VCID_1  
RADIANCE_MULT_BAND_6_VCID_2 | RADIANCE_MULT_BAND_6_VCID_2  
RADIANCE_MULT_BAND_7 | RADIANCE_MULT_BAND_7  
RADIANCE_MULT_BAND_8 | RADIANCE_MULT_BAND_8  
REFLECTANCE_ADD_BAND_1 | REFLECTANCE_ADD_BAND_1  
REFLECTANCE_ADD_BAND_2 | REFLECTANCE_ADD_BAND_2  
REFLECTANCE_ADD_BAND_3 | REFLECTANCE_ADD_BAND_3  
REFLECTANCE_ADD_BAND_4 | REFLECTANCE_ADD_BAND_4  
REFLECTANCE_ADD_BAND_5 | REFLECTANCE_ADD_BAND_5  
REFLECTANCE_ADD_BAND_7 | REFLECTANCE_ADD_BAND_7  
REFLECTANCE_ADD_BAND_8 | REFLECTANCE_ADD_BAND_8  
REFLECTANCE_MAXIMUM_BAND_1 |   
REFLECTANCE_MAXIMUM_BAND_2 |   
REFLECTANCE_MAXIMUM_BAND_3 |   
REFLECTANCE_MAXIMUM_BAND_4 |   
REFLECTANCE_MAXIMUM_BAND_5 |   
REFLECTANCE_MAXIMUM_BAND_7 |   
REFLECTANCE_MAXIMUM_BAND_8 |   
REFLECTANCE_MINIMUM_BAND_1 |   
REFLECTANCE_MINIMUM_BAND_2 |   
REFLECTANCE_MINIMUM_BAND_3 |   
REFLECTANCE_MINIMUM_BAND_4 |   
REFLECTANCE_MINIMUM_BAND_5 |   
REFLECTANCE_MINIMUM_BAND_7 |   
REFLECTANCE_MINIMUM_BAND_8 |   
REFLECTANCE_MULT_BAND_1 | REFLECTANCE_MULT_BAND_1  
REFLECTANCE_MULT_BAND_2 | REFLECTANCE_MULT_BAND_2  
REFLECTANCE_MULT_BAND_3 | REFLECTANCE_MULT_BAND_3  
REFLECTANCE_MULT_BAND_4 | REFLECTANCE_MULT_BAND_4  
REFLECTANCE_MULT_BAND_5 | REFLECTANCE_MULT_BAND_5  
REFLECTANCE_MULT_BAND_7 | REFLECTANCE_MULT_BAND_7  
REFLECTANCE_MULT_BAND_8 | REFLECTANCE_MULT_BAND_8  
REFLECTIVE_LINES | REFLECTIVE_LINES  
REFLECTIVE_SAMPLES | REFLECTIVE_SAMPLES  
REQUEST_ID | REQUEST_ID  
RESAMPLING_OPTION | RESAMPLING_OPTION  
SATURATION_BAND_1 | SATURATION_BAND_1  
SATURATION_BAND_2 | SATURATION_BAND_2  
SATURATION_BAND_3 | SATURATION_BAND_3  
SATURATION_BAND_4 | SATURATION_BAND_4  
SATURATION_BAND_5 | SATURATION_BAND_5  
SATURATION_BAND_6_VCID_1 | SATURATION_BAND_6_VCID_1  
SATURATION_BAND_6_VCID_2 | SATURATION_BAND_6_VCID_2  
SATURATION_BAND_7 | SATURATION_BAND_7  
SATURATION_BAND_8 | SATURATION_BAND_8  
SCENE_CENTER_TIME | SCENE_CENTER_TIME  
| SENSOR_ANOMALIES  
SENSOR_ID | SENSOR_ID  
SENSOR_MODE | SENSOR_MODE  
| SENSOR_MODE_SLC  
SPACECRAFT_ID | SPACECRAFT_ID  
STATION_ID | STATION_ID  
SUN_AZIMUTH | SUN_AZIMUTH  
SUN_ELEVATION | SUN_ELEVATION  
THERMAL_LINES | THERMAL_LINES  
THERMAL_SAMPLES | THERMAL_SAMPLES  
UTM_ZONE | UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
google:registration_count |   
google:registration_offset_x |   
google:registration_offset_y |   
google:registration_ratio |   
### Asset ID
Replace `C01` with `C02` in image and collection IDs. For example, [Landsat 5 TM Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_TOA):
Collection 1 | Collection 2  
---|---  
LANDSAT/LT05/**C01** /T1_TOA | LANDSAT/LT05/**C02** /T1_TOA  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Blue | B1 | B1  
Green | B2 | B2  
Red | B3 | B3  
Near infrared | B4 | B4  
Shortwave infrared 1 | B5 | B5  
Thermal infrared 1 | B6 | B6  
Shortwave infrared 2 | B7 | B7  
QA bitmask | **BQA** | **QA_PIXEL**  
Radiometric saturation QA |  | **QA_RADSAT**  
Solar azimuth angle |  | **SAA**  
Solar zenith angle |  | **SZA**  
View azimuth angle |  | **VAA**  
View zenith angle |  | **VZA**  
Update code that selects bands whose names have changed, for example, the QA bitmask band:
Collection 1 | Collection 2  
---|---  
`image.select('BQA')` | `image.select('QA_PIXEL')`  
### Value scaling
No changes required. Collection 1 and Collection 2 have the same scaling for top-of-atmosphere reflectance and thermal values.
### QA masking
Bit codes have changed for the QA bitmask. See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_TOA#bands)) and "Bitmask for BQA" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1_TOA#bands)) sections in catalog entries for codes (TM 5, for example).
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11010',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11010', 2)).eq(0)
```

### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. No property names were changed. See the following property comparison table to determine whether you need to modify your code to accommodate missing or added properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_TOA#image-properties) in the product's catalog page for Collection 2 property descriptions (TM 5, for example).
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
COLLECTION_CATEGORY | COLLECTION_CATEGORY  
COLLECTION_NUMBER | COLLECTION_NUMBER  
CORNER_LL_LAT_PRODUCT |   
CORNER_LL_LON_PRODUCT |   
CORNER_LL_PROJECTION_X_PRODUCT |   
CORNER_LL_PROJECTION_Y_PRODUCT |   
CORNER_LR_LAT_PRODUCT |   
CORNER_LR_LON_PRODUCT |   
CORNER_LR_PROJECTION_X_PRODUCT |   
CORNER_LR_PROJECTION_Y_PRODUCT |   
CORNER_UL_LAT_PRODUCT |   
CORNER_UL_LON_PRODUCT |   
CORNER_UL_PROJECTION_X_PRODUCT |   
CORNER_UL_PROJECTION_Y_PRODUCT |   
CORNER_UR_LAT_PRODUCT |   
CORNER_UR_LON_PRODUCT |   
CORNER_UR_PROJECTION_X_PRODUCT |   
CORNER_UR_PROJECTION_Y_PRODUCT |   
CORRECTION_BIAS_BAND_1 | CORRECTION_BIAS_BAND_1  
CORRECTION_BIAS_BAND_2 | CORRECTION_BIAS_BAND_2  
CORRECTION_BIAS_BAND_3 | CORRECTION_BIAS_BAND_3  
CORRECTION_BIAS_BAND_4 | CORRECTION_BIAS_BAND_4  
CORRECTION_BIAS_BAND_5 | CORRECTION_BIAS_BAND_5  
CORRECTION_BIAS_BAND_6 | CORRECTION_BIAS_BAND_6  
CORRECTION_BIAS_BAND_7 | CORRECTION_BIAS_BAND_7  
CORRECTION_GAIN_BAND_1 | CORRECTION_GAIN_BAND_1  
CORRECTION_GAIN_BAND_2 | CORRECTION_GAIN_BAND_2  
CORRECTION_GAIN_BAND_3 | CORRECTION_GAIN_BAND_3  
CORRECTION_GAIN_BAND_4 | CORRECTION_GAIN_BAND_4  
CORRECTION_GAIN_BAND_5 | CORRECTION_GAIN_BAND_5  
CORRECTION_GAIN_BAND_6 | CORRECTION_GAIN_BAND_6  
CORRECTION_GAIN_BAND_7 | CORRECTION_GAIN_BAND_7  
CPF_NAME |   
DATA_CATEGORY |   
| DATA_SOURCE_ELEVATION  
DATA_TYPE |   
DATA_TYPE_L0RP | DATA_TYPE_L0RP  
DATE_ACQUIRED | DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
DATUM | DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
ELEVATION_SOURCE |   
ELLIPSOID | ELLIPSOID  
EPHEMERIS_TYPE | EPHEMERIS_TYPE  
FILE_DATE |   
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
GEOMETRIC_RMSE_VERIFY | GEOMETRIC_RMSE_VERIFY  
GEOMETRIC_RMSE_VERIFY_QUAD_LL | GEOMETRIC_RMSE_VERIFY_QUAD_LL  
GEOMETRIC_RMSE_VERIFY_QUAD_LR | GEOMETRIC_RMSE_VERIFY_QUAD_LR  
GEOMETRIC_RMSE_VERIFY_QUAD_UL | GEOMETRIC_RMSE_VERIFY_QUAD_UL  
GEOMETRIC_RMSE_VERIFY_QUAD_UR | GEOMETRIC_RMSE_VERIFY_QUAD_UR  
GRID_CELL_SIZE_REFLECTIVE | GRID_CELL_SIZE_REFLECTIVE  
GRID_CELL_SIZE_THERMAL | GRID_CELL_SIZE_THERMAL  
GROUND_CONTROL_POINTS_MODEL | GROUND_CONTROL_POINTS_MODEL  
GROUND_CONTROL_POINTS_VERIFY | GROUND_CONTROL_POINTS_VERIFY  
GROUND_CONTROL_POINTS_VERSION | GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY | IMAGE_QUALITY  
K1_CONSTANT_BAND_6 | K1_CONSTANT_BAND_6  
K2_CONSTANT_BAND_6 | K2_CONSTANT_BAND_6  
LANDSAT_PRODUCT_ID | LANDSAT_PRODUCT_ID  
LANDSAT_SCENE_ID | LANDSAT_SCENE_ID  
MAP_PROJECTION | MAP_PROJECTION  
MAP_PROJECTION_L0RA | MAP_PROJECTION_L0RA  
ORIENTATION | ORIENTATION  
| PROCESSING_LEVEL  
PROCESSING_SOFTWARE_VERSION | PROCESSING_SOFTWARE_VERSION  
RADIANCE_ADD_BAND_1 | RADIANCE_ADD_BAND_1  
RADIANCE_ADD_BAND_2 | RADIANCE_ADD_BAND_2  
RADIANCE_ADD_BAND_3 | RADIANCE_ADD_BAND_3  
RADIANCE_ADD_BAND_4 | RADIANCE_ADD_BAND_4  
RADIANCE_ADD_BAND_5 | RADIANCE_ADD_BAND_5  
RADIANCE_ADD_BAND_6 | RADIANCE_ADD_BAND_6  
RADIANCE_ADD_BAND_7 | RADIANCE_ADD_BAND_7  
RADIANCE_MAXIMUM_BAND_1 |   
RADIANCE_MAXIMUM_BAND_2 |   
RADIANCE_MAXIMUM_BAND_3 |   
RADIANCE_MAXIMUM_BAND_4 |   
RADIANCE_MAXIMUM_BAND_5 |   
RADIANCE_MAXIMUM_BAND_6 |   
RADIANCE_MAXIMUM_BAND_7 |   
RADIANCE_MINIMUM_BAND_1 |   
RADIANCE_MINIMUM_BAND_2 |   
RADIANCE_MINIMUM_BAND_3 |   
RADIANCE_MINIMUM_BAND_4 |   
RADIANCE_MINIMUM_BAND_5 |   
RADIANCE_MINIMUM_BAND_6 |   
RADIANCE_MINIMUM_BAND_7 |   
RADIANCE_MULT_BAND_1 | RADIANCE_MULT_BAND_1  
RADIANCE_MULT_BAND_2 | RADIANCE_MULT_BAND_2  
RADIANCE_MULT_BAND_3 | RADIANCE_MULT_BAND_3  
RADIANCE_MULT_BAND_4 | RADIANCE_MULT_BAND_4  
RADIANCE_MULT_BAND_5 | RADIANCE_MULT_BAND_5  
RADIANCE_MULT_BAND_6 | RADIANCE_MULT_BAND_6  
RADIANCE_MULT_BAND_7 | RADIANCE_MULT_BAND_7  
REFLECTANCE_ADD_BAND_1 | REFLECTANCE_ADD_BAND_1  
REFLECTANCE_ADD_BAND_2 | REFLECTANCE_ADD_BAND_2  
REFLECTANCE_ADD_BAND_3 | REFLECTANCE_ADD_BAND_3  
REFLECTANCE_ADD_BAND_4 | REFLECTANCE_ADD_BAND_4  
REFLECTANCE_ADD_BAND_5 | REFLECTANCE_ADD_BAND_5  
REFLECTANCE_ADD_BAND_7 | REFLECTANCE_ADD_BAND_7  
REFLECTANCE_MAXIMUM_BAND_1 |   
REFLECTANCE_MAXIMUM_BAND_2 |   
REFLECTANCE_MAXIMUM_BAND_3 |   
REFLECTANCE_MAXIMUM_BAND_4 |   
REFLECTANCE_MAXIMUM_BAND_5 |   
REFLECTANCE_MAXIMUM_BAND_7 |   
REFLECTANCE_MINIMUM_BAND_1 |   
REFLECTANCE_MINIMUM_BAND_2 |   
REFLECTANCE_MINIMUM_BAND_3 |   
REFLECTANCE_MINIMUM_BAND_4 |   
REFLECTANCE_MINIMUM_BAND_5 |   
REFLECTANCE_MINIMUM_BAND_7 |   
REFLECTANCE_MULT_BAND_1 | REFLECTANCE_MULT_BAND_1  
REFLECTANCE_MULT_BAND_2 | REFLECTANCE_MULT_BAND_2  
REFLECTANCE_MULT_BAND_3 | REFLECTANCE_MULT_BAND_3  
REFLECTANCE_MULT_BAND_4 | REFLECTANCE_MULT_BAND_4  
REFLECTANCE_MULT_BAND_5 | REFLECTANCE_MULT_BAND_5  
REFLECTANCE_MULT_BAND_7 | REFLECTANCE_MULT_BAND_7  
REFLECTIVE_LINES | REFLECTIVE_LINES  
REFLECTIVE_SAMPLES | REFLECTIVE_SAMPLES  
REQUEST_ID | REQUEST_ID  
RESAMPLING_OPTION | RESAMPLING_OPTION  
SATURATION_BAND_1 | SATURATION_BAND_1  
SATURATION_BAND_2 | SATURATION_BAND_2  
SATURATION_BAND_3 | SATURATION_BAND_3  
SATURATION_BAND_4 | SATURATION_BAND_4  
SATURATION_BAND_5 | SATURATION_BAND_5  
SATURATION_BAND_6 | SATURATION_BAND_6  
SATURATION_BAND_7 | SATURATION_BAND_7  
SCENE_CENTER_TIME | SCENE_CENTER_TIME  
| SENSOR_ANOMALIES  
SENSOR_ID | SENSOR_ID  
SENSOR_MODE | SENSOR_MODE  
| SENSOR_MODE_SLC  
SPACECRAFT_ID | SPACECRAFT_ID  
STATION_ID | STATION_ID  
SUN_AZIMUTH | SUN_AZIMUTH  
SUN_ELEVATION | SUN_ELEVATION  
THERMAL_LINES | THERMAL_LINES  
THERMAL_SAMPLES | THERMAL_SAMPLES  
UTM_ZONE | UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
google:registration_count |   
google:registration_offset_x |   
google:registration_offset_y |   
google:registration_ratio |   
## Scaled radiance (DN)
[OLI](https://developers.google.com/earth-engine/landsat_c1_to_c2#oli)[ETM+](https://developers.google.com/earth-engine/landsat_c1_to_c2#etm+)[TM](https://developers.google.com/earth-engine/landsat_c1_to_c2#tm)[MSS](https://developers.google.com/earth-engine/landsat_c1_to_c2#mss) More
### Asset ID
Replace `C01` with `C02` in image and collection IDs. For example, [Landsat 8 OLI Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1) (Landsat 9 OLI-2 was not included in Collection 1):
Collection 1 | Collection 2  
---|---  
LANDSAT/LC08/**C01** /T1 | LANDSAT/LC08/**C02** /T1  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Coastal aerosol | B1 | B1  
Blue | B2 | B2  
Green | B3 | B3  
Red | B4 | B4  
Near infrared | B5 | B5  
Shortwave infrared 1 | B6 | B6  
Shortwave infrared 2 | B7 | B7  
Panchromatic | B8 | B8  
Cirrus | B9 | B9  
Thermal infrared 1 | B10 | B10  
Thermal infrared 2 | B11 | B11  
QA bitmask | **BQA** | **QA_PIXEL**  
Radiometric saturation QA |  | **QA_RADSAT**  
Solar azimuth angle |  | **SAA**  
Solar zenith angle |  | **SZA**  
View azimuth angle |  | **VAA**  
View zenith angle |  | **VZA**  
Update code that selects bands whose names have changed, for example, the QA bitmask band:
Collection 1 | Collection 2  
---|---  
`image.select('BQA')` | `image.select('QA_PIXEL')`  
### Value scaling
No changes required. Collection 1 and Collection 2 have the same scaling for raw DN reflectance and thermal values.
### QA masking
Bit codes have changed for the QA bitmask. See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1#bands)) and "Bitmask for BQA" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1#bands)) sections in catalog entries for codes.
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11010',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11010', 2)).eq(0)
```

### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. No property names were changed. See the following property comparison table to determine whether you need to modify your code to accommodate missing or added properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1#image-properties) in the product's catalog page for Collection 2 property descriptions.
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
BPF_NAME_OLI |   
BPF_NAME_TIRS |   
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
COLLECTION_CATEGORY | COLLECTION_CATEGORY  
COLLECTION_NUMBER | COLLECTION_NUMBER  
CPF_NAME |   
| DATA_SOURCE_ELEVATION  
| DATA_SOURCE_TIRS_STRAY_LIGHT_CORRECTION  
DATA_TYPE |   
DATE_ACQUIRED | DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
DATUM | DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
ELEVATION_SOURCE |   
ELLIPSOID | ELLIPSOID  
FILE_DATE |   
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
GEOMETRIC_RMSE_VERIFY | GEOMETRIC_RMSE_VERIFY  
GRID_CELL_SIZE_PANCHROMATIC | GRID_CELL_SIZE_PANCHROMATIC  
GRID_CELL_SIZE_REFLECTIVE | GRID_CELL_SIZE_REFLECTIVE  
GRID_CELL_SIZE_THERMAL | GRID_CELL_SIZE_THERMAL  
GROUND_CONTROL_POINTS_MODEL | GROUND_CONTROL_POINTS_MODEL  
GROUND_CONTROL_POINTS_VERIFY | GROUND_CONTROL_POINTS_VERIFY  
GROUND_CONTROL_POINTS_VERSION | GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY_OLI | IMAGE_QUALITY_OLI  
IMAGE_QUALITY_TIRS | IMAGE_QUALITY_TIRS  
K1_CONSTANT_BAND_10 | K1_CONSTANT_BAND_10  
K1_CONSTANT_BAND_11 | K1_CONSTANT_BAND_11  
K2_CONSTANT_BAND_10 | K2_CONSTANT_BAND_10  
K2_CONSTANT_BAND_11 | K2_CONSTANT_BAND_11  
LANDSAT_PRODUCT_ID | LANDSAT_PRODUCT_ID  
LANDSAT_SCENE_ID | LANDSAT_SCENE_ID  
MAP_PROJECTION | MAP_PROJECTION  
NADIR_OFFNADIR | NADIR_OFFNADIR  
ORIENTATION | ORIENTATION  
PANCHROMATIC_LINES | PANCHROMATIC_LINES  
PANCHROMATIC_SAMPLES | PANCHROMATIC_SAMPLES  
| PROCESSING_LEVEL  
PROCESSING_SOFTWARE_VERSION | PROCESSING_SOFTWARE_VERSION  
RADIANCE_ADD_BAND_1 | RADIANCE_ADD_BAND_1  
RADIANCE_ADD_BAND_10 | RADIANCE_ADD_BAND_10  
RADIANCE_ADD_BAND_11 | RADIANCE_ADD_BAND_11  
RADIANCE_ADD_BAND_2 | RADIANCE_ADD_BAND_2  
RADIANCE_ADD_BAND_3 | RADIANCE_ADD_BAND_3  
RADIANCE_ADD_BAND_4 | RADIANCE_ADD_BAND_4  
RADIANCE_ADD_BAND_5 | RADIANCE_ADD_BAND_5  
RADIANCE_ADD_BAND_6 | RADIANCE_ADD_BAND_6  
RADIANCE_ADD_BAND_7 | RADIANCE_ADD_BAND_7  
RADIANCE_ADD_BAND_8 | RADIANCE_ADD_BAND_8  
RADIANCE_ADD_BAND_9 | RADIANCE_ADD_BAND_9  
RADIANCE_MULT_BAND_1 | RADIANCE_MULT_BAND_1  
RADIANCE_MULT_BAND_10 | RADIANCE_MULT_BAND_10  
RADIANCE_MULT_BAND_11 | RADIANCE_MULT_BAND_11  
RADIANCE_MULT_BAND_2 | RADIANCE_MULT_BAND_2  
RADIANCE_MULT_BAND_3 | RADIANCE_MULT_BAND_3  
RADIANCE_MULT_BAND_4 | RADIANCE_MULT_BAND_4  
RADIANCE_MULT_BAND_5 | RADIANCE_MULT_BAND_5  
RADIANCE_MULT_BAND_6 | RADIANCE_MULT_BAND_6  
RADIANCE_MULT_BAND_7 | RADIANCE_MULT_BAND_7  
RADIANCE_MULT_BAND_8 | RADIANCE_MULT_BAND_8  
RADIANCE_MULT_BAND_9 | RADIANCE_MULT_BAND_9  
REFLECTANCE_ADD_BAND_1 | REFLECTANCE_ADD_BAND_1  
REFLECTANCE_ADD_BAND_2 | REFLECTANCE_ADD_BAND_2  
REFLECTANCE_ADD_BAND_3 | REFLECTANCE_ADD_BAND_3  
REFLECTANCE_ADD_BAND_4 | REFLECTANCE_ADD_BAND_4  
REFLECTANCE_ADD_BAND_5 | REFLECTANCE_ADD_BAND_5  
REFLECTANCE_ADD_BAND_6 | REFLECTANCE_ADD_BAND_6  
REFLECTANCE_ADD_BAND_7 | REFLECTANCE_ADD_BAND_7  
REFLECTANCE_ADD_BAND_8 | REFLECTANCE_ADD_BAND_8  
REFLECTANCE_ADD_BAND_9 | REFLECTANCE_ADD_BAND_9  
REFLECTANCE_MULT_BAND_1 | REFLECTANCE_MULT_BAND_1  
REFLECTANCE_MULT_BAND_2 | REFLECTANCE_MULT_BAND_2  
REFLECTANCE_MULT_BAND_3 | REFLECTANCE_MULT_BAND_3  
REFLECTANCE_MULT_BAND_4 | REFLECTANCE_MULT_BAND_4  
REFLECTANCE_MULT_BAND_5 | REFLECTANCE_MULT_BAND_5  
REFLECTANCE_MULT_BAND_6 | REFLECTANCE_MULT_BAND_6  
REFLECTANCE_MULT_BAND_7 | REFLECTANCE_MULT_BAND_7  
REFLECTANCE_MULT_BAND_8 | REFLECTANCE_MULT_BAND_8  
REFLECTANCE_MULT_BAND_9 | REFLECTANCE_MULT_BAND_9  
REFLECTIVE_LINES | REFLECTIVE_LINES  
REFLECTIVE_SAMPLES | REFLECTIVE_SAMPLES  
REQUEST_ID | REQUEST_ID  
RESAMPLING_OPTION | RESAMPLING_OPTION  
RLUT_FILE_NAME |   
ROLL_ANGLE | ROLL_ANGLE  
SATURATION_BAND_1 | SATURATION_BAND_1  
SATURATION_BAND_2 | SATURATION_BAND_2  
SATURATION_BAND_3 | SATURATION_BAND_3  
SATURATION_BAND_4 | SATURATION_BAND_4  
SATURATION_BAND_5 | SATURATION_BAND_5  
SATURATION_BAND_6 | SATURATION_BAND_6  
SATURATION_BAND_7 | SATURATION_BAND_7  
SATURATION_BAND_8 | SATURATION_BAND_8  
SATURATION_BAND_9 | SATURATION_BAND_9  
SCENE_CENTER_TIME | SCENE_CENTER_TIME  
SENSOR_ID | SENSOR_ID  
SPACECRAFT_ID | SPACECRAFT_ID  
STATION_ID | STATION_ID  
SUN_AZIMUTH | SUN_AZIMUTH  
SUN_ELEVATION | SUN_ELEVATION  
TARGET_WRS_PATH | TARGET_WRS_PATH  
TARGET_WRS_ROW | TARGET_WRS_ROW  
THERMAL_LINES | THERMAL_LINES  
THERMAL_SAMPLES | THERMAL_SAMPLES  
TIRS_SSM_MODEL | TIRS_SSM_MODEL  
TIRS_SSM_POSITION_STATUS | TIRS_SSM_POSITION_STATUS  
TIRS_STRAY_LIGHT_CORRECTION_SOURCE |   
TRUNCATION_OLI | TRUNCATION_OLI  
UTM_ZONE | UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
google:registration_count |   
google:registration_offset_x |   
google:registration_offset_y |   
google:registration_ratio |   
### Asset ID
Replace `C01` with `C02` in image and collection IDs. For example, [Landsat 7 ETM+ Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1):
Collection 1 | Collection 2  
---|---  
LANDSAT/LE07/**C01** /T1 | LANDSAT/LE07/**C02** /T1  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Blue | B1 | B1  
Green | B2 | B2  
Red | B3 | B3  
Near infrared | B4 | B4  
Shortwave infrared 1 | B5 | B5  
Low-gain thermal infrared 1 | B6_VCID_1 | B6_VCID_1  
High-gain thermal infrared 1 | B6_VCID_2 | B6_VCID_2  
Shortwave infrared 2 | B7 | B7  
Panchromatic | B8 | B8  
QA bitmask | **BQA** | **QA_PIXEL**  
Radiometric saturation QA |  | **QA_RADSAT**  
Solar azimuth angle |  | **SAA**  
Solar zenith angle |  | **SZA**  
View azimuth angle |  | **VAA**  
View zenith angle |  | **VZA**  
Update code that selects bands whose names have changed, for example, the QA bitmask band:
Collection 1 | Collection 2  
---|---  
`image.select('BQA')` | `image.select('QA_PIXEL')`  
### Value scaling
No changes required. Collection 1 and Collection 2 have the same scaling for raw DN reflectance and thermal values.
### QA masking
Bit codes have changed for the QA bitmask. See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1#bands)) and "Bitmask for BQA" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C01_T1#bands)) sections in catalog entries for codes.
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11010',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11010', 2)).eq(0)
```

### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. No property names were changed. See the following property comparison table to determine whether you need to modify your code to accommodate missing or added properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1#image-properties) in the product's catalog page for Collection 2 property descriptions.
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
COLLECTION_CATEGORY | COLLECTION_CATEGORY  
COLLECTION_NUMBER | COLLECTION_NUMBER  
CORRECTION_BIAS_BAND_1 | CORRECTION_BIAS_BAND_1  
CORRECTION_BIAS_BAND_2 | CORRECTION_BIAS_BAND_2  
CORRECTION_BIAS_BAND_3 | CORRECTION_BIAS_BAND_3  
CORRECTION_BIAS_BAND_4 | CORRECTION_BIAS_BAND_4  
CORRECTION_BIAS_BAND_5 | CORRECTION_BIAS_BAND_5  
CORRECTION_BIAS_BAND_6_VCID_1 | CORRECTION_BIAS_BAND_6_VCID_1  
CORRECTION_BIAS_BAND_6_VCID_2 | CORRECTION_BIAS_BAND_6_VCID_2  
CORRECTION_BIAS_BAND_7 | CORRECTION_BIAS_BAND_7  
CORRECTION_BIAS_BAND_8 | CORRECTION_BIAS_BAND_8  
CORRECTION_GAIN_BAND_1 | CORRECTION_GAIN_BAND_1  
CORRECTION_GAIN_BAND_2 | CORRECTION_GAIN_BAND_2  
CORRECTION_GAIN_BAND_3 | CORRECTION_GAIN_BAND_3  
CORRECTION_GAIN_BAND_4 | CORRECTION_GAIN_BAND_4  
CORRECTION_GAIN_BAND_5 | CORRECTION_GAIN_BAND_5  
CORRECTION_GAIN_BAND_6_VCID_1 | CORRECTION_GAIN_BAND_6_VCID_1  
CORRECTION_GAIN_BAND_6_VCID_2 | CORRECTION_GAIN_BAND_6_VCID_2  
CORRECTION_GAIN_BAND_7 | CORRECTION_GAIN_BAND_7  
CORRECTION_GAIN_BAND_8 | CORRECTION_GAIN_BAND_8  
CPF_NAME |   
DATA_CATEGORY |   
| DATA_SOURCE_ELEVATION  
DATA_TYPE |   
DATE_ACQUIRED | DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
DATUM | DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
ELEVATION_SOURCE |   
ELLIPSOID | ELLIPSOID  
EPHEMERIS_TYPE | EPHEMERIS_TYPE  
FILE_DATE |   
GAIN_BAND_1 | GAIN_BAND_1  
GAIN_BAND_2 | GAIN_BAND_2  
GAIN_BAND_3 | GAIN_BAND_3  
GAIN_BAND_4 | GAIN_BAND_4  
GAIN_BAND_5 | GAIN_BAND_5  
GAIN_BAND_6_VCID_1 | GAIN_BAND_6_VCID_1  
GAIN_BAND_6_VCID_2 | GAIN_BAND_6_VCID_2  
GAIN_BAND_7 | GAIN_BAND_7  
GAIN_BAND_8 | GAIN_BAND_8  
GAIN_CHANGE_BAND_1 | GAIN_CHANGE_BAND_1  
GAIN_CHANGE_BAND_2 | GAIN_CHANGE_BAND_2  
GAIN_CHANGE_BAND_3 | GAIN_CHANGE_BAND_3  
GAIN_CHANGE_BAND_4 | GAIN_CHANGE_BAND_4  
GAIN_CHANGE_BAND_5 | GAIN_CHANGE_BAND_5  
GAIN_CHANGE_BAND_6_VCID_1 | GAIN_CHANGE_BAND_6_VCID_1  
GAIN_CHANGE_BAND_6_VCID_2 | GAIN_CHANGE_BAND_6_VCID_2  
GAIN_CHANGE_BAND_7 | GAIN_CHANGE_BAND_7  
GAIN_CHANGE_BAND_8 | GAIN_CHANGE_BAND_8  
GAIN_CHANGE_SCAN_BAND_1 | GAIN_CHANGE_SCAN_BAND_1  
GAIN_CHANGE_SCAN_BAND_2 | GAIN_CHANGE_SCAN_BAND_2  
GAIN_CHANGE_SCAN_BAND_3 | GAIN_CHANGE_SCAN_BAND_3  
GAIN_CHANGE_SCAN_BAND_4 | GAIN_CHANGE_SCAN_BAND_4  
GAIN_CHANGE_SCAN_BAND_5 | GAIN_CHANGE_SCAN_BAND_5  
GAIN_CHANGE_SCAN_BAND_6_VCID_1 | GAIN_CHANGE_SCAN_BAND_6_VCID_1  
GAIN_CHANGE_SCAN_BAND_6_VCID_2 | GAIN_CHANGE_SCAN_BAND_6_VCID_2  
GAIN_CHANGE_SCAN_BAND_7 | GAIN_CHANGE_SCAN_BAND_7  
GAIN_CHANGE_SCAN_BAND_8 | GAIN_CHANGE_SCAN_BAND_8  
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
GRID_CELL_SIZE_PANCHROMATIC | GRID_CELL_SIZE_PANCHROMATIC  
GRID_CELL_SIZE_REFLECTIVE | GRID_CELL_SIZE_REFLECTIVE  
GRID_CELL_SIZE_THERMAL | GRID_CELL_SIZE_THERMAL  
GROUND_CONTROL_POINTS_MODEL | GROUND_CONTROL_POINTS_MODEL  
GROUND_CONTROL_POINTS_VERSION | GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY | IMAGE_QUALITY  
K1_CONSTANT_BAND_6_VCID_1 | K1_CONSTANT_BAND_6_VCID_1  
K1_CONSTANT_BAND_6_VCID_2 | K1_CONSTANT_BAND_6_VCID_2  
K2_CONSTANT_BAND_6_VCID_1 | K2_CONSTANT_BAND_6_VCID_1  
K2_CONSTANT_BAND_6_VCID_2 | K2_CONSTANT_BAND_6_VCID_2  
LANDSAT_PRODUCT_ID | LANDSAT_PRODUCT_ID  
LANDSAT_SCENE_ID | LANDSAT_SCENE_ID  
MAP_PROJECTION | MAP_PROJECTION  
ORIENTATION | ORIENTATION  
PANCHROMATIC_LINES | PANCHROMATIC_LINES  
PANCHROMATIC_SAMPLES | PANCHROMATIC_SAMPLES  
| PROCESSING_LEVEL  
PROCESSING_SOFTWARE_VERSION | PROCESSING_SOFTWARE_VERSION  
RADIANCE_ADD_BAND_1 | RADIANCE_ADD_BAND_1  
RADIANCE_ADD_BAND_2 | RADIANCE_ADD_BAND_2  
RADIANCE_ADD_BAND_3 | RADIANCE_ADD_BAND_3  
RADIANCE_ADD_BAND_4 | RADIANCE_ADD_BAND_4  
RADIANCE_ADD_BAND_5 | RADIANCE_ADD_BAND_5  
RADIANCE_ADD_BAND_6_VCID_1 | RADIANCE_ADD_BAND_6_VCID_1  
RADIANCE_ADD_BAND_6_VCID_2 | RADIANCE_ADD_BAND_6_VCID_2  
RADIANCE_ADD_BAND_7 | RADIANCE_ADD_BAND_7  
RADIANCE_ADD_BAND_8 | RADIANCE_ADD_BAND_8  
RADIANCE_MAXIMUM_BAND_1 |   
RADIANCE_MAXIMUM_BAND_2 |   
RADIANCE_MAXIMUM_BAND_3 |   
RADIANCE_MAXIMUM_BAND_4 |   
RADIANCE_MAXIMUM_BAND_5 |   
RADIANCE_MAXIMUM_BAND_6_VCID_1 |   
RADIANCE_MAXIMUM_BAND_6_VCID_2 |   
RADIANCE_MAXIMUM_BAND_7 |   
RADIANCE_MAXIMUM_BAND_8 |   
RADIANCE_MINIMUM_BAND_1 |   
RADIANCE_MINIMUM_BAND_2 |   
RADIANCE_MINIMUM_BAND_3 |   
RADIANCE_MINIMUM_BAND_4 |   
RADIANCE_MINIMUM_BAND_5 |   
RADIANCE_MINIMUM_BAND_6_VCID_1 |   
RADIANCE_MINIMUM_BAND_6_VCID_2 |   
RADIANCE_MINIMUM_BAND_7 |   
RADIANCE_MINIMUM_BAND_8 |   
RADIANCE_MULT_BAND_1 | RADIANCE_MULT_BAND_1  
RADIANCE_MULT_BAND_2 | RADIANCE_MULT_BAND_2  
RADIANCE_MULT_BAND_3 | RADIANCE_MULT_BAND_3  
RADIANCE_MULT_BAND_4 | RADIANCE_MULT_BAND_4  
RADIANCE_MULT_BAND_5 | RADIANCE_MULT_BAND_5  
RADIANCE_MULT_BAND_6_VCID_1 | RADIANCE_MULT_BAND_6_VCID_1  
RADIANCE_MULT_BAND_6_VCID_2 | RADIANCE_MULT_BAND_6_VCID_2  
RADIANCE_MULT_BAND_7 | RADIANCE_MULT_BAND_7  
RADIANCE_MULT_BAND_8 | RADIANCE_MULT_BAND_8  
REFLECTANCE_ADD_BAND_1 | REFLECTANCE_ADD_BAND_1  
REFLECTANCE_ADD_BAND_2 | REFLECTANCE_ADD_BAND_2  
REFLECTANCE_ADD_BAND_3 | REFLECTANCE_ADD_BAND_3  
REFLECTANCE_ADD_BAND_4 | REFLECTANCE_ADD_BAND_4  
REFLECTANCE_ADD_BAND_5 | REFLECTANCE_ADD_BAND_5  
REFLECTANCE_ADD_BAND_7 | REFLECTANCE_ADD_BAND_7  
REFLECTANCE_ADD_BAND_8 | REFLECTANCE_ADD_BAND_8  
REFLECTANCE_MAXIMUM_BAND_1 |   
REFLECTANCE_MAXIMUM_BAND_2 |   
REFLECTANCE_MAXIMUM_BAND_3 |   
REFLECTANCE_MAXIMUM_BAND_4 |   
REFLECTANCE_MAXIMUM_BAND_5 |   
REFLECTANCE_MAXIMUM_BAND_7 |   
REFLECTANCE_MAXIMUM_BAND_8 |   
REFLECTANCE_MINIMUM_BAND_1 |   
REFLECTANCE_MINIMUM_BAND_2 |   
REFLECTANCE_MINIMUM_BAND_3 |   
REFLECTANCE_MINIMUM_BAND_4 |   
REFLECTANCE_MINIMUM_BAND_5 |   
REFLECTANCE_MINIMUM_BAND_7 |   
REFLECTANCE_MINIMUM_BAND_8 |   
REFLECTANCE_MULT_BAND_1 | REFLECTANCE_MULT_BAND_1  
REFLECTANCE_MULT_BAND_2 | REFLECTANCE_MULT_BAND_2  
REFLECTANCE_MULT_BAND_3 | REFLECTANCE_MULT_BAND_3  
REFLECTANCE_MULT_BAND_4 | REFLECTANCE_MULT_BAND_4  
REFLECTANCE_MULT_BAND_5 | REFLECTANCE_MULT_BAND_5  
REFLECTANCE_MULT_BAND_7 | REFLECTANCE_MULT_BAND_7  
REFLECTANCE_MULT_BAND_8 | REFLECTANCE_MULT_BAND_8  
REFLECTIVE_LINES | REFLECTIVE_LINES  
REFLECTIVE_SAMPLES | REFLECTIVE_SAMPLES  
REQUEST_ID | REQUEST_ID  
RESAMPLING_OPTION | RESAMPLING_OPTION  
SATURATION_BAND_1 | SATURATION_BAND_1  
SATURATION_BAND_2 | SATURATION_BAND_2  
SATURATION_BAND_3 | SATURATION_BAND_3  
SATURATION_BAND_4 | SATURATION_BAND_4  
SATURATION_BAND_5 | SATURATION_BAND_5  
SATURATION_BAND_6_VCID_1 | SATURATION_BAND_6_VCID_1  
SATURATION_BAND_6_VCID_2 | SATURATION_BAND_6_VCID_2  
SATURATION_BAND_7 | SATURATION_BAND_7  
SATURATION_BAND_8 | SATURATION_BAND_8  
SCENE_CENTER_TIME | SCENE_CENTER_TIME  
| SENSOR_ANOMALIES  
SENSOR_ID | SENSOR_ID  
SENSOR_MODE | SENSOR_MODE  
| SENSOR_MODE_SLC  
SPACECRAFT_ID | SPACECRAFT_ID  
STATION_ID | STATION_ID  
SUN_AZIMUTH | SUN_AZIMUTH  
SUN_ELEVATION | SUN_ELEVATION  
THERMAL_LINES | THERMAL_LINES  
THERMAL_SAMPLES | THERMAL_SAMPLES  
UTM_ZONE | UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
google:registration_count |   
google:registration_offset_x |   
google:registration_offset_y |   
google:registration_ratio |   
### Asset ID
Replace `C01` with `C02` in image and collection IDs. For example, [Landsat 5 TM Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1):
Collection 1 | Collection 2  
---|---  
LANDSAT/LT05/**C01** /T1 | LANDSAT/LT05/**C02** /T1  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Blue | B1 | B1  
Green | B2 | B2  
Red | B3 | B3  
Near infrared | B4 | B4  
Shortwave infrared 1 | B5 | B5  
Thermal infrared 1 | B6 | B6  
Shortwave infrared 2 | B7 | B7  
QA bitmask | **BQA** | **QA_PIXEL**  
Radiometric saturation QA |  | **QA_RADSAT**  
Solar azimuth angle |  | **SAA**  
Solar zenith angle |  | **SZA**  
View azimuth angle |  | **VAA**  
View zenith angle |  | **VZA**  
Update code that selects bands whose names have changed, for example, the QA bitmask band:
Collection 1 | Collection 2  
---|---  
`image.select('BQA')` | `image.select('QA_PIXEL')`  
### Value scaling
No changes required. Collection 1 and Collection 2 have the same scaling for raw DN reflectance and thermal values.
### QA masking
Bit codes have changed for the QA bitmask. See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1#bands)) and "Bitmask for BQA" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C01_T1#bands)) sections in catalog entries for codes (TM 5, for example).
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11010',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11010', 2)).eq(0)
```

### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. No property names were changed. See the following property comparison table to determine whether you need to modify your code to accommodate missing or added properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1#image-properties) in the product's catalog page for Collection 2 property descriptions (TM 5, for example).
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
COLLECTION_CATEGORY | COLLECTION_CATEGORY  
COLLECTION_NUMBER | COLLECTION_NUMBER  
CORNER_LL_LAT_PRODUCT |   
CORNER_LL_LON_PRODUCT |   
CORNER_LL_PROJECTION_X_PRODUCT |   
CORNER_LL_PROJECTION_Y_PRODUCT |   
CORNER_LR_LAT_PRODUCT |   
CORNER_LR_LON_PRODUCT |   
CORNER_LR_PROJECTION_X_PRODUCT |   
CORNER_LR_PROJECTION_Y_PRODUCT |   
CORNER_UL_LAT_PRODUCT |   
CORNER_UL_LON_PRODUCT |   
CORNER_UL_PROJECTION_X_PRODUCT |   
CORNER_UL_PROJECTION_Y_PRODUCT |   
CORNER_UR_LAT_PRODUCT |   
CORNER_UR_LON_PRODUCT |   
CORNER_UR_PROJECTION_X_PRODUCT |   
CORNER_UR_PROJECTION_Y_PRODUCT |   
CORRECTION_BIAS_BAND_1 | CORRECTION_BIAS_BAND_1  
CORRECTION_BIAS_BAND_2 | CORRECTION_BIAS_BAND_2  
CORRECTION_BIAS_BAND_3 | CORRECTION_BIAS_BAND_3  
CORRECTION_BIAS_BAND_4 | CORRECTION_BIAS_BAND_4  
CORRECTION_BIAS_BAND_5 | CORRECTION_BIAS_BAND_5  
CORRECTION_BIAS_BAND_6 | CORRECTION_BIAS_BAND_6  
CORRECTION_BIAS_BAND_7 | CORRECTION_BIAS_BAND_7  
CORRECTION_GAIN_BAND_1 | CORRECTION_GAIN_BAND_1  
CORRECTION_GAIN_BAND_2 | CORRECTION_GAIN_BAND_2  
CORRECTION_GAIN_BAND_3 | CORRECTION_GAIN_BAND_3  
CORRECTION_GAIN_BAND_4 | CORRECTION_GAIN_BAND_4  
CORRECTION_GAIN_BAND_5 | CORRECTION_GAIN_BAND_5  
CORRECTION_GAIN_BAND_6 | CORRECTION_GAIN_BAND_6  
CORRECTION_GAIN_BAND_7 | CORRECTION_GAIN_BAND_7  
CPF_NAME |   
DATA_CATEGORY |   
| DATA_SOURCE_ELEVATION  
DATA_TYPE |   
DATA_TYPE_L0RP | DATA_TYPE_L0RP  
DATE_ACQUIRED | DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
DATUM | DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
ELEVATION_SOURCE |   
ELLIPSOID | ELLIPSOID  
EPHEMERIS_TYPE | EPHEMERIS_TYPE  
FILE_DATE |   
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
GEOMETRIC_RMSE_VERIFY | GEOMETRIC_RMSE_VERIFY  
GEOMETRIC_RMSE_VERIFY_QUAD_LL | GEOMETRIC_RMSE_VERIFY_QUAD_LL  
GEOMETRIC_RMSE_VERIFY_QUAD_LR | GEOMETRIC_RMSE_VERIFY_QUAD_LR  
GEOMETRIC_RMSE_VERIFY_QUAD_UL | GEOMETRIC_RMSE_VERIFY_QUAD_UL  
GEOMETRIC_RMSE_VERIFY_QUAD_UR | GEOMETRIC_RMSE_VERIFY_QUAD_UR  
GRID_CELL_SIZE_REFLECTIVE | GRID_CELL_SIZE_REFLECTIVE  
GRID_CELL_SIZE_THERMAL | GRID_CELL_SIZE_THERMAL  
GROUND_CONTROL_POINTS_MODEL | GROUND_CONTROL_POINTS_MODEL  
GROUND_CONTROL_POINTS_VERIFY | GROUND_CONTROL_POINTS_VERIFY  
GROUND_CONTROL_POINTS_VERSION | GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY | IMAGE_QUALITY  
K1_CONSTANT_BAND_6 | K1_CONSTANT_BAND_6  
K2_CONSTANT_BAND_6 | K2_CONSTANT_BAND_6  
LANDSAT_PRODUCT_ID | LANDSAT_PRODUCT_ID  
LANDSAT_SCENE_ID | LANDSAT_SCENE_ID  
MAP_PROJECTION | MAP_PROJECTION  
MAP_PROJECTION_L0RA | MAP_PROJECTION_L0RA  
ORIENTATION | ORIENTATION  
| PROCESSING_LEVEL  
PROCESSING_SOFTWARE_VERSION | PROCESSING_SOFTWARE_VERSION  
RADIANCE_ADD_BAND_1 | RADIANCE_ADD_BAND_1  
RADIANCE_ADD_BAND_2 | RADIANCE_ADD_BAND_2  
RADIANCE_ADD_BAND_3 | RADIANCE_ADD_BAND_3  
RADIANCE_ADD_BAND_4 | RADIANCE_ADD_BAND_4  
RADIANCE_ADD_BAND_5 | RADIANCE_ADD_BAND_5  
RADIANCE_ADD_BAND_6 | RADIANCE_ADD_BAND_6  
RADIANCE_ADD_BAND_7 | RADIANCE_ADD_BAND_7  
RADIANCE_MAXIMUM_BAND_1 |   
RADIANCE_MAXIMUM_BAND_2 |   
RADIANCE_MAXIMUM_BAND_3 |   
RADIANCE_MAXIMUM_BAND_4 |   
RADIANCE_MAXIMUM_BAND_5 |   
RADIANCE_MAXIMUM_BAND_6 |   
RADIANCE_MAXIMUM_BAND_7 |   
RADIANCE_MINIMUM_BAND_1 |   
RADIANCE_MINIMUM_BAND_2 |   
RADIANCE_MINIMUM_BAND_3 |   
RADIANCE_MINIMUM_BAND_4 |   
RADIANCE_MINIMUM_BAND_5 |   
RADIANCE_MINIMUM_BAND_6 |   
RADIANCE_MINIMUM_BAND_7 |   
RADIANCE_MULT_BAND_1 | RADIANCE_MULT_BAND_1  
RADIANCE_MULT_BAND_2 | RADIANCE_MULT_BAND_2  
RADIANCE_MULT_BAND_3 | RADIANCE_MULT_BAND_3  
RADIANCE_MULT_BAND_4 | RADIANCE_MULT_BAND_4  
RADIANCE_MULT_BAND_5 | RADIANCE_MULT_BAND_5  
RADIANCE_MULT_BAND_6 | RADIANCE_MULT_BAND_6  
RADIANCE_MULT_BAND_7 | RADIANCE_MULT_BAND_7  
REFLECTANCE_ADD_BAND_1 | REFLECTANCE_ADD_BAND_1  
REFLECTANCE_ADD_BAND_2 | REFLECTANCE_ADD_BAND_2  
REFLECTANCE_ADD_BAND_3 | REFLECTANCE_ADD_BAND_3  
REFLECTANCE_ADD_BAND_4 | REFLECTANCE_ADD_BAND_4  
REFLECTANCE_ADD_BAND_5 | REFLECTANCE_ADD_BAND_5  
REFLECTANCE_ADD_BAND_7 | REFLECTANCE_ADD_BAND_7  
REFLECTANCE_MAXIMUM_BAND_1 |   
REFLECTANCE_MAXIMUM_BAND_2 |   
REFLECTANCE_MAXIMUM_BAND_3 |   
REFLECTANCE_MAXIMUM_BAND_4 |   
REFLECTANCE_MAXIMUM_BAND_5 |   
REFLECTANCE_MAXIMUM_BAND_7 |   
REFLECTANCE_MINIMUM_BAND_1 |   
REFLECTANCE_MINIMUM_BAND_2 |   
REFLECTANCE_MINIMUM_BAND_3 |   
REFLECTANCE_MINIMUM_BAND_4 |   
REFLECTANCE_MINIMUM_BAND_5 |   
REFLECTANCE_MINIMUM_BAND_7 |   
REFLECTANCE_MULT_BAND_1 | REFLECTANCE_MULT_BAND_1  
REFLECTANCE_MULT_BAND_2 | REFLECTANCE_MULT_BAND_2  
REFLECTANCE_MULT_BAND_3 | REFLECTANCE_MULT_BAND_3  
REFLECTANCE_MULT_BAND_4 | REFLECTANCE_MULT_BAND_4  
REFLECTANCE_MULT_BAND_5 | REFLECTANCE_MULT_BAND_5  
REFLECTANCE_MULT_BAND_7 | REFLECTANCE_MULT_BAND_7  
REFLECTIVE_LINES | REFLECTIVE_LINES  
REFLECTIVE_SAMPLES | REFLECTIVE_SAMPLES  
REQUEST_ID | REQUEST_ID  
RESAMPLING_OPTION | RESAMPLING_OPTION  
SATURATION_BAND_1 | SATURATION_BAND_1  
SATURATION_BAND_2 | SATURATION_BAND_2  
SATURATION_BAND_3 | SATURATION_BAND_3  
SATURATION_BAND_4 | SATURATION_BAND_4  
SATURATION_BAND_5 | SATURATION_BAND_5  
SATURATION_BAND_6 | SATURATION_BAND_6  
SATURATION_BAND_7 | SATURATION_BAND_7  
SCENE_CENTER_TIME | SCENE_CENTER_TIME  
| SENSOR_ANOMALIES  
SENSOR_ID | SENSOR_ID  
SENSOR_MODE | SENSOR_MODE  
SPACECRAFT_ID | SENSOR_MODE_SLC  
STATION_ID | SPACECRAFT_ID  
| STATION_ID  
SUN_AZIMUTH | SUN_AZIMUTH  
SUN_ELEVATION | SUN_ELEVATION  
THERMAL_LINES | THERMAL_LINES  
THERMAL_SAMPLES | THERMAL_SAMPLES  
UTM_ZONE | UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
google:registration_count |   
google:registration_offset_x |   
google:registration_offset_y |   
google:registration_ratio |   
### Asset ID
Replace `C01` with `C02` in image and collection IDs. For example, [Landsat 1 MSS Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM01_C02_T1):
Collection 1 | Collection 2  
---|---  
LANDSAT/LM01/**C01** /T1 | LANDSAT/LM01/**C02** /T1  
### Band names
Note band name changes and the addition of new bands.
**Expand to see band name changes and the addition of new bands**
Description | Collection 1 Name | Collection 2 Name  
---|---|---  
Green | B4 _(MSS 1-3)_ ; B1 _(MSS 4-5)_ | B4 _(MSS 1-3)_ ; B1 _(MSS 4-5)_  
Red | B5 _(MSS 1-3)_ ; B2 _(MSS 4-5)_ | B5 _(MSS 1-3)_ ; B2 _(MSS 4-5)_  
Near infrared 1 | B6 _(MSS 1-3)_ ; B3 _(MSS 4-5)_ | B6 _(MSS 1-3)_ ; B3 _(MSS 4-5)_  
Near infrared 2 | B7 _(MSS 1-3)_ ; B4 _(MSS 4-5)_ | B7 _(MSS 1-3)_ ; B4 _(MSS 4-5)_  
QA bitmask | **BQA** | **QA_PIXEL**  
Radiometric saturation QA |  | **QA_RADSAT**  
Update code that selects bands whose names have changed, for example, the QA bitmask band:
Collection 1 | Collection 2  
---|---  
`image.select('BQA')` | `image.select('QA_PIXEL')`  
### Value scaling
No changes required. Collection 1 and Collection 2 have the same scaling for raw DN values.
### QA masking
Bit codes have changed for the QA bitmask. See the "Bitmask for QA_PIXEL" ([Collection 2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM01_C02_T1#bands)) and "Bitmask for BQA" ([Collection 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM01_C01_T1#bands)) sections in catalog entries for codes (MSS 1, for example).
The following expression creates a cloud and shadow mask for a given image using the Collection 2 QA bitmask codes.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/landsat_c1_to_c2#code-editor-javascript)[Colab (Python)](https://developers.google.com/earth-engine/landsat_c1_to_c2#colab-python) More
```
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11010',2)).eq(0)
```
```
qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11010', 2)).eq(0)
```

### Image properties
In the transition from Collection 1 to Collection 2, some image properties were added and some were removed. No property names were changed. See the following property comparison table to determine whether you need to modify your code to accommodate missing or added properties (e.g., in filtering or processing). Refer to the [Image Properties tab](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LM01_C02_T2#image-properties) in the product's catalog page for Collection 2 property descriptions (MSS 1, for example).
Expand to compare property lists
Collection 1 | Collection 2  
---|---  
CLOUD_COVER | CLOUD_COVER  
CLOUD_COVER_LAND | CLOUD_COVER_LAND  
COLLECTION_CATEGORY | COLLECTION_CATEGORY  
COLLECTION_NUMBER | COLLECTION_NUMBER  
CORRECTION_GAIN_BAND_4 | CORRECTION_GAIN_BAND_4  
CORRECTION_GAIN_BAND_5 | CORRECTION_GAIN_BAND_5  
CORRECTION_GAIN_BAND_6 | CORRECTION_GAIN_BAND_6  
CORRECTION_GAIN_BAND_7 | CORRECTION_GAIN_BAND_7  
CPF_NAME |   
DATA_CATEGORY |   
| DATA_SOURCE_ELEVATION  
DATA_TYPE |   
DATA_TYPE_L0RP | DATA_TYPE_L0RP  
DATE_ACQUIRED | DATE_ACQUIRED  
| DATE_PRODUCT_GENERATED  
DATUM | DATUM  
EARTH_SUN_DISTANCE | EARTH_SUN_DISTANCE  
ELEVATION_SOURCE |   
ELLIPSOID | ELLIPSOID  
EPHEMERIS_TYPE | EPHEMERIS_TYPE  
FILE_DATE |   
GAIN_BAND_4 | GAIN_BAND_4  
GAIN_BAND_5 | GAIN_BAND_5  
GAIN_BAND_6 | GAIN_BAND_6  
GAIN_BAND_7 | GAIN_BAND_7  
GEOMETRIC_RMSE_MODEL | GEOMETRIC_RMSE_MODEL  
GEOMETRIC_RMSE_MODEL_X | GEOMETRIC_RMSE_MODEL_X  
GEOMETRIC_RMSE_MODEL_Y | GEOMETRIC_RMSE_MODEL_Y  
GEOMETRIC_RMSE_VERIFY | GEOMETRIC_RMSE_VERIFY  
GEOMETRIC_RMSE_VERIFY_QUAD_LL | GEOMETRIC_RMSE_VERIFY_QUAD_LL  
GEOMETRIC_RMSE_VERIFY_QUAD_LR | GEOMETRIC_RMSE_VERIFY_QUAD_LR  
GEOMETRIC_RMSE_VERIFY_QUAD_UL | GEOMETRIC_RMSE_VERIFY_QUAD_UL  
GEOMETRIC_RMSE_VERIFY_QUAD_UR | GEOMETRIC_RMSE_VERIFY_QUAD_UR  
GRID_CELL_SIZE_REFLECTIVE | GRID_CELL_SIZE_REFLECTIVE  
GROUND_CONTROL_POINTS_MODEL | GROUND_CONTROL_POINTS_MODEL  
GROUND_CONTROL_POINTS_VERIFY | GROUND_CONTROL_POINTS_VERIFY  
GROUND_CONTROL_POINTS_VERSION | GROUND_CONTROL_POINTS_VERSION  
IMAGE_QUALITY | IMAGE_QUALITY  
LANDSAT_PRODUCT_ID | LANDSAT_PRODUCT_ID  
LANDSAT_SCENE_ID | LANDSAT_SCENE_ID  
MAP_PROJECTION | MAP_PROJECTION  
MAP_PROJECTION_L0RA | MAP_PROJECTION_L0RA  
ORIENTATION | ORIENTATION  
PRESENT_BAND_4 | PRESENT_BAND_4  
PRESENT_BAND_5 | PRESENT_BAND_5  
PRESENT_BAND_6 | PRESENT_BAND_6  
PRESENT_BAND_7 | PRESENT_BAND_7  
| PROCESSING_LEVEL  
PROCESSING_SOFTWARE_VERSION | PROCESSING_SOFTWARE_VERSION  
RADIANCE_ADD_BAND_4 | RADIANCE_ADD_BAND_4  
RADIANCE_ADD_BAND_5 | RADIANCE_ADD_BAND_5  
RADIANCE_ADD_BAND_6 | RADIANCE_ADD_BAND_6  
RADIANCE_ADD_BAND_7 | RADIANCE_ADD_BAND_7  
RADIANCE_MULT_BAND_4 | RADIANCE_MULT_BAND_4  
RADIANCE_MULT_BAND_5 | RADIANCE_MULT_BAND_5  
RADIANCE_MULT_BAND_6 | RADIANCE_MULT_BAND_6  
RADIANCE_MULT_BAND_7 | RADIANCE_MULT_BAND_7  
REFLECTANCE_ADD_BAND_4 | REFLECTANCE_ADD_BAND_4  
REFLECTANCE_ADD_BAND_5 | REFLECTANCE_ADD_BAND_5  
REFLECTANCE_ADD_BAND_6 | REFLECTANCE_ADD_BAND_6  
REFLECTANCE_ADD_BAND_7 | REFLECTANCE_ADD_BAND_7  
REFLECTANCE_MULT_BAND_4 | REFLECTANCE_MULT_BAND_4  
REFLECTANCE_MULT_BAND_5 | REFLECTANCE_MULT_BAND_5  
REFLECTANCE_MULT_BAND_6 | REFLECTANCE_MULT_BAND_6  
REFLECTANCE_MULT_BAND_7 | REFLECTANCE_MULT_BAND_7  
REFLECTIVE_LINES | REFLECTIVE_LINES  
REFLECTIVE_SAMPLES | REFLECTIVE_SAMPLES  
REQUEST_ID | REQUEST_ID  
RESAMPLING_OPTION | RESAMPLING_OPTION  
SATURATION_BAND_4 | SATURATION_BAND_4  
SATURATION_BAND_5 | SATURATION_BAND_5  
SATURATION_BAND_6 | SATURATION_BAND_6  
SATURATION_BAND_7 | SATURATION_BAND_7  
SCENE_CENTER_TIME | SCENE_CENTER_TIME  
SENSOR_ID | SENSOR_ID  
SPACECRAFT_ID | SPACECRAFT_ID  
STATION_ID | STATION_ID  
SUN_AZIMUTH | SUN_AZIMUTH  
SUN_ELEVATION | SUN_ELEVATION  
UTM_ZONE | UTM_ZONE  
WRS_PATH | WRS_PATH  
WRS_ROW | WRS_ROW  
| WRS_TYPE  
## Landsat Pre-Collection
The Earth Engine data archive contains Landsat Pre-Collection data. It can be identified by image and collection IDs that lack a collection component.
  * Collection 1 / Collection 2: `LANDSAT/[MISSION]/[COLLECTION]/[PRODUCT]` (e.g., `LANDSAT/LE07/C02/T1`)
  * Pre-Collection: `LANDSAT/[MISSION]_[PRODUCT]` (e.g., `LANDSAT/LE7_L1T`)


If you are using Pre-Collection data, switch to Collection 2 as soon as possible. Use the information about Collection 2 throughout this guide to update your scripts.
## Temporal composites
Earth Engine provides computed temporal composites (8-day, 32-day, and annual). There are a series of differences between those generated for Collection 1 and pre-Collection (PC/C1) and Collection 2 (C2). The code used to generate the C2 composites can be [viewed on GitHub](https://github.com/google/earthengine-catalog/blob/main/pipelines/landsat.py).
  * **Surface reflectance composites**
The C2 composites are generated from the USGS L2 surface reflectance product, whereas PC/C1 composites were made using top-of-atmosphere reflectance.
  * **One collection for all instruments**
The PC/C1 composites were separated into a set of temporal index composites for each instruments. This was primarily due to calibration differences between instruments. With C2 surface reflectance data, the inter-calibration is sufficient to combine are instruments together.
  * **Strict filtering**
More aggressive filtering for data quality is applied for the C2 composites, including:
    * Limiting L7 to the range 1999–2017 due to orbital drift / scene acquisition time.
    * Omitting L8 data before May 1, 2013 due to orbit stability issues.
    * Omitting data with WRS_ROW ≥ 122 (no nighttime images).
    * Omitting any pixels that are QA-flagged as anything other than clear.
    * Omitting L4–L7 pixels with ATMOS_OPACITY > 300 (haze).
    * Omitting L8–L9 pixels with any QA_AEROSOL issues.
    * Omitting any pixels flagged as saturated or which have values that are out of bounds.
  * **Median composites**
The PC/C1 composites used a last-on-top compositing. Collection 2 composites use a median compositor.
  * **Naming**
The PC/C1 composite paths are in the form of `LANDSAT/INSTRUMENT/C01/T1_PERIOD_INDEX`, while the C2 composites are in the form of `LANDSAT/COMPOSITES/C02/T1_L2_PERIOD_INDEX`, where INSTRUMENT is one of LT04, LT05, LE07, or LC08 and PERIOD is one of 8DAY, 32DAY, or ANNUAL. As an example, the following table shows asset paths for C2 composites that roughly correspond to C1 LC08 annual composites for each INDEX. Recall that INSTRUMENT is not included in the C2 composites because all relevant data from L4–L9 are included in each composite.
Collection 1 | Collection 2  
---|---  
LANDSAT/LC08/C01/T1_ANNUAL_BAI | LANDSAT/COMPOSITES/C02/T1_L2_ANNUAL_BAI  
LANDSAT/LC08/C01/T1_ANNUAL_EVI | LANDSAT/COMPOSITES/C02/T1_L2_ANNUAL_EVI  
LANDSAT/LC08/C01/T1_ANNUAL_GREENEST_TOA |   
LANDSAT/LC08/C01/T1_ANNUAL_NBRT | LANDSAT/COMPOSITES/C02/T1_L2_ANNUAL_NBR  
LANDSAT/LC08/C01/T1_ANNUAL_NDSI | _Not produced because snow pixels are masked during the compositing process_  
LANDSAT/LC08/C01/T1_ANNUAL_NDVI | LANDSAT/COMPOSITES/C02/T1_L2_ANNUAL_NDVI  
LANDSAT/LC08/C01/T1_ANNUAL_NDWI | LANDSAT/COMPOSITES/C02/T1_L2_ANNUAL_NDWI  
LANDSAT/LC08/C01/T1_ANNUAL_RAW |   
LANDSAT/LC08/C01/T1_ANNUAL_TOA |   


