 
#  MYD21C3.061 Aqua Land Surface Temperature and 3-Band Emissivity Monthly L3 Global 0.05 Deg CMG 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![MODIS/061/MYD21C3](https://developers.google.com/earth-engine/datasets/images/MODIS/MODIS_061_MYD21C3_sample.png) 

Dataset Availability
    2000-02-24T00:00:00Z–2025-03-01T00:00:00Z 

Dataset Provider
     [ NASA LP DAAC at the USGS EROS Center ](https://doi.org/10.5067/MODIS/MYD21C3.061) 

Earth Engine Snippet
     `    ee.ImageCollection("MODIS/061/MYD21C3")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD21C3) 

Cadence
    1 Month 

Tags
     [aqua](https://developers.google.com/earth-engine/datasets/tags/aqua) [climate](https://developers.google.com/earth-engine/datasets/tags/climate) [emissivity](https://developers.google.com/earth-engine/datasets/tags/emissivity) [global](https://developers.google.com/earth-engine/datasets/tags/global) [lst](https://developers.google.com/earth-engine/datasets/tags/lst) [monthly](https://developers.google.com/earth-engine/datasets/tags/monthly) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [surface-temperature](https://developers.google.com/earth-engine/datasets/tags/surface-temperature) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3#dois) More
The MYD21C3 dataset is a monthly composite LST product that uses an algorithm based on a simple averaging method. The algorithm calculates the average from all the cloud free MYD21A1D and MYD21A1N daily acquisitions from the 8-day period. Unlike the MYD21A1 data sets where the daytime and nighttime acquisitions are separate products, the MYD21A2 contains both daytime and nighttime acquisitions. The LST, Quality Control (QC), view zenith angle, and viewing time have separate day and night bands, while the values for the MODIS emissivity bands 29, 31, and 32 are the average of both the nighttime and daytime acquisitions.
Documentation:
  * [User's Guide](https://lpdaac.usgs.gov/documents/1398/MOD21_User_Guide_V61.pdf)
  * [Algorithm Theoretical Basis Document (ATBD)](https://lpdaac.usgs.gov/documents/1399/MOD21_ATBD.pdf)
  * [General Documentation](https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MYD21C3)


**Pixel Size** 1000 meters 
**Bands**
Name | Units | Min | Max | Scale | Offset | Description  
---|---|---|---|---|---|---  
`Count_Day` |  1  |  65535  | Count of Daytime Input Values  
`Count_Night` |  1  |  65535  | Count of Nighttime Input Values  
`QC_Day` | Quality Control for Daytime LST and Emissivity  
Bitmask for QC_Day
  * Bits 0-1: Mandatory QA flags 
    * 0: Pixel produced, good quality, no further QA info necessary
    * 1: Pixel produced, nominal quality. Recommend more detailed analysis of other QC information
    * 2: Pixel not produced due to cloud
    * 3: Pixel not produced due to reasons other than cloud
  * Bits 2-3: Data quality flag 
    * 0: Good data quality of L1B bands 29, 31, 32
    * 1: Missing pixel
    * 2: Fairly calibrated
    * 3: Poorly calibrated, TES processing skipped
  * Bits 4-5: Emissivity accuracy 
    * 0: 
> 0.02 (Poor performance) 
    * 1: 0.015 - 0.02 (Marginal performance)
    * 2: 0.01 - 0.015 (Good performance)
    * 3: <0.01 (Excellent performance)
  * Bits 6-7: LST accuracy 
    * 0: 
> 2K (Poor performance) 
    * 1: 1.5 - 2K (Marginal performance)
    * 2: 1 - 1.5K (Good performance)
    * 3: <1K (Excellent performance)

  
`QC_Night` | Quality Control for Nighttime LST and Emissivity  
Bitmask for QC_Night
  * Bits 0-1: Mandatory QA flags 
    * 0: Pixel produced, good quality, no further QA info necessary
    * 1: Pixel produced, nominal quality. Recommend more detailed analysis of other QC information
    * 2: Pixel not produced due to cloud
    * 3: Pixel not produced due to reasons other than cloud
  * Bits 2-3: Data quality flag 
    * 0: Good data quality of L1B bands 29, 31, 32
    * 1: Missing pixel
    * 2: Fairly calibrated
    * 3: Poorly calibrated, TES processing skipped
  * Bits 4-5: Emissivity accuracy 
    * 0: 
> 0.02 (Poor performance) 
    * 1: 0.015 - 0.02 (Marginal performance)
    * 2: 0.01 - 0.015 (Good performance)
    * 3: <0.01 (Excellent performance)
  * Bits 6-7: LST accuracy 
    * 0: 
> 2K (Poor performance) 
    * 1: 1.5 - 2K (Marginal performance)
    * 2: 1 - 1.5K (Good performance)
    * 3: <1K (Excellent performance)

  
`LST_Day` | K |  7500  |  65535  | 0.02 | Average Daytime Land Surface Temperature  
`LST_Night` | K |  7500  |  65535  | 0.02 | Average Nighttime Land Surface Temperature  
`LST_Day_err` | K |  1  |  255  | 0.04 | Root-mean-square-error Daytime Land Surface Temperature  
`LST_Night_err` | K |  1  |  255  | 0.04 | Average Nighttime Land Surface Temperature  
`Day_view_angle` | deg |  0  |  130  | -65 | Average Daytime View Zenith Angle  
`Night_view_angle` | deg |  0  |  130  | -65 | Average Nighttime View Zenith Angle  
`Day_view_time` | h |  0  |  120  | 0.2 | Average Daytime View Time (UTC)  
`Night_view_time` | h |  0  |  120  | 0.2 | Average Nighttime View Time (UTC)  
`Emis_29_Day` |  1  |  255  | 0.002 | 0.49 | Average Daytime Band 29 Emissivity  
`Emis_29_Night` |  1  |  255  | 0.002 | 0.49 | Average Nighttime Band 29 Emissivity  
`Emis_29_Day_err` |  1  |  65535  | 0.0001 | Root-mean-square-error Daytime Band 29 Emissivity  
`Emis_29_Night_err` |  1  |  65535  | 0.0001 | Root-mean-square-error Nighttime Band 29 Emissivity  
`Emis_31_Day` |  1  |  255  | 0.002 | 0.49 | Average Daytime Band 31 Emissivity  
`Emis_31_Night` |  1  |  255  | 0.002 | 0.49 | Average Nighttime Band 31 Emissivity  
`Emis_31_Day_err` |  1  |  65535  | 0.0001 | Root-mean-square-error Daytime Band 31 Emissivity  
`Emis_31_Night_err` |  1  |  65535  | 0.0001 | Root-mean-square-error Nighttime Band 31 Emissivity  
`Emis_32_Day` |  1  |  255  | 0.002 | 0.49 | Average Daytime Band 32 Emissivity  
`Emis_32_Night` |  1  |  255  | 0.002 | 0.49 | Average Nighttime Band 32 Emissivity  
`Emis_32_Day_err` |  1  |  65535  | 0.0001 | Root-mean-square-error Daytime Band 32 Emissivity  
`Emis_32_Night_err` |  1  |  65535  | 0.0001 | Root-mean-square-error Nighttime Band 32 Emissivity  
`View_Angle` | deg | -65 | MODIS view zenith angle  
`Percent_land_in_grid` | % |  1  |  100  | Percent of Land Detections in Grid Cell  
`Clear_sky_days` |  0  |  2.14748e+09  | Bitmap of Clear Sky Days (1 = clear, LSB = 1st day)  
`Clear_sky_nights` |  0  |  2.14748e+09  | Bitmap of Clear Sky Nights (1 = clear, LSB = 1st day)  
**Terms of Use**
MODIS data and products acquired through the LP DAAC have no restrictions on subsequent use, sale, or redistribution.
Citations:
  * Please visit [LP DAAC 'Citing Our Data' page](https://lpdaac.usgs.gov/citing_our_data) for information on citing LP DAAC datasets.


  * [ https://doi.org/10.5067/MODIS/MYD21C3.061 ](https://doi.org/10.5067/MODIS/MYD21C3.061)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('MODIS/061/MYD21C3')
.filter(ee.Filter.date('2018-01-01','2018-05-01'));
varlandSurfaceTemperature=dataset.select('LST_Day');
varlandSurfaceTemperatureVis={
min:216.0,
max:348.0,
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
'Average Daytime Land Surface Temperature');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/MODIS/MODIS_061_MYD21C3)
[ MYD21C3.061 Aqua Land Surface Temperature and 3-Band Emissivity Monthly L3 Global 0.05 Deg CMG ](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3)
The MYD21C3 dataset is a monthly composite LST product that uses an algorithm based on a simple averaging method. The algorithm calculates the average from all the cloud free MYD21A1D and MYD21A1N daily acquisitions from the 8-day period. Unlike the MYD21A1 data sets where the daytime and nighttime acquisitions are …
MODIS/061/MYD21C3, aqua,climate,emissivity,global,lst,monthly,nasa,surface-temperature,usgs 
2000-02-24T00:00:00Z/2025-03-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.5067/MODIS/MYD21C3.061 ](https://doi.org/https://doi.org/10.5067/MODIS/MYD21C3.061)
  * [ https://doi.org/10.5067/MODIS/MYD21C3.061 ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MYD21C3)


