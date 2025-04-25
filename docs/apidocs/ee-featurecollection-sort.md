 
#  ee.FeatureCollection.sort 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-sort#examples)


Sort a collection by the specified property. 
Returns the sorted collection.
Usage| Returns  
---|---  
`FeatureCollection.sort(property,  _ascending_)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`property`| String| The property to sort by.  
`ascending`| Boolean, optional| Whether to sort in ascending or descending order. The default is true (ascending).  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-sort#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-sort#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('Belgium power plants in ascending order by capacity',
fc.sort('capacitymw'));
print('Belgium power plants in descending order by capacity',
fc.sort('capacitymw',false));
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
print('Belgium power plants in ascending order by capacity:',
   fc.sort('capacitymw').getInfo())
print('Belgium power plants in descending order by capacity:',
   fc.sort('capacitymw', False).getInfo())
```

