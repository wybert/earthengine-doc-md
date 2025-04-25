 
#  MOD09Q1.061 Terra Surface Reflectance 8-Day Global 250m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MOD09Q1](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MOD09Q1_sample.png) 

Dataset Availability
    2000-02-18T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MOD09Q1.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MOD09Q1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD09Q1) 

Cadence
    8 Days 

Tags
     [8-day](https://developers.google.com/earth-engine/datasets/tags/8-day) [global](https://developers.google.com/earth-engine/datasets/tags/global) [mod09q1](https://developers.google.com/earth-engine/datasets/tags/mod09q1) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [surface-reflectance](https://developers.google.com/earth-engine/datasets/tags/surface-reflectance) [terra](https://developers.google.com/earth-engine/datasets/tags/terra) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1#dois) More
The MOD09Q1 product provides an estimate of the surface spectral reflectance of bands 1 and 2 at 250m resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the two reflectance bands, a quality layer is also included. For each pixel, a value is selected from all the acquisitions within the 8-day composite on the basis of high observation coverage, low view angle, the absence of clouds or cloud shadow, and aerosol loading.
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/306/MOD09_User_Guide_V6.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD09Q1)


**Pixel Size** 250 meters 
**Bands**
Name | Min | Max | Scale | Wavelength | Description  
---|---|---|---|---|---  
`sur_refl_b01` |  -100  |  16000  | 0.0001 | 620-670nm | Surface reflectance band 1  
`sur_refl_b02` |  -100  |  16000  | 0.0001 | 841-876nm | Surface reflectance for band 2  
`State` | Surface reflectance 250m state flags  
Bitmask for State
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

  
`QA` | Surface reflectance 250m band quality control flags  
Bitmask for QA
  * Bits 0-1: MODLAND QA bits 
    * 0: Corrected product produced at ideal quality - all bands
    * 1: Corrected product produced at less than ideal quality - some or all bands
    * 2: Corrected product not produced due to cloud effects - all bands
    * 3: Corrected product not produced for other reasons - some or all bands, may be fill value (11) [Note that a value of (11) overrides a value of (01)]
  * Bits 2-3: Spare (unused) 
    * 0: N/A
  * Bits 4-7: Band 1 data quality 
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
  * Bits 8-11: Band 2 data quality 
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
  * Bit 12: Atmospheric correction performed 
    * 0: No
    * 1: Yes
  * Bit 13: Adjacency correction performed 
    * 0: No
    * 1: Yes
  * Bit 14: Different orbit from 500m 
    * 0: No
    * 1: Yes
  * Bit 15: Spare (unused) 
    * 0: N/A

  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MOD09Q1.061 ](https://doi.org/10.5067/MODIS/MOD09Q1.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MOD09Q1')
.filter(ee.Filter.date('2018-01-01','2018-05-01'));
varfalseColorVis={
min:-100.0,
max:8000.0,
bands:['sur_refl_b02','sur_refl_b02','sur_refl_b01'],
};
Map.setCenter(6.746,46.529,2);
Map.addLayer(dataset,falseColorVis,'False Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MOD09Q1)
[ MOD09Q1.061 Terra Surface Reflectance 8-Day Global 250m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1)
The MOD09Q1 product provides an estimate of the surface spectral reflectance of bands 1 and 2 at 250m resolution and corrected for atmospheric conditions such as gasses, aerosols, and Rayleigh scattering. Along with the two reflectance bands, a quality layer is also included. For each pixel, a value is selected …
MODIS/061/MOD09Q1, 8-day,global,mod09q1,modis,nasa,satellite-imagery,sr,surface-reflectance,terra,usgs 
2000-02-18T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MOD09Q1.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MOD09Q1.061)
  * [ https://doi.org/10.5067/MODIS/MOD09Q1.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD09Q1)


