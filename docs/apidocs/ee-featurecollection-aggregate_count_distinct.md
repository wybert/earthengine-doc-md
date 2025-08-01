 
#  ee.FeatureCollection.aggregate_count_distinct
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_count_distinct#examples)


Aggregates over a given property of the objects in a collection, calculating the number of distinct values for the selected property.
Usage | Returns  
---|---  
`FeatureCollection.aggregate_count_distinct(property)` | Number  
Argument | Type | Details  
---|---|---  
this: `collection` | FeatureCollection | The collection to aggregate over.  
`property` | String | The property to use from each element of the collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_count_distinct#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-aggregate_count_distinct#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');

print('Number of distinct power plant fuel sources',
fc.aggregate_count_distinct('fuel1'));// 7
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

print('Number of distinct power plant fuel sources:',
      fc.aggregate_count_distinct('fuel1').getInfo())  # 7
```

Was this helpful?
