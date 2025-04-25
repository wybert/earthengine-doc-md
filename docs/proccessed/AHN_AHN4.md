 
#  AHN4: Netherlands AHN 0.5m 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![AHN/AHN4](https://developers.google.com/earth-engine/datasets/images/AHN/AHN_AHN4_sample.png) 

Dataset Availability
    2020-01-01T00:00:00Z–2022-01-01T00:00:00Z 

Dataset Provider
     [ AHN ](https://www.ahn.nl) 

Earth Engine Snippet
     `    ee.ImageCollection("AHN/AHN4")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/AHN/AHN_AHN4) 

Tags
     [ahn](https://developers.google.com/earth-engine/datasets/tags/ahn) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [lidar](https://developers.google.com/earth-engine/datasets/tags/lidar) [netherlands](https://developers.google.com/earth-engine/datasets/tags/netherlands)
[Description](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN4#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN4#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN4#terms-of-use) More
The Actueel Hoogtebestand Nederland (AHN) is a dataset with detailed and precise elevation data for the whole of the Netherlands. Elevation information was collected from helicopters and aircraft using laser technology with vertical accuracy of 5 cm.
AHN4 Dataset contains the Netherlands AHN 0.5m DSM and DTM variables. The data cover the period between 2020 and 2022.
The Digital Terrain Model (DTM) product represents the elevation of the ground, while the Digital Surface Model (DSM) product represents the elevation of the tallest surfaces at that point.
**Pixel Size** 0.5 meters 
**Bands**
Name | Units | Description  
---|---|---  
`dtm` | m | Elevation of the ground  
`dsm` | m | Elevation of the tallest surfaces at that point  
**Terms of Use**
The datasets of the AHN are available as Open Data. This means that the data can be used by anyone for free and without restrictions. For more information visit the [Open Data](https://www.ahn.nl/open-data/) page. Downloads are available under the terms of the [CC-0 license](https://data.overheid.nl/licenties-voor-hergebruik).
### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN4#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('AHN/AHN4');
varelevation=dataset.select('dsm');
varelevationVis={
min:-5.0,
max:30.0,
};
Map.setCenter(5.76583,51.855276,16);
Map.addLayer(elevation,elevationVis,'AHN4 dsm');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/AHN/AHN_AHN4)
[ AHN4: Netherlands AHN 0.5m ](https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN4)
The Actueel Hoogtebestand Nederland (AHN) is a dataset with detailed and precise elevation data for the whole of the Netherlands. Elevation information was collected from helicopters and aircraft using laser technology with vertical accuracy of 5 cm. AHN4 Dataset contains the Netherlands AHN 0.5m DSM and DTM variables. The data …
AHN/AHN4, ahn,dem,elevation,elevation-topography,geophysical,lidar,netherlands 
2020-01-01T00:00:00Z/2022-01-01T00:00:00Z
50.74 3.35 53.55 7.24 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.ahn.nl)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/AHN_AHN4)


