 
#  MOD09A1.061 Terra Surface Reflectance 8-Day Global 500m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MOD09A1](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MOD09A1_sample.png) 

Dataset Availability
    2000-02-18T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MOD09A1.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MOD09A1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD09A1) 

Cadence
    8 Days 

Tags
     [8-day](https://developers.google.com/earth-engine/datasets/tags/8-day) [global](https://developers.google.com/earth-engine/datasets/tags/global) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [surface-reflectance](https://developers.google.com/earth-engine/datasets/tags/surface-reflectance) [terra](https://developers.google.com/earth-engine/datasets/tags/terra) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
mod09a1
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1#dois) More
The MOD09A1 V6.1 product provides an estimate of the surface spectral reflectance of Terra MODIS bands 1-7 at 500m resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the seven reflectance bands is a quality layer and four observation bands. For each pixel, a value is selected from all the acquisitions within the 8-day composite on the basis of high observation coverage, low view angle, the absence of clouds or cloud shadow, and aerosol loading.
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/306/MOD09_User_Guide_V6.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09A1)


**Pixel Size** 500 meters 
**Bands**
Name | Units | Min | Max | Scale | Wavelength | Description  
---|---|---|---|---|---|---  
`sur_refl_b01` |  -100  |  16000  | 0.0001 | 620-670nm | Surface reflectance for band 1  
`sur_refl_b02` |  -100  |  16000  | 0.0001 | 841-876nm | Surface reflectance for band 2  
`sur_refl_b03` |  -100  |  16000  | 0.0001 | 459-479nm | Surface reflectance for band 3  
`sur_refl_b04` |  -100  |  16000  | 0.0001 | 545-565nm | Surface reflectance for band 4  
`sur_refl_b05` |  -100  |  16000  | 0.0001 | 1230-1250nm | Surface reflectance for band 5  
`sur_refl_b06` |  -100  |  16000  | 0.0001 | 1628-1652nm | Surface reflectance for band 6  
`sur_refl_b07` |  -100  |  16000  | 0.0001 | 2105-2155nm | Surface reflectance for band 7  
`QA` | Surface reflectance 500m band quality control flags  
Bitmask for QA
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

  
`SolarZenith` | deg |  0  |  18000  | 0.01 | MODIS Solar zenith angle  
`ViewZenith` | deg |  0  |  18000  | 0.01 | MODIS view zenith angle  
`RelativeAzimuth` | deg |  -18000  |  18000  | 0.01 | MODIS relative azimuth angle  
`StateQA` | Surface reflectance 500m state flags  
Bitmask for StateQA
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

  
`DayOfYear` |  1  |  366  | Julian day of the year for the pixel  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MOD09A1.061 ](https://doi.org/10.5067/MODIS/MOD09A1.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MOD09A1')
.filter(ee.Filter.date('2018-01-01','2018-05-01'));
vartrueColor=
dataset.select(['sur_refl_b01','sur_refl_b04','sur_refl_b03']);
vartrueColorVis={
min:-100.0,
max:3000.0,
};
Map.setCenter(6.746,46.529,6);
Map.addLayer(trueColor,trueColorVis,'True Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD09A1)
[ MOD09A1.061 Terra Surface Reflectance 8-Day Global 500m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1)
The MOD09A1 V6.1 product provides an estimate of the surface spectral reflectance of Terra MODIS bands 1-7 at 500m resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the seven reflectance bands is a quality layer and four observation bands. For each pixel, a …
MODIS/061/MOD09A1, 8-day,global,modis,nasa,satellite-imagery,sr,surface-reflectance,terra,usgs 
2000-02-18T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MOD09A1.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MOD09A1.061)
  * [ https://doi.org/10.5067/MODIS/MOD09A1.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09A1)


