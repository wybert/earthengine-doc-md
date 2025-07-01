 
#  ee.Array.mask
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-mask#examples)


Creates a subarray by slicing out each position in an input array that is parallel to a non-zero element of the given mask array. 
Usage| Returns  
---|---  
`Array.mask(mask)`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| Array to mask.  
`mask`| Array| Mask array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-mask#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-mask#colab-python-sample) More
```
print(ee.Array([1]).mask([0]));// []
print(ee.Array([1]).mask([1]));// [1]
print(ee.Array([0,1,2,3]).mask([0,4,-1,1.2]));// [1,2,3]
print(ee.Array([[1,2,3,4]]).mask([[0,0,0,0]]));// [[]]
print(ee.Array([[1,2,3,4]]).mask([[1,0,1,1]]));// [[1,3,4]]
vararray=ee.Array([[1],[2],[3],[4]]);
print(array.mask([[0],[0],[0],[0]]));// []
print(array.mask([[1],[0],[1],[1]]));// [[1],[3],[4]]
varempty=ee.Array([],ee.PixelType.int8());
print(empty.mask(empty));// []
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([1]).mask([0])) # []
display(ee.Array([1]).mask([1])) # [1]
display(ee.Array([0, 1, 2, 3]).mask([0, 4, -1, 1.2])) # [1, 2, 3]
display(ee.Array([[1, 2, 3, 4]]).mask([[0, 0, 0, 0]])) # [[]]
display(ee.Array([[1, 2, 3, 4]]).mask([[1, 0, 1, 1]])) # [[1, 3, 4]]
array = ee.Array([[1], [2], [3], [4]])
display(array.mask([[0], [0], [0], [0]])) # []
display(array.mask([[1], [0], [1], [1]])) # [[1], [3], [4]]
empty = ee.Array([], ee.PixelType.int8())
display(empty.mask(empty)) # []
```

