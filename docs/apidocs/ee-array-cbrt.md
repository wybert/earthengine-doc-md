 
#  ee.Array.cbrt
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-cbrt#examples)


On an element-wise basis, computes the cubic root of the input.
Usage | Returns  
---|---  
`Array.cbrt()` | Array  
Argument | Type | Details  
---|---|---  
this: `input` | Array | The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-cbrt#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-cbrt#colab-python-sample) More
```
// Requires an explicit PixelType if no data.
print(ee.Array([],ee.PixelType.int8()).cbrt());// []

print(ee.Array([0]).cbrt());// [0]
print(ee.Array([27]).cbrt());// [3]
print(ee.Array([-27]).cbrt());// -3

print(ee.Array([0,1,8,27]).cbrt());// [0,1,2,3]
print(ee.Array([[0,1,8],[27,64,125]]).cbrt());// [[0,1,2],[3,4,5]]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Requires an explicit PixelType if no data.
display(ee.Array([], ee.PixelType.int8()).cbrt())  # []

display(ee.Array([0]).cbrt())  # [0]
display(ee.Array([27]).cbrt())  # [3]
display(ee.Array([-27]).cbrt())  # -3

display(ee.Array([0, 1, 8, 27]).cbrt())  # [0, 1, 2, 3]

# [[0, 1, 2], [3, 4, 5]]
display(ee.Array([[0, 1, 8], [27, 64, 125]]).cbrt())
```

