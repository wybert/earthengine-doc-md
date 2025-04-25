 
#  MYDOCGA.006 Aqua Ocean Reflectance Daily Global 1km 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/006/MYDOCGA](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_006_MYDOCGA_sample.png) 

Dataset Availability
    2002-07-04T00:00:00Z–2023-02-25T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MYDOCGA.006) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/006/MYDOCGA")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_006_MYDOCGA) 

Cadence
    1 Day 

Tags
     [aqua](https://developers.google.com/earth-engine/datasets/tags/aqua) [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [global](https://developers.google.com/earth-engine/datasets/tags/global) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [ocean](https://developers.google.com/earth-engine/datasets/tags/ocean) [reflectance](https://developers.google.com/earth-engine/datasets/tags/reflectance) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
mydocga
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA#dois) More
The MYDOCGA V6 ocean reflectance product consists of 1 kilometer reflectance data from Aqua MODIS bands 8-16. The product is referred to as ocean reflectance, because bands 8-16 are used primarily to produce ocean products, but this is not an ocean product as the tiles produced are land tiles.
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/306/MOD09_User_Guide_V6.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/305/MOD09_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MYDOCGA)


**Pixel Size** 1000 meters 
**Bands**
Name | Min | Max | Scale | Wavelength | Description  
---|---|---|---|---|---  
`num_observations` |  0  |  127  | Number of observations per pixel  
`sur_refl_b08` |  -100  |  16000  | 0.0001 | 405-420nm | MODIS band 8 surface reflectance  
`sur_refl_b09` |  -100  |  16000  | 0.0001 | 438-448nm | MODIS band 9 surface reflectance  
`sur_refl_b10` |  -100  |  16000  | 0.0001 | 483-493nm | MODIS band 10 surface reflectance  
`sur_refl_b11` |  -100  |  16000  | 0.0001 | 526-536nm | MODIS band 11 surface reflectance  
`sur_refl_b12` |  -100  |  16000  | 0.0001 | 546-556nm | MODIS band 12 surface reflectance  
`sur_refl_b13` |  -100  |  16000  | 0.0001 | 662-672nm | MODIS band 13 surface reflectance  
`sur_refl_b14` |  -100  |  16000  | 0.0001 | 673-683nm | MODIS band 14 surface reflectance  
`sur_refl_b15` |  -100  |  16000  | 0.0001 | 743-753nm | MODIS band 15 surface reflectance  
`sur_refl_b16` |  -100  |  16000  | 0.0001 | 862-877nm | MODIS band 16 surface reflectance  
`QC_b8_15_1km` | Band quality for MODIS bands 8-15  
Bitmask for QC_b8_15_1km
  * Bits 0-3: Band 8 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 4-7: Band 9 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 8-11: Band 10 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 12-15: Band 11 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 16-19: Band 12 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 20-23: Band 13 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 24-27: Band 14 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds
  * Bits 28-31: Band 15 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds

  
`QC_b16_15_1km` | Band quality for MODIS band 16  
Bitmask for QC_b16_15_1km
  * Bits 0-3: Unused 
    * 0: N/A
  * Bits 4-7: Band 16 data quality 
    * 0: Highest quality
    * 7: Noisy detector
    * 8: Dead detector; data interpolated in L1B
    * 9: Solar zenith >= 86 degrees
    * 10: Solar zenith >= 85 and < 86 degrees
    * 11: Missing input
    * 12: Internal constant used in place of climatological data for at least one atmospheric constant
    * 13: Correction out of bounds pixel constrained to extreme allowable value
    * 14: L1B data faulty
    * 15: Not processed due to deep ocean or clouds

  
`orbit_pnt` |  0  |  15  | Pointer to the orbit of each observation  
`granule_pnt` |  0  |  254  | Pointer to the granule of each observation  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MYDOCGA.006 ](https://doi.org/10.5067/MODIS/MYDOCGA.006)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/006/MYDOCGA')
.filter(ee.Filter.date('2018-01-01','2018-05-01'));
varfalseColor=
dataset.select(['sur_refl_b11','sur_refl_b10','sur_refl_b09']);
varfalseColorVis={
min:0.0,
max:2000.0,
};
Map.setCenter(6.746,46.529,2);
Map.addLayer(falseColor,falseColorVis,'False Color');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_006_MYDOCGA)
[ MYDOCGA.006 Aqua Ocean Reflectance Daily Global 1km ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA)
The MYDOCGA V6 ocean reflectance product consists of 1 kilometer reflectance data from Aqua MODIS bands 8-16. The product is referred to as ocean reflectance, because bands 8-16 are used primarily to produce ocean products, but this is not an ocean product as the tiles produced are land tiles. Documentation: …
MODIS/006/MYDOCGA, aqua,daily,global,modis,nasa,ocean,reflectance,satellite-imagery,sr,usgs 
2002-07-04T00:00:00Z/2023-02-25T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MYDOCGA.006 ](https://doi.org/https://doi.org/10.5067/MODIS/MYDOCGA.006)
  * [ https://doi.org/10.5067/MODIS/MYDOCGA.006 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MYDOCGA)


