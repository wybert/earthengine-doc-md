 
#  Map.addLayer
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/map-addlayer#examples)


Adds a given EE object to the map as a layer. 
Returns the new map layer.
Usage| Returns  
---|---  
`Map.addLayer(eeObject,  _visParams_, _name_, _shown_, _opacity_)`| ui.Map.Layer  
Argument| Type| Details  
---|---|---  
`eeObject`| Collection|Feature|Image|RawMapId| The object to add to the map.  
`visParams`| FeatureVisualizationParameters|ImageVisualizationParameters, optional| The visualization parameters. For Images and ImageCollection, see ee.data.getMapId for valid parameters. For Features and FeatureCollections, the only supported key is "color", as a CSS 3.0 color string or a hex string in "RRGGBB" format. Ignored when eeObject is a map ID.  
`name`| String, optional| The name of the layer. Defaults to "Layer N".  
`shown`| Boolean, optional| A flag indicating whether the layer should be on by default.  
`opacity`| Number, optional| The layer's opacity represented as a number between 0 and 1. Defaults to 1.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/map-addlayer#code-editor-javascript-sample) More
```
// A Sentinel-2 surface reflectance image.
varimage=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
Map.setCenter(-121.87,37.44,9);
// Set multi-band RGB image visualization parameters. If the "bands" parameter
// is not defined, the first three bands are used.
varrgbVis={
bands:['B11','B8','B3'],
min:0,
max:3000
};
Map.addLayer(image,rgbVis,'Multi-band RGB image');
// Set band-specific "min" and "max" properties.
varrgbVisBandSpec={
bands:['B11','B8','B3'],
min:[0,75,150],
max:[3500,3000,2500]
};
Map.addLayer(image,rgbVisBandSpec,'Band-specific min/max');
// If you don't specify "min" and "max" properties, they will be determined
// from the data type range, often resulting in an ineffective color stretch.
Map.addLayer(image.select('B8'),null,'Default visParams');
// If an image layer has already been styled, set "visParams" as null.
varimageRgb=image.visualize(rgbVis);
Map.addLayer(imageRgb,null,'Pre-styled image');
// Use the "palette" parameter with single-band image inputs to define the
// linear color gradient to stretch between the "min" and "max" values.
varsingleBandVis={
min:0,
max:3000,
palette:['blue','yellow','green']
};
Map.addLayer(image.select('B8'),singleBandVis,'Single-band palette');
// Images within ImageCollections are automatically mosaicked according to mask
// status and image order. The last image in the collection takes priority,
// invalid pixels are filled by valid pixels in preceding images.
varimageCol=ee.ImageCollection('COPERNICUS/S2_SR')
.filterDate('2021-03-01','2021-04-01');
Map.addLayer(imageCol,rgbVis,'ImageCollection mosaic');
// FeatureCollection, Feature, and Geometry objects can be styled using the
// "color" parameter.
varfeatureCol=ee.FeatureCollection('WCMC/WDPA/current/polygons');
Map.addLayer(featureCol,{color:'purple'},'FeatureCollection');
```

Was this helpful?
