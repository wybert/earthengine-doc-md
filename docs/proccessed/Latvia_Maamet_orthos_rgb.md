 
#  Latvia RGB orthophotos 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Latvia/Maamet/orthos/rgb](https://developers.google.com/earth-engine/datasets/images/Latvia/Latvia_Maamet_orthos_rgb_sample.png) 

Dataset Availability
    2007-01-01T00:00:00Z–2018-01-01T00:00:00Z 

Dataset Provider
     [ Latvia orthophotos ](https://www.lgia.gov.lv/lv/ortofotokartes-1) 

Earth Engine Snippet
     `    ee.ImageCollection("Latvia/Maamet/orthos/rgb")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Latvia/Latvia_Maamet_orthos_rgb) 

Tags
     [latvia](https://developers.google.com/earth-engine/datasets/tags/latvia) [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos) [rgb](https://developers.google.com/earth-engine/datasets/tags/rgb)
[Description](https://developers.google.com/earth-engine/datasets/catalog/Latvia_Maamet_orthos_rgb#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Latvia_Maamet_orthos_rgb#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Latvia_Maamet_orthos_rgb#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Latvia_Maamet_orthos_rgb#citations) More
In Latvia, orthophoto maps are prepared in the Latvian coordinate system LKS-92 TM according to the TKS-93 map sheet division (scale 1:10000 map sheet corresponds to 5 x 5 kilometers in nature). Orthophoto maps are prepared for the whole territory of Latvia at the scale of 1:10000, but for separate territories - for cities and densely populated areas - at the scale of 1:2000 or 1:1000.
The RGB dataset has three bands: red, green, and blue.
For more information, please see the [Latvia orthophotos documentation](https://www.lgia.gov.lv/lv/ortofotokartes-1)
**Pixel Size** 0.2 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`R` | dn |  0  |  255  | Red  
`G` | dn |  0  |  255  | Green  
`B` | dn |  0  |  255  | Blue  
**Terms of Use**
For more details please see the [Terms of use](https://www.lgia.gov.lv/sites/lgia/files/document/Atverto%20datu%20licence%20CC%20BY_0.pdf)
Citations:
  * Latvijas Geospatial Information Agency


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Latvia_Maamet_orthos_rgb#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('Latvia/Maamet/orthos/rgb');
Map.setCenter(24.737,56.861,15);
Map.addLayer(dataset,null,'Latvia Maamet RGB');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Latvia/Latvia_Maamet_orthos_rgb)
[ Latvia RGB orthophotos ](https://developers.google.com/earth-engine/datasets/catalog/Latvia_Maamet_orthos_rgb)
In Latvia, orthophoto maps are prepared in the Latvian coordinate system LKS-92 TM according to the TKS-93 map sheet division (scale 1:10000 map sheet corresponds to 5 x 5 kilometers in nature). Orthophoto maps are prepared for the whole territory of Latvia at the scale of 1:10000, but for separate …
Latvia/Maamet/orthos/rgb, latvia,orthophotos,rgb 
2007-01-01T00:00:00Z/2018-01-01T00:00:00Z
55.5 20.5 58.5 28.6 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.lgia.gov.lv/lv/ortofotokartes-1)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Latvia_Maamet_orthos_rgb)


