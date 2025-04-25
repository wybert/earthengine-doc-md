 
#  ee.Dictionary.contains 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-contains#examples)


Returns true if the dictionary contains the given key. 
Usage| Returns  
---|---  
`Dictionary.contains(key)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`key`| String|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-contains#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-contains#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
print('Dictionary contains key "B1"?',dict.contains('B1'));
print('Dictionary contains key "Band_1"?',dict.contains('Band_1'));
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
print('Dictionary contains key "B1"?:', dic.contains('B1').getInfo())
print('Dictionary contains key "Band_1"?:', dic.contains('Band_1').getInfo())
```

Was this helpful?
