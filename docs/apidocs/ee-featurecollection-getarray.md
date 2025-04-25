 
#  ee.FeatureCollection.getArray 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getarray#examples)


Extract a property from a feature. 
Usage| Returns  
---|---  
`FeatureCollection.getArray(property)`| Array  
Argument| Type| Details  
---|---|---  
this: `object`| Element| The feature to extract the property from.  
`property`| String| The property to extract.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getarray#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getarray#colab-python-sample) More
```
// A FeatureCollection with an array property value.
varfc=ee.FeatureCollection([]).set('array_property',ee.Array([1,2,3,4]));
// Fetch the array property value as an ee.Array object.
print('Array property value as ee.Array',fc.getArray('array_property'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A FeatureCollection with an array property value.
fc = ee.FeatureCollection([]).set('array_property', ee.Array([1, 2, 3, 4]))
# Fetch the array property value as an ee.Array object.
print('Array property value as ee.Array:',
   fc.getArray('array_property').getInfo())
```

Was this helpful?
