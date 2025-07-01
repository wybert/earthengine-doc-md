 
#  ee.Image.sampleRegions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-sampleregions#examples)


Converts each pixel of an image (at a given scale) that intersects one or more regions to a Feature, returning them as a FeatureCollection. Each output feature will have one property per band of the input image, as well as any specified properties copied from the input feature. 
Note that geometries will be snapped to pixel centers.
Usage| Returns  
---|---  
`Image.sampleRegions(collection,  _properties_, _scale_, _projection_, _tileScale_, _geometries_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to sample.  
`collection`| FeatureCollection| The regions to sample over.  
`properties`| List, default: null| The list of properties to copy from each input feature. Defaults to all non-system properties.  
`scale`| Float, default: null| A nominal scale in meters of the projection to sample in. If unspecified, the scale of the image's first band is used.  
`projection`| Projection, default: null| The projection in which to sample. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale.  
`tileScale`| Float, default: 1| A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default.  
`geometries`| Boolean, default: false| If true, the results will include a point geometry per sampled pixel. Otherwise, geometries will be omitted (saving memory).  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-sampleregions#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-sampleregions#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
Map.setCenter(-122.503881,37.765588,18);
Map.addLayer(img,{bands:['B11','B8','B3'],min:100,max:4500},'img');
// A feature collection with two polygon regions each intersecting 36
// pixels at 10 m scale.
varfcPolygon=ee.FeatureCollection([
ee.Feature(ee.Geometry.Rectangle(
-122.50620929,37.76502806,-122.50552264,37.76556663),{id:0}),
ee.Feature(ee.Geometry.Rectangle(
-122.50530270,37.76565568,-122.50460533,37.76619425),{id:1})
]);
Map.addLayer(fcPolygon,{color:'yellow'},'fcPolygon');
varfcPolygonSamp=img.sampleRegions({
collection:fcPolygon,
scale:10,
geometries:true
});
// Note that 7 pixels are missing from the sample. If a pixel contains a masked
// band value it will be excluded from the sample. In this case, the TCI_B band
// is masked for each unsampled pixel.
print('A feature per pixel (at given scale) in each region',fcPolygonSamp);
Map.addLayer(fcPolygonSamp,{color:'purple'},'fcPolygonSamp');
// A feature collection with two points intersecting two different pixels.
// This example is included to show the behavior for point geometries. In
// practice, if the feature collection is all points, ee.Image.reduceRegions
// should be used instead to save memory.
varfcPoint=ee.FeatureCollection([
ee.Feature(ee.Geometry.Point([-122.50309256,37.76605006]),{id:0}),
ee.Feature(ee.Geometry.Point([-122.50344661,37.76560903]),{id:1})
]);
Map.addLayer(fcPoint,{color:'cyan'},'fcPoint');
varfcPointSamp=img.sampleRegions({
collection:fcPoint,
scale:10
});
print('A feature per point',fcPointSamp);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Sentinel-2 surface reflectance image.
img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
m = geemap.Map()
m.set_center(-122.503881, 37.765588, 18)
m.add_layer(
  img, {'bands': ['B11', 'B8', 'B3'], 'min': 100, 'max': 4500}, 'img'
)
display(m)
# A feature collection with two polygon regions each intersecting 36
# pixels at 10 m scale.
fc_polygon = ee.FeatureCollection([
  ee.Feature(
    ee.Geometry.Rectangle(
      -122.50620929, 37.76502806, -122.50552264, 37.76556663
    ),
    {'id': 0},
  ),
  ee.Feature(
    ee.Geometry.Rectangle(
      -122.50530270, 37.76565568, -122.50460533, 37.76619425
    ),
    {'id': 1},
  ),
])
m.add_layer(fc_polygon, {'color': 'yellow'}, 'fc_polygon')
fc_polygon_samp = img.sampleRegions(
  collection=fc_polygon, scale=10, geometries=True
)
# Note that 7 pixels are missing from the sample. If a pixel contains a masked
# band value it will be excluded from the sample. In this case, the TCI_B band
# is masked for each unsampled pixel.
display('A feature per pixel (at given scale) in each region', fc_polygon_samp)
m.add_layer(fc_polygon_samp, {'color': 'purple'}, 'fc_polygon_samp')
# A feature collection with two points intersecting two different pixels.
# This example is included to show the behavior for point geometries. In
# practice, if the feature collection is all points, ee.Image.reduceRegions
# should be used instead to save memory.
fc_point = ee.FeatureCollection([
  ee.Feature(ee.Geometry.Point([-122.50309256, 37.76605006]), {'id': 0}),
  ee.Feature(ee.Geometry.Point([-122.50344661, 37.76560903]), {'id': 1}),
])
m.add_layer(fc_point, {'color': 'cyan'}, 'fc_point')
fc_point_samp = img.sampleRegions(collection=fc_point, scale=10)
display('A feature per point', fc_point_samp)
```

