 
#  Filtering an ImageCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
As illustrated in the [Get Started section](https://developers.google.com/earth-engine/guides/getstarted) and the [ImageCollection Information section](https://developers.google.com/earth-engine/guides/ic_info), Earth Engine provides a variety of convenience methods for filtering image collections. Specifically, many common use cases are handled by `imageCollection.filterDate()`, and `imageCollection.filterBounds()`. For general purpose filtering, use `imageCollection.filter()` with an `ee.Filter` as an argument. The following example demonstrates both convenience methods and `filter()` to identify and remove images with high cloud cover from an `ImageCollection`.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_filtering#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_filtering#colab-python-sample) More
```
// Load Landsat 8 data, filter by date, month, and bounds.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterDate('2015-01-01','2018-01-01')// Three years of data
.filter(ee.Filter.calendarRange(11,2,'month'))// Only Nov-Feb observations
.filterBounds(ee.Geometry.Point(25.8544,-18.08874));// Intersecting ROI
// Also filter the collection by the CLOUD_COVER property.
varfiltered=collection.filter(ee.Filter.eq('CLOUD_COVER',0));
// Create two composites to check the effect of filtering by CLOUD_COVER.
varbadComposite=collection.mean();
vargoodComposite=filtered.mean();
// Display the composites.
Map.setCenter(25.8544,-18.08874,13);
Map.addLayer(badComposite,
{bands:['B3','B2','B1'],min:0.05,max:0.35,gamma:1.1},
'Bad composite');
Map.addLayer(goodComposite,
{bands:['B3','B2','B1'],min:0.05,max:0.35,gamma:1.1},
'Good composite');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load Landsat 8 data, filter by date, month, and bounds.
collection = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  # Three years of data
  .filterDate('2015-01-01', '2018-01-01')
  # Only Nov-Feb observations
  .filter(ee.Filter.calendarRange(11, 2, 'month'))
  # Intersecting ROI
  .filterBounds(ee.Geometry.Point(25.8544, -18.08874))
)
# Also filter the collection by the CLOUD_COVER property.
filtered = collection.filter(ee.Filter.eq('CLOUD_COVER', 0))
# Create two composites to check the effect of filtering by CLOUD_COVER.
bad_composite = collection.mean()
good_composite = filtered.mean()
# Display the composites.
m = geemap.Map()
m.set_center(25.8544, -18.08874, 13)
m.add_layer(
  bad_composite,
  {'bands': ['B3', 'B2', 'B1'], 'min': 0.05, 'max': 0.35, 'gamma': 1.1},
  'Bad composite',
)
m.add_layer(
  good_composite,
  {'bands': ['B3', 'B2', 'B1'], 'min': 0.05, 'max': 0.35, 'gamma': 1.1},
  'Good composite',
)
m
```

Was this helpful?
