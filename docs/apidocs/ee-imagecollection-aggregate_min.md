 
#  ee.ImageCollection.aggregate_min 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-aggregate_min#examples)


Aggregates over a given property of the objects in a collection, calculating the minimum of the values of the selected property. 
Usage| Returns  
---|---  
`ImageCollection.aggregate_min(property)`|   
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to aggregate over.  
`property`| String| The property to use from each element of the collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-aggregate_min#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-aggregate_min#colab-python-sample) More
```
// A Lansat 8 TOA image collection for a specific year and location.
varcol=ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")
.filterBounds(ee.Geometry.Point([-122.073,37.188]))
.filterDate('2018','2019');
// An image property of interest, percent cloud cover in this case.
varprop='CLOUD_COVER';
// Use ee.ImageCollection.aggregate_* functions to fetch information about
// values of a selected property across all images in the collection. For
// example, produce a list of all values, get counts, and calculate statistics.
print('List of property values',col.aggregate_array(prop));
print('Count of property values',col.aggregate_count(prop));
print('Count of distinct property values',col.aggregate_count_distinct(prop));
print('First collection element property value',col.aggregate_first(prop));
print('Histogram of property values',col.aggregate_histogram(prop));
print('Min of property values',col.aggregate_min(prop));
print('Max of property values',col.aggregate_max(prop));
// The following methods are applicable to numerical properties only.
print('Mean of property values',col.aggregate_mean(prop));
print('Sum of property values',col.aggregate_sum(prop));
print('Product of property values',col.aggregate_product(prop));
print('Std dev (sample) of property values',col.aggregate_sample_sd(prop));
print('Variance (sample) of property values',col.aggregate_sample_var(prop));
print('Std dev (total) of property values',col.aggregate_total_sd(prop));
print('Variance (total) of property values',col.aggregate_total_var(prop));
print('Summary stats of property values',col.aggregate_stats(prop));
// Note that if the property is formatted as a string, min and max will
// respectively return the first and last values according to alphanumeric
// order of the property values.
varpropString='LANDSAT_SCENE_ID';
print('List of property values (string)',col.aggregate_array(propString));
print('Min of property values (string)',col.aggregate_min(propString));
print('Max of property values (string)',col.aggregate_max(propString));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
# A Lansat 8 TOA image collection for a specific year and location.
col = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA").filterBounds(
  ee.Geometry.Point([-122.073, 37.188])).filterDate('2018', '2019')
# An image property of interest, percent cloud cover in this case.
prop = 'CLOUD_COVER'
# Use ee.ImageCollection.aggregate_* functions to fetch information about
# values of a selected property across all images in the collection. For
# example, produce a list of all values, get counts, and calculate statistics.
print('List of property values:', col.aggregate_array(prop).getInfo())
print('Count of property values:', col.aggregate_count(prop).getInfo())
print('Count of distinct property values:',
   col.aggregate_count_distinct(prop).getInfo())
print('First collection element property value:',
   col.aggregate_first(prop).getInfo())
print('Histogram of property values:')
pprint(col.aggregate_histogram(prop).getInfo())
print('Min of property values:', col.aggregate_min(prop).getInfo())
print('Max of property values:', col.aggregate_max(prop).getInfo())
# The following methods are applicable to numerical properties only.
print('Mean of property values:', col.aggregate_mean(prop).getInfo())
print('Sum of property values:', col.aggregate_sum(prop).getInfo())
print('Product of property values:', col.aggregate_product(prop).getInfo())
print('Std dev (sample) of property values:',
   col.aggregate_sample_sd(prop).getInfo())
print('Variance (sample) of property values:',
   col.aggregate_sample_var(prop).getInfo())
print('Std dev (total) of property values:',
   col.aggregate_total_sd(prop).getInfo())
print('Variance (total) of property values:',
   col.aggregate_total_var(prop).getInfo())
print('Summary stats of property values:')
pprint(col.aggregate_stats(prop).getInfo())
# Note that if the property is formatted as a string, min and max will
# respectively return the first and last values according to alphanumeric
# order of the property values.
prop_string = 'LANDSAT_SCENE_ID'
print('List of property values (string):',
   col.aggregate_array(prop_string).getInfo())
print('Min of property values (string):',
   col.aggregate_min(prop_string).getInfo())
print('Max of property values (string):',
   col.aggregate_max(prop_string).getInfo())
```

