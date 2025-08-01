 
#  ee.Dictionary.getNumber
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getnumber#examples)


Extracts a named number value from a dictionary.
Usage | Returns  
---|---  
`Dictionary.getNumber(key)` | Number  
Argument | Type | Details  
---|---|---  
this: `dictionary` | Dictionary |   
`key` | String |   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getnumber#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-getnumber#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});

print('The "B1" value as an ee.Number object',dict.getNumber('B1'));
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

print('The "B1" value as an ee.Number object:', dic.getNumber('B1').getInfo())
```

