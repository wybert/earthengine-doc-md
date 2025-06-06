 
#  ArcticDEM Mosaic 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![UMN/PGC/ArcticDEM/V3/2m_mosaic](https://developers.google.com/earth-engine/datasets/images/UMN/UMN_PGC_ArcticDEM_V3_2m_mosaic_sample.png) 

Dataset Availability
    2016-09-21T00:00:00Z–2016-09-21T00:00:00Z 

Dataset Provider
     [ University of Minnesota Polar Geospatial Center ](https://www.pgc.umn.edu/data/arcticdem/) 

Earth Engine Snippet
     `    ee.Image("UMN/PGC/ArcticDEM/V3/2m_mosaic")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMN/UMN_PGC_ArcticDEM_V3_2m_mosaic) 

Tags
     [arctic](https://developers.google.com/earth-engine/datasets/tags/arctic) [dem](https://developers.google.com/earth-engine/datasets/tags/dem) [elevation-topography](https://developers.google.com/earth-engine/datasets/tags/elevation-topography) [geophysical](https://developers.google.com/earth-engine/datasets/tags/geophysical) [pgc](https://developers.google.com/earth-engine/datasets/tags/pgc) [umn](https://developers.google.com/earth-engine/datasets/tags/umn)
[Description](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic#citations)[DOIs](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic#dois) More
ArcticDEM is a National Geospatial-Intelligence Agency (NGA) and National Science Foundation (NSF) public-private initiative to automatically produce a high-resolution, high-quality digital surface model (DSM) of the Arctic using optical stereo imagery, high-performance computing, and open source photogrammetry software. It includes vegetation, tree canopy, buildings, and other man-made surface features. The 2m asset is a collection of strips rather than a single mosaic due to projection differences between strips.
Mosaicked DEM files are compiled from the best quality strip DEM files which have been blended and feathered to reduce void areas and edge-matching artifacts. Filtered IceSAT altimetry data has been applied to the raster files to improve absolute accuracy.
**Pixel Size** 2 meters 
**Bands**
Name | Units | Min | Max | Description  
---|---|---|---|---  
`elevation` | m |  -416.45*  |  5971.24*  | Elevation  
* estimated min or max value 
**Terms of Use**
National Science Foundation (PGC's primary funding source) policy requires researchers to acknowledge NSF support in all publications, web pages, and media interviews.
By using PGC data in Earth Engine, users agree to cite PGC and its sponsorship by the NSF. The original source of any third-party data supplied by PGC must also be properly attributed.
For more information see the PGC's [Acknowledgement Policy](https://www.pgc.umn.edu/guides/user-services/acknowledgement-policy/).
Citations:
  * DEM(s) created by the Polar Geospatial Center from DigitalGlobe, Inc. imagery. Porter, Claire; Morin, Paul; Howat, Ian; Noh, Myoung-Jon; Bates, Brian; Peterman, Kenneth; Keesey, Scott; Schlenk, Matthew; Gardiner, Judith; Tomko, Karen; Willis, Michael; Kelleher, Cole; Cloutier, Michael; Husby, Eric; Foga, Steven; Nakamura, Hitomi; Platson, Melisa; Wethington, Michael, Jr.; Williamson, Cathleen; Bauer, Gregory; Enos, Jeremy; Arnold, Galen; Kramer, William; Becker, Peter; Doshi, Abhijit; D'Souza, Cristelle; Cummens, Pat; Laurier, Fabien; Bojesen, Mikkel, 2018, ArcticDEM, Harvard Dataverse, V1, [Date Accessed].


  * [ https://doi.org/10.7910/DVN/OHHUKH ](https://doi.org/10.7910/DVN/OHHUKH)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic#code-editor-javascript-sample) More
```
vardataset=ee.Image('UMN/PGC/ArcticDEM/V3/2m_mosaic');
varelevation=dataset.select('elevation');
varelevationVis={
min:-50.0,
max:1000.0,
palette:['0d13d8','60e1ff','ffffff'],
};
Map.setCenter(-63.402,66.368,7);
Map.addLayer(elevation,elevationVis,'Elevation');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/UMN/UMN_PGC_ArcticDEM_V3_2m_mosaic)
[ ArcticDEM Mosaic ](https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic)
ArcticDEM is a National Geospatial-Intelligence Agency (NGA) and National Science Foundation (NSF) public-private initiative to automatically produce a high-resolution, high-quality digital surface model (DSM) of the Arctic using optical stereo imagery, high-performance computing, and open source photogrammetry software. It includes vegetation, tree canopy, buildings, and other man-made surface features. The …
UMN/PGC/ArcticDEM/V3/2m_mosaic, arctic,dem,elevation-topography,geophysical,pgc,umn 
2016-09-21T00:00:00Z/2016-09-21T00:00:00Z
50 -180 90 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ https://doi.org/10.7910/DVN/OHHUKH ](https://doi.org/https://www.pgc.umn.edu/data/arcticdem/)
  * [ https://doi.org/10.7910/DVN/OHHUKH ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/UMN_PGC_ArcticDEM_V3_2m_mosaic)


