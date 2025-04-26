 
#  ee.Dictionary.combine 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-combine#examples)


Combines two dictionaries. In the case of duplicate names, the output will contain the value of the second dictionary unless overwrite is false. Null values in both dictionaries are ignored / removed. 
Usage| Returns  
---|---  
`Dictionary.combine(second,  _overwrite_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `first`| Dictionary|   
`second`| Dictionary|   
`overwrite`| Boolean, default: true|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-combine#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-combine#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict1=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
// A second dictionary.
vardict2=ee.Dictionary({
Region:'The Forest of Nisene Marks State Park',
Image:'Sentinel-2 surface reflectance (scaled by 1e4)',
B1:-9999// Note that the B1 key is present in both dictionaries.
});
print('Combined dictionaries (overwrite false)',
dict1.combine(dict2,false));
print('Combined dictionaries (overwrite true)',
dict1.combine(dict2,true));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importpprint
# A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
dic_1 = ee.Dictionary({
  'B1': 182,
  'B2': 219,
  'B3': 443
})
# A second dictionary.
dic_2 = ee.Dictionary({
  'Region': 'The Forest of Nisene Marks State Park',
  'Image': 'Sentinel-2 surface reflectance (scaled by 1e4)',
  'B1': -9999 # Note that the B1 key is present in both dictionaries.
})
print('Combined dictionaries (overwrite false)')
pprint.pprint(dic_1.combine(dic_2, False).getInfo())
print('\nCombined dictionaries (overwrite true)')
pprint.pprint(dic_1.combine(dic_2, True).getInfo())
```

Was this helpful?
