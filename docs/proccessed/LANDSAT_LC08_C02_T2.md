 
#  USGS Landsat 8 Collection 2 Tier 2 Raw Scenes 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDSAT/LC08/C02/T2](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_LC08_C02_T2_sample.png) 

Dataset Availability
    2021-10-28T23:17:26Z–2025-04-13T15:57:46.366000Z 

Dataset Provider
     [ USGS ](https://www.usgs.gov/land-resources/nli/landsat/landsat-8-data-users-handbook) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/LC08/C02/T2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LC08_C02_T2) 

Revisit Interval
    16 Days 

Tags
     [c2](https://developers.google.com/earth-engine/datasets/tags/c2) [global](https://developers.google.com/earth-engine/datasets/tags/global) [l8](https://developers.google.com/earth-engine/datasets/tags/l8) [landsat](https://developers.google.com/earth-engine/datasets/tags/landsat) [lc8](https://developers.google.com/earth-engine/datasets/tags/lc8) [oli-tirs](https://developers.google.com/earth-engine/datasets/tags/oli-tirs) [radiance](https://developers.google.com/earth-engine/datasets/tags/radiance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [t2](https://developers.google.com/earth-engine/datasets/tags/t2) [tier2](https://developers.google.com/earth-engine/datasets/tags/tier2) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T2#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T2#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T2#terms-of-use) More
Landsat 8 Collection 2 Tier 2 DN values, representing scaled, calibrated at-sensor radiance. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications due to significant cloud cover, insufficient ground control, and other factors. Users interested in Tier 2 scenes can analyze the RMSE and other properties to determine the suitability for use in individual applications and studies. See more information [in the USGS docs](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collections).
**Bands**
Name | Pixel Size | Wavelength | Description  
---|---|---|---  
`B1` |  30 meters  | 0.43 - 0.45 μm | Coastal aerosol  
`B2` |  30 meters  | 0.45 - 0.51 μm | Blue  
`B3` |  30 meters  | 0.53 - 0.59 μm | Green  
`B4` |  30 meters  | 0.64 - 0.67 μm | Red  
`B5` |  30 meters  | 0.85 - 0.88 μm | Near infrared  
`B6` |  30 meters  | 1.57 - 1.65 μm | Shortwave infrared 1  
`B7` |  30 meters  | 2.11 - 2.29 μm | Shortwave infrared 2  
`B8` |  15 meters  | 0.52 - 0.90 μm | Band 8 Panchromatic  
`B9` |  30 meters  | 1.36 - 1.38 μm | Cirrus  
`B10` |  30 meters  | 10.60 - 11.19 μm | Thermal infrared 1, resampled from 100m to 30m  
`B11` |  30 meters  | 11.50 - 12.51 μm | Thermal infrared 2, resampled from 100m to 30m  
`QA_PIXEL` |  30 meters  | Landsat Collection 2 OLI/TIRS QA Bitmask  
Bitmask for QA_PIXEL
  * Bit 0: Fill 
    * 0: Image data
    * 1: Fill data
  * Bit 1: Dilated Cloud 
    * 0: Cloud is not dilated or no cloud
    * 1: Cloud dilation
  * Bit 2: Cirrus 
    * 0: Cirrus Confidence: no confidence level set or Low Confidence
    * 1: High confidence cirrus
  * Bit 3: Cloud 
    * 0: Cloud confidence is not high
    * 1: High confidence cloud
  * Bit 4: Cloud Shadow 
    * 0: Cloud Shadow Confidence is not high
    * 1: High confidence cloud shadow
  * Bit 5: Snow 
    * 0: Snow/Ice Confidence is not high
    * 1: High confidence snow cover
  * Bit 6: Clear 
    * 0: Cloud or Dilated Cloud bits are set
    * 1: Cloud and Dilated Cloud bits are not set
  * Bit 7: Water 
    * 0: Land or cloud
    * 1: Water
  * Bits 8-9: Cloud Confidence 
    * 0: No confidence level set
    * 1: Low confidence
    * 2: Medium confidence
    * 3: High confidence
  * Bits 10-11: Cloud Shadow Confidence 
    * 0: No confidence level set
    * 1: Low confidence
    * 2: Reserved
    * 3: High confidence
  * Bits 12-13: Snow / Ice Confidence 
    * 0: No confidence level set
    * 1: Low confidence
    * 2: Reserved
    * 3: High confidence
  * Bits 14-15: Cirrus Confidence 
    * 0: No confidence level set
    * 1: Low confidence
    * 2: Reserved
    * 3: High confidence

  
`QA_RADSAT` |  30 meters  | Radiometric saturation QA  
Bitmask for QA_RADSAT
  * Bit 0: Band 1 data saturated 
  * Bit 1: Band 2 data saturated 
  * Bit 2: Band 3 data saturated 
  * Bit 3: Band 4 data saturated 
  * Bit 4: Band 5 data saturated 
  * Bit 5: Band 6 data saturated 
  * Bit 6: Band 7 data saturated 
  * Bit 7: Unused 
  * Bit 8: Band 9 data saturated 
  * Bits 9-10: Unused 
  * Bit 11: Terrian occlusion 
    * 0: No terrain occlusion
    * 1: Terrain occlusion

  
`SAA` |  30 meters  | Solar Azimuth Angle  
`SZA` |  30 meters  | Solar Zenith Angle  
`VAA` |  30 meters  | View Azimuth Angle  
`VZA` |  30 meters  | View Zenith Angle  
**Image Properties**
Name | Type | Description  
---|---|---  
CLOUD_COVER | DOUBLE | Percentage cloud cover (0-100), -1 = not calculated.  
CLOUD_COVER_LAND | DOUBLE | Percentage cloud cover over land (0-100), -1 = not calculated.  
COLLECTION_CATEGORY | STRING | Tier of scene. (T1 or T2)  
COLLECTION_NUMBER | DOUBLE | Number of collection.  
DATA_SOURCE_ELEVATION | STRING | Indicates the source of the DEM used in the correction process. Possible values: "GLS2000", "RAMP", "GTOPO30".'  
DATA_SOURCE_TIRS_STRAY_LIGHT_CORRECTION | STRING | The correction source used in creating the Landsat 8 TIRS stray light correction image. This field is not included for Landsat 9.  
DATE_ACQUIRED | STRING | Image acquisition date. "YYYY-MM-DD"  
DATE_PRODUCT_GENERATED | INT | Product generation epoch.  
DATUM | STRING | Datum used in image creation.  
EARTH_SUN_DISTANCE | DOUBLE | Earth sun distance in astronomical units (AU).  
ELLIPSOID | STRING | Ellipsoid used in image creation.  
GEOMETRIC_RMSE_MODEL | DOUBLE | Combined Root Mean Square Error (RMSE) of the geometric residuals (meters) in both across-track and along-track directions measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GEOMETRIC_RMSE_MODEL_X | DOUBLE | RMSE of the X direction geometric residuals (in meters) measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GEOMETRIC_RMSE_MODEL_Y | DOUBLE | RMSE of the Y direction geometric residuals (in meters) measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GRID_CELL_SIZE_PANCHROMATIC | DOUBLE | Grid cell size used in creating the image for the panchromatic band.  
GRID_CELL_SIZE_REFLECTIVE | DOUBLE | Grid cell size used in creating the image for the reflective band.  
GRID_CELL_SIZE_THERMAL | DOUBLE | Grid cell size used in creating the image for the thermal band.  
GROUND_CONTROL_POINTS_MODEL | DOUBLE | The number of ground control points used. Not used in L1GT products. Values: 0 - 999 (0 is used for L1T products that have used Multi-scene refinement).  
GROUND_CONTROL_POINTS_VERSION | DOUBLE | The number of ground control points used in the verification of the terrain corrected product. Values: -1 to 1615 (-1 = not available)  
IMAGE_QUALITY_OLI | DOUBLE | The composite image quality for the OLI bands. Values: 9 = Best. 1 = Worst. 0 = Image quality not calculated. This parameter is only present if OLI bands are present in the product.  
IMAGE_QUALITY_TIRS | DOUBLE | The composite image quality for the TIRS bands. Values: 9 = Best. 1 = Worst. 0 = Image quality not calculated. This parameter is only present if OLI bands are present in the product.  
K1_CONSTANT_BAND_10 | DOUBLE | Calibration K1 constant for Band 10 radiance to temperature conversion.  
K1_CONSTANT_BAND_11 | DOUBLE | Calibration K1 constant for Band 11 radiance to temperature conversion.  
K2_CONSTANT_BAND_10 | DOUBLE | Calibration K2 constant for Band 10 radiance to temperature conversion.  
K2_CONSTANT_BAND_11 | DOUBLE | Calibration K2 constant for Band 11 radiance to temperature conversion.  
LANDSAT_PRODUCT_ID | STRING | The naming convention of each Landsat Collection N Level-1 image based on acquisition parameters and processing parameters. Format: LXSS_LLLL_PPPRRR_YYYYMMDD_yyyymmdd_CC_TX
  * L = Landsat
  * X = Sensor (O = Operational Land Imager, T = Thermal Infrared Sensor, C = Combined OLI/TIRS)
  * SS = Satellite (08 = Landsat 8)
  * LLLL = Processing Correction Level (L1TP = precision and terrain, L1GT = systematic terrain, L1GS = systematic)
  * PPP = WRS Path
  * RRR = WRS Row
  * YYYYMMDD = Acquisition Date expressed in Year, Month, Day
  * yyyymmdd = Processing Date expressed in Year, Month, Day
  * CC = Collection Number (02)
  * TX = Collection Category (RT = Real Time, T1 = Tier 1, T2 = Tier 2)

  
LANDSAT_SCENE_ID | STRING | The Pre-Collection naming convention of each image is based on acquisition parameters. This was the naming convention used prior to Collection 1. Format: LXSPPPRRRYYYYDDDGSIVV
  * L = Landsat
  * X = Sensor (O = Operational Land Imager, T = Thermal Infrared Sensor, C = Combined OLI/TIRS)
  * S = Satellite (08 = Landsat 8)
  * PPP = WRS Path
  * RRR = WRS Row
  * YYYY = Year of Acquisition
  * DDD = Julian Day of Acquisition
  * GSI = Ground Station Identifier
  * VV = Version

  
MAP_PROJECTION | STRING | Projection used to represent the 3-dimensional surface of the earth for the Level-1 product.  
NADIR_OFFNADIR | STRING | Nadir or Off-Nadir condition of the scene.  
ORIENTATION | STRING | Orientation used in creating the image. Values: NOMINAL = Nominal Path, NORTH_UP = North Up, TRUE_NORTH = True North, USER = User  
PANCHROMATIC_LINES | DOUBLE | Number of product lines for the panchromatic band.  
PANCHROMATIC_SAMPLES | DOUBLE | Number of product samples for the panchromatic bands.  
PROCESSING_SOFTWARE_VERSION | STRING | Name and version of the processing software used to generate the L1 product.  
RADIANCE_ADD_BAND_1 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 1.  
RADIANCE_ADD_BAND_10 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 10.  
RADIANCE_ADD_BAND_11 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 11.  
RADIANCE_ADD_BAND_2 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 2.  
RADIANCE_ADD_BAND_3 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 3.  
RADIANCE_ADD_BAND_4 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 4.  
RADIANCE_ADD_BAND_5 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 5.  
RADIANCE_ADD_BAND_6 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 6.  
RADIANCE_ADD_BAND_7 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 7.  
RADIANCE_ADD_BAND_8 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 8.  
RADIANCE_ADD_BAND_9 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 9.  
RADIANCE_MULT_BAND_1 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 1 DN to radiance.  
RADIANCE_MULT_BAND_10 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 10 DN to radiance.  
RADIANCE_MULT_BAND_11 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 11 DN to radiance.  
RADIANCE_MULT_BAND_2 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 2 DN to radiance.  
RADIANCE_MULT_BAND_3 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 3 DN to radiance.  
RADIANCE_MULT_BAND_4 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 4 DN to radiance.  
RADIANCE_MULT_BAND_5 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 5 DN to radiance.  
RADIANCE_MULT_BAND_6 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 6 DN to radiance.  
RADIANCE_MULT_BAND_7 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 7 DN to radiance.  
RADIANCE_MULT_BAND_8 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 8 DN to radiance.  
RADIANCE_MULT_BAND_9 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 9 DN to radiance.  
REFLECTANCE_ADD_BAND_1 | DOUBLE | Additive rescaling factor used to convert calibrated Band 1 DN to reflectance.  
REFLECTANCE_ADD_BAND_2 | DOUBLE | Additive rescaling factor used to convert calibrated Band 2 DN to reflectance.  
REFLECTANCE_ADD_BAND_3 | DOUBLE | Additive rescaling factor used to convert calibrated Band 3 DN to reflectance.  
REFLECTANCE_ADD_BAND_4 | DOUBLE | Additive rescaling factor used to convert calibrated Band 4 DN to reflectance.  
REFLECTANCE_ADD_BAND_5 | DOUBLE | Additive rescaling factor used to convert calibrated Band 5 DN to reflectance.  
REFLECTANCE_ADD_BAND_7 | DOUBLE | Multiplicative factor used to convert calibrated Band 7 DN to reflectance.  
REFLECTANCE_ADD_BAND_8 | DOUBLE | Multiplicative factor used to convert calibrated Band 8 DN to reflectance.  
REFLECTANCE_ADD_BAND_9 | DOUBLE | Minimum achievable spectral reflectance value for Band 8.  
REFLECTANCE_MULT_BAND_1 | DOUBLE | Multiplicative factor used to convert calibrated Band 1 DN to reflectance.  
REFLECTANCE_MULT_BAND_2 | DOUBLE | Multiplicative factor used to convert calibrated Band 2 DN to reflectance.  
REFLECTANCE_MULT_BAND_3 | DOUBLE | Multiplicative factor used to convert calibrated Band 3 DN to reflectance.  
REFLECTANCE_MULT_BAND_4 | DOUBLE | Multiplicative factor used to convert calibrated Band 4 DN to reflectance.  
REFLECTANCE_MULT_BAND_5 | DOUBLE | Multiplicative factor used to convert calibrated Band 5 DN to reflectance.  
REFLECTANCE_MULT_BAND_6 | DOUBLE | Multiplicative factor used to convert calibrated Band 6 DN to reflectance.  
REFLECTANCE_MULT_BAND_7 | DOUBLE | Multiplicative factor used to convert calibrated Band 7 DN to reflectance.  
REFLECTANCE_MULT_BAND_8 | DOUBLE | Multiplicative factor used to convert calibrated Band 8 DN to reflectance.  
REFLECTANCE_MULT_BAND_9 | DOUBLE | Multiplicative factor used to convert calibrated Band 9 DN to reflectance.  
REFLECTIVE_LINES | DOUBLE | Number of product lines for the reflective bands.  
REFLECTIVE_SAMPLES | DOUBLE | Number of product samples for the reflective bands.  
REQUEST_ID | STRING | Request id, nnnyymmdd0000_0000
  * nnn = node number
  * yy = year
  * mm = month
  * dd = day

  
RESAMPLING_OPTION | STRING | Resampling option used in creating the image.  
ROLL_ANGLE | DOUBLE | The amount of spacecraft roll angle at the scene center.  
SATURATION_BAND_1 | STRING | Flag indicating saturated pixels for band 1 ('Y'/'N')  
SATURATION_BAND_10 | STRING | Flag indicating saturated pixels for band 10 ('Y'/'N')  
SATURATION_BAND_11 | STRING | Flag indicating saturated pixels for band 11 ('Y'/'N')  
SATURATION_BAND_2 | STRING | Flag indicating saturated pixels for band 2 ('Y'/'N')  
SATURATION_BAND_3 | STRING | Flag indicating saturated pixels for band 3 ('Y'/'N')  
SATURATION_BAND_4 | STRING | Flag indicating saturated pixels for band 4 ('Y'/'N')  
SATURATION_BAND_5 | STRING | Flag indicating saturated pixels for band 5 ('Y'/'N')  
SATURATION_BAND_6 | STRING | Flag indicating saturated pixels for band 6 ('Y'/'N')  
SATURATION_BAND_7 | STRING | Flag indicating saturated pixels for band 7 ('Y'/'N')  
SATURATION_BAND_8 | STRING | Flag indicating saturated pixels for band 8 ('Y'/'N')  
SATURATION_BAND_9 | STRING | Flag indicating saturated pixels for band 9 ('Y'/'N')  
SCENE_CENTER_TIME | STRING | Scene center time of acquired image. HH:MM:SS.SSSSSSSZ
  * HH = Hour (00-23)
  * MM = Minutes
  * SS.SSSSSSS = Fractional seconds
  * Z = "Zulu" time (same as GMT)

  
SENSOR_ID | STRING | Sensor used to capture data.  
SPACECRAFT_ID | STRING | Spacecraft identification.  
STATION_ID | STRING | Ground Station/Organisation that received the data.  
SUN_AZIMUTH | DOUBLE | Sun azimuth angle in degrees for the image center location at the image center acquisition time.  
SUN_ELEVATION | DOUBLE | Sun elevation angle in degrees for the image center location at the image center acquisition time.  
TARGET_WRS_PATH | DOUBLE | Nearest WRS-2 path to the line-of-sight scene center of the image.  
TARGET_WRS_ROW | DOUBLE | Nearest WRS-2 row to the line-of-sight scene center of the image. Rows 880-889 and 990-999 are reserved for the polar regions where it is undefined in the WRS-2.  
THERMAL_LINES | DOUBLE | Number of product lines for the thermal band.  
THERMAL_SAMPLES | DOUBLE | Number of product samples for the thermal band.  
TIRS_SSM_MODEL | STRING | Due to an anomalous condition on the Thermal Infrared Sensor (TIRS) Scene Select Mirror (SSM) encoder electronics, this field has been added to indicate which model was used to process the data. (Actual, Preliminary, Final)  
TIRS_SSM_POSITION_STATUS | STRING | TIRS SSM position status.  
TIRS_STRAY_LIGHT_CORRECTION_SOURCE | STRING | TIRS stray light correction source.  
TRUNCATION_OLI | STRING | Region of OLCI truncated.  
UTM_ZONE | DOUBLE | UTM zone number used in product map projection.  
WRS_PATH | DOUBLE | The WRS orbital path number (001 - 251).  
WRS_ROW | DOUBLE | Landsat satellite WRS row (001-248).  
WRS_TYPE | DOUBLE | World Reference System (WRS) type used for the collection of this scene.  
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T2#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDSAT/LC08/C02/T2')
.filterDate('2017-01-01','2017-12-31');
vartrueColor432=dataset.select(['B4','B3','B2']);
vartrueColor432Vis={
min:0.0,
max:30000.0,
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(trueColor432,trueColor432Vis,'True Color (432)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LC08_C02_T2)
[ USGS Landsat 8 Collection 2 Tier 2 Raw Scenes ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T2)
Landsat 8 Collection 2 Tier 2 DN values, representing scaled, calibrated at-sensor radiance. Scenes not meeting Tier 1 criteria during processing are assigned to Tier 2. This includes Systematic terrain (L1GT) and Systematic (L1GS) processed scenes, as well as any L1TP scenes that do not meet the Tier 1 specifications …
LANDSAT/LC08/C02/T2, c2,global,l8,landsat,lc8,oli-tirs,radiance,satellite-imagery,t2,tier2,usgs 
2021-10-28T23:17:26Z/2025-04-13T15:57:46.366000Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.usgs.gov/land-resources/nli/landsat/landsat-8-data-users-handbook)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T2)


