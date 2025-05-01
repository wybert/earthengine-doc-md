 
#  ee.Array.add 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, adds the first value to the second. 
Usage| Returns  
---|---  
`Array.add(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.add(empty));// []
print(ee.Array([0]).add(1));// [1]
print(ee.Array([1]).add([2]));// [3]
print(ee.Array([-3]).add([-4]));// [-7]
print(ee.Array([5,6]).add([7,8]));// [12,14]
vararray2x3=ee.Array([[0,1,2],[3,4,5]]);
print(array2x3.add(1));// [[1,2,3],[4,5,6]]
print(array2x3.add(array2x3));// [[0,2,4],[6,8,10]]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.add(empty)) # []
display(ee.Array([0]).add(1)) # [1]
display(ee.Array([1]).add([2])) # [3]
display(ee.Array([-3]).add([-4])) # [-7]
display(ee.Array([5, 6]).add([7, 8])) # [12 ,14]
array2x3 = ee.Array([[0, 1, 2], [3, 4, 5]])
display(array2x3.add(1)) # [[1, 2 ,3], [4, 5, 6]]
display(array2x3.add(array2x3)) # [[0, 2, 4], [6, 8, 10]]
```

