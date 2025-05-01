 
#  ee.FeatureCollection.size 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the number of elements in the collection. 
Usage| Returns  
---|---  
`FeatureCollection.size()`| Integer  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to count.  
## Examples
### Code Editor (JavaScript)
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('Number of power plants in Belgium',fc.size());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"')
print('Number of power plants in Belgium:', fc.size().getInfo())
```

