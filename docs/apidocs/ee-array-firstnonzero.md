 
#  ee.Array.firstNonZero 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-firstnonzero#examples)


On an element-wise basis, selects the first value if it is non-zero, and the second value otherwise. 
Usage| Returns  
---|---  
`Array.firstNonZero(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-firstnonzero#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-firstnonzero#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.firstNonZero(empty));// []
print(ee.Array([0]).firstNonZero(0));// [0]
print(ee.Array([0]).firstNonZero([0]));// [0]
print(ee.Array([0]).firstNonZero([1]));// [1]
print(ee.Array([2]).firstNonZero([3]));// [2]
print(ee.Array([1]).firstNonZero([0]));// [1]
print(ee.Array([-1,0,1]).firstNonZero([2,-1,2]));// [-1,-1,1]
// [[1,2],[3,4]]
print(ee.Array([[1,2],[0,0]]).firstNonZero([[0,0],[3,4]]));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.firstNonZero(empty)) # []
display(ee.Array([0]).firstNonZero(0)) # [0]
display(ee.Array([0]).firstNonZero([0])) # [0]
display(ee.Array([0]).firstNonZero([1])) # [1]
display(ee.Array([2]).firstNonZero([3])) # [2]
display(ee.Array([1]).firstNonZero([0])) # [1]
display(ee.Array([-1, 0, 1]).firstNonZero([2, -1, 2])) # [-1, -1, 1]
# [[1, 2], [3, 4]]
display(ee.Array([[1, 2], [0, 0]]).firstNonZero([[0, 0], [3, 4]]))
```

