 
#  US Physiography 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![CSP/ERGo/1_0/US/physiography](https://developers.google.com/earth-engine/datasets/images/CSP/CSP_ERGo_1_0_US_physiography_sample.png) 

Dataset Availability
    2006-01-24T00:00:00Z–2011-05-13T00:00:00Z 

Dataset Provider
     [ Conservation Science Partners ](https://www.csp-inc.org/) 

Earth Engine Snippet
     `    ee.Image("CSP/ERGo/1_0/US/physiography")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CSP/CSP_ERGo_1_0_US_physiography) 

Tags
     [aspect](https://developers.google.com/earth-engine/datasets/tags/aspect) [csp](https://developers.google.com/earth-engine/datasets/tags/csp) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [ergo](https://developers.google.com/earth-engine/datasets/tags/ergo) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [landforms](https://developers.google.com/earth-engine/datasets/tags/landforms) [slope](https://developers.google.com/earth-engine/datasets/tags/slope) [topography](https://developers.google.com/earth-engine/datasets/tags/topography) [us](https://developers.google.com/earth-engine/datasets/tags/us)
[Description](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_US_physiography#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_US_physiography#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_US_physiography#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_US_physiography#citations) More
The Physiography dataset represents the spatial intersection of landforms (available in EE as ERGo/1_0/US/landforms) and lithology (available in EE as ERGo/1_0/US/lithology) data layers. It provides 247 unique combinations out of a possible 270. The values for each type are formed by concatenating the landform and lithology types (e.g., 1101 is "Peak/ridge" landform on "carbonate" lithology). This data layer is sometimes referred to as characterizing "land facets".
The landforms layer is based on the USGS's 10m NED DEM (available in EE as USGS/NED). The lithology layer is not basen on any DEM.
This dataset is provided just for the US, because of the availability of the lithology data layer, though these data are likely available for other countries.
**Pixel Size** 90 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`constant` |  1100  |  4220  | Landforms and lithology intersection  
**Terms of Use**
[CC-BY-NC-SA-4.0](https://spdx.org/licenses/CC-BY-NC-SA-4.0.html)
Citations:
  * Theobald, D. M., Harrison-Atlas, D., Monahan, W. B., & Albano, C. M. (2015). Ecologically-relevant maps of landforms and physiographic diversity for climate adaptation planning. PloS one, 10(12), [e0143619](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0143619)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_US_physiography#code-editor-javascript-sample) More
```
vardataset=ee.Image('CSP/ERGo/1_0/US/physiography');
varphysiography=dataset.select('constant');
varphysiographyVis={
min:1100.0,
max:4220.0,
};
Map.setCenter(-105.4248,40.5242,8);
Map.addLayer(physiography,physiographyVis,'Physiography');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/CSP/CSP_ERGo_1_0_US_physiography)
[ US Physiography ](https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_US_physiography)
The Physiography dataset represents the spatial intersection of landforms (available in EE as ERGo/1_0/US/landforms) and lithology (available in EE as ERGo/1_0/US/lithology) data layers. It provides 247 unique combinations out of a possible 270. The values for each type are formed by concatenating the landform and lithology types (e.g., 1101 is …
CSP/ERGo/1_0/US/physiography, aspect,csp,elevation,elevation-topography,ergo,geophysical,landforms,slope,topography,us 
2006-01-24T00:00:00Z/2011-05-13T00:00:00Z
12.54 -132.09 56.21 -60.35 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.csp-inc.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/CSP_ERGo_1_0_US_physiography)


