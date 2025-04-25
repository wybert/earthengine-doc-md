 
#  Oxford MAP: Malaria Atlas Project Fractional International Geosphere-Biosphere Programme Landcover 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Oxford/MAP/IGBP_Fractional_Landcover_5km_Annual](https://developers.google.com/earth-engine/datasets/images/Oxford/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual_sample.png) 

Dataset Availability
    2001-01-01T00:00:00Z–2013-01-01T00:00:00Z 

Dataset Provider
     [ Oxford Malaria Atlas Project ](https://malariaatlas.org/) 

Earth Engine Snippet
     `    ee.ImageCollection("Oxford/MAP/IGBP_Fractional_Landcover_5km_Annual")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Oxford/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual) 

Cadence
    1 Year 

Tags
     [landcover](https://developers.google.com/earth-engine/datasets/tags/landcover) [landuse-landcover](https://developers.google.com/earth-engine/datasets/tags/landuse-landcover) [map](https://developers.google.com/earth-engine/datasets/tags/map) [oxford](https://developers.google.com/earth-engine/datasets/tags/oxford)
igbp
[Description](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual#citations) More
The underlying dataset for this landcover product is the IGBP layer found within the MODIS annual landcover product (MCD12Q1). This data was converted from its categorical format, which has a ≈500 meter resolution, to a fractional product indicating the integer percentage (0-100) of the output pixel covered by each of the 17 landcover classes (1 per band).
This dataset was produced by Harry Gibson and Daniel Weiss of the Malaria Atlas Project (Big Data Institute, University of Oxford, United Kingdom, <https://malariaatlas.org/>).
**Pixel Size** 5000 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`Overall_Class` |  0  |  17  | Dominant class of each resulting pixel  
`Water` | % |  0  |  100  | Percentage of water  
`Evergreen_Needleleaf_Forest` | % |  0  |  100  | Percentage of evergreen needleleaf forest  
`Evergreen_Broadleaf_Forest` | % |  0  |  100  | Percentage of evergreen broadleaf forest  
`Deciduous_Needleleaf_Forest` | % |  0  |  100  | Percentage of deciduous needleleaf forest  
`Deciduous_Broadleaf_Forest` | % |  0  |  100  | Percentage of deciduous broadleaf forest  
`Mixed_Forest` | % |  0  |  100  | Percentage of mixed forest  
`Closed_Shrublands` | % |  0  |  100  | Percentage of closed shrublands  
`Open_Shrublands` | % |  0  |  100  | Percentage of open shrublands  
`Woody_Savannas` | % |  0  |  100  | Percentage of woody savannas  
`Savannas` | % |  0  |  100  | Percentage of savannas  
`Grasslands` | % |  0  |  100  | Percentage of grasslands  
`Permanent_Wetlands` | % |  0  |  100  | Percentage of permanent wetlands  
`Croplands` | % |  0  |  100  | Percentage of croplands  
`Urban_And_Built_Up` | % |  0  |  100  | Percentage of urban and built up  
`Cropland_Natural_Vegetation_Mosaic` | % |  0  |  100  | Percentage of cropland natural vegetation mosaic  
`Snow_And_Ice` | % |  0  |  100  | Percentage of snow and ice  
`Barren_Or_Sparsely_Populated` | % |  0  |  100  | Percentage of barren or sparsely populated  
`Unclassified` | % |  0  |  100  | Percentage of unclassified  
`No_Data` | % |  0  |  100  | Percentage of no data  
**Overall_Class Class Table**
Value | Color | Description  
---|---|---  
0 | #032f7e | Water  
1 | #02740b | Evergreen_Needleleaf_Fores  
2 | #02740b | Evergreen_Broadleaf_Forest  
3 | #8cf502 | Deciduous_Needleleaf_Forest  
4 | #8cf502 | Deciduous_Broadleaf_Forest  
5 | #a4da01 | Mixed_Forest  
6 | #ffbd05 | Closed_Shrublands  
7 | #ffbd05 | Open_Shrublands  
8 | #7a5a02 | Woody_Savannas  
9 | #f0ff0f | Savannas  
10 | #869b36 | Grasslands  
11 | #6091b4 | Permanent_Wetlands  
12 | #ff4e4e | Croplands  
13 | #999999 | Urban_and_Built-up  
14 | #ff4e4e | Cropland_Natural_Vegetation_Mosaic  
15 | #ffffff | Snow_and_Ice  
16 | #feffc0 | Barren_Or_Sparsely_Vegetated  
17 | #020202 | Unclassified  
**Terms of Use**
[CC-BY-NC-SA-4.0](https://spdx.org/licenses/CC-BY-NC-SA-4.0.html)
Citations:
  * Weiss, D.J., P.M. Atkinson, S. Bhatt, B. Mappin, S.I. Hay & P.W. Gething (2014) An effective approach for gap-filling continental scale remotely sensed time-series. ISPRS Journal of Photogrammetry and Remote Sensing, 98, 106-118.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual#code-editor-javascript-sample) More
```
vardataset=
ee.ImageCollection('Oxford/MAP/IGBP_Fractional_Landcover_5km_Annual')
.filter(ee.Filter.date('2012-01-01','2012-12-31'));
varlandcover=dataset.select('Overall_Class');
varlandcoverVis={
min:1.0,
max:19.0,
palette:[
'032f7e','02740b','02740b','8cf502','8cf502','a4da01','ffbd05',
'ffbd05','7a5a02','f0ff0f','869b36','6091b4','999999','ff4e4e',
'ff4e4e','ffffff','feffc0','020202','020202'
],
};
Map.setCenter(-88.6,26.4,1);
Map.addLayer(landcover,landcoverVis,'Landcover');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Oxford/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual)
[ Oxford MAP: Malaria Atlas Project Fractional International Geosphere-Biosphere Programme Landcover ](https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual)
The underlying dataset for this landcover product is the IGBP layer found within the MODIS annual landcover product (MCD12Q1). This data was converted from its categorical format, which has a ≈500 meter resolution, to a fractional product indicating the integer percentage (0-100) of the output pixel covered by each of …
Oxford/MAP/IGBP_Fractional_Landcover_5km_Annual, landcover,landuse-landcover,map,oxford 
2001-01-01T00:00:00Z/2013-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://malariaatlas.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Oxford_MAP_IGBP_Fractional_Landcover_5km_Annual)


