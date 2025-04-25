 
#  ee.FeatureCollection.propertyNames 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the names of properties on this element. Usage| Returns  
---|---  
`FeatureCollection.propertyNames()`| List  
Argument| Type| Details  
---|---|---  
this: `element`| Element|   
## Examples
### Code Editor (JavaScript)
```
// A global power plant FeatureCollection.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants');
// View a list of FeatureCollection property names.
print(fc.propertyNames());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A global power plant FeatureCollection.
fc = ee.FeatureCollection('WRI/GPPD/power_plants')
# View a list of FeatureCollection property names.
print(fc.propertyNames().getInfo())
```

