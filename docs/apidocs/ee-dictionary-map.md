 
#  ee.Dictionary.map 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-map#examples)


Map an algorithm over a dictionary. The algorithm is expected to take 2 arguments, a key from the existing dictionary and the value it corresponds to, and return a new value for the given key. If the algorithm returns null, the key is dropped. 
Usage| Returns  
---|---  
`Dictionary.map(baseAlgorithm)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary  
`baseAlgorithm`| Algorithm  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-map#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-map#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
/**
 * Convert S2 surface reflectance units to native scale.
 */
functionscale(key,value){
returnee.Number(value).divide(1e4);
}
print('S2 surface reflectance in native units',dict.map(scale));
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

defscale(key, value):
"""Convert S2 surface reflectance units to native scale."""
 return ee.Number(value).divide(1e4)
print('S2 surface reflectance in native units:', dic.map(scale).getInfo())
```

Was this helpful?
