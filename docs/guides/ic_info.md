 
#  ImageCollection Information and Metadata
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
As with Images, there are a variety of ways to get information about an `ImageCollection`. The collection can be printed directly to the console, but the console printout is limited to 5000 elements. Collections larger than 5000 images will need to be filtered before printing. Printing a large collection will be correspondingly slower. The following example shows various ways of getting information about image collections programmatically:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_info#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_info#colab-python-sample) More
```
// Load a Landsat 8 ImageCollection for a single path-row.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filter(ee.Filter.eq('WRS_PATH',44))
.filter(ee.Filter.eq('WRS_ROW',34))
.filterDate('2014-03-01','2014-08-01');
print('Collection: ',collection);
// Get the number of images.
varcount=collection.size();
print('Count: ',count);
// Get the date range of images in the collection.
varrange=collection.reduceColumns(ee.Reducer.minMax(),['system:time_start'])
print('Date range: ',ee.Date(range.get('min')),ee.Date(range.get('max')))
// Get statistics for a property of the images in the collection.
varsunStats=collection.aggregate_stats('SUN_ELEVATION');
print('Sun elevation statistics: ',sunStats);
// Sort by a cloud cover property, get the least cloudy image.
varimage=ee.Image(collection.sort('CLOUD_COVER').first());
print('Least cloudy image: ',image);
// Limit the collection to the 10 most recent images.
varrecent=collection.sort('system:time_start',false).limit(10);
print('Recent images: ',recent);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 ImageCollection for a single path-row.
collection = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filter(ee.Filter.eq('WRS_PATH', 44))
  .filter(ee.Filter.eq('WRS_ROW', 34))
  .filterDate('2014-03-01', '2014-08-01')
)
display('Collection:', collection)
# Get the number of images.
count = collection.size()
display('Count:', count)
# Get the date range of images in the collection.
range = collection.reduceColumns(ee.Reducer.minMax(), ['system:time_start'])
display('Date range:', ee.Date(range.get('min')), ee.Date(range.get('max')))
# Get statistics for a property of the images in the collection.
sun_stats = collection.aggregate_stats('SUN_ELEVATION')
display('Sun elevation statistics:', sun_stats)
# Sort by a cloud cover property, get the least cloudy image.
image = ee.Image(collection.sort('CLOUD_COVER').first())
display('Least cloudy image:', image)
# Limit the collection to the 10 most recent images.
recent = collection.sort('system:time_start', False).limit(10)
display('Recent images:', recent)
```

