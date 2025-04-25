 
#  GPWv411: Data Context (Gridded Population of the World Version 4.11) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![CIESIN/GPWv411/GPW_Data_Context](https://developers.google.com/earth-engine/datasets/images/CIESIN/CIESIN_GPWv411_GPW_Data_Context_sample.png) 

Dataset Availability
    2000-01-01T00:00:00Z–2020-01-01T00:00:00Z 

Dataset Provider
     [ NASA SEDAC at the Center for International Earth Science Information Network ](https://doi.org/10.7927/H42Z13KG) 

Earth Engine Snippet
     `    ee.ImageCollection("CIESIN/GPWv411/GPW_Data_Context")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CIESIN/CIESIN_GPWv411_GPW_Data_Context) 

Tags
     [ciesin](https://developers.google.com/earth-engine/datasets/tags/ciesin) [gpw](https://developers.google.com/earth-engine/datasets/tags/gpw) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [population](https://developers.google.com/earth-engine/datasets/tags/population)
[Description](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context#dois) More
This dataset categorizes pixels with estimated zero population based on information provided in the census documents.
[General Documentation](https://sedac.ciesin.columbia.edu/data/set/gpw-v4-admin-unit-center-points-population-estimates-rev11/docs)
The Gridded Population of World Version 4 (GPWv4), Revision 11 models the distribution of global human population for the years 2000, 2005, 2010, 2015, and 2020 on 30 arc-second (approximately 1 km) grid cells. Population is distributed to cells using proportional allocation of population from census and administrative units. Population input data are collected at the most detailed spatial resolution available from the results of the 2010 round of censuses, which occurred between 2005 and 2014. The input data are extrapolated to produce population estimates for each modeled year.
**Pixel Size** 927.67 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`data_context` |  0*  |  207*  | Categorizes pixels with estimated zero population based on information provided in the census documents.  
* estimated min or max value 
**data_context Class Table**
Value | Color | Description  
---|---|---  
0 | #ffffff | Not Applicable  
201 | #099506 | Park or protected area  
202 | #f04923 | Military district, airport zone, or other infrastructure  
203 | #e62440 | Not enumerated or not reported in census  
204 | #706984 | No households  
205 | #a5a5a5 | Uninhabited  
206 | #d4cc11 | Population not gridded  
207 | #000000 | Missing age or sex data  
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Center for International Earth Science Information Network - CIESIN - Columbia University. 2018. Gridded Population of the World, Version 4 (GPWv4): Data Context, Revision 11. Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). [doi:10.7927/H42Z13KG](https://doi.org/10.7927/H42Z13KG). Accessed DAY MONTH YEAR.


  * [ https://doi.org/10.7927/H42Z13KG ](https://doi.org/10.7927/H42Z13KG)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('CIESIN/GPWv411/GPW_Data_Context');
varraster=dataset.select('data_context');
varraster_vis={
'min':200.0,
'palette':[
'ffffff',
'099506',
'f04923',
'e62440',
'706984',
'a5a5a5',
'ffe152',
'd4cc11',
'000000'
],
'max':207.0
};
Map.setCenter(-88.6,26.4,1);
Map.addLayer(raster,raster_vis,'data_context');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CIESIN/CIESIN_GPWv411_GPW_Data_Context)
[ GPWv411: Data Context (Gridded Population of the World Version 4.11) ](https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context)
This dataset categorizes pixels with estimated zero population based on information provided in the census documents. General Documentation The Gridded Population of World Version 4 (GPWv4), Revision 11 models the distribution of global human population for the years 2000, 2005, 2010, 2015, and 2020 on 30 arc-second (approximately 1 km) …
CIESIN/GPWv411/GPW_Data_Context, ciesin,gpw,nasa,population 
2000-01-01T00:00:00Z/2020-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.7927/H42Z13KG ](https://doi.org/https://doi.org/10.7927/H42Z13KG)
  * [ https://doi.org/10.7927/H42Z13KG ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CIESIN_GPWv411_GPW_Data_Context)


