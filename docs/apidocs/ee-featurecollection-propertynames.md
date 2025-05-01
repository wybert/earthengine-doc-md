 
#  ee.FeatureCollection.propertyNames 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-propertynames#examples)


Returns the names of properties on this element. 
Usage| Returns  
---|---  
`FeatureCollection.propertyNames()`| List  
Argument| Type| Details  
---|---|---  
this: `element`| Element|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-propertynames#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-propertynames#colab-python-sample) More
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
```
# A global power plant FeatureCollection.
fc = ee.FeatureCollection('WRI/GPPD/power_plants')
# View a list of FeatureCollection property names.
print(fc.propertyNames().getInfo())
```

