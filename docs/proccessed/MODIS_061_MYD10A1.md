 
#  MYD10A1.061 Aqua Snow Cover Daily Global 500m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MYD10A1](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MYD10A1_sample.png) 

Dataset Availability
    2002-07-04T00:00:00Z–2025-04-18T00:00:00Z 

Dataset Provider
     [ NASA NSIDC DAAC at CIRES ](https://doi.org/10.5067/MODIS/MYD10A1.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MYD10A1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD10A1) 

Cadence
    1 Day 

Tags
     [albedo](https://developers.google.com/earth-engine/datasets/tags/albedo) [aqua](https://developers.google.com/earth-engine/datasets/tags/aqua) [cryosphere](https://developers.google.com/earth-engine/datasets/tags/cryosphere) [daily](https://developers.google.com/earth-engine/datasets/tags/daily) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [global](https://developers.google.com/earth-engine/datasets/tags/global) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [nsidc](https://developers.google.com/earth-engine/datasets/tags/nsidc) [snow](https://developers.google.com/earth-engine/datasets/tags/snow)
myd10a1
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1#dois) More
The MYD10A1 V6 Snow Cover Daily Global 500m product contains snow cover, snow albedo, fractional snow cover, and quality assessment (QA) data. Snow cover data are based on a snow mapping algorithm that employs a Normalized Difference Snow Index (NDSI) and other criteria tests.
[General documentation](https://doi.org/10.5067/MODIS/MYD10A1.061)
**Pixel Size** 500 meters 
**Bands**
Name | Min | Max | Scale | Description  
---|---|---|---|---  
`NDSI_Snow_Cover` |  0  |  100  | NDSI snow cover. This value is computed for MOD10_L2 and retrieved when the observation of the day is selected. Provider values above 100 are masked out in this band (they can be found in the "NDSI_Snow_Cover_Class" band).  
`NDSI_Snow_Cover_Basic_QA` | A basic estimate of the quality of the algorithm result. This value is computed for MOD10_L2 and retrieved with the corresponding observation of the day.  
Bitmask for NDSI_Snow_Cover_Basic_QA
  * Bits 0-15: QA 
    * 0: Best
    * 1: Good
    * 2: Ok
    * 3: Poor - not currently in use
    * 211: Night
    * 239: Ocean

  
`NDSI_Snow_Cover_Algorithm_Flags_QA` | Bit flags indicating screen results and the presence of inland water. These flags are set when MOD10_L2 is generated and retrieved with the corresponding observation of the day.  
Bitmask for NDSI_Snow_Cover_Algorithm_Flags_QA
  * Bit 0: Inland water 
    * 0: No
    * 1: Yes
  * Bit 1: Low visible screen failed. Snow detection reversed. 
    * 0: No fail/not reversed
    * 1: The MODIS band 2 reflectance is <= 0.10 or the band 4 reflectance is <= 0.11
  * Bit 2: Low NDSI screen failed. Snow detection reversed. 
    * 0: No fail/not reversed
    * 1: Pixels detected as having snow cover with 0.0 < NDSI < 0.10 are reversed to no snow
  * Bit 3: Combined temperature/height screen failed. 
    * 1: Brightness temperature >= 281K, pixel height < 1300m, flag set, snow detection reversed to not snow or brightness temperature >= 281K, pixel height >= 1300m, flag set, snow detection NOT reversed.
  * Bit 4: Shortwave IR (SWIR) reflectance anomalously high. 
    * 1: Snow pixel with SWIR > 0.45, flag set, snow detection reversed to not snow or snow pixel with 25% < SWIR <= 45%, flag set to indicate unusual snow condition, snow detection NOT reversed.
  * Bit 5: Spare 
    * 0: N/A
  * Bit 6: Spare 
    * 0: N/A
  * Bit 7: Solar zenith screen failed (angles exceed 70°), uncertainty increased. 
    * 0: No
    * 1: Yes

  
`NDSI` |  0  |  10000  | 0.0001 | Raw NDSI (i.e. prior to screening). This value is computed for MOD10_L2 and retrieved with the corresponding observation of the day.  
`Snow_Albedo_Daily_Tile` |  1  |  100  | Snow albedo percentage. Provider values above 100 are masked out in this band (they can be found in the "Snow_Albedo_Daily_Tile_Class" band).  
`orbit_pnt` | Pointer to the orbit number of the swath that was selected as the observation of the day. The pointer references by index the list of orbit numbers written to the ORBITNUMBERARRAY metadata object in ArchiveMetadata.0.  
`granule_pnt` | Pointer to the granule (swath) that was mapped into the tile. The pointer references the corresponding value in the GRANULEPOINTERARRAY metadata object written to ArchiveMetadata.0.  
`NDSI_Snow_Cover_Class` | Landcover classes from the "NDSI_Snow_Cover" subdataset (provider values less than or equal to 100 are masked out).  
`Snow_Albedo_Daily_Tile_Class` | Landcover classes from the "Snow_Albedo_Daily_Tile" subdataset (provider values less than or equal to 100 are masked out).  
**NDSI_Snow_Cover_Class Class Table**
Value | Color | Description  
---|---|---  
200 | Missing data  
201 | No decision  
211 | Night  
237 | Inland water  
239 | Ocean  
250 | Cloud  
254 | Detector saturated  
**Snow_Albedo_Daily_Tile_Class Class Table**
Value | Color | Description  
---|---|---  
101 | No decision  
111 | Night  
125 | Land  
137 | Inland water  
139 | Ocean  
150 | Cloud  
151 | Cloud detected as snow  
250 | Missing  
251 | Self-shadowing  
252 | Land mask mismatch  
253 | BRDF failure  
254 | Non-production mask  
**Terms of Use**
You may download and use photographs, imagery, or text from the NSIDC web site, unless limitations for its use are specifically stated. For more information on usage and citing NSIDC datasets, please visit the [NSIDC 'Use and Copyright' page](https://nsidc.org/about/data-use-and-copyright).
Citations:
  * Hall, D. K., V. V. Salomonson, and G. A. Riggs. 2016. MODIS/Terra Snow Cover Daily L3 Global 500m Grid. Version 6. Boulder, Colorado USA: NASA National Snow and Ice Data Center Distributed Active Archive Center.


  * [ https://doi.org/10.5067/MODIS/MYD10A1.061 ](https://doi.org/10.5067/MODIS/MYD10A1.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MYD10A1')
.filter(ee.Filter.date('2018-04-01','2018-05-01'));
varsnowCover=dataset.select('NDSI_Snow_Cover');
varsnowCoverVis={
min:0.0,
max:100.0,
palette:['black','0dffff','0524ff','ffffff'],
};
Map.setCenter(-38.13,40,2);
Map.addLayer(snowCover,snowCoverVis,'Snow Cover');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD10A1)
[ MYD10A1.061 Aqua Snow Cover Daily Global 500m ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1)
The MYD10A1 V6 Snow Cover Daily Global 500m product contains snow cover, snow albedo, fractional snow cover, and quality assessment (QA) data. Snow cover data are based on a snow mapping algorithm that employs a Normalized Difference Snow Index (NDSI) and other criteria tests. General documentation
MODIS/061/MYD10A1, albedo,aqua,cryosphere,daily,geophysical,global,modis,nasa,nsidc,snow 
2002-07-04T00:00:00Z/2025-04-18T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MYD10A1.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MYD10A1.061)
  * [ https://doi.org/10.5067/MODIS/MYD10A1.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD10A1)


