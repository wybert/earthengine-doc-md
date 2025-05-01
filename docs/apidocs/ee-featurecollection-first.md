 
#  ee.FeatureCollection.first 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the first entry from a given collection. Usage| Returns  
---|---  
`FeatureCollection.first()`| Element  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection from which to select the first entry.  
## Examples
### Code Editor (JavaScript)
```
// A global power plant FeatureCollection.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants');
print('The first feature (power plant) in the collection',fc.first());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
frompprintimport pprint
# A global power plant FeatureCollection.
fc = ee.FeatureCollection('WRI/GPPD/power_plants')
print('The first feature (power plant) in the collection:')
pprint(fc.first().getInfo())
```

