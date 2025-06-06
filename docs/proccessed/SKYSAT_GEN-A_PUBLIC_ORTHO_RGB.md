 
#  Planet SkySat Public Ortho Imagery, RGB 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![SKYSAT/GEN-A/PUBLIC/ORTHO/RGB](https://developers.google.com/earth-engine/datasets/images/SKYSAT/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB_sample.png) 

Dataset Availability
    2014-07-03T00:00:00Z–2016-12-24T00:00:00Z 

Dataset Provider
     [ Planet Labs Inc. ](https://www.planet.com/) 

Earth Engine Snippet
     `    ee.ImageCollection("SKYSAT/GEN-A/PUBLIC/ORTHO/RGB")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/SKYSAT/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB) 

Tags
     [highres](https://developers.google.com/earth-engine/datasets/tags/highres) [pansharpened](https://developers.google.com/earth-engine/datasets/tags/pansharpened) [planet](https://developers.google.com/earth-engine/datasets/tags/planet) [rgb](https://developers.google.com/earth-engine/datasets/tags/rgb) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [skysat](https://developers.google.com/earth-engine/datasets/tags/skysat)
[Description](https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB#description)[Bands](https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB#bands)[Image Properties](https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB#image-properties)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB#citations) More
This data from Planet labs Inc. SkySat satellites was collected for the experimental "Skybox for Good Beta" program in 2015, as well as for various crisis response events and a few other projects. The data is available in both a 5-band Multispectral/Pan collection, and a Pansharpened RGB collection.
Each image's asset ID contains the acquisition date and time, for example, image s01_20150304T080608Z was acquired on March 4, 2015 at 08:06 Zulu (UTC). For more information, please see the [Planet Imagery Product Specifications](https://assets.planet.com/docs/Planet_Combined_Imagery_Product_Specs_letter_screen.pdf) and visit the [Planet Imagery and Archive](https://www.planet.com/products/planet-imagery/) site.
This RGB collection contains images with three pansharpened, 8-bit bands. The resolution is approximately 0.8m per pixel (closer to 1m for off-nadir images).
**Pixel Size** 0.8 meters 
**Bands**
Name | Min | Max | Wavelength | Description  
---|---|---|---|---  
`R` |  1*  |  255*  | 605-695nm | Red  
`G` |  1*  |  255*  | 515-595nm | Green  
`B` |  1*  |  255*  | 450-515nm | Blue  
* estimated min or max value 
**Image Properties**
Name | Type | Description  
---|---|---  
catalogID | STRING | Unique catalog ID corresponding to a single collection event; same across all three detectors.  
collectionEndTime | STRING | ISO 8601 collection end time (UTC).  
collectionStartTime | STRING | ISO 8601 collection start time (UTC).  
collectionType | STRING | 'Strip', 'Point', 'Area', or 'Path'.  
productType | STRING | Product type identifying the product level ('Orthorectified Imagery').  
productionID | STRING | ID of this version of this product, generated by Singer/TileMill.  
productionSystemVersion | STRING | N/A  
resamplingMethod | STRING | The method used for interpolated pixel values.  
satelliteAzimuthAngleMax | DOUBLE | Maximum satellite azimuth angle over the collection (degrees).  
satelliteAzimuthAngleMean | DOUBLE | Mean satellite azimuth angle over the collection (degrees).  
satelliteAzimuthAngleMin | DOUBLE | Minimum satellite azimuth angle over the collection (degrees).  
satelliteElevationAngleMax | DOUBLE | Maximum satellite elevation angle over the collection (degrees).  
satelliteElevationAngleMean | DOUBLE | Mean satellite elevation angle over the collection (degrees).  
satelliteElevationAngleMin | DOUBLE | Minimum satellite elevation angle over the collection (degrees).  
satelliteName | STRING | Unique name identifying the spacecraft.  
snaptoAlignmentConfidence | DOUBLE | N/A  
snaptoReferenceAssets | STRING | N/A  
solarAzimuthAngle | DOUBLE | Solar azimuth angle at the time of collection.  
solarElevationAngle | DOUBLE | Solar elevation angle at the time of collection.  
terrainBlendEpoch | DOUBLE | N/A  
**Terms of Use**
This dataset is made available publicly under the Creative Commons by Attribution license(CC-BY-4.0).
Citations:
  * © <year> Planet Labs Inc.


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB#code-editor-javascript-sample) More
```
vardataset=ee.ImageCollection('SKYSAT/GEN-A/PUBLIC/ORTHO/RGB');
varrgb=dataset.select(['R','G','B']);
varrgbVis={
min:11.0,
max:190.0,
};
Map.setCenter(-70.892,41.6555,15);
Map.addLayer(rgb,rgbVis,'RGB');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/SKYSAT/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB)
[ Planet SkySat Public Ortho Imagery, RGB ](https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB)
This data from Planet labs Inc. SkySat satellites was collected for the experimental "Skybox for Good Beta" program in 2015, as well as for various crisis response events and a few other projects. The data is available in both a 5-band Multispectral/Pan collection, and a Pansharpened RGB collection. Each image's …
SKYSAT/GEN-A/PUBLIC/ORTHO/RGB, highres,pansharpened,planet,rgb,satellite-imagery,skysat 
2014-07-03T00:00:00Z/2016-12-24T00:00:00Z
-70 -180 53 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://www.planet.com/)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/SKYSAT_GEN-A_PUBLIC_ORTHO_RGB)


