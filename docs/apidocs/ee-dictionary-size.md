 
#  ee.Dictionary.size
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the number of entries in a dictionary. Usage| Returns  
---|---  
`Dictionary.size()`| Integer  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
## Examples
### Code Editor (JavaScript)
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
print('The number of dictionary entries',dict.size());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
dic = ee.Dictionary({
  'B1': 182,
  'B2': 219,
  'B3': 443
})
print('The number of dictionary entries:', dic.size().getInfo())
```

