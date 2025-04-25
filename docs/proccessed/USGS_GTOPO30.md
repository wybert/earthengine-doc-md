 
#  GTOPO30: Global 30 Arc-Second Elevation 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USGS/GTOPO30](https://developers.google.com/earth-engine/datasets/images/USGS/USGS_GTOPO30_sample.png) 

Dataset Availability
    1996-01-01T00:00:00Z–1996-01-01T00:00:00Z 

Dataset Provider
     [ United States Geological Survey ](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-global-30-arc-second-elevation-gtopo30) 

Earth Engine Snippet
     `    ee.Image("USGS/GTOPO30")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_GTOPO30) 

Tags
     [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation](https://developers.google.com/earth-engine/datasets/tags/elevation) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [nasa](https://developers.google.com/earth-engine/datasets/tags/nasa) [topography](https://developers.google.com/earth-engine/datasets/tags/topography) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
gtopo30
[Description](https://developers.google.com/earth-engine/datasets/catalog/USGS_GTOPO30#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USGS_GTOPO30#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USGS_GTOPO30#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USGS_GTOPO30#citations) More
GTOPO30 is a global digital elevation model (DEM) with a horizontal grid spacing of 30 arc seconds (approximately 1 kilometer). The DEM was derived from several raster and vector sources of topographic information. Completed in late 1996, GTOPO30 was developed over a three-year period through a collaborative effort led by the U.S. Geological Survey''s Center for Earth Resources Observation and Science (EROS). The following organizations participated by contributing funding or source data: the National Aeronautics and Space Administration (NASA), the United Nations Environment Programme/Global Resource Information Database (UNEP/GRID), the U.S. Agency for International Development (USAID), the Instituto Nacional de Estadistica Geografica e Informatica (INEGI) of Mexico, the Geographical Survey Institute (GSI) of Japan, Manaaki Whenua Landcare Research of New Zealand, and the Scientific Committee on Antarctic Research (SCAR).
**Bands**
Name | Units | Min | Max | Pixel Size | Description  
---|---|---|---|---|---  
`elevation` | m |  -407*  |  8752*  |  927.67 meters  | Elevation  
* estimated min or max value 
**Terms of Use**
There are no restrictions on the use of data received from the U.S. Geological Survey's Earth Resources Observation and Science (EROS) Center. For more information, visit the USGS' [Data Use and Citation](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-data-use-and-citation) page.
Citations:
  * GTOPO30 DEM courtesy of the U.S. Geological Survey


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USGS_GTOPO30#code-editor-javascript-sample) More
```
vardataset=ee.Image('USGS/GTOPO30');
varelevation=dataset.select('elevation');
varelevationVis={
min:-10.0,
max:8000.0,
gamma:1.6,
};
Map.setCenter(11.69,43.9,4);
Map.addLayer(elevation,elevationVis,'Elevation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_GTOPO30)
[ GTOPO30: Global 30 Arc-Second Elevation ](https://developers.google.com/earth-engine/datasets/catalog/USGS_GTOPO30)
GTOPO30 is a global digital elevation model (DEM) with a horizontal grid spacing of 30 arc seconds (approximately 1 kilometer). The DEM was derived from several raster and vector sources of topographic information. Completed in late 1996, GTOPO30 was developed over a three-year period through a collaborative effort led by …
USGS/GTOPO30, dem,elevation,elevation-topography,geophysical,nasa,topography,usgs 
1996-01-01T00:00:00Z/1996-01-01T00:00:00Z
-90 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-global-30-arc-second-elevation-gtopo30)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USGS_GTOPO30)


