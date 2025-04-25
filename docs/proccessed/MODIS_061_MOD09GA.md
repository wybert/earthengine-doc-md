 
#  MOD09GA.061 Terra Surface Reflectance Daily Global 1km and 500m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MOD09GA](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MOD09GA_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2025-04-19T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MOD09GA.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MOD09GA")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD09GA) 

Cadence
    1 Day 

Tags
     [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [global](https://developers.google.com/earth-engine/datasets/tags/global) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [surface-reflectance](https://developers.google.com/earth-engine/datasets/tags/surface-reflectance) [terra](https://developers.google.com/earth-engine/datasets/tags/terra) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
mod09ga
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA#dois) More
The MODIS Surface Reflectance products provide an estimate of the surface spectral reflectance as it would be measured at ground level in the absence of atmospheric scattering or absorption. Low-level data are corrected for atmospheric gases and aerosols. MOD09GA version 6.1 provides bands 1-7 in a daily gridded L2G product in the sinusoidal projection, including 500m reflectance values and 1km observation and geolocation statistics.
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/306/MOD09_User_Guide_V6.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09GA)


**Bands**
Name | Units | Min | Max | Scale | Pixel Size | Wavelength | Description  
---|---|---|---|---|---|---|---  
`num_observations_1km` |  2  |  127  |  1000 meters  | Number of observations per 1K pixel  
`state_1km` |  1000 meters  | Reflectance data state QA  
Bitmask for state_1km
  * Bits 0-1: Cloud state 
    * 0: Clear
    * 1: Cloudy
    * 2: Mixed
    * 3: Not set, assumed clear
  * Bit 2: Cloud shadow 
    * 0: No
    * 1: Yes
  * Bits 3-5: Land/water flag 
    * 0: Shallow ocean
    * 1: Land
    * 2: Ocean coastlines and lake shorelines
    * 3: Shallow inland water
    * 4: Ephemeral water
    * 5: Deep inland water
    * 6: Continental/moderate ocean
    * 7: Deep ocean
  * Bits 6-7: Aerosol quantity 
    * 0: Climatology
    * 1: Low
    * 2: Average
    * 3: High
  * Bits 8-9: Cirrus detected 
    * 0: None
    * 1: Small
    * 2: Average
    * 3: High
  * Bit 10: Internal cloud algorithm flag 
    * 0: No cloud
    * 1: Cloud
  * Bit 11: Internal fire algorithm flag 
    * 0: No fire
    * 1: Fire
  * Bit 12: MOD35 snow/ice flag 
    * 0: No
    * 1: Yes
  * Bit 13: Pixel is adjacent to cloud 
    * 0: No
    * 1: Yes
  * Bit 14: BRDF correction performed data 
    * 0: No
    * 1: Yes
  * Bit 15: Internal snow mask 
    * 0: No snow
    * 1: Snow

  
`SensorZenith` | deg |  0  |  18000  | 0.01 |  1000 meters  | Sensor zenith angle  
`SensorAzimuth` | deg |  -18000  |  18000  | 0.01 |  1000 meters  | Sensor azimuth angle  
`Range` | m |  27000  |  65535  | 25 |  1000 meters  | Distance to sensor  
`SolarZenith` | deg |  0  |  18000  | 0.01 |  1000 meters  | Solar zenith angle  
`SolarAzimuth` | deg |  -18000  |  18000  | 0.01 |  1000 meters  | Solar azimuth angle  
`gflags` |  1000 meters  | Geolocation flags  
Bitmask for gflags
  * Bits 0-2: Fill 
    * 0: Fill
  * Bit 3: Sensor range validity flag 
    * 0: Valid
    * 1: Invalid
  * Bit 4: Digital elevation model quality flag 
    * 0: Valid
    * 1: Missing/inferior
  * Bit 5: Terrain data validity 
    * 0: Valid
    * 1: Invalid
  * Bit 6: Ellipsoid intersection flag 
    * 0: Valid intersection
    * 1: No intersection
  * Bit 7: Input data flag 
    * 0: Valid
    * 1: Invalid

  
`orbit_pnt` |  0  |  15  |  1000 meters  | Orbit pointer  
`granule_pnt` |  0  |  254  |  1000 meters  | Granule pointer  
`num_observations_500m` |  0  |  127  |  500 meters  | Number of observations  
`sur_refl_b01` |  -100  |  16000  | 0.0001 |  500 meters  | 620-670nm | Surface reflectance for band 1  
`sur_refl_b02` |  -100  |  16000  | 0.0001 |  500 meters  | 841-876nm | Surface reflectance for band 2  
`sur_refl_b03` |  -100  |  16000  | 0.0001 |  500 meters  | 459-479nm | Surface reflectance for band 3  
`sur_refl_b04` |  -100  |  16000  | 0.0001 |  500 meters  | 545-565nm | Surface reflectance for band 4  
`sur_refl_b05` |  -100  |  16000  | 0.0001 |  500 meters  | 1230-1250nm | Surface reflectance for band 5  
`sur_refl_b06` |  -100  |  16000  | 0.0001 |  500 meters  | 1628-1652nm | Surface reflectance for band 6  
`sur_refl_b07` |  -100  |  16000  | 0.0001 |  500 meters  | 2105-2155nm | Surface reflectance for band 7  
`QC_500m` |  500 meters  | Surface reflectance quality assurance  
Bitmask for QC_500m
  * Bits 0-1: MODLAND QA bits 
    * 0: Corrected product produced at ideal quality - all bands
    * 1: Corrected product produced at less than ideal quality - some or all bands
    * 2: Corrected product not produced due to cloud effects - all bands
    * 3: Corrected product not produced for other reasons - some or all bands, may be fill value (11) [Note that a value of (11) overrides a value of (01)]
  * Bits 2-5: Band 1 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 6-9: Band 2 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 10-13: Band 3 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 14-17: Band 4 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 18-21: Band 5 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 22-25: Band 6 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 26-29: Band 7 data quality, four bit range 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector, data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds, pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bit 30: Atmospheric correction performed 
    * 0: No
    * 1: Yes
  * Bit 31: Adjacency correction performed 
    * 0: No
    * 1: Yes

  
`obscov_500m` |  0  |  100  |  500 meters  | Observation coverage percent  
`iobs_res` |  0  |  254  |  500 meters  | Observation number in coarser grid  
`q_scan` |  500 meters  | 250m scan value information  
Bitmask for q_scan
  * Bit 0: Scan of observation in quadrant 1 [-0.5 row, -0.5 column] 
    * 0: No
    * 1: Yes
  * Bit 1: Scan of observation in quadrant 2 [-0.5 row, +0.5 column] 
    * 0: No
    * 1: Yes
  * Bit 2: Scan of observation in quadrant 3 [+0.5 row, -0.5 column] 
    * 0: No
    * 1: Yes
  * Bit 3: Scan of observation in quadrant 4 [+0.5 row, +0.5 column] 
    * 0: No
    * 1: Yes
  * Bit 4: Missing observation in quadrant 1 [-0.5 row, -0.5 column] 
    * 0: Different
    * 1: Same
  * Bit 5: Missing observation in quadrant 2 [-0.5 row, +0.5 column] 
    * 0: Different
    * 1: Same
  * Bit 6: Missing observation in quadrant 3 [+0.5 row, -0.5 column] 
    * 0: Different
    * 1: Same
  * Bit 7: Missing observation in quadrant 4 [+0.5 row, +0.5 column] 
    * 0: Different
    * 1: Same

  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MOD09GA.061 ](https://doi.org/10.5067/MODIS/MOD09GA.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MOD09GA')
.filter(ee.Filter.date('2018-04-01','2018-06-01'));
vartrueColor143=
dataset.select(['sur_refl_b01','sur_refl_b04','sur_refl_b03']);
vartrueColor143Vis={
min:-100.0,
max:8000.0,
};
Map.setCenter(-7.03125,31.0529339857,2);
Map.addLayer(trueColor143,trueColor143Vis,'True Color (143)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD09GA)
[ MOD09GA.061 Terra Surface Reflectance Daily Global 1km and 500m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA)
The MODIS Surface Reflectance products provide an estimate of the surface spectral reflectance as it would be measured at ground level in the absence of atmospheric scattering or absorption. Low-level data are corrected for atmospheric gases and aerosols. MOD09GA version 6.1 provides bands 1-7 in a daily gridded L2G product …
MODIS/061/MOD09GA, daily,global,modis,nasa,satellite-imagery,sr,surface-reflectance,terra,usgs 
2000-02-24T00:00:00Z/2025-04-19T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MOD09GA.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MOD09GA.061)
  * [ https://doi.org/10.5067/MODIS/MOD09GA.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09GA)


