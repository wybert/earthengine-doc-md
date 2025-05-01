 
#  Object-based methods 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Thermal hotspots](https://developers.google.com/earth-engine/guides/image_objects#thermal_hotspots)
  * [Label objects](https://developers.google.com/earth-engine/guides/image_objects#label_objects)
  * [Object size](https://developers.google.com/earth-engine/guides/image_objects#object_size)
    * [Number of pixels](https://developers.google.com/earth-engine/guides/image_objects#number_of_pixels)
    * [Area](https://developers.google.com/earth-engine/guides/image_objects#area)
  * [Filter objects by size](https://developers.google.com/earth-engine/guides/image_objects#filter_objects_by_size)
  * [Zonal statistics](https://developers.google.com/earth-engine/guides/image_objects#zonal_statistics)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/image_objects.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/image_objects.ipynb)  
---|---  
Image objects are sets of connected pixels having the same integer value. Categorical, binned, and boolean image data are suitable for object analysis.
Earth Engine offers methods for labeling each object with a unique ID, counting the number of pixels composing objects, and computing statistics for values of pixels that intersect objects.
  * [`connectedComponents()`](https://developers.google.com/earth-engine/guides/image_objects#label_objects): label each object with a unique identifier.
  * [`connectedPixelCount()`](https://developers.google.com/earth-engine/guides/image_objects#object_size): compute the number of pixels in each object.
  * [`reduceConnectedComponents()`](https://developers.google.com/earth-engine/guides/image_objects#zonal_statistics): compute a statistic for pixels in each object.


**Caution:** results of object-based methods depend on scale, which is determined by: 
  * the requested scale of an output (e.g., `Export.image.toAsset()` or `Export.image.toDrive()`).
  * functions that require a scale of analysis (e.g., `reduceRegions()` or `reduceToVectors()`).
  * Map zoom level.


Take special note of scale determined by Map zoom level. Results of object-based methods will vary when viewing or inspecting image layers in the Map, as each pyramid layer has a different scale. To force a desired scale of analysis in Map exploration, use `reproject()`. However, it is strongly recommended that you **NOT** use `reproject()` because the entire area visible in the Map will be requested at the set scale and projection. At large extents this can cause too much data to be requested, often triggering errors. Within the image pyramid-based architecture of Earth Engine, scale and projection need only be set for operations that provide `scale` and `crs` as parameters. See [Scale of Analysis](https://developers.google.com/earth-engine/scale#scale-of-analysis) and [Reprojecting](https://developers.google.com/earth-engine/projections#reprojecting) for more information. 
## Thermal hotspots
The following sections provide examples of object-based methods applied to Landsat 8 surface temperature with each section building on the former. Run the next snippet to generate the base image: thermal hotspots (> 303 degrees Kelvin) for a small region of San Francisco.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_objects#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_objects#colab-python-sample) More
```
// Make an area of interest geometry centered on San Francisco.
varpoint=ee.Geometry.Point(-122.1899,37.5010);
varaoi=point.buffer(10000);
// Import a Landsat 8 image, subset the thermal band, and clip to the
// area of interest.
varkelvin=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
.select(['B10'],['kelvin'])
.clip(aoi);
// Display the thermal band.
Map.centerObject(point,13);
Map.addLayer(kelvin,{min:288,max:305},'Kelvin');
// Threshold the thermal band to set hot pixels as value 1, mask all else.
varhotspots=kelvin.gt(303)
.selfMask()
.rename('hotspots');
// Display the thermal hotspots on the Map.
Map.addLayer(hotspots,{palette:'FF0000'},'Hotspots');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Make an area of interest geometry centered on San Francisco.
point = ee.Geometry.Point(-122.1899, 37.5010)
aoi = point.buffer(10000)
# Import a Landsat 8 image, subset the thermal band, and clip to the
# area of interest.
kelvin = (
  ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
  .select(['B10'], ['kelvin'])
  .clip(aoi)
)
# Threshold the thermal band to set hot pixels as value 1, mask all else.
hotspots = kelvin.gt(303).selfMask().rename('hotspots')
# Define a map centered on Redwood City, California.
map_objects = geemap.Map(center=[37.5010, -122.1899], zoom=13)
# Add the image layers to the map.
map_objects.add_layer(kelvin, {'min': 288, 'max': 305}, 'Kelvin')
map_objects.add_layer(hotspots, {'palette': 'FF0000'}, 'Hotspots')
```
![](https://developers.google.com/static/earth-engine/images/Images_object_hotspots.png) Figure 1. Temperature for a region of San Francisco. Pixels with temperature greater than 303 degrees Kelvin are distinguished by the color red (thermal hotspots). 
## Label objects
Labeling objects is often the first step in object analysis. Here, the `connectedComponents()` function is used to identify image objects and assign a unique ID to each; all pixels belonging to an object are assigned the same integer ID value. The result is a copy of the input image with an additional "labels" band associating pixels with an object ID value based on connectivity of pixels in the first band of the image.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_objects#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_objects#colab-python-sample) More
```
// Uniquely label the hotspot image objects.
varobjectId=hotspots.connectedComponents({
connectedness:ee.Kernel.plus(1),
maxSize:128
});
// Display the uniquely ID'ed objects to the Map.
Map.addLayer(objectId.randomVisualizer(),null,'Objects');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Uniquely label the hotspot image objects.
object_id = hotspots.connectedComponents(
  connectedness=ee.Kernel.plus(1), maxSize=128
)
# Add the uniquely ID'ed objects to the map.
map_objects.add_layer(object_id.randomVisualizer(), None, 'Objects')
```

Note that the maximum patch size is set to 128 pixels; objects composed of more pixels are masked. The connectivity is specified by an `ee.Kernel.plus(1)` kernel, which defines four-neighbor connectivity; use `ee.Kernel.square(1)` for eight-neighbor.
![](https://developers.google.com/static/earth-engine/images/Images_object_hotspots_label.png) Figure 2. Thermal hotspot objects labeled and styled by a unique ID. 
## Object size
### Number of pixels
Calculate the number of pixels composing objects using the `connectedPixelCount()` image method. Knowing the number of pixels in an object can be helpful for masking objects by size and calculating object area. The following snippet applies `connectedPixelCount()` to the "labels" band of the `objectId` image defined in the previous section.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_objects#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_objects#colab-python-sample) More
```
// Compute the number of pixels in each object defined by the "labels" band.
varobjectSize=objectId.select('labels')
.connectedPixelCount({
maxSize:128,eightConnected:false
});
// Display object pixel count to the Map.
Map.addLayer(objectSize,null,'Object n pixels');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Compute the number of pixels in each object defined by the "labels" band.
object_size = object_id.select('labels').connectedPixelCount(
  maxSize=128, eightConnected=False
)
# Add the object pixel count to the map.
map_objects.add_layer(object_size, None, 'Object n pixels')
```

`connectedPixelCount()` returns a copy of the input image where each pixel of each band contains the number of connected neighbors according to either the four- or eight-neighbor connectivity rule determined by a boolean argument passed to the `eightConnected` parameter. Note that connectivity is determined independently for each band of the input image. In this example, a single-band image (`objectId`) representing object ID was provided as input, so a single-band image was returned with a "labels" band (present as such in the input image), but now the values represent the number of pixels composing objects; every pixel of each object will have the same pixel count value.
![](https://developers.google.com/static/earth-engine/images/Images_object_hotspots_size.png) Figure 3. Thermal hotspot objects labeled and styled by size. 
### Area
Calculate object area by multiplying the area of a single pixel by the number of pixels composing an object (determined by `connectedPixelCount()`). Pixel area is provided by an image generated from `ee.Image.pixelArea()`.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_objects#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_objects#colab-python-sample) More
```
// Get a pixel area image.
varpixelArea=ee.Image.pixelArea();
// Multiply pixel area by the number of pixels in an object to calculate
// the object area. The result is an image where each pixel
// of an object relates the area of the object in m^2.
varobjectArea=objectSize.multiply(pixelArea);
// Display object area to the Map.
Map.addLayer(objectArea,
{min:0,max:30000,palette:['0000FF','FF00FF']},
'Object area m^2');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Get a pixel area image.
pixel_area = ee.Image.pixelArea()
# Multiply pixel area by the number of pixels in an object to calculate
# the object area. The result is an image where each pixel
# of an object relates the area of the object in m^2.
object_area = object_size.multiply(pixel_area)
# Add the object area to the map.
map_objects.add_layer(
  object_area,
  {'min': 0, 'max': 30000, 'palette': ['0000FF', 'FF00FF']},
  'Object area m^2',
)
```

The result is an image where each pixel of an object relates the area of the object in square meters. In this example, the `objectSize` image contains a single band, if it were multi-band, the multiplication operation would be applied to each band of the image.
## Filter objects by size
Object size can be used as a mask condition to focus your analysis on objects of a certain size (e.g., mask out objects that are too small). Here the `objectArea` image calculated in the previous step is used as a mask to remove objects whose area are less than one hectare.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_objects#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_objects#colab-python-sample) More
```
// Threshold the `objectArea` image to define a mask that will mask out
// objects below a given size (1 hectare in this case).
varareaMask=objectArea.gte(10000);
// Update the mask of the `objectId` layer defined previously using the
// minimum area mask just defined.
objectId=objectId.updateMask(areaMask);
Map.addLayer(objectId,null,'Large hotspots');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Threshold the `object_area` image to define a mask that will mask out
# objects below a given size (1 hectare in this case).
area_mask = object_area.gte(10000)
# Update the mask of the `object_id` layer defined previously using the
# minimum area mask just defined.
object_id = object_id.updateMask(area_mask)
map_objects.add_layer(object_id, None, 'Large hotspots')
```

The result is a copy of the `objectId` image where objects less than one hectare are masked out.
![](https://developers.google.com/static/earth-engine/images/Images_object_hotspots_before_mmu.png) | ![](https://developers.google.com/static/earth-engine/images/Images_object_hotspots_after_mmu.png)  
---|---  
Figure 4a. Thermal hotspot objects labeled and styled by unique ID. | Figure 4b. Thermal hotspot objects filtered by minimum area (1 hectare).  
## Zonal statistics
The `reduceConnectedComponents()` method applies a reducer to the pixels composing unique objects. The following snippet uses it to calculate the mean temperature of hotspot objects. `reduceConnectedComponents()` requires an input image with a band (or bands) to be reduced and a band that defines object labels. Here, the `objectID` "labels" image band is added to the `kelvin` temperature image to construct a suitable input image.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_objects#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_objects#colab-python-sample) More
```
// Make a suitable image for `reduceConnectedComponents()` by adding a label
// band to the `kelvin` temperature image.
kelvin=kelvin.addBands(objectId.select('labels'));
// Calculate the mean temperature per object defined by the previously added
// "labels" band.
varpatchTemp=kelvin.reduceConnectedComponents({
reducer:ee.Reducer.mean(),
labelBand:'labels'
});
// Display object mean temperature to the Map.
Map.addLayer(
patchTemp,
{min:303,max:304,palette:['yellow','red']},
'Mean temperature'
);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Make a suitable image for `reduceConnectedComponents()` by adding a label
# band to the `kelvin` temperature image.
kelvin = kelvin.addBands(object_id.select('labels'))
# Calculate the mean temperature per object defined by the previously added
# "labels" band.
patch_temp = kelvin.reduceConnectedComponents(
  reducer=ee.Reducer.mean(), labelBand='labels'
)
# Add object mean temperature to the map and display it.
map_objects.add_layer(
  patch_temp,
  {'min': 303, 'max': 304, 'palette': ['yellow', 'red']},
  'Mean temperature',
)
display(map_objects)
```

The result is a copy of the input image without the band used to define objects, where pixel values represent the result of the reduction per object, per band.
![](https://developers.google.com/static/earth-engine/images/Images_object_hotspots_temperature.png) Figure 5. Thermal hotspot object pixels summarized and styled by mean temperature. **Note:** `reduceToVectors()` provides similar functionality, except that the result is an `ee.FeatureCollection`, where each feature of the collection represents an object and the reduction of the pixels in each objects is expressed as a feature property for each band in the input image. `reduceToVectors()` is resource intensive, so use `reduceConnectedComponents()` whenever possible. See [Raster to Vector Conversion](https://developers.google.com/earth-engine/reducers_reduce_to_vectors) for more information.
