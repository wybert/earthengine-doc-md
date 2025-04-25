 
#  geoBoundaries: Political administrative boundaries at Country level (ADM0), v6.0.0 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WM/geoLab/geoBoundaries/600/ADM0](https://developers.google.com/earth-engine/datasets/images/WM/WM_geoLab_geoBoundaries_600_ADM0_sample.png) 

Dataset Availability
    2023-09-14T00:00:00Z–2023-09-14T00:00:00Z 

Dataset Provider
     [ William and Mary geoLab ](https://www.geoboundaries.org/index.html) 

Earth Engine Snippet
     FeatureCollection `    ee.FeatureCollection("WM/geoLab/geoBoundaries/600/ADM0")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WM/WM_geoLab_geoBoundaries_600_ADM0)      FeatureView  `    ui.Map.FeatureViewLayer("WM/geoLab/geoBoundaries/600/ADM0_FeatureView")   ` 

Tags
     [borders](https://developers.google.com/earth-engine/datasets/tags/borders) [countries](https://developers.google.com/earth-engine/datasets/tags/countries) [infrastructure-boundaries](https://developers.google.com/earth-engine/datasets/tags/infrastructure-boundaries) [table](https://developers.google.com/earth-engine/datasets/tags/table)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WM_geoLab_geoBoundaries_600_ADM0#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/WM_geoLab_geoBoundaries_600_ADM0#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WM_geoLab_geoBoundaries_600_ADM0#terms-of-use) More
The geoBoundaries Global Database of Political Administrative Boundaries Database is an online, open license resource of boundaries (i.e., state, county) for every country in the world. Currently 199 total entities are tracked, including all 195 UN member states, Greenland, Taiwan, Niue, and Kosovo.
Comprehensive Global Administrative Zones (CGAZ) is a set of global composites for administrative boundaries. Disputed areas are removed and replaced with polygons following US Department of State definitions. It has three boundary levels ADM0, ADM1, and ADM2, clipped to international boundaries (US Department of State), with gaps filled between borders.
This dataset is part of CGAZ. It was ingested from [version 6.0.0](https://github.com/wmgeolab/geoBoundaries/tree/1289e40e366c7b320550be1ee0614a9472d572d4) of Global Composite Files with DBF_DATE_LAST_UPDATE=2023-09-13. It shows boundaries at level ADM0 (country-level boundaries).
**Table Schema**
Name | Type | Description  
---|---|---  
shapeGroup | STRING | Unique country code  
shapeName | STRING | Administrative region name  
shapeType | STRING | Boundary type:
  * ADM0: Country level
  * ADM1: District level
  * ADM2: Municipality level

  
**Terms of Use**
geoBoundaries datasets are provided under the CC BY 4.0 license, which allows for most commmercial, noncommercial, and academic uses. See [provider terms of use](https://www.geoboundaries.org/index.html#usage).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WM_geoLab_geoBoundaries_600_ADM0#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('WM/geoLab/geoBoundaries/600/ADM0');
Map.setCenter(-100.0,38.5,4);
varstyleParams={
fillColor:'b5ffb4',
color:'00909F',
width:1.0,
};
dataset=dataset.style(styleParams);
Map.addLayer(dataset,{},'ADM0 Boundaries');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WM/WM_geoLab_geoBoundaries_600_ADM0)
[ geoBoundaries: Political administrative boundaries at Country level (ADM0), v6.0.0 ](https://developers.google.com/earth-engine/datasets/catalog/WM_geoLab_geoBoundaries_600_ADM0)
The geoBoundaries Global Database of Political Administrative Boundaries Database is an online, open license resource of boundaries (i.e., state, county) for every country in the world. Currently 199 total entities are tracked, including all 195 UN member states, Greenland, Taiwan, Niue, and Kosovo. Comprehensive Global Administrative Zones (CGAZ) is a …
WM/geoLab/geoBoundaries/600/ADM0, borders,countries,infrastructure-boundaries,table 
2023-09-14T00:00:00Z/2023-09-14T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.geoboundaries.org/index.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WM_geoLab_geoBoundaries_600_ADM0)


