 
#  ee.Array.or
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-or#examples)


On an element-wise basis, returns 1 if and only if either input value is non-zero.
Usage | Returns  
---|---  
`Array.or(right)` | Array  
Argument | Type | Details  
---|---|---  
this: `left` | Array | The left-hand value.  
`right` | Array | The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-or#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-or#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.or(empty));// []

print(ee.Array([0,0,1,1]).or(ee.Array([0,1,0,1])));// [0,1,1,1]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.Or(empty))  # []

# [0, 1, 1, 1]
display(ee.Array([0, 0, 1, 1]).Or(ee.Array([0, 1, 0, 1])))
```

Was this helpful?
