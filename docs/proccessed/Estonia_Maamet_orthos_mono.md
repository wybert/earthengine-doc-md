 
#  Estonia mono orthophotos 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![Estonia/Maamet/orthos/mono](https://developers.google.com/earth-engine/datasets/images/Estonia/Estonia_Maamet_orthos_mono_sample.png) 

Dataset Availability
    1993-01-01T00:00:00Z–2021-06-16T00:00:00Z 

Dataset Provider
     [ Estonia orthophotos ](https://geoportaal.maaamet.ee/eng/Spatial-Data/Orthophotos-p309.html) 

Earth Engine Snippet
     `    ee.ImageCollection("Estonia/Maamet/orthos/mono")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Estonia/Estonia_Maamet_orthos_mono) 

Tags
     [estonia](https://developers.google.com/earth-engine/datasets/tags/estonia) [orthophotos](https://developers.google.com/earth-engine/datasets/tags/orthophotos)
[Description](https://developers.google.com/earth-engine/datasets/catalog/Estonia_Maamet_orthos_mono#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/Estonia_Maamet_orthos_mono#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/Estonia_Maamet_orthos_mono#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/Estonia_Maamet_orthos_mono#citations) More
Orthophotos are an aerial photo dataset covering Estonia.
An orthophoto is a processed aerial photo from which distortions caused by terrain relief, camera tilt relative to the ground at the moment of exposure and camera central projection are removed. A digital orthophoto has a certain pixel size or resolution which shows the smallest indivisible exposed area on the ground (Ground Sampling Distance, GSD).
Orthophotos have a nationwide coverage and correspond to the scale of 1:5000-1:10000 (pixel size 20-40 cm). Orthophotos for densely-populated areas are produced with the pixel size of 10-16 cm.
The mono dataset has a single grayscale band with nationwide coverage.
For more information, please see the [Estonia orthophotos documentation](https://geoportaal.maaamet.ee/eng/Spatial-Data/Orthophotos-p309.html)
**Pixel Size** 0.4 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`mono` |  0  |  255  | Grayscale  
**Terms of Use**
The data is free to use for commercial and non-commercial purposes for a non-specified term, provided that proper attribution is given to the licensor (e.g. Estonian Land Board) along with the title and age of the data.
For more details please see the [Terms of use](https://geoportaal.maaamet.ee/docs/Avaandmed/Licence-of-open-data-of-Estonian-Land-Board.pdf)
Citations:
  * Map data: Estonian Land Board


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/Estonia_Maamet_orthos_mono#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('Estonia/Maamet/orthos/mono');
Map.setCenter(26.61312,58.5879,15);
Map.addLayer(dataset,null,'Estonia Maamet mono');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/Estonia/Estonia_Maamet_orthos_mono)
[ Estonia mono orthophotos ](https://developers.google.com/earth-engine/datasets/catalog/Estonia_Maamet_orthos_mono)
Orthophotos are an aerial photo dataset covering Estonia. An orthophoto is a processed aerial photo from which distortions caused by terrain relief, camera tilt relative to the ground at the moment of exposure and camera central projection are removed. A digital orthophoto has a certain pixel size or resolution which …
Estonia/Maamet/orthos/mono, estonia,orthophotos 
1993-01-01T00:00:00Z/2021-06-16T00:00:00Z
57.3 21.5 59.5 28.1 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://geoportaal.maaamet.ee/eng/Spatial-Data/Orthophotos-p309.html)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/Estonia_Maamet_orthos_mono)


