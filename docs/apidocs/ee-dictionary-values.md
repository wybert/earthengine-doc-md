 
#  ee.Dictionary.values
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-values#examples)


Returns the values of a dictionary as a list. If no keys are specified, all values are returned in the natural ordering of the dictionary's keys. 
Usage| Returns  
---|---  
`Dictionary.values( _keys_)`| List  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`keys`| List, default: null|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-values#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-values#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
print('Values for selected keys converted to ee.List',
dict.values(['B1','B2']));
print('Values for all keys converted to ee.List',dict.values());
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
print('Values for selected keys converted to ee.List:',
   dic.values(['B1', 'B2']).getInfo())
print('Values for all keys converted to ee.List:', dic.values().getInfo())
```

