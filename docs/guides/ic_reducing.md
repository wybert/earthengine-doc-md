 
#  Reducing an ImageCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Composites have no projection](https://developers.google.com/earth-engine/guides/ic_reducing#composites-have-no-projection)


To composite images in an `ImageCollection`, use `imageCollection.reduce()`. This will composite all the images in the collection to a single image representing, for example, the min, max, mean or standard deviation of the images. (See the [Reducers section](https://developers.google.com/earth-engine/guides/reducers_image_collection) for more information about reducers). For example, to create a median value image from a collection:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_reducing#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_reducing#colab-python-sample) More
```
// Load a Landsat 8 collection for a single path-row.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filter(ee.Filter.eq('WRS_PATH',44))
.filter(ee.Filter.eq('WRS_ROW',34))
.filterDate('2014-01-01','2015-01-01');
// Compute a median image and display.
varmedian=collection.median();
Map.setCenter(-122.3578,37.7726,12);
Map.addLayer(median,{bands:['B4','B3','B2'],max:0.3},'Median');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 collection for a single path-row.
collection = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filter(ee.Filter.eq('WRS_PATH', 44))
  .filter(ee.Filter.eq('WRS_ROW', 34))
  .filterDate('2014-01-01', '2015-01-01')
)
# Compute a median image and display.
median = collection.median()
m = geemap.Map()
m.set_center(-122.3578, 37.7726, 12)
m.add_layer(median, {'bands': ['B4', 'B3', 'B2'], 'max': 0.3}, 'Median')
m
```

At each location in the output image, in each band, the pixel value is the median of all unmasked pixels in the input imagery (the images in the collection). In the previous example, `median()` is a convenience method for the following call:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_reducing#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_reducing#colab-python-sample) More
```
// Reduce the collection with a median reducer.
varmedian=collection.reduce(ee.Reducer.median());
// Display the median image.
Map.addLayer(median,
{bands:['B4_median','B3_median','B2_median'],max:0.3},
'Also median');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Reduce the collection with a median reducer.
median = collection.reduce(ee.Reducer.median())
# Display the median image.
m.add_layer(
  median,
  {'bands': ['B4_median', 'B3_median', 'B2_median'], 'max': 0.3},
  'Also median',
)
m
```

Note that the band names differ as a result of using `reduce()` instead of the convenience method. Specifically, the names of the reducer have been appended to the band names.
More complex reductions are also possible using `reduce()`. For example, to compute the long term linear trend over a collection, use one of the linear regression reducers. The following code computes the linear trend of MODIS Enhanced Vegetation Index (EVI):
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_reducing#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_reducing#colab-python-sample) More
```
// This function adds a band representing the image timestamp.
varaddTime=function(image){
returnimage.addBands(image.metadata('system:time_start')
// Convert milliseconds from epoch to years to aid in
// interpretation of the following trend calculation.
.divide(1000*60*60*24*365));
};
// Load a MODIS collection, filter to several years of 16 day mosaics,
// and map the time band function over it.
varcollection=ee.ImageCollection('MODIS/006/MYD13A1')
.filterDate('2004-01-01','2010-10-31')
.map(addTime);
// Select the bands to model with the independent variable first.
vartrend=collection.select(['system:time_start','EVI'])
// Compute the linear trend over time.
.reduce(ee.Reducer.linearFit());
// Display the trend with increasing slopes in green, decreasing in red.
Map.setCenter(-96.943,39.436,5);
Map.addLayer(
trend,
{min:0,max:[-100,100,10000],bands:['scale','scale','offset']},
'EVI trend');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# This function adds a band representing the image timestamp.
defadd_time(image):
 return image.addBands(
   image.metadata('system:time_start')
   # Convert milliseconds from epoch to years to aid in
   # interpretation of the following trend calculation.
   .divide(1000 * 60 * 60 * 24 * 365)
 )

# Load a MODIS collection, filter to several years of 16 day mosaics,
# and map the time band function over it.
collection = (
  ee.ImageCollection('MODIS/006/MYD13A1')
  .filterDate('2004-01-01', '2010-10-31')
  .map(add_time)
)
# Select the bands to model with the independent variable first.
trend = collection.select(['system:time_start', 'EVI']).reduce(
  # Compute the linear trend over time.
  ee.Reducer.linearFit()
)
# Display the trend with increasing slopes in green, decreasing in red.
m.set_center(-96.943, 39.436, 5)
m = geemap.Map()
m.add_layer(
  trend,
  {
    'min': 0,
    'max': [-100, 100, 10000],
    'bands': ['scale', 'scale', 'offset'],
  },
  'EVI trend',
)
m
```

Note that the output of the reduction in this example is a two banded image with one band for the slope of a linear regression (`scale`) and one band for the intercept (`offset`). Explore the API documentation to see a list of the reducers that are available to reduce an `ImageCollection` to a single `Image`.
## Composites have no projection
Composite images created by reducing an image collection are able to produce pixels in any requested projection and therefore _have no fixed output projection_. Instead, composites have [the default projection](https://developers.google.com/earth-engine/guides/projections#the-default-projection) of WGS-84 with 1-degree resolution pixels. Composites with the default projection will be computed in whatever output projection is requested. A request occurs by displaying the composite in the Code Editor (learn about how the Code editor sets [scale](https://developers.google.com/earth-engine/guides/scale#scale-of-analysis) and [projection](https://developers.google.com/earth-engine/guides/projections)), or by explicitly specifying a projection/scale as in an aggregation such as `ReduceRegion` or `Export`.
