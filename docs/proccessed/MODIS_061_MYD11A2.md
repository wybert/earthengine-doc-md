 
#  MYD11A2.061 Aqua Land Surface Temperature and Emissivity 8-Day Global 1km 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MYD11A2](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MYD11A2_sample.png) 

Dataset Availability
    2002-07-04T00:00:00Z–2025-04-07T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MYD11A2.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MYD11A2")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD11A2) 

Cadence
    8 Days 

Tags
     [8-day](https://developers.google.com/earth-engine/datasets/tags/8-day) [aqua](https://developers.google.com/earth-engine/datasets/tags/aqua) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [emissivity](https://developers.google.com/earth-engine/datasets/tags/emissivity) [global](https://developers.google.com/earth-engine/datasets/tags/global) [lst](https://developers.google.com/earth-engine/datasets/tags/lst) [modis](https://developers.google.com/earth-engine/datasets/tags/modis) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [surface-temperature](https://developers.google.com/earth-engine/datasets/tags/surface-temperature) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
myd11a2
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2#dois) More
The MYD11A2 V6.1 product provides an average 8-day land surface temperature (LST) in a 1200 x 1200 kilometer grid. Each pixel value in MYD11A2 is a simple average of all the corresponding MYD11A1 LST pixels collected within that 8 day period. The MYD11A2 does a simple averaging of all daily LST values, without any filtering for specific QA bits. Each of the MYD11A2 QA values are set based on what majority of input daily QA values are for any given pixel.
The 8 day compositing period was chosen because twice that period is the exact ground track repeat period of the Terra and Aqua platforms. In this product, along with both the day- and night-time surface temperature bands and their quality indicator (QC) layers, are also MODIS bands 31 and 32 and eight observation layers.
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/118/MOD11_User_Guide_V6.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/119/MOD11_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD11A2)


**Pixel Size** 1000 meters 
**Bands**
Name | Units | Min | Max | Scale | Offset | Description  
---|---|---|---|---|---|---  
`LST_Day_1km` | K |  7500  |  65535  | 0.02 | Day land surface temperature  
`QC_Day` | Daytime LST quality indicators  
Bitmask for QC_Day
  * Bits 0-1: Mandatory QA flags 
    * 0: Pixel produced, good quality, not necessary to examine more detailed QA
    * 1: Pixel produced, unreliable or unquantifiable quality, recommend examination of more detailed QA
    * 2: Pixel not produced due to cloud effects
    * 3: Pixel not produced primarily due to reasons other than cloud (such as ocean pixel, poor input data)
  * Bits 2-3: Data quality flag 
    * 0: Good data quality
    * 1: Other quality data
    * 2: TBD
    * 3: TBD
  * Bits 4-5: Emissivity error flag 
    * 0: Average emissivity error <= 0.01
    * 1: Average emissivity error <= 0.02
    * 2: Average emissivity error <= 0.04
    * 3: Average emissivity error > 0.04
  * Bits 6-7: LST error flag 
    * 0: Average LST error <= 1K
    * 1: Average LST error <= 2K
    * 2: Average LST error <= 3K
    * 3: Average LST error > 3K

  
`Day_view_time` | h |  0  |  240  | 0.1 | Local time of day observation  
`Day_view_angl` | deg |  0  |  130  | -65 | View zenith angle of day observation  
`LST_Night_1km` | K |  7500  |  65635  | 0.02 | Night land surface temperature  
`QC_Night` | Nighttime LST quality indicators  
Bitmask for QC_Night
  * Bits 0-1: Mandatory QA flags 
    * 0: Pixel produced, good quality, not necessary to examine more detailed QA
    * 1: Pixel produced, unreliable or unquantifiable quality, recommend examination of more detailed QA
    * 2: Pixel not produced due to cloud effects
    * 3: Pixel not produced primarily due to reasons other than cloud (such as ocean pixel, poor input data)
  * Bits 2-3: Data quality flag 
    * 0: Good data quality
    * 1: Other quality data
    * 2: TBD
    * 3: TBD
  * Bits 4-5: Emissivity error flag 
    * 0: Average emissivity error <= 0.01
    * 1: Average emissivity error <= 0.02
    * 2: Average emissivity error <= 0.04
    * 3: Average emissivity error > 0.04
  * Bits 6-7: LST error flag 
    * 0: Average LST error <= 1K
    * 1: Average LST error <= 2K
    * 2: Average LST error <= 3K
    * 3: Average LST error > 3K

  
`Night_view_time` | h |  0  |  240  | 0.1 | Local time of night observation  
`Night_view_angl` | deg |  0  |  130  | -65 | View zenith angle of night observation  
`Emis_31` |  1  |  255  | 0.002 | 0.49 | Band 31 emissivity  
`Emis_32` |  1  |  255  | 0.002 | 0.49 | Band 32 emissivity  
`Clear_sky_days` | Days in clear-sky conditions  
Bitmask for Clear_sky_days
  * Bit 0: Day 1 clear sky flag 
    * 0: Day 1 is not clear-sky
    * 1: Day 1 is clear-sky
  * Bit 1: Day 2 clear sky flag 
    * 0: Day 2 is not clear-sky
    * 1: Day 2 is clear-sky
  * Bit 2: Day 3 clear sky flag 
    * 0: Day 3 is not clear-sky
    * 1: Day 3 is clear-sky
  * Bit 3: Day 4 clear sky flag 
    * 0: Day 4 is not clear-sky
    * 1: Day 4 is clear-sky
  * Bit 4: Day 5 clear sky flag 
    * 0: Day 5 is not clear-sky
    * 1: Day 5 is clear-sky
  * Bit 5: Day 6 clear sky flag 
    * 0: Day 6 is not clear-sky
    * 1: Day 6 is clear-sky
  * Bit 6: Day 7 clear sky flag 
    * 0: Day 7 is not clear-sky
    * 1: Day 7 is clear-sky
  * Bit 7: Day 8 clear sky flag 
    * 0: Day 8 is not clear-sky
    * 1: Day 8 is clear-sky

  
`Clear_sky_nights` | Nights in clear-sky conditions  
Bitmask for Clear_sky_nights
  * Bit 0: Night 1 clear sky flag 
    * 0: Night 1 is not clear-sky
    * 1: Night 1 is clear-sky
  * Bit 1: Night 2 clear sky flag 
    * 0: Night 2 is not clear-sky
    * 1: Night 2 is clear-sky
  * Bit 2: Night 3 clear sky flag 
    * 0: Night 3 is not clear-sky
    * 1: Night 3 is clear-sky
  * Bit 3: Night 4 clear sky flag 
    * 0: Night 4 is not clear-sky
    * 1: Night 4 is clear-sky
  * Bit 4: Night 5 clear sky flag 
    * 0: Night 5 is not clear-sky
    * 1: Night 5 is clear-sky
  * Bit 5: Night 6 clear sky flag 
    * 0: Night 6 is not clear-sky
    * 1: Night 6 is clear-sky
  * Bit 6: Night 7 clear sky flag 
    * 0: Night 7 is not clear-sky
    * 1: Night 7 is clear-sky
  * Bit 7: Night 8 clear sky flag 
    * 0: Night 8 is not clear-sky
    * 1: Night 8 is clear-sky

  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MYD11A2.061 ](https://doi.org/10.5067/MODIS/MYD11A2.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MYD11A2')
.filter(ee.Filter.date('2018-01-01','2018-05-01'));
varlandSurfaceTemperature=dataset.select('LST_Day_1km');
varlandSurfaceTemperatureVis={
min:14000.0,
max:16000.0,
palette:[
'040274','040281','0502a3','0502b8','0502ce','0502e6',
'0602ff','235cb1','307ef3','269db1','30c8e2','32d3ef',
'3be285','3ff38f','86e26f','3ae237','b5e22e','d6e21f',
'fff705','ffd611','ffb613','ff8b13','ff6e08','ff500d',
'ff0000','de0101','c21301','a71001','911003'
],
};
Map.setCenter(6.746,46.529,2);
Map.addLayer(
landSurfaceTemperature,landSurfaceTemperatureVis,
'Land Surface Temperature');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD11A2)
[ MYD11A2.061 Aqua Land Surface Temperature and Emissivity 8-Day Global 1km ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2)
The MYD11A2 V6.1 product provides an average 8-day land surface temperature (LST) in a 1200 x 1200 kilometer grid. Each pixel value in MYD11A2 is a simple average of all the corresponding MYD11A1 LST pixels collected within that 8 day period. The MYD11A2 does a simple averaging of all daily …
MODIS/061/MYD11A2, 8-day,aqua,climate,emissivity,global,lst,modis,nasa,surface-temperature,usgs 
2002-07-04T00:00:00Z/2025-04-07T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MYD11A2.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MYD11A2.061)
  * [ https://doi.org/10.5067/MODIS/MYD11A2.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD11A2)


