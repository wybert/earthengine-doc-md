 
#  Projections 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [ The default projection ](https://developers.google.com/earth-engine/guides/projections#the-default-projection)
  * [Reprojecting](https://developers.google.com/earth-engine/guides/projections#reprojecting)


Earth Engine is designed so that you rarely have to worry about map projections when doing computations. As with scale, the projection in which computations take place is determined on a "pull" basis. Specifically, inputs are requested in the output projection. The output may be determined from a function parameter (e.g. `crs`), Code Editor and geemap map objects (which have a [maps mercator (EPSG:3857)](http://epsg.io/3857) projection), or with a `reproject()` call. When you display images in the Code Editor or geemap, inputs are requested in [maps mercator](http://epsg.io/3857). Consider the following simple operation on a MODIS image, which has a [sinusoidal](http://spatialreference.org/ref/sr-org/6974/) projection:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/projections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/projections#colab-python-sample) More
```
// The input image has a SR-ORG:6974 (sinusoidal) projection.
varimage=ee.Image('MODIS/061/MOD13A1/2014_05_09').select(0);
// Normalize the image and add it to the map.
varrescaled=image.unitScale(-2000,10000);
varvisParams={min:0.15,max:0.7};
Map.addLayer(rescaled,visParams,'Rescaled');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The input image has a SR-ORG:6974 (sinusoidal) projection.
image = ee.Image('MODIS/061/MOD13A1/2014_05_09').select(0)
# Normalize the image and add it to the map.
rescaled = image.unitScale(-2000, 10000)
vis_params = {'min': 0.15, 'max': 0.7}
m = geemap.Map()
m.add_layer(rescaled, vis_params, 'Rescaled')
m
```

The order of operations for this code sample is diagrammed in Figure 1. Note that the projection of the input is determined by the output, specifically the [maps mercator](http://epsg.io/3857) projection of the map display in the Code Editor. This projection propagates back through the sequence of operations such that the inputs are requested in maps mercator, at a scale determined by the zoom level of the map.
![projection](https://developers.google.com/static/earth-engine/images/Projection.png) Figure 1. Flow chart of operations corresponding to the display of a MODIS image in the Code Editor map. Projections (left side of flow chart) of each operation are determined from the output. Curved lines indicate the flow of information to the reprojection: specifically, the output projection and scale. 
In Earth Engine, projections are specified by a Coordinate Reference System (CRS or the `crs` parameter of many methods). You can check the projection of an image by calling `projection()` on it:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/projections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/projections#colab-python-sample) More
```
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318').select(0);
print('Projection, crs, and crs_transform:',image.projection());
print('Scale in meters:',image.projection().nominalScale());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318').select(0)
display('Projection, crs, and crs_transform:', image.projection())
display('Scale in meters:', image.projection().nominalScale())
```

Note that by calling `nominalScale()` on the `ee.Projection` returned by `projection()`, you can determine the native resolution of the image. The native resolution is the nominal pixel scale in meters of the lowest level of the [image pyramid](https://developers.google.com/earth-engine/guides/scale#image-pyramids). Because each band of an image can have a different scale and/or projection, if you call `projection()` on an image with at least one band that doesn't have the same projection as the others, you may see an error like:
Image.projection: The bands of the specified image contain different projections. Use Image.select to pick a single band.
##  The default projection 
Unless you need your computation to occur in a specific projection, there is generally no need to specify a projection. Only for output that's ambiguous will Earth Engine require you to specify a projection and/or scale. Ambiguity can result from reducing an `ImageCollection` containing images with different projections (i.e. [creating a composite](https://developers.google.com/earth-engine/guides/ic_reducing#projection)). An image which is a composite or mosaic of input images with different projections will have the default projection, which is [WGS84](https://epsg.io/4326) with 1-degree scale. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/projections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/projections#colab-python-sample) More
```
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA');
varmosaic=collection.filterDate('2018-01-01','2019-01-01').mosaic();
print(mosaic.projection());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
collection = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
mosaic = collection.filterDate('2018-01-01', '2019-01-01').mosaic()
display(mosaic.projection())
```

If you try to use an image like this in a computation, you may see an error like:
The default WGS84 projection is invalid for aggregations. Specify a scale or crs & crs_transform.
Generally, an aggregation at 1-degree scale is not desired or intended, so Earth Engine gives this friendly reminder to provide a complete specification for the output.
Users often find this behavior confusing and worry about the "lost" projection information, but the pixels aren't actually computed until they're needed ([learn more](https://developers.google.com/earth-engine/guides/deferred_execution)), and at that point, there's always an output projection that accompanies the request that specified how to compute the composite.
In the vast majority of use cases, having no projection is not a problem and is actually a valuable optimization, as it allows previewing the results at any zoom level without having to wait for the full resolution computation to complete. But it does mean that the output can appear different at different zoom levels.
If the optimized display image somehow isn't sufficient, computation in a specific projection can be forced by reprojecting the output as described in the following section.
## Reprojecting
You can force operations to be performed in a specific projection with the `reproject()` method. Using `reproject()` results in the inputs being requested in the projection specified in the `reproject()` call. Computations in your code _before_ the `reproject()` call will be done in the specified projection. For example, to force a composite to be produced in a specific projection:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/projections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/projections#colab-python-sample) More
```
// Some projection that is suitable for your area of interest.
varproj=ee.Projection(...);
varoutput=collection.reduce(...).reproject(proj);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Some projection that is suitable for your area of interest.
proj = ee.Projection(...)
output = collection.reduce(...).reproject(proj)
```

A few cases that require a fixed projection include: 
  * Computing gradients (e.g. `ee.Terrain.gradient` or `ee.Terrain.slope`).
  * `reduceResolution`, for when you want to aggregate higher resolution pixels into lower resolution. ([Learn more about reducing resolution](https://developers.google.com/earth-engine/guides/resample#reduce-resolution)).

**Warning:** Use `reproject()` with caution! 
There are several reasons you should avoid using `reproject()` unless you absolutely need to. Suppose, for example, you reproject something and add it to the map. If the scale you specified in the `reproject()` call is much smaller than the zoom level of the map, Earth Engine will request all the inputs at very small scale, over a very wide spatial extent. This can result in much too much data being requested at once and lead to an error.
If the eventual output is in a different projection from that specified in the `reproject()` call, that will result in _another_ reprojection. This is another reason to be cautious about using `reproject()` in your code. Consider the following example, which forces the MODIS image to first be reprojected to [WGS84](https://epsg.io/4326), then reprojected to [maps mercator](http://epsg.io/3857) for display in the Code Editor map:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/projections#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/projections#colab-python-sample) More
```
// The input image has a SR-ORG:6974 (sinusoidal) projection.
varimage=ee.Image('MODIS/061/MOD13A1/2014_05_09').select(0);
// Operations *before* the reproject call will be done in the projection
// specified by reproject(). The output results in another reprojection.
varreprojected=image
.unitScale(-2000,10000)
.reproject('EPSG:4326',null,500);
Map.addLayer(reprojected,{min:0.15,max:0.7},'Reprojected');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The input image has a SR-ORG:6974 (sinusoidal) projection.
image = ee.Image('MODIS/061/MOD13A1/2014_05_09').select(0)
# Operations *before* the reproject call will be done in the projection
# specified by reproject(). The output results in another reprojection.
reprojected = image.unitScale(-2000, 10000).reproject('EPSG:4326', None, 500)
m = geemap.Map()
m.add_layer(reprojected, {'min': 0.15, 'max': 0.7}, 'Reprojected')
m
```

Figure 2 diagrams the flow of operations corresponding to this simple reprojection example. Note that the first reprojection is explicit, as specified in the `reproject()` call. The second reprojection is implicit, performed by Earth Engine automatically in order to display the result on the map. Also observe that the information about what projection to use propagates back from the request to the input.
![reprojection](https://developers.google.com/static/earth-engine/images/Reprojection.png) Figure 2. Flow chart of operations corresponding to the reprojection of a MODIS image in the Code Editor map. Curved lines indicate the flow of information to the reprojections: specifically, the output projection and scale. 
