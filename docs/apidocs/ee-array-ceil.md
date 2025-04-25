 
#  ee.Array.ceil 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-ceil#examples)


On an element-wise basis, computes the smallest integer greater than or equal to the input. 
Usage| Returns  
---|---  
`Array.ceil()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-ceil#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-ceil#colab-python-sample) More
```
// Requires an explicit PixelType if no data.
print(ee.Array([],ee.PixelType.int8()).ceil());// []
print(ee.Array([-1.1]).ceil());// [-1]
print(ee.Array([-0.1]).ceil());// [0]
print(ee.Array([0]).ceil());// [0]
print(ee.Array([0.1]).ceil());// [1]
print(ee.Array([1.1]).ceil());// [2]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Requires an explicit PixelType if no data.
display(ee.Array([], ee.PixelType.int8()).ceil()) # []
display(ee.Array([-1.1]).ceil()) # [-1]
display(ee.Array([-0.1]).ceil()) # [0]
display(ee.Array([0]).ceil()) # [0]
display(ee.Array([0.1]).ceil()) # [1]
display(ee.Array([1.1]).ceil()) # [2]
```

