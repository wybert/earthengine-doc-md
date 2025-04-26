 
#  ee.FeatureCollection.toDictionary 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-todictionary#examples)


Extract properties from a feature as a dictionary. 
Usage| Returns  
---|---  
`FeatureCollection.toDictionary( _properties_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `element`| Element| The feature to extract the property from.  
`properties`| List, default: null| The list of properties to extract. Defaults to all non-system properties.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-todictionary#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-todictionary#colab-python-sample) More
```
// FeatureCollection of power plants.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants');
print('All non-system FeatureCollection properties as an ee.Dictionary',
fc.toDictionary());
print('Selected properties as an ee.Dictionary',
fc.toDictionary(['description','provider']));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants.
fc = ee.FeatureCollection('WRI/GPPD/power_plants')
print('All non-system FeatureCollection properties as an ee.Dictionary:',
   fc.toDictionary().getInfo())
print('Selected properties as an ee.Dictionary:',
   fc.toDictionary(['description', 'provider']).getInfo())
```

