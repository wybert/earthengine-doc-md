 
#  Landsat Image Mosaic of Antarctica (LIMA) - Processed Landsat Scenes (16 bit) Metadata 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
![USGS/LIMA/SR_METADATA](https://developers.google.com/earth-engine/datasets/images/USGS/USGS_LIMA_SR_METADATA_sample.png) 

Dataset Availability
    1999-06-30T00:00:00Z–2002-09-04T00:00:00Z 

Dataset Provider
     [ USGS ](https://lima.usgs.gov/index.php) 

Earth Engine Snippet
     `    ee.FeatureCollection("USGS/LIMA/SR_METADATA")   ` [ open_in_new ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_LIMA_SR_METADATA) 

Tags
     [antarctica](https://developers.google.com/earth-engine/datasets/tags/antarctica) [ice](https://developers.google.com/earth-engine/datasets/tags/ice) [landsat-derived](https://developers.google.com/earth-engine/datasets/tags/landsat-derived) [lima](https://developers.google.com/earth-engine/datasets/tags/lima) [mosaic](https://developers.google.com/earth-engine/datasets/tags/mosaic) [satellite-imagery](https://developers.google.com/earth-engine/datasets/tags/satellite-imagery) [sr](https://developers.google.com/earth-engine/datasets/tags/sr) [table](https://developers.google.com/earth-engine/datasets/tags/table) [usgs](https://developers.google.com/earth-engine/datasets/tags/usgs)
[Description](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR_METADATA#description)[Table Schema](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR_METADATA#table-schema)[Terms of Use](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR_METADATA#terms-of-use)[Citations](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR_METADATA#citations) More
The Landsat Image Mosaic of Antarctica (LIMA) is a seamless and virtually cloudless mosaic created from processed Landsat 7 ETM+ scenes.
Processed Landsat Scenes (16 bit) are Level 1Gt NLAPS scenes converted to 16 bit, processed with sun-angle correction, and converted to reflectance values ([Bindschadler 2008](https://lima.usgs.gov/LIMA_paper.pdf)).
Each Landsat scene is processed with elevation data and sun-angle correction to ensure surface features were accurately represented. The sun's angle in Antarctica gives the appearance of a setting sun. Because of the low sun angle, as Landsat passes over Antarctica, the outer edges of the continent appear brighter than areas closer to the South Pole, so scenes have bright and dark areas. Inconsistent sun angles and shadows where corrected for these scenes. Without this process, mosaicking would produce a patchwork of scenes since each scene would have a brighter and a darker side.
This is a table which contains metadata for the Image Collection [USGS/LIMA/SR](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR)
**Table Schema**
Name | Type | Description  
---|---|---  
ACQ_DATE | STRING | Acquisition date in YYYY-MM-DD format  
PATH | INT | WRS path  
POLY_ID | INT | Unique ID assigned to a polygon  
ROW | INT | WRS row  
SCENE_ID | STRING | Scene ID  
SENSOR | STRING | Sensor  
SPACE | STRING | Name of the satellite used to gather data  
**Terms of Use**
These images are in the public domain and can be used freely and without acknowledgement. However, credit to the Landsat Image Mosaic of Antarctica (LIMA) Project is greatly appreciated.
Citations:
  * Bindschadler, R., Vornberger, P., Fleming, A., Fox, A., Mullins, J., Binnie, D., Paulson, S., Granneman, B., and Gorodetzky, D., 2008, The Landsat Image Mosaic of Antarctica, Remote Sensing of Environment, 112, pp. 4214-4226. [PDF](https://lima.usgs.gov/LIMA_paper.pdf)


### Explore with Earth Engine
**Important:** Earth Engine is a platform for petabyte-scale scientific analysis and visualization of geospatial datasets, both for public benefit and for business and government users. Earth Engine is free to use for research, education, and nonprofit use. To get started, please [register for Earth Engine access.](https://console.cloud.google.com/earth-engine)
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR_METADATA#code-editor-javascript-sample) More
```
vardataset=ee.FeatureCollection('USGS/LIMA/SR_METADATA');
// Calculate the age of each feature by subtracting
// the acquisition date from "today".
varfeature_ages=dataset.map(
function(feature){
vartoday=ee.Date.fromYMD(2024,1,12);
varacq_date=ee.Date.parse(
'yyyy-MM-dd',feature.get('ACQ_DATE'));
vardiff=today.difference(acq_date,'day');
returnfeature.set({'ACQ_AGE':diff});
}
);
// Reduce by calculating the smallest ACQ_AGE,
// which gives the most recent acquisition date for
// that area.
varreduced_ages=feature_ages.reduceToImage({
properties:['ACQ_AGE'],
reducer:ee.Reducer.min()
});
varreduced_ages_vis={
min:6000,
max:9000,
palette:['00ff00','ff0000'],
};
varlon=-43.6;
varlat=-74.2;
vargray=150;
varbackground=ee.Image.rgb(gray,gray,gray).visualize({min:0,max:255});
Map.setCenter(lon,lat,2);
Map.addLayer(
reduced_ages,
reduced_ages_vis,
'Acquisition Age');
```
[ Open in Code Editor ](https://code.earthengine.google.com/?scriptPath=Examples:Datasets/USGS/USGS_LIMA_SR_METADATA)
[ Landsat Image Mosaic of Antarctica (LIMA) - Processed Landsat Scenes (16 bit) Metadata ](https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR_METADATA)
The Landsat Image Mosaic of Antarctica (LIMA) is a seamless and virtually cloudless mosaic created from processed Landsat 7 ETM+ scenes. Processed Landsat Scenes (16 bit) are Level 1Gt NLAPS scenes converted to 16 bit, processed with sun-angle correction, and converted to reflectance values (Bindschadler 2008). Each Landsat scene is …
USGS/LIMA/SR_METADATA, antarctica,ice,landsat-derived,lima,mosaic,satellite-imagery,sr,table,usgs 
1999-06-30T00:00:00Z/2002-09-04T00:00:00Z
-90 -180 -55 180 
Google Earth Engine
https://developers.google.com/earth-engine/datasets
  * [ ](https://doi.org/https://lima.usgs.gov/index.php)
  * [ ](https://doi.org/https://developers.google.com/earth-engine/datasets/catalog/USGS_LIMA_SR_METADATA)


