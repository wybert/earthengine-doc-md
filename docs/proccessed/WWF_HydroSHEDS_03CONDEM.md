 
#  WWF HydroSHEDS Hydrologically Conditioned DEM, 3 Arc-Seconds 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WWF/HydroSHEDS/03CONDEM](https://developers.google.com/earth-engine/datasets/images/WWF/WWF_HydroSHEDS_03CONDEM_sample.png) 

Dataset Availability
    2000-02-11T00:00:00Z–2000-02-22T00:00:00Z 

Dataset Provider
     [ WWF ](https://www.hydrosheds.org/) 

Earth Engine Snippet
     `    ee.Image("WWF/HydroSHEDS/03CONDEM")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WWF/WWF_HydroSHEDS_03CONDEM) 

Tags
     [conditioned](https://developers.google.com/earth-engine/datasets/tags/conditioned) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [hydrography](https://developers.google.com/earth-engine/datasets/tags/hydrography) [hydrology](https://developers.google.com/earth-engine/datasets/tags/hydrology) [hydrosheds](https://developers.google.com/earth-engine/datasets/tags/hydrosheds) [srtm](https://developers.google.com/earth-engine/datasets/tags/srtm) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [topography](https://developers.google.com/earth-engine/datasets/tags/topography) [water](https://developers.google.com/earth-engine/datasets/tags/water) [wwf](https://developers.google.com/earth-engine/datasets/tags/wwf)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_03CONDEM#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_03CONDEM#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_03CONDEM#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_03CONDEM#citations) More
HydroSHEDS is a mapping product that provides hydrographic information for regional and global-scale applications in a consistent format. It offers a suite of geo-referenced datasets (vector and raster) at various scales, including river networks, watershed boundaries, drainage directions, and flow accumulations. HydroSHEDS is based on elevation data obtained in 2000 by NASA's Shuttle Radar Topography Mission (SRTM).
This hydrologically conditioned elevation dataset is the result of an iterative conditioning and correction process. Note that the conditioning process alters the original DEM and may render it incorrect for applications other than deriving drainage directions. Endorheic basins (inland sinks) are ''seeded'' with a no-data cell at their lowest point in order to terminate the flow. Full details of the underlying digital elevation model are available in the HydroSHEDS website and documentation.
This dataset is at 3 arc-second resolution. The datasets available at 3 arc-seconds are the Void-Filled DEM, Hydrologically Conditioned DEM, and Drainage (Flow) Direction.
There are two areas with incorrect negative values of -100 close to Vancouver, Canada around (50.16, -123.85) and Australia (-14.96, 129.62)
**Pixel Size** 92.77 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`b1` | m |  -440*  |  8527*  | Elevation  
* estimated min or max value 
**Terms of Use**
HydroSHEDS data are free for non-commercial and commercial use. For more information, please refer to the [License Agreement](https://www.hydrosheds.org/page/license).
Citations:
  * Lehner, B., Verdin, K., Jarvis, A. (2008): New global hydrography derived from spaceborne elevation data. Eos, Transactions, AGU, 89(10): 93-94.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_03CONDEM#code-editor-javascript-sample) More
```
vardataset=ee.Image('WWF/HydroSHEDS/03CONDEM');
varelevation=dataset.select('b1');
varelevationVis={
min:-50.0,
max:3000.0,
gamma:2.0,
};
Map.setCenter(-121.652,38.022,8);
Map.addLayer(elevation,elevationVis,'Elevation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WWF/WWF_HydroSHEDS_03CONDEM)
[ WWF HydroSHEDS Hydrologically Conditioned DEM, 3 Arc-Seconds ](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_03CONDEM)
HydroSHEDS is a mapping product that provides hydrographic information for regional and global-scale applications in a consistent format. It offers a suite of geo-referenced datasets (vector and raster) at various scales, including river networks, watershed boundaries, drainage directions, and flow accumulations. HydroSHEDS is based on elevation data obtained in 2000 …
WWF/HydroSHEDS/03CONDEM, conditioned,dem,elevation,geophysical,hydrography,hydrology,hydrosheds,srtm,surface-ground-water,topography,water,wwf 
2000-02-11T00:00:00Z/2000-02-22T00:00:00Z
-67.3 -180 60 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.hydrosheds.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_03CONDEM)


