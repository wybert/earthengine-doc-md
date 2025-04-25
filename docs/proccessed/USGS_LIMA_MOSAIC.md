 
#  Landsat Image Mosaic of Antarctica (LIMA) 16-Bit Pan-Sharpened Mosaic 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USGS/LIMA/MOSAIC](https://developers.google.com/earth-engine/datasets/images/USGS/USGS_LIMA_MOSAIC_sample.png) 

Dataset Availability
    1999-06-30T00:00:00Z–2002-09-04T00:00:00Z 

Dataset Provider
     [ USGS ](https://lima.usgs.gov/index.php) 

Earth Engine Snippet
     `    ee.Image("USGS/LIMA/MOSAIC")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_LIMA_MOSAIC) 

Tags
     [antarctica](https://developers.google.com/earth-engine/datasets/tags/antarctica) [ice](https://developers.google.com/earth-engine/datasets/tags/ice) [landsat-derived](https://developers.google.com/earth-engine/datasets/tags/landsat-derived) [lima](https://developers.google.com/earth-engine/datasets/tags/lima) [mosaic](https://developers.google.com/earth-engine/datasets/tags/mosaic) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_MOSAIC#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_MOSAIC#bands)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_MOSAIC#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_MOSAIC#citations) More
The Landsat Image Mosaic of Antarctica (LIMA) is a seamless and virtually cloudless mosaic created from processed Landsat 7 ETM+ scenes.
This LIMA dataset is the 16-bit Intermediate LIMA. The mosaic consists of pan-sharpened normalized surface reflectance scenes (Landsat ETM+ bands 1, 2, 3, and 4). The mosaic was constructed by ordering cloud free images on top and trimming image boundaries when tile discontinuities occurred.
Users can find the mosaic tile footprints available at: [USGS/LIMA/MOSAIC_TILE_FOOTPRINTS](https://code.earthengine.google.com/?asset=USGS/LIMA/MOSAIC_TILE_FOOTPRINTS)
**Pixel Size** 15 meters 
**Bands**
Name | Wavelength | Description  
---|---|---  
`B1` | 0.45 - 0.52 μm | Blue  
`B2` | 0.52 - 0.60 μm | Green  
`B3` | 0.63 - 0.69 μm | Red  
`B4` | 0.77 - 0.90 μm | Near infrared  
**Terms of Use**
These images are in the public domain and can be used freely and without acknowledgement. However, credit to the Landsat Image Mosaic of Antarctica (LIMA) Project is greatly appreciated.
Citations:
  * Bindschadler, R., Vornberger, P., Fleming, A., Fox, A., Mullins, J., Binnie, D., Paulson, S., Granneman, B., and Gorodetzky, D., 2008, The Landsat Image Mosaic of Antarctica, Remote Sensing of Environment, 112, pp. 4214-4226. [PDF](https://lima.usgs.gov/LIMA_paper.pdf)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_MOSAIC#code-editor-javascript-sample) More
```
vardataset=ee.Image('USGS/LIMA/MOSAIC');
varantarctica=dataset.select(['B3','B2','B1']);
varantarcticaVis={
min:0.0,
max:10000.0,
};
Map.setCenter(164.619,-77.99,7);
Map.addLayer(antarctica,antarcticaVis,'Antartica Imagery (RGB)');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_LIMA_MOSAIC)
[ Landsat Image Mosaic of Antarctica (LIMA) 16-Bit Pan-Sharpened Mosaic ](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_MOSAIC)
The Landsat Image Mosaic of Antarctica (LIMA) is a seamless and virtually cloudless mosaic created from processed Landsat 7 ETM+ scenes. This LIMA dataset is the 16-bit Intermediate LIMA. The mosaic consists of pan-sharpened normalized surface reflectance scenes (Landsat ETM+ bands 1, 2, 3, and 4). The mosaic was constructed …
USGS/LIMA/MOSAIC, antarctica,ice,landsat-derived,lima,mosaic,satellite-imagery,sr,usgs 
1999-06-30T00:00:00Z/2002-09-04T00:00:00Z
-90 -180 -55 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://lima.usgs.gov/index.php)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_MOSAIC)


