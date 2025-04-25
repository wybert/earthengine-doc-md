 
#  ee.Dictionary.set 
Stay organized with collections  Save and categorize content based on your preferences. 
Set a value in a dictionary. Usage| Returns  
---|---  
`Dictionary.set(key, value)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`key`| String|   
`value`| Object|   
## Examples
### Code Editor (JavaScript)
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});
print('Set value for B3 key as -9999',dict.set('B3',-9999));
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
print('Set value for B3 key as -9999:', dic.set('B3', -9999).getInfo())
```

