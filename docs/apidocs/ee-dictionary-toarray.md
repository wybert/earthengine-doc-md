 
#  ee.Dictionary.toArray 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-toarray#examples)


Returns numeric values of a dictionary as an array. If no keys are specified, all values are returned in the natural ordering of the dictionary's keys. The default 'axis' is 0. 
Usage| Returns  
---|---  
`Dictionary.toArray( _keys_, _axis_)`| Array  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`keys`| List, default: null|   
`axis`| Integer, default: 0|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-toarray#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-toarray#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
print('Values for selected keys converted to ee.Array',
dict.toArray(['B1','B2']));
print('Values for all keys converted to ee.Array',
dict.toArray());
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
print('Values for selected keys converted to ee.Array:',
   dic.toArray(['B1', 'B2']).getInfo())
print('Values for all keys converted to ee.Array:',
   dic.toArray().getInfo())
```

