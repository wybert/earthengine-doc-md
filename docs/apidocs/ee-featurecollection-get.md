 
#  ee.FeatureCollection.get 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-get#examples)


Extract a property from a feature. 
Usage| Returns  
---|---  
`FeatureCollection.get(property)`|   
Argument| Type| Details  
---|---|---  
this: `object`| Element| The feature to extract the property from.  
`property`| String| The property to extract.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-get#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-get#colab-python-sample) More
```
// A global power plant FeatureCollection.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants');
// View a list of FeatureCollection property names.
print(fc.propertyNames());
// Get the value of a listed property.
print('Global power plant data provider as ee.ComputedObject',
fc.get('provider'));
// The returned value is an ee.ComputedObject which has no methods available for
// further processing; cast to the relevant Earth Engine object class for use.
print('Global power plant data provider as ee.String',
ee.String(fc.get('provider')));
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
# Get the value of a listed property.
print('Global power plant data provider as ee.ComputedObject:',
   fc.get('provider').getInfo())
# The returned value is an ee.ComputedObject which has no methods available for
# further processing; cast to the relevant Earth Engine object class for use.
print('Global power plant data provider as ee.String:',
   ee.String(fc.get('provider')).getInfo())
```

