 
#  ee.Dictionary.getGeometry 
Stay organized with collections  Save and categorize content based on your preferences. 
Extracts a named geometry value from a dictionary. Usage| Returns  
---|---  
`Dictionary.getGeometry(key)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `dictionary`| Dictionary|   
`key`| String|   
## Examples
### Code Editor (JavaScript)
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

### Colab (Python)
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

