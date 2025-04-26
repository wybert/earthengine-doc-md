 
#  ee.Array.bitwiseXor 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-bitwisexor#examples)


On an element-wise basis, calculates the bitwise XOR of the input values. 
Usage| Returns  
---|---  
`Array.bitwiseXor(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-bitwisexor#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-bitwisexor#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.bitwiseXor(empty));// []
print(ee.Array(0).bitwiseXor(ee.Array(0)));// 0
print(ee.Array(0).bitwiseXor(ee.Array(1)));// 1
print(ee.Array(1).bitwiseXor(ee.Array(0)));// 1
print(ee.Array(1).bitwiseXor(ee.Array(1)));// 0
print(ee.Array(0x00FF).bitwiseXor(ee.Array(0xFF00)));// 65535
print(ee.Array([1,2,3]).bitwiseXor(ee.Array([5,8,16])));// [4,10,19]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.bitwiseXor(empty)) # []
display(ee.Array(0).bitwiseXor(ee.Array(0))) # 0
display(ee.Array(0).bitwiseXor(ee.Array(1))) # 1
display(ee.Array(1).bitwiseXor(ee.Array(0))) # 1
display(ee.Array(1).bitwiseXor(ee.Array(1))) # 0
display(ee.Array(0x00FF).bitwiseXor(ee.Array(0xFF00))) # 65535
# [4, 10, 19]
display(ee.Array([1, 2, 3]).bitwiseXor(ee.Array([5, 8, 16])))
```

