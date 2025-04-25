 
#  ee.Array.gt 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-gt#examples)


On an element-wise basis, returns 1 if and only if the first value is greater than the second. 
Usage| Returns  
---|---  
`Array.gt(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-gt#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-gt#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.gt(empty));// []
print(ee.Array([0]).gt([0]));// [0]
print(ee.Array([1]).gt([2]));// [0]
print(ee.Array([2]).gt([1]));// [1]
print(ee.Array([-1,0,1]).gt([-2,1,0]));// [1,0,1]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.gt(empty)) # []
display(ee.Array([0]).gt([0])) # [0]
display(ee.Array([1]).gt([2])) # [0]
display(ee.Array([2]).gt([1])) # [1]
display(ee.Array([-1, 0, 1]).gt([-2, 1, 0])) # [1, 0, 1]
```

Was this helpful?
