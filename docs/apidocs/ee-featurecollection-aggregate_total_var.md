 
#  ee.FeatureCollection.aggregate_total_var
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_total_var#examples)


Aggregates over a given property of the objects in a collection, calculating the total variance of the values of the selected property.
Usage | Returns  
---|---  
`FeatureCollection.aggregate_total_var(property)` | Number  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The collection to aggregate over.  
`property` | String | The property to use from each element of the collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_total_var#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_total_var#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');

print('Total variance of power plant capacities (MW)',
fc.aggregate_total_var('capacitymw'));// 214307.38335169878
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
    'country_lg == "Belgium"')

print('Total variance of power plant capacities (MW):',
      fc.aggregate_total_var('capacitymw').getInfo())  # 214307.38335169878
```

Was this helpful?
