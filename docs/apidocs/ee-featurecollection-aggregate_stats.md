 
#  ee.FeatureCollection.aggregate_stats 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_stats#examples)


Aggregates over a given property of the objects in a collection, calculating the sum, min, max, mean, sample standard deviation, sample variance, total standard deviation and total variance of the selected property. 
Usage| Returns  
---|---  
`FeatureCollection.aggregate_stats(property)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to aggregate over.  
`property`| String| The property to use from each element of the collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_stats#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_stats#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('Power plant capacities (MW) summary stats',
fc.aggregate_stats('capacitymw'));
/**
 * Expected ee.Dictionary output
 *
 * {
 *  "max": 2910,
 *  "mean": 201.34242424242427,
 *  "min": 1.8,
 *  "sample_sd": 466.4808892319684,
 *  "sample_var": 217604.42001864797,
 *  "sum": 13288.600000000002,
 *  "sum_sq": 16819846.24,
 *  "total_count": 66,
 *  "total_sd": 462.9334545609107,
 *  "total_var": 214307.38335169878,
 *  "valid_count": 66,
 *  "weight_sum": 66,
 *  "weighted_sum": 13288.600000000002
 * }
 */
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
print('Power plant capacities (MW) summary stats:')
pprint(fc.aggregate_stats('capacitymw').getInfo())
# Expected ee.Dictionary output
# {
#  "max": 2910,
#  "mean": 201.34242424242427,
#  "min": 1.8,
#  "sample_sd": 466.4808892319684,
#  "sample_var": 217604.42001864797,
#  "sum": 13288.600000000002,
#  "sum_sq": 16819846.24,
#  "total_count": 66,
#  "total_sd": 462.9334545609107,
#  "total_var": 214307.38335169878,
#  "valid_count": 66,
#  "weight_sum": 66,
#  "weighted_sum": 13288.600000000002
# }
```

