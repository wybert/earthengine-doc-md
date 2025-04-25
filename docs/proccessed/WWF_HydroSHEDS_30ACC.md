 
#  WWF HydroSHEDS Flow Accumulation, 30 Arc-Seconds 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![WWF/HydroSHEDS/30ACC](https://developers.google.com/earth-engine/datasets/images/WWF/WWF_HydroSHEDS_30ACC_sample.png) 

Dataset Availability
    2000-02-11T00:00:00Z–2000-02-22T00:00:00Z 

Dataset Provider
     [ WWF ](https://www.hydrosheds.org/) 

Earth Engine Snippet
     `    ee.Image("WWF/HydroSHEDS/30ACC")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WWF/WWF_HydroSHEDS_30ACC) 

Tags
     [accumulation](https://developers.google.com/earth-engine/datasets/tags/accumulation) [drainage](https://developers.google.com/earth-engine/datasets/tags/drainage) [flow](https://developers.google.com/earth-engine/datasets/tags/flow) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [hydrography](https://developers.google.com/earth-engine/datasets/tags/hydrography) [hydrology](https://developers.google.com/earth-engine/datasets/tags/hydrology) [hydrosheds](https://developers.google.com/earth-engine/datasets/tags/hydrosheds) [srtm](https://developers.google.com/earth-engine/datasets/tags/srtm) [surface-ground-water](https://developers.google.com/earth-engine/datasets/tags/surface-ground-water) [water](https://developers.google.com/earth-engine/datasets/tags/water) [wwf](https://developers.google.com/earth-engine/datasets/tags/wwf)
[Description](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_30ACC#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_30ACC#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_30ACC#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_30ACC#citations) More
HydroSHEDS is a mapping product that provides hydrographic information for regional and global-scale applications in a consistent format. It offers a suite of geo-referenced datasets (vector and raster) at various scales, including river networks, watershed boundaries, drainage directions, and flow accumulations. HydroSHEDS is based on elevation data obtained in 2000 by NASA's Shuttle Radar Topography Mission (SRTM).
This flow accumulation dataset defines the amount of upstream area (in number of cells) draining into each cell. The drainage direction layer is used to define which cells flow into the target cell. The number of accumulated cells is essentially a measure of the upstream catchment area. However, since the cell size of the HydroSHEDS data set depends on latitude, the cell accumulation value cannot directly be translated into drainage areas in square kilometers. Values range from 1 at topographic highs (river sources) to very large numbers (on the order of millions of cells) at the mouths of large rivers.
This dataset is at 30 arc-second resolution. The datasets available at 30 arc-seconds are the Hydrologically Conditioned DEM, Drainage (Flow) Direction, and Flow Accumulation.
Note that the quality of the HydroSHEDS data is significantly lower for regions above 60 degrees northern latitude as there is no underlying SRTM elevation data available and thus a coarser-resolution DEM was (HYDRO1k provided by USGS).
HydroSHEDS was developed by the World Wildlife Fund (WWF) Conservation Science Program in partnership with the U.S. Geological Survey, the International Centre for Tropical Agriculture, The Nature Conservancy, and the Center for Environmental Systems Research of the University of Kassel, Germany.
**Pixel Size** 927.67 meters 
**Bands**
Name | Min | Max | Description  
---|---|---|---  
`b1` |  1*  |  6.96575e+06*  | Flow accumulation  
* estimated min or max value 
**Terms of Use**
HydroSHEDS data are free for non-commercial and commercial use. For more information, please refer to the [License Agreement](https://www.hydrosheds.org/page/license).
Citations:
  * Lehner, B., Verdin, K., Jarvis, A. (2008): New global hydrography derived from spaceborne elevation data. Eos, Transactions, AGU, 89(10): 93-94.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_30ACC#code-editor-javascript-sample) More
```
vardataset=ee.Image('WWF/HydroSHEDS/30ACC');
varflowAccumulation=dataset.select('b1');
varflowAccumulationVis={
min:0.0,
max:500.0,
palette:[
'000000','023858','006837','1a9850','66bd63','a6d96a','d9ef8b',
'ffffbf','fee08b','fdae61','f46d43','d73027'
],
};
Map.setCenter(-121.652,38.022,8);
Map.addLayer(flowAccumulation,flowAccumulationVis,'Flow Accumulation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/WWF/WWF_HydroSHEDS_30ACC)
[ WWF HydroSHEDS Flow Accumulation, 30 Arc-Seconds ](https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_30ACC)
HydroSHEDS is a mapping product that provides hydrographic information for regional and global-scale applications in a consistent format. It offers a suite of geo-referenced datasets (vector and raster) at various scales, including river networks, watershed boundaries, drainage directions, and flow accumulations. HydroSHEDS is based on elevation data obtained in 2000 …
WWF/HydroSHEDS/30ACC, accumulation,drainage,flow,geophysical,hydrography,hydrology,hydrosheds,srtm,surface-ground-water,water,wwf 
2000-02-11T00:00:00Z/2000-02-22T00:00:00Z
-67.3 -180 62 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.hydrosheds.org/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_30ACC)


