 
#  ee.Array.max
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-max#examples)


On an element-wise basis, selects the maximum of the first and second values. 
Usage| Returns  
---|---  
`Array.max(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-max#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-max#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.max(empty));// []
vararray1=ee.Array([0,-3,5,3]);
vararray2=ee.Array([0,-1,2,4]);
print(array1.max(array2));// [0,-1,5,4]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.max(empty)) # []
array1 = ee.Array([0, -3, 5, 3])
array2 = ee.Array([0, -1, 2, 4])
display(array1.max(array2)) # [0, -1, 5, 4]
```

Was this helpful?
