 
#  ee.FeatureCollection.set 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-set#examples)


Overrides one or more metadata properties of an Element. 
Returns the element with the specified properties overridden.
Usage| Returns  
---|---  
`FeatureCollection.set(var_args)`| Element  
Argument| Type| Details  
---|---|---  
this: `element`| Element| The Element instance.  
`var_args`| VarArgs| Either a dictionary of properties, or a vararg sequence of properties, e.g. key1, value1, key2, value2, ...  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-set#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-set#colab-python-sample) More
```
// An empty FeatureCollection for simple demonstration.
varfc=ee.FeatureCollection([]);
// Set a single new property using a key-value pair.
fc=fc.set('key_1','value 1');
// Set multiple new properties using a series of key-value pairs.
fc=fc.set('key_2','value 2',
'key_3',3);
// Set new properties using a dictionary of key-value pairs.
fc=fc.set({
key_5:ee.Array([1,2,3]),
key_6:ee.Image(0),
key_7:ee.Feature(null)
});
print('New FeatureCollection properties added',fc);
// Overwrite an existing property.
fc=fc.set('key_1','overwritten');
print('FeatureCollection property overwritten',fc);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
frompprintimport pprint
# An empty FeatureCollection for simple demonstration.
fc = ee.FeatureCollection([])
# Set a single new property using a key-value pair.
fc = fc.set('key_1', 'value 1')
# Set multiple new properties using a series of key-value pairs.
fc = fc.set('key_2', 'value 2', 'key_3', 3)
# Set new properties using a dictionary of key-value pairs.
fc = fc.set({
 'key_5': ee.Array([1, 2, 3]),
 'key_6': ee.Image(0),
 'key_7': ee.Feature(None)
})
print('New FeatureCollection properties added:')
pprint(fc.getInfo())
# Overwrite an existing property.
fc = fc.set('key_1', 'overwritten')
print('FeatureCollection property overwritten:')
pprint(fc.getInfo())
```

Was this helpful?
