 
#  CCNL: Consistent and Corrected Nighttime Light Dataset from DMSP-OLS (1992-2013) v1 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![BNU/FGS/CCNL/v1](https://developers.google.com/earth-engine/datasets/images/BNU/BNU_FGS_CCNL_v1_sample.png) 

Dataset Availability
    1992-01-01T00:00:00Z–2014-01-01T00:00:00Z 

Dataset Provider
     [ Beijing Normal University ](https://doi.org/10.5281/zenodo.6644980) 

Earth Engine Snippet
     `    ee.ImageCollection("BNU/FGS/CCNL/v1")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/BNU/BNU_FGS_CCNL_v1) 

Cadence
    1 Year 

Tags
     [dmsp](https://developers.google.com/earth-engine/datasets/tags/dmsp) [eog](https://developers.google.com/earth-engine/datasets/tags/eog) [imagery](https://developers.google.com/earth-engine/datasets/tags/imagery) [lights](https://developers.google.com/earth-engine/datasets/tags/lights) [nighttime](https://developers.google.com/earth-engine/datasets/tags/nighttime) [ols](https://developers.google.com/earth-engine/datasets/tags/ols) [population](https://developers.google.com/earth-engine/datasets/tags/population) [visible](https://developers.google.com/earth-engine/datasets/tags/visible) [yearly](https://developers.google.com/earth-engine/datasets/tags/yearly)
bnu
[Description](https://developers.google.com/earth-engine/datasets/catalog/BNU_FGS_CCNL_v1#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/BNU_FGS_CCNL_v1#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/BNU_FGS_CCNL_v1#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/BNU_FGS_CCNL_v1#citations) More
The Consistent and Corrected Nighttime Lights (CCNL) dataset is a reprocessed version of the [Defense Meteorological Program (DMSP) Operational Line-Scan System (OLS) Version 4](https://developers.google.com/earth-engine/datasets/catalog/NOAA_DMSP-OLS_NIGHTTIME_LIGHTS). A series of methods was used to mitigate the impact of inter-annual inconsistency, saturation, and blooming effects and to improve data quality.
CCNL Version 1 spans the globe from 75N to 65S and has 1 km pixel size.
**Pixel Size** 1000 meters 
**Bands**
Name | Description  
---|---  
`b1` | Corrected nighttime light intensity.  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Zhao,Chenchen, Cao,Xin, Chen,Xuehong, & Cui,Xihong. (2020). A Consistent and Corrected Nighttime Light dataset (CCNL 1992-2013) from DMSP-OLS data (Version 1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6644980


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/BNU_FGS_CCNL_v1#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('BNU/FGS/CCNL/v1')
.filter(ee.Filter.date('2010-01-01','2010-12-31'));
varnighttimeLights=dataset.select('b1');
varnighttimeLightsVis={
min:3.0,
max:60.0,
};
Map.setCenter(31.4,30,6);
Map.addLayer(nighttimeLights,nighttimeLightsVis,'Nighttime Lights');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/BNU/BNU_FGS_CCNL_v1)
[ CCNL: Consistent and Corrected Nighttime Light Dataset from DMSP-OLS (1992-2013) v1 ](https://developers.google.com/earth-engine/datasets/catalog/BNU_FGS_CCNL_v1)
The Consistent and Corrected Nighttime Lights (CCNL) dataset is a reprocessed version of the Defense Meteorological Program (DMSP) Operational Line-Scan System (OLS) Version 4. A series of methods was used to mitigate the impact of inter-annual inconsistency, saturation, and blooming effects and to improve data quality. CCNL Version 1 spans …
BNU/FGS/CCNL/v1, dmsp,eog,imagery,lights,nighttime,ols,population,visible,yearly 
1992-01-01T00:00:00Z/2014-01-01T00:00:00Z
-65 -180 75 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://doi.org/10.5281/zenodo.6644980)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/BNU_FGS_CCNL_v1)


