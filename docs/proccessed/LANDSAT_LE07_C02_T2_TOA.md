 
#  USGS Landsat 7 Collection 2 Tier 2 TOA Reflectance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDSAT/LE07/C02/T2_TOA](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_LE07_C02_T2_TOA_sample.png) 

Dataset Availability
    2003-12-01T01:15:15Z–2024-01-19T00:08:51.725000Z 

Dataset Provider
     [ USGS/Google ](https://landsat.usgs.gov/) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/LE07/C02/T2_TOA")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LE07_C02_T2_TOA) 

Revisit Interval
    16 Days 

Tags
     [c2](https://developers.google.com/earth-engine/datasets/tags/c2) [global](https://developers.google.com/earth-engine/datasets/tags/global) [landsat](https://developers.google.com/earth-engine/datasets/tags/landsat) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [toa](https://developers.google.com/earth-engine/datasets/tags/toa) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T2_TOA#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T2_TOA#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T2_TOA#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T2_TOA#terms-of-use) More
Landsat 7 Collection 2 Tier 2 calibrated top-of-atmosphere (TOA) reflectance. Calibration coefficients are extracted from the image metadata. See [Chander et al. (2009)](https://www.sciencedirect.com/science/article/pii/S0034425709000169) for details on the TOA computation.
Note that [Landsat 7's orbit has been drifting to an earlier acquisition time since 2017](https://www.sciencedirect.com/science/article/pii/S2666017221000134?via%3Dihub).
**Bands**
Name | Pixel Size | Wavelength | Description  
---|---|---|---  
`B1` |  30 meters  | 0.45 - 0.52 μm | Blue  
`B2` |  30 meters  | 0.52 - 0.60 μm | Green  
`B3` |  30 meters  | 0.63 - 0.69 μm | Red  
`B4` |  30 meters  | 0.77 - 0.90 μm | Near infrared  
`B5` |  30 meters  | 1.55 - 1.75 μm | Shortwave infrared 1  
`B6_VCID_1` |  60 meters  | 10.40 - 12.50 μm | Low-gain Thermal Infrared 1. This band has expanded dynamic range and lower radiometric resolution (sensitivity), with less saturation at high Digital Number (DN) values. Resampled from 60m to 30m.  
`B6_VCID_2` |  60 meters  | 10.40 - 12.50 μm | High-gain Thermal Infrared 1. This band has higher radiometric resolution (sensitivity), although it has a more restricted dynamic range. Resampled from 60m to 30m.  
`B7` |  30 meters  | 2.08 - 2.35 μm | Shortwave infrared 2  
`B8` |  15 meters  | 0.52 - 0.90 μm | Panchromatic  
`QA_PIXEL` |  30 meters  | Landsat Collection 2 TM/ETM QA Bitmask  
Bitmask for QA_PIXEL
  * Bit 0: Fill 
    * 0: Image data
    * 1: Fill data
  * Bit 1: Dilated Cloud 
    * 0: Cloud is not dilated or no cloud
    * 1: Cloud dilation
  * Bit 2: Unused 
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
  * Bits 14-15: Unused 

  
`QA_RADSAT` |  30 meters  | Radiometric saturation QA  
Bitmask for QA_RADSAT
  * Bit 0: Band 1 data saturated 
  * Bit 1: Band 2 data saturated 
  * Bit 2: Band 3 data saturated 
  * Bit 3: Band 4 data saturated 
  * Bit 4: Band 5 data saturated 
  * Bit 5: Band 6L data saturated 
  * Bit 6: Band 7 data saturated 
  * Bit 7: Unused 
  * Bit 8: Band 6H data saturated 
  * Bit 9: Dropped pixel 
    * 0: Pixel present
    * 1: Detector does not have a value

  
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
CORRECTION_BIAS_BAND_1 | STRING | Internal calibration bias method for band 1.  
CORRECTION_BIAS_BAND_2 | STRING | Internal calibration bias method for band 2.  
CORRECTION_BIAS_BAND_3 | STRING | Internal calibration bias method for band 3.  
CORRECTION_BIAS_BAND_4 | STRING | Internal calibration bias method for band 4.  
CORRECTION_BIAS_BAND_5 | STRING | Internal calibration bias method for band 5.  
CORRECTION_BIAS_BAND_6_VCID_1 | STRING | Internal calibration bias method for band 6_VICD_1.  
CORRECTION_BIAS_BAND_6_VCID_2 | STRING | Internal calibration bias method for band 6_VICD_2.  
CORRECTION_BIAS_BAND_7 | STRING | Internal calibration bias method for band 7.  
CORRECTION_BIAS_BAND_8 | STRING | Internal calibration bias method for band 8.  
CORRECTION_GAIN_BAND_1 | STRING | Internal calibration gain method for band 1.  
CORRECTION_GAIN_BAND_2 | STRING | Internal calibration gain method for band 2.  
CORRECTION_GAIN_BAND_3 | STRING | Internal calibration gain method for band 3.  
CORRECTION_GAIN_BAND_4 | STRING | Internal calibration gain method for band 4.  
CORRECTION_GAIN_BAND_5 | STRING | Internal calibration gain method for band 5.  
CORRECTION_GAIN_BAND_6_VCID_1 | STRING | Internal calibration gain method for band 6_VCID_1.  
CORRECTION_GAIN_BAND_6_VCID_2 | STRING | Internal calibration gain method for band 6_VCID_2.  
CORRECTION_GAIN_BAND_7 | STRING | Internal calibration gain method for band 7.  
CORRECTION_GAIN_BAND_8 | STRING | Internal calibration gain method for band 8.  
DATA_SOURCE_ELEVATION | STRING | Indicates the source of the DEM used in the correction process. Possible values: "GLS2000", "RAMP", "GTOPO30".'  
DATE_ACQUIRED | STRING | Image acquisition date. "YYYY-MM-DD"  
DATE_PRODUCT_GENERATED | INT | Product generation epoch.  
DATUM | STRING | Datum used in image creation.  
EARTH_SUN_DISTANCE | DOUBLE | Earth sun distance in astronomical units (AU).  
ELLIPSOID | STRING | Ellipsoid used in image creation.  
EPHEMERIS_TYPE | STRING | Ephemeris data type used to perform geometric correction. (Definitive or Predictive)  
GAIN_BAND_1 | STRING | Gain state for Band 1. (L = Low gain, H = High)  
GAIN_BAND_2 | STRING | Gain state for Band 2. (L = Low gain, H = High)  
GAIN_BAND_3 | STRING | Gain state for Band 3. (L = Low gain, H = High)  
GAIN_BAND_4 | STRING | Gain state for Band 4. (L = Low gain, H = High)  
GAIN_BAND_5 | STRING | Gain state for Band 5. (L = Low gain, H = High)  
GAIN_BAND_6_VCID_1 | STRING | Gain state for Band 6 VCID_1. (L = Low gain, H = High)  
GAIN_BAND_6_VCID_2 | STRING | Gain state for Band 6 VCID_2. (L = Low gain, H = High)  
GAIN_BAND_7 | STRING | Gain state for Band 7. (L = Low gain, H = High)  
GAIN_BAND_8 | STRING | Gain state for Band 8. (L = Low gain, H = High)  
GAIN_CHANGE_BAND_1 | STRING | Presence and direction of gain change for Band 1 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_2 | STRING | Presence and direction of gain change for Band 2 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_3 | STRING | Presence and direction of gain change for Band 3 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_4 | STRING | Presence and direction of gain change for Band 4 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_5 | STRING | Presence and direction of gain change for Band 5 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_6_VCID_1 | STRING | Presence and direction of gain change for Band 6 VCID_1 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_6_VCID_2 | STRING | Presence and direction of gain change for Band 6 VCID_2 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_7 | STRING | Presence and direction of gain change for Band 7 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_BAND_8 | STRING | Presence and direction of gain change for Band 8 (LL = no change, HH = no change, LH = low to high, HL = high to low, U = Unknown).  
GAIN_CHANGE_SCAN_BAND_1 | DOUBLE | Scan line number where the first change in Band 1 gain was detected.  
GAIN_CHANGE_SCAN_BAND_2 | DOUBLE | Scan line number where the first change in Band 2 gain was detected.  
GAIN_CHANGE_SCAN_BAND_3 | DOUBLE | Scan line number where the first change in Band 3 gain was detected.  
GAIN_CHANGE_SCAN_BAND_4 | DOUBLE | Scan line number where the first change in Band 4 gain was detected.  
GAIN_CHANGE_SCAN_BAND_5 | DOUBLE | Scan line number where the first change in Band 5 gain was detected.  
GAIN_CHANGE_SCAN_BAND_6_VCID_1 | DOUBLE | Scan line number where the first change in Band 6 VCID 1 gain was detected.  
GAIN_CHANGE_SCAN_BAND_6_VCID_2 | DOUBLE | Scan line number where the first change in Band 6 VCID 2 gain was detected.  
GAIN_CHANGE_SCAN_BAND_7 | DOUBLE | Scan line number where the first change in Band 7 gain was detected.  
GAIN_CHANGE_SCAN_BAND_8 | DOUBLE | Scan line number where the first change in Band 8 gain was detected.  
GEOMETRIC_RMSE_MODEL | DOUBLE | Combined Root Mean Square Error (RMSE) of the geometric residuals (meters) in both across-track and along-track directions measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GEOMETRIC_RMSE_MODEL_X | DOUBLE | RMSE of the X direction geometric residuals (in meters) measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GEOMETRIC_RMSE_MODEL_Y | DOUBLE | RMSE of the Y direction geometric residuals (in meters) measured on the GCPs used in geometric precision correction. Not present in L1G products.  
GRID_CELL_SIZE_PANCHROMATIC | DOUBLE | Grid cell size used in creating the image for the panchromatic band.  
GRID_CELL_SIZE_REFLECTIVE | DOUBLE | Grid cell size used in creating the image for the reflective band.  
GRID_CELL_SIZE_THERMAL | DOUBLE | Grid cell size used in creating the image for the thermal band.  
GROUND_CONTROL_POINTS_MODEL | DOUBLE | The number of ground control points used. Not used in L1GT products. Values: 0 - 999 (0 is used for L1T products that have used Multi-scene refinement).  
GROUND_CONTROL_POINTS_VERSION | DOUBLE | The number of ground control points used in the verification of the terrain corrected product. Values: -1 to 1615 (-1 = not available)  
IMAGE_QUALITY | DOUBLE | Image quality, 0 = worst, 9 = best, -1 = quality not calculated  
K1_CONSTANT_BAND_6_VCID_1 | DOUBLE | Calibration K1 constant for Band 6 VCID 1 radiance to temperature conversion.  
K1_CONSTANT_BAND_6_VCID_2 | DOUBLE | Calibration K1 constant for Band 6 VCID 2 radiance to temperature conversion.  
K2_CONSTANT_BAND_6_VCID_1 | DOUBLE | Calibration K2 constant for Band 6 VCID 1 radiance to temperature conversion.  
K2_CONSTANT_BAND_6_VCID_2 | DOUBLE | Calibration K2 constant for Band 6 VCID 2 radiance to temperature conversion.  
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
ORIENTATION | STRING | Orientation used in creating the image. Values: NOMINAL = Nominal Path, NORTH_UP = North Up, TRUE_NORTH = True North, USER = User  
PANCHROMATIC_LINES | DOUBLE | Number of product lines for the panchromatic band.  
PANCHROMATIC_SAMPLES | DOUBLE | Number of product samples for the panchromatic bands.  
PROCESSING_LEVEL | STRING | One of L1GS, L1GT, or L1TP.  
PROCESSING_SOFTWARE_VERSION | STRING | Name and version of the processing software used to generate the L1 product.  
RADIANCE_ADD_BAND_1 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 1.  
RADIANCE_ADD_BAND_2 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 2.  
RADIANCE_ADD_BAND_3 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 3.  
RADIANCE_ADD_BAND_4 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 4.  
RADIANCE_ADD_BAND_5 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 5.  
RADIANCE_ADD_BAND_6_VCID_1 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 6 VCID 1.  
RADIANCE_ADD_BAND_6_VCID_2 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 6 VCID 2.  
RADIANCE_ADD_BAND_7 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 7.  
RADIANCE_ADD_BAND_8 | DOUBLE | Additive rescaling factor used to convert calibrated DN to radiance for Band 8.  
RADIANCE_MULT_BAND_1 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 1 DN to radiance.  
RADIANCE_MULT_BAND_2 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 2 DN to radiance.  
RADIANCE_MULT_BAND_3 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 3 DN to radiance.  
RADIANCE_MULT_BAND_4 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 4 DN to radiance.  
RADIANCE_MULT_BAND_5 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 5 DN to radiance.  
RADIANCE_MULT_BAND_6_VCID_1 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 6 VCID 1 DN to radiance.  
RADIANCE_MULT_BAND_6_VCID_2 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 6 VCID 2 DN to radiance.  
RADIANCE_MULT_BAND_7 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 7 DN to radiance.  
RADIANCE_MULT_BAND_8 | DOUBLE | Multiplicative rescaling factor used to convert calibrated Band 8 DN to radiance.  
REFLECTANCE_ADD_BAND_1 | DOUBLE | Additive rescaling factor used to convert calibrated Band 1 DN to reflectance.  
REFLECTANCE_ADD_BAND_2 | DOUBLE | Additive rescaling factor used to convert calibrated Band 2 DN to reflectance.  
REFLECTANCE_ADD_BAND_3 | DOUBLE | Additive rescaling factor used to convert calibrated Band 3 DN to reflectance.  
REFLECTANCE_ADD_BAND_4 | DOUBLE | Additive rescaling factor used to convert calibrated Band 4 DN to reflectance.  
REFLECTANCE_ADD_BAND_5 | DOUBLE | Additive rescaling factor used to convert calibrated Band 5 DN to reflectance.  
REFLECTANCE_ADD_BAND_7 | DOUBLE | Additive rescaling factor used to convert calibrated Band 7 DN to reflectance.  
REFLECTANCE_ADD_BAND_8 | DOUBLE | Additive rescaling factor used to convert calibrated Band 8 DN to reflectance.  
REFLECTANCE_MULT_BAND_1 | DOUBLE | Multiplicative factor used to convert calibrated Band 1 DN to reflectance.  
REFLECTANCE_MULT_BAND_2 | DOUBLE | Multiplicative factor used to convert calibrated Band 2 DN to reflectance.  
REFLECTANCE_MULT_BAND_3 | DOUBLE | Multiplicative factor used to convert calibrated Band 3 DN to reflectance.  
REFLECTANCE_MULT_BAND_4 | DOUBLE | Multiplicative factor used to convert calibrated Band 4 DN to reflectance.  
REFLECTANCE_MULT_BAND_5 | DOUBLE | Multiplicative factor used to convert calibrated Band 5 DN to reflectance.  
REFLECTANCE_MULT_BAND_7 | DOUBLE | Multiplicative factor used to convert calibrated Band 7 DN to reflectance.  
REFLECTANCE_MULT_BAND_8 | DOUBLE | Multiplicative factor used to convert calibrated Band 8 DN to reflectance.  
REFLECTIVE_LINES | DOUBLE | Number of product lines for the reflective bands.  
REFLECTIVE_SAMPLES | DOUBLE | Number of product samples for the reflective bands.  
REQUEST_ID | STRING | Request id, nnnyymmdd0000_0000
  * nnn = node number
  * yy = year
  * mm = month
  * dd = day

  
RESAMPLING_OPTION | STRING | Resampling option used in creating the image.  
SATURATION_BAND_1 | STRING | Flag indicating saturated pixels for band 1 ('Y'/'N')  
SATURATION_BAND_2 | STRING | Flag indicating saturated pixels for band 2 ('Y'/'N')  
SATURATION_BAND_3 | STRING | Flag indicating saturated pixels for band 3 ('Y'/'N')  
SATURATION_BAND_4 | STRING | Flag indicating saturated pixels for band 4 ('Y'/'N')  
SATURATION_BAND_5 | STRING | Flag indicating saturated pixels for band 5 ('Y'/'N')  
SATURATION_BAND_6_VCID_1 | STRING | Flag indicating saturated pixels for band 6 VCID 1 ('Y'/'N')  
SATURATION_BAND_6_VCID_2 | STRING | Flag indicating saturated pixels for band 6 VCID 2 ('Y'/'N')  
SATURATION_BAND_7 | STRING | Flag indicating saturated pixels for band 7 ('Y'/'N')  
SATURATION_BAND_8 | STRING | Flag indicating saturated pixels for band 8 ('Y'/'N')  
SCENE_CENTER_TIME | STRING | Scene center time of acquired image. HH:MM:SS.SSSSSSSZ
  * HH = Hour (00-23)
  * MM = Minutes
  * SS.SSSSSSS = Fractional seconds
  * Z = "Zulu" time (same as GMT)

  
SENSOR_ANOMALIES | STRING | Indicates if shutter intrusion is found within scene.  
SENSOR_ID | STRING | Sensor used to capture data.  
SENSOR_MODE | STRING | Operational mode. Scan Angle Monitor (SAM) or BUMPER.  
SENSOR_MODE_SLC | STRING | Indicates the Scan Line Corrector (SLC) was ON.  
SPACECRAFT_ID | STRING | Spacecraft identification.  
STATION_ID | STRING | Ground Station/Organisation that received the data.  
SUN_AZIMUTH | DOUBLE | Sun azimuth angle in degrees for the image center location at the image center acquisition time.  
SUN_ELEVATION | DOUBLE | Sun elevation angle in degrees for the image center location at the image center acquisition time.  
THERMAL_LINES | DOUBLE | Number of product lines for the thermal band.  
THERMAL_SAMPLES | DOUBLE | Number of product samples for the thermal band.  
UTM_ZONE | DOUBLE | UTM zone number used in product map projection.  
WRS_PATH | DOUBLE | The WRS orbital path number (001 - 251).  
WRS_ROW | DOUBLE | Landsat satellite WRS row (001-248).  
WRS_TYPE | STRING | World Reference System (WRS) type used for the collection of this scene.  
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T2_TOA#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('LANDSAT/LE07/C02/T2_TOA')
.filterDate('1999-01-01','2002-12-31');
vartrueColor321=dataset.select(['B3','B2','B1']);
vartrueColor321Vis={
min:0.0,
max:0.4,
gamma:1.2,
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(trueColor321,trueColor321Vis,'True Color (321)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LE07_C02_T2_TOA)
[ USGS Landsat 7 Collection 2 Tier 2 TOA Reflectance ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T2_TOA)
Landsat 7 Collection 2 Tier 2 calibrated top-of-atmosphere (TOA) reflectance. Calibration coefficients are extracted from the image metadata. See Chander et al. (2009) for details on the TOA computation. Note that Landsat 7's orbit has been drifting to an earlier acquisition time since 2017.
LANDSAT/LE07/C02/T2_TOA, c2,global,landsat,satellite-imagery,toa,usgs 
2003-12-01T01:15:15Z/2024-01-19T00:08:51.725000Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://landsat.usgs.gov/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T2_TOA)


