 
#  ee.Dictionary.getGeometry 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getgeometry#examples)


Extracts a named geometry value from a dictionary. 
Usage| Returns  
---|---  
`Dictionary.getGeometry(key)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`key`| String|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getgeometry#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getgeometry#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443,
Geometry:ee.Geometry.Point([-122.01,36.97])
});
print('The "Geometry" value as an ee.Geometry object',
dict.getGeometry('Geometry'));
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
  'Geometry': ee.Geometry.Point([-122.01, 36.97])
})
print('The "Geometry" value as an ee.Geometry object',
   dic.getGeometry('Geometry').getInfo(), sep='\n')
```

Was this helpful?
