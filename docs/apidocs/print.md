 
#  print 
Stay organized with collections  Save and categorize content based on your preferences. 
Prints the arguments to the console. Usage| Returns  
---|---  
`print(var_args)`|   
Argument| Type| Details  
---|---|---  
`var_args`| VarArgs| The objects to print.  
## Examples
### Code Editor (JavaScript)
```
print(1);// 1
print(ee.Number(1));// 1
print(ee.Array([1]));// [1]
print(ee.ImageCollection('AAFC/ACI').size());// 10
print(ee.Image('AAFC/ACI/2009'));// Image AAFC/ACI/2009 (1 band)
print(ee.FeatureCollection("NOAA/NHC/HURDAT2/pacific").size());// 28547
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
"""There is no dedicated print function for the Earth Engine Python API.
To print Earth Engine objects, use Python's built-in `print` function.
Printing an Earth Engine object in Python prints the serialized request for the
object, not the object itself, so you must call `getInfo()` on Earth Engine
objects to get the desired object from the server to the client. For example,
`print(ee.Number(1).getInfo())`. Note that `getInfo()` is a synchronous
operation. Alternatively, the eerepr library provides rich Earth Engine object
representation; it is included in the geemap library.
"""
print(1) # 1
print(ee.Number(1).getInfo()) # 1
print(ee.Array([1]).getInfo()) # [1]
print(ee.ImageCollection('AAFC/ACI').size().getInfo()) # 10
print(ee.Image('AAFC/ACI/2009').getInfo()) # Image AAFC/ACI/2009 (1 band)
print(
  ee.FeatureCollection("NOAA/NHC/HURDAT2/pacific").size().getInfo()
) # 28547
```

