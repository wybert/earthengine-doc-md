 
#  ee.FeatureCollection.toList 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the elements of a collection as a list. Usage| Returns  
---|---  
`FeatureCollection.toList(count,  _offset_)`| List  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection to fetch.  
`count`| Integer| The maximum number of elements to fetch.  
`offset`| Integer, default: 0| The number of elements to discard from the start. If set, (offset + count) elements will be fetched and the first offset elements will be discarded.  
## Examples
### Code Editor (JavaScript)
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
print('First 5 features to an ee.List',fc.toList(5));
print('Second 5 features to an ee.List',fc.toList(5,5));
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
print('First 5 features to an ee.List:', fc.toList(5).getInfo())
print('Second 5 features to an ee.List:', fc.toList(5, 5).getInfo())
```

