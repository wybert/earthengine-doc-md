 
#  ee.PixelType 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a PixelType of the given precision with the given limits per element, and an optional dimensionality. Usage| Returns  
---|---  
`ee.PixelType(precision,  _minValue_, _maxValue_, _dimensions_)`| PixelType  
Argument| Type| Details  
---|---|---  
`precision`| Object| The pixel precision, one of 'int', 'float', or 'double'.  
`minValue`| Number, default: null| The minimum value of pixels of this type. If precision is 'float' or 'double', this can be null, signifying negative infinity.  
`maxValue`| Number, default: null| The maximum value of pixels of this type. If precision is 'float' or 'double', this can be null, signifying positive infinity.  
`dimensions`| Integer, default: 0| The number of dimensions in which pixels of this type can vary; 0 is a scalar, 1 is a vector, 2 is a matrix, etc.  
## Examples
### Code Editor (JavaScript)
```
print(ee.PixelType('int',0,1));// int ∈ [0, 1]
print(ee.PixelType('int',-20,-10));// int ∈ [-20, -10]
print(ee.PixelType('float'));// float
print(ee.PixelType('double'));// double
print(ee.PixelType('double',null));// double
print(ee.PixelType('double',null,null));// double
print(ee.PixelType('double',null,null,0));// double
print(ee.PixelType('double',null,null,1));// double, 1 dimensions
print(ee.PixelType('double',null,null,2));// double, 2 dimensions
print(ee.PixelType('double',null,null,3));// double, 3 dimensions
print(ee.PixelType('double',null,null,10));// double, 10 dimensions
print(ee.PixelType('double',null,null,1e8));// double, 100000000 dimensions
print(ee.PixelType('double',1,2,0));// double ∈ [1, 2]
print(ee.PixelType('double',1,3,2));// double ∈ [1, 3], 2 dimensions
print(ee.PixelType('double',-4,-3,0));// double ∈ [-4, -3]
print(ee.PixelType('double',null,2.3,0));// double
print(ee.PixelType('double',3.4,null,0));// double
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.PixelType('int', 0, 1).getInfo()) # int ∈ [0, 1]
print(ee.PixelType('int', -20, -10).getInfo()) # int ∈ [-20, -10]
print(ee.PixelType('float').getInfo()) # float
print(ee.PixelType('double').getInfo()) # double
print(ee.PixelType('double', None).getInfo()) # double
print(ee.PixelType('double', None, None).getInfo()) # double
print(ee.PixelType('double', None, None, 0).getInfo()) # double
print(ee.PixelType('double', None, None, 1).getInfo()) # double, 1 dimensions
print(ee.PixelType('double', None, None, 2).getInfo()) # double, 2 dimensions
print(ee.PixelType('double', None, None, 3).getInfo()) # double, 3 dimensions
print(ee.PixelType('double', None, None, 10).getInfo()) # double, 10 dimensions
# double, 100000000 dimensions
print(ee.PixelType('double', None, None, 1e8).getInfo())
print(ee.PixelType('double', 1, 2, 0).getInfo()) # double ∈ [1, 2]
# double ∈ [1, 3], 2 dimensions
print(ee.PixelType('double', 1, 3, 2).getInfo())
print(ee.PixelType('double', -4, -3, 0).getInfo()) # double ∈ [-4, -3]
print(ee.PixelType('double', None, 2.3, 0).getInfo()) # double
print(ee.PixelType('double', 3.4, None, 0).getInfo()) # double
```

