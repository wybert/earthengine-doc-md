 
#  DEM-S: Australian Smoothed Digital Elevation Model 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![AU/GA/DEM_1SEC/v10/DEM-S](https://developers.google.com/earth-engine/datasets/images/AU/AU_GA_DEM_1SEC_v10_DEM-S_sample.png) 

Dataset Availability
    2010-02-01T00:00:00Z–2010-02-01T00:00:00Z 

Dataset Provider
     [ Geoscience Australia ](https://www.ga.gov.au/metadata-gateway/metadata/record/72759/) 

Earth Engine Snippet
     `    ee.Image("AU/GA/DEM_1SEC/v10/DEM-S")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/AU/AU_GA_DEM_1SEC_v10_DEM-S) 

Tags
     [australia](https://developers.google.com/earth-engine/datasets/tags/australia) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [ga](https://developers.google.com/earth-engine/datasets/tags/ga) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [geoscience-australia](https://developers.google.com/earth-engine/datasets/tags/geoscience-australia) [smoothed](https://developers.google.com/earth-engine/datasets/tags/smoothed) [srtm](https://developers.google.com/earth-engine/datasets/tags/srtm)
[Description](https://developers.google.com/earth-engine/datasets/catalog/AU_GA_DEM_1SEC_v10_DEM-S#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/AU_GA_DEM_1SEC_v10_DEM-S#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/AU_GA_DEM_1SEC_v10_DEM-S#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/AU_GA_DEM_1SEC_v10_DEM-S#citations) More
The Smoothed Digital Elevation Model (DEM-S) was derived from the SRTM data acquired by NASA in February 2000. DEM-S represents ground surface topography (excluding vegetation features) and has been smoothed to reduce noise and improve the representation of surface shape. An adaptive process applied more smoothing in flatter areas than hilly areas, and more smoothing in noisier areas than in less noisy areas.
This DEM-S supports calculation of local terrain shape attributes such as slope, aspect, and curvature that could not be reliably derived from the unsmoothed 1 second DEM because of noise.
There are several areas with unexpected negative values: close to Canberra around (150.443044, -35.355281) with values of -55 and in Western Australia around (124.84, -16.44) with -43.
**Pixel Size** 30.92 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`elevation` | m |  -73.31*  |  2224.32*  | Elevation  
* estimated min or max value 
**Terms of Use**
[CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0.html)
Citations:
  * Geoscience Australia, 2015. Digital Elevation Model (DEM) of Australia derived from LiDAR 5 Metre Grid. Geoscience Australia, Canberra.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/AU_GA_DEM_1SEC_v10_DEM-S#code-editor-javascript-sample) More
```
vardataset=ee.Image('AU/GA/DEM_1SEC/v10/DEM-S');
varelevation=dataset.select('elevation');
varelevationVis={
min:-10.0,
max:1300.0,
palette:[
'3ae237','b5e22e','d6e21f','fff705','ffd611','ffb613','ff8b13',
'ff6e08','ff500d','ff0000','de0101','c21301','0602ff','235cb1',
'307ef3','269db1','30c8e2','32d3ef','3be285','3ff38f','86e26f'
],
};
Map.setCenter(133.95,-24.69,5);
Map.addLayer(elevation,elevationVis,'Elevation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/AU/AU_GA_DEM_1SEC_v10_DEM-S)
[ DEM-S: Australian Smoothed Digital Elevation Model ](https://developers.google.com/earth-engine/datasets/catalog/AU_GA_DEM_1SEC_v10_DEM-S)
The Smoothed Digital Elevation Model (DEM-S) was derived from the SRTM data acquired by NASA in February 2000. DEM-S represents ground surface topography (excluding vegetation features) and has been smoothed to reduce noise and improve the representation of surface shape. An adaptive process applied more smoothing in flatter areas than …
AU/GA/DEM_1SEC/v10/DEM-S, australia,dem,elevation,elevation-topography,ga,geophysical,geoscience-australia,smoothed,srtm 
2010-02-01T00:00:00Z/2010-02-01T00:00:00Z
-44.06 112.99 -9.99 154 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.ga.gov.au/metadata-gateway/metadata/record/72759/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/AU_GA_DEM_1SEC_v10_DEM-S)


