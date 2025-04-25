 
#  USGS Landsat 9 Level 2, Collection 2, Tier 1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![LANDSAT/LC09/C02/T1_L2](https://developers.google.com/earth-engine/datasets/images/LANDSAT/LANDSAT_LC09_C02_T1_L2_sample.png) 

Dataset Availability
    2021-10-31T00:00:00Z–2025-04-20T23:46:18.608000Z 

Dataset Provider
     [ USGS ](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products) 

Earth Engine Snippet
     `    ee.ImageCollection("LANDSAT/LC09/C02/T1_L2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LC09_C02_T1_L2) 

Revisit Interval
    16 Days 

Tags
     [cfmask](https://developers.google.com/earth-engine/datasets/tags/cfmask) [cloud](https://developers.google.com/earth-engine/datasets/tags/cloud) [fmask](https://developers.google.com/earth-engine/datasets/tags/fmask) [global](https://developers.google.com/earth-engine/datasets/tags/global) [l9sr](https://developers.google.com/earth-engine/datasets/tags/l9sr) [landsat](https://developers.google.com/earth-engine/datasets/tags/landsat) [lasrc](https://developers.google.com/earth-engine/datasets/tags/lasrc) [lc09](https://developers.google.com/earth-engine/datasets/tags/lc09) [lst](https://developers.google.com/earth-engine/datasets/tags/lst) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2#terms-of-use) More
This dataset contains atmospherically corrected surface reflectance and land surface temperature derived from the data produced by the Landsat 9 OLI/TIRS sensors. These images contain 5 visible and near-infrared (VNIR) bands and 2 short-wave infrared (SWIR) bands processed to orthorectified surface reflectance, and one thermal infrared (TIR) band processed to orthorectified surface temperature. They also contain intermediate bands used in calculation of the ST products, as well as QA bands.
Landsat 9 SR products are created with the Land Surface Reflectance Code (LaSRC). All Collection 2 ST products are created with a single-channel algorithm jointly created by the Rochester Institute of Technology (RIT) and National Aeronautics and Space Administration (NASA) Jet Propulsion Laboratory (JPL).
Strips of collected data are packaged into overlapping "scenes" covering approximately 170km x 183km using a [standardized reference grid](https://landsat.gsfc.nasa.gov/about/worldwide-reference-system).
Some assets have only SR data, in which case ST bands are present but empty. For assets with both ST and SR bands, 'PROCESSING_LEVEL' is set to 'L2SP'. For assets with only SR bands, 'PROCESSING_LEVEL' is set to 'L2SR'.
[Additional documentation and usage examples.](https://developers.google.com/earth-engine/guides/landsat)
Data provider notes:
  * Data products must contain both optical and thermal data to be successfully processed to surface temperature, as ASTER NDVI is required to temporally adjust the ASTER GED product to the target Landsat scene. Therefore, night time acquisitions cannot be processed to surface temperature.
  * A known error exists in the surface temperature retrievals relative to clouds and possibly cloud shadows. The characterization of these issues has been documented by [Cook et al., (2014)](https://doi.org/10.3390/rs61111244).
  * ASTER GED contains areas of missing mean emissivity data required for successful ST product generation. If there is missing ASTER GED information, there will be missing ST data in those areas.
  * The ASTER GED dataset is created from all clear-sky pixels of ASTER scenes acquired from 2000 through 2008. While this dataset has a global spatial extent, there are areas missing mean emissivity information due to persistent cloud contamination in the ASTER measurements.
  * The USGS further screens unphysical values (emissivity < 0.6) in ASTER GED to remove any emissivity underestimation due to undetected clouds. For any given pixel with no ASTER GED input or unphysical emissivity value, the resulting Landsat ST products have missing pixels. The missing Landsat ST pixels will be consistent through time (1982-present) given the static nature of ASTER GED mean climatology data. For more information refer to [landsat-collection-2-surface-temperature-data-gaps-due-missing](https://www.usgs.gov/landsat-missions/landsat-collection-2-surface-temperature-data-gaps-due-missing-aster-ged)


**Pixel Size** 30 meters 
**Bands**
Name | Units | Min | Max | Scale | Offset | Wavelength | Description  
---|---|---|---|---|---|---|---  
`SR_B1` |  1  |  65455  | 2.75e-05 | -0.2 | 0.435-0.451 μm | Band 1 (ultra blue, coastal aerosol) surface reflectance  
`SR_B2` |  1  |  65455  | 2.75e-05 | -0.2 | 0.452-0.512 μm | Band 2 (blue) surface reflectance  
`SR_B3` |  1  |  65455  | 2.75e-05 | -0.2 | 0.533-0.590 μm | Band 3 (green) surface reflectance  
`SR_B4` |  1  |  65455  | 2.75e-05 | -0.2 | 0.636-0.673 μm | Band 4 (red) surface reflectance  
`SR_B5` |  1  |  65455  | 2.75e-05 | -0.2 | 0.851-0.879 μm | Band 5 (near infrared) surface reflectance  
`SR_B6` |  1  |  65455  | 2.75e-05 | -0.2 | 1.566-1.651 μm | Band 6 (shortwave infrared 1) surface reflectance  
`SR_B7` |  1  |  65455  | 2.75e-05 | -0.2 | 2.107-2.294 μm | Band 7 (shortwave infrared 2) surface reflectance  
`SR_QA_AEROSOL` | Aerosol attributes  
Bitmask for SR_QA_AEROSOL
  * Bit 0: Fill 
  * Bit 1: Aerosol retrieval - valid 
  * Bit 2: Water pixel 
  * Bit 3: Unused 
  * Bit 4: Unused 
  * Bit 5: Interpolated Aerosol 
  * Bits 6-7: Aerosol Level 
    * 0: Climatology
    * 1: Low
    * 2: Medium
    * 3: High

  
`ST_B10` | K |  0  |  65535  | 0.00341802 | 149 | 10.60-11.19 μm | Band 10 surface temperature. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_ATRAN` |  0  |  10000  | 0.0001 | Atmospheric Transmittance. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_CDIST` | km |  0  |  24000  | 0.01 | Pixel distance to cloud. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_DRAD` | W/(m^2*sr*um)/ DN |  0  |  28000  | 0.001 | Downwelled Radiance. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_EMIS` |  0  |  10000  | 0.0001 | Emissivity of Band 10 estimated from ASTER GED. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_EMSD` |  0  |  10000  | 0.0001 | Emissivity standard deviation. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_QA` | K |  0  |  32767  | 0.01 | Uncertainty of the Surface Temperature band. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_TRAD` | W/(m^2*sr*um)/ DN |  0  |  22000  | 0.001 | Thermal band converted to radiance. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`ST_URAD` | W/(m^2*sr*um)/ DN |  0  |  28000  | 0.001 | Upwelled Radiance. If 'PROCESSING_LEVEL' is set to 'L2SR', this band is fully masked out.  
`QA_PIXEL` | Pixel quality attributes generated from the CFMASK algorithm.  
Bitmask for QA_PIXEL
  * Bit 0: Fill 
  * Bit 1: Dilated Cloud 
  * Bit 2: Cirrus (high confidence) 
  * Bit 3: Cloud 
  * Bit 4: Cloud Shadow 
  * Bit 5: Snow 
  * Bit 6: Clear 
    * 0: Cloud or Dilated Cloud bits are set
    * 1: Cloud and Dilated Cloud bits are not set
  * Bit 7: Water 
  * Bits 8-9: Cloud Confidence 
    * 0: None
    * 1: Low
    * 2: Medium
    * 3: High
  * Bits 10-11: Cloud Shadow Confidence 
    * 0: None
    * 1: Low
    * 2: Medium
    * 3: High
  * Bits 12-13: Snow/Ice Confidence 
    * 0: None
    * 1: Low
    * 2: Medium
    * 3: High
  * Bits 14-15: Cirrus Confidence 
    * 0: None
    * 1: Low
    * 2: Medium
    * 3: High

  
`QA_RADSAT` | Radiometric saturation QA  
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
  * Bit 9: Unused 
  * Bit 10: Unused 
  * Bit 11: Terrain occlusion 

  
**Image Properties**
Name | Type | Description  
---|---|---  
ALGORITHM_SOURCE_SURFACE_REFLECTANCE | STRING | Name and version of the surface reflectance algorithm.  
ALGORITHM_SOURCE_SURFACE_TEMPERATURE | STRING | Name and version of the surface temperature algorithm.  
CLOUD_COVER | DOUBLE | Percentage cloud cover (0-100), -1 = not calculated.  
CLOUD_COVER_LAND | DOUBLE | Percentage cloud cover over land (0-100), -1 = not calculated.  
COLLECTION_CATEGORY | STRING | Scene collection category, "T1" or "T2".  
DATA_SOURCE_AIR_TEMPERATURE | STRING | Air temperature data source.  
DATA_SOURCE_ELEVATION | STRING | Elevation data source.  
DATA_SOURCE_OZONE | STRING | Ozone data source.  
DATA_SOURCE_PRESSURE | STRING | Pressure data source.  
DATA_SOURCE_REANALYSIS | STRING | Reanalysis data source.  
DATA_SOURCE_TIRS_STRAY_LIGHT_CORRECTION | STRING | TIRS stray light correction data source.  
DATA_SOURCE_WATER_VAPOR | STRING | Water vapor data source.  
DATE_PRODUCT_GENERATED | DOUBLE | Timestamp of the date when the product was generated.  
EARTH_SUN_DISTANCE | DOUBLE | Earth-Sun distance (AU).  
EPHEMERIS_TYPE | STRING | Identifier to inform the user of the orbital ephemeris type used: "DEFINITIVE" or "PREDICTIVE". If the field is not present, the user should assume "PREDICTIVE".  
GEOMETRIC_RMSE_MODEL | DOUBLE | Combined RMSE (Root Mean Square Error) of the geometric residuals (meters) in both across-track and along-track directions. This parameter is only present if the L1_PROCESSING_LEVEL is L1TP.  
GEOMETRIC_RMSE_MODEL_X | DOUBLE | RMSE (Root Mean Square Error) of the geometric residuals (meters) measured on the GCPs (Ground Control Points) used in geometric precision correction in the across-track direction. This parameter is only present if the L1_PROCESSING_LEVEL is L1TP.  
GEOMETRIC_RMSE_MODEL_Y | DOUBLE | RMSE (Root Mean Square Error) of the geometric residuals (meters) measured on the GCPs (Ground Control Points) used in geometric precision correction in the along-track direction. This parameter is only present if the L1_PROCESSING_LEVEL is L1TP.  
GEOMETRIC_RMSE_VERIFY | DOUBLE | RMSE of the geometric residuals (meters) measured on the terrain-corrected product independently using GLS2000. This parameter is only present if the L1_PROCESSING_LEVEL is L1TP.  
GROUND_CONTROL_POINTS_MODEL | DOUBLE | Number of GCPs used in the precision correction process. This parameter is only present if the L1_PROCESSING_LEVEL is L1TP.  
GROUND_CONTROL_POINTS_VERIFY | DOUBLE | Number of GCPs (Ground Control Points) used in the verification of the terrain corrected product.  
GROUND_CONTROL_POINTS_VERSION | DOUBLE | GCP dataset version used in the precision correction process. This parameter is only present if the L1_PROCESSING_LEVEL is L1TP.  
IMAGE_QUALITY_OLI | INT | Image quality of the OLI bands. 1 = worst, 9 = best, 0 = quality not calculated. For Landsat 8, this parameter is adjusted downward for scenes collected using the lower 12 bits from the OLI sensor (TRUNCATION_OLI = "LOWER").  
IMAGE_QUALITY_TIRS | INT | Image quality of the TIRS bands. 1 = worst, 9 = best, 0 = quality not calculated. It is also adjusted downward for scenes processed with "SWITCHED" for the TIRS_SSM_POSITION_STATUS value.  
L1_DATE_PRODUCT_GENERATED | STRING | Product generation date for the corresponding L1 product.  
L1_LANDSAT_PRODUCT_ID | STRING | Landsat Product Identifier for the corresponding L1 product.  
L1_PROCESSING_LEVEL | STRING | Processing Level for the corresponding L1 product.  
L1_PROCESSING_SOFTWARE_VERSION | STRING | Processing software version for the corresponding L1 product.  
LANDSAT_PRODUCT_ID | STRING | Landsat Product Identifier  
LANDSAT_SCENE_ID | STRING | Short Landsat Scene Identifier  
PROCESSING_LEVEL | STRING | "L2SP" when both SR and LST bands are present, or "L2SR" when only SR bands are present.  
PROCESSING_SOFTWARE_VERSION | STRING | The processing software version that created the product.  
ROLL_ANGLE | DOUBLE | The amount of spacecraft roll angle at the scene center. The roll value is given in the Yaw Steering Frame (YSF) reference, whose x-axis is aligned with the instantaneous ground track velocity vector. Rolls about this x-axis go by the right-hand rule: a positive roll results in the instruments pointing to the left of the ground track, while a negative roll results in the instrument pointing to the right.  
SCENE_CENTER_TIME | STRING | Time of the observations as in ISO 8601 string.  
SENSOR_ID | STRING | Name of the sensor.  
SPACECRAFT_ID | STRING | Name of the spacecraft.  
SUN_AZIMUTH | DOUBLE | Sun azimuth angle in degrees for the image center location at the image center acquisition time. A positive value indicates angles to the east or clockwise from the north. A negative value indicates angles to the west or counterclockwise from the north.  
SUN_ELEVATION | DOUBLE | Sun elevation angle in degrees for the image center location at the image center acquisition time. A positive value indicates a daytime scene. A negative value indicates a nighttime scene. Note: For reflectance calculation, the sun zenith angle is needed, which is 90 - sun elevation angle.  
TARGET_WRS_PATH | INT | Nearest WRS-2 path to the Line-ofSight (LOS) scene center of the image.  
TARGET_WRS_ROW | INT | Nearest WRS-2 row to the LOS scene center of the image. Rows 880-889 are reserved for the north pole and 990-999 are reserved for the south pole, where WRS-2 is not defined.  
TEMPERATURE_MAXIMUM_BAND_ST_B10 | DOUBLE | Maximum achievable temperature value for Band 10.  
TEMPERATURE_MINIMUM_BAND_ST_B10 | DOUBLE | Minimum achievable temperature value for Band 10.  
TIRS_SSM_MODEL | STRING | Indicates how the Landsat 8 TIRS Scene Select Mirror (SSM) position was determined.
  * "FINAL" indicates final estimated encoder values generated after the switch event.
  * "ACTUAL" indicates actual encoder values.

  
TIRS_SSM_POSITION_STATUS | STRING | 
  * "NOMINAL" indicates the SSM was functioning normally for this scene.
  * "SWITCHED" indicates the SSM switched operating modes in the scene and may have TIRS image quality issues, which directly impact the IMAGE_QUALITY_TIRS value.
  * "ESTIMATED" indicates the SSM position was estimated, which may not be as accurate as the "NOMINAL" status.

  
TRUNCATION_OLI | STRING | 
  * "LOWER" indicates that the lower 12 bits were used.
  * "UPPER" indicates the upper 12 bits were used.

The normal truncation mode is "UPPER".  
WRS_PATH | INT | WRS path number of scene.  
WRS_ROW | INT | WRS row number of scene.  
**Terms of Use**
Landsat datasets are federally created data and therefore reside in the public domain and may be used, transferred, or reproduced without copyright restriction.
Acknowledgement or credit of the USGS as data source should be provided by including a line of text citation such as the example shown below.
(Product, Image, Photograph, or Dataset Name) courtesy of the U.S. Geological Survey
Example: Landsat-7 image courtesy of the U.S. Geological Survey
See the [USGS Visual Identity System Guidance](https://www.usgs.gov/information-policies-and-instructions/usgs-visual-identity-system) for further details on proper citation and acknowledgement of USGS products.
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2#colab-python-sample) More
```
vardataset=ee.ImageCollection('LANDSAT/LC09/C02/T1_L2')
.filterDate('2022-01-01','2022-02-01');
// Applies scaling factors.
functionapplyScaleFactors(image){
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBands=image.select('ST_B.*').multiply(0.00341802).add(149.0);
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBands,null,true);
}
dataset=dataset.map(applyScaleFactors);
varvisualization={
bands:['SR_B4','SR_B3','SR_B2'],
min:0.0,
max:0.3,
};
Map.setCenter(-114.2579,38.9275,8);
Map.addLayer(dataset,visualization,'True Color (432)');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
dataset = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2').filterDate(
  '2022-01-01', '2022-02-01'
)

# Applies scaling factors.
defapply_scale_factors(image):
 optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
 thermal_bands = image.select('ST_B.*').multiply(0.00341802).add(149.0)
 return image.addBands(optical_bands, None, True).addBands(
   thermal_bands, None, True
 )

dataset = dataset.map(apply_scale_factors)
visualization = {
  'bands': ['SR_B4', 'SR_B3', 'SR_B2'],
  'min': 0.0,
  'max': 0.3,
}
m = geemap.Map()
m.set_center(-114.2579, 38.9275, 8)
m.add_layer(dataset, visualization, 'True Color (432)')
m
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/LANDSAT/LANDSAT_LC09_C02_T1_L2)
[ USGS Landsat 9 Level 2, Collection 2, Tier 1 ](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2)
This dataset contains atmospherically corrected surface reflectance and land surface temperature derived from the data produced by the Landsat 9 OLI/TIRS sensors. These images contain 5 visible and near-infrared (VNIR) bands and 2 short-wave infrared (SWIR) bands processed to orthorectified surface reflectance, and one thermal infrared (TIR) band processed to …
LANDSAT/LC09/C02/T1_L2, cfmask,cloud,fmask,global,l9sr,landsat,lasrc,lc09,lst,reflectance,satellite-imagery,sr,usgs 
2021-10-31T00:00:00Z/2025-04-20T23:46:18.608000Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2)


