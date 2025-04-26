 
#  ee.Dictionary.get 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-get#examples)


Extracts a named value from a dictionary. If the dictionary does not contain the given key, then defaultValue is returned, unless it is null. 
Usage| Returns  
---|---  
`Dictionary.get(key,  _defaultValue_)`| Object  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`key`| String|   
`defaultValue`| Object, default: null|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-get#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-get#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
print('Value for "B1" key',dict.get('B1'));
// Set a default value for the case where the key does not exist.
print('Value for nonexistent "Band_1" key',
dict.get({key:'Band_1',defaultValue:-9999}));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
dic = ee.Dictionary({
  'B1': 182,
  'B2': 219,
  'B3': 443
})
print('Value for "B1" key:', dic.get('B1').getInfo())
# Set a default value for the case where the key does not exist.
print('Value for nonexistent "Band_1" key:',
   dic.get(**{'key': 'Band_1', 'defaultValue': -9999}).getInfo())
```

Was this helpful?
