 
#  ee.Dictionary.getString 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getstring#examples)


Extracts a named string value from a dictionary. 
Usage| Returns  
---|---  
`Dictionary.getString(key)`| String  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`key`| String|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getstring#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getstring#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443,
Region:'The Forest of Nisene Marks State Park'
});
print('The "Region" value as an ee.String object',dict.getString('Region'));
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
  'B3': 443,
  'Region': 'The Forest of Nisene Marks State Park'
})
print('The "Region" value as an ee.String object:',
   dic.getString('Region').getInfo(), sep='\n')
```

Was this helpful?
