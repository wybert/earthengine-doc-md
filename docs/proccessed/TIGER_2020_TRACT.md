 
#  TIGER: US Census Tracts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![TIGER/2020/TRACT](https://developers.google.com/earth-engine/datasets/images/TIGER/TIGER_2020_TRACT_sample.png) 

Dataset Availability
    2020-01-01T00:00:00Z–2020-01-02T00:00:00Z 

Dataset Provider
     [ United States Census Bureau ](https://www.census.gov/programs-surveys/geography/guidance/tiger-data-products-guide.html) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("TIGER/2020/TRACT")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2020_TRACT)      FeatureView  `    ui.Map.FeatureViewLayer("TIGER/2020/TRACT_FeatureView")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2020_TRACT_FeatureView) 

Tags
     [census](https://developers.google.com/earth-engine/datasets/tags/census) [city](https://developers.google.com/earth-engine/datasets/tags/city) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [neighborhood](https://developers.google.com/earth-engine/datasets/tags/neighborhood) [table](https://developers.google.com/earth-engine/datasets/tags/table) [tiger](https://developers.google.com/earth-engine/datasets/tags/tiger) [urban](https://developers.google.com/earth-engine/datasets/tags/urban) [us](https://developers.google.com/earth-engine/datasets/tags/us)
[Description](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT#citations) More
The United States Census Bureau regularly releases a geodatabase named TIGER. This dataset contains the 2020 census tracts. Tract areas vary tremendously, but in urban areas are roughly equivalent to a neighborhood. There are just over 85000 polygon features covering the United States, the District of Columbia, Puerto Rico, and the [Island areas](https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/release/2020-island-areas-data-products.html).
For full technical details on all TIGER 2020 products, see the [TIGER technical documentation](https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2020/TGRSHP2020_TechDoc.pdf).
**Table Schema**
Name | Type | Description  
---|---|---  
ALAND | DOUBLE | Land Area (square meters)  
AWATER | DOUBLE | Water Area (square meters)  
COUNTYFP | STRING | County FIPS Code  
FUNCSTAT | STRING | Functional Status (S = Statistical)  
GEOID | STRING | Unique Identifier of Summary Level, Characteristic Iteration, US, State, County, Tract, Block Group Code  
INTPTLAT | DOUBLE | Internal Point Latitude  
INTPTLON | DOUBLE | Internal Point Longitude  
MTFCC | STRING | MAF/TIGER Feature Classification Code  
NAME | STRING | 2020 Census tract name: this is the census tract code converted to an integer or integer plus 2-character decimal if the last two characters of the code are not both zeros.  
NAMELSAD | STRING | Full Name  
STATEFP | STRING | State FIPS Code  
TRACTCE | STRING | Census Tract Code  
**Terms of Use**
The U.S. Census Bureau offers some of its public data in machine-readable format via an Application Programming Interface (API). All of the content, documentation, code and related materials made available to you through the API are subject to [these terms and conditions](https://www.census.gov/data/developers/about/terms-of-service.html).
Citations:
  * For the creation of any reports, publications, new data sets, derived products, or services resulting from the data set, users should [cite the US Census Bureau](https://www.census.gov/about/policies/citation.html).


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('TIGER/2020/TRACT');
varvisParams={
min:0.0,
max:1e7,
palette:['d8d9d9','aaaaaa','b6dfe9','2ea3f2','0c71c3']
};
// plotting the water area per polygon
dataset=dataset.map(function(f){
returnf.set('AWATER',ee.Number.parse(f.get('AWATER')));
});

varimage=ee.Image().float().paint(dataset,'AWATER');
Map.setCenter(-81.99172,29.74101,6);
Map.addLayer(ee.Image(1),{min:0,max:1},'background');
Map.addLayer(image,visParams,'TIGER/2020/TRACT');
Map.addLayer(dataset,null,'for Inspector',false);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2020_TRACT)
### Visualize as a FeatureView
A `FeatureView` is a view-only, accelerated representation of a `FeatureCollection`. For more details, visit the [ `FeatureView` documentation. ](https://developers.google.com/earth-engine/guides/featureview_overview)
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT#code-editor-javascript-sample) More
```
varfvLayer=ui.Map.FeatureViewLayer('TIGER/2020/TRACT_FeatureView');
varvisParams={
opacity:1,
color:{
property:'AWATER',
mode:'linear',
palette:['d8d9d9','aaaaaa','b6dfe9','2ea3f2','0c71c3'],
min:0,
max:1e7
}
};
fvLayer.setVisParams(visParams);
fvLayer.setName('Water area by US census tract');
Map.setCenter(-73.15,40.9,9);
Map.add(fvLayer);
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/TIGER/TIGER_2020_TRACT_FeatureView)
[ TIGER: US Census Tracts ](https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT)
The United States Census Bureau regularly releases a geodatabase named TIGER. This dataset contains the 2020 census tracts. Tract areas vary tremendously, but in urban areas are roughly equivalent to a neighborhood. There are just over 85000 polygon features covering the United States, the District of Columbia, Puerto Rico, and …
TIGER/2020/TRACT, census,city,infrastructure-boundaries,neighborhood,table,tiger,urban,us 
2020-01-01T00:00:00Z/2020-01-02T00:00:00Z
-14.69 -180 71.567 -64.435 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.census.gov/programs-surveys/geography/guidance/tiger-data-products-guide.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/TIGER_2020_TRACT)


