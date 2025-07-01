 
#  ee.Array.multiply
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-multiply#examples)


On an element-wise basis, multiplies the first value by the second. 
Usage| Returns  
---|---  
`Array.multiply(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-multiply#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-multiply#colab-python-sample) More
```
print(ee.Array([1]).multiply(0));// [0]
print(ee.Array([1]).multiply(1));// [1]
print(ee.Array([1]).multiply([0]));// [0]
print(ee.Array([1]).multiply([1]));// [1]
// [-1,8,-2,4.8]
print(ee.Array([1,-2,2,4]).multiply([-1,-4,-1,1.2]));
// [-1,2,-2,-3]
print(ee.Array([1,-2,2,3]).multiply(-1));
varempty=ee.Array([],ee.PixelType.int8());
print(empty.multiply(empty));// []
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([1]).multiply(0)) # [0]
display(ee.Array([1]).multiply(1)) # [1]
display(ee.Array([1]).multiply([0])) # [0]
display(ee.Array([1]).multiply([1])) # [1]
# [-1, 8, -2, 4.8]
display(ee.Array([1, -2, 2, 4]).multiply([-1, -4, -1, 1.2]))
# [-1, 2, -2, -3]
display(ee.Array([1, -2, 2, 3]).multiply(-1))
empty = ee.Array([], ee.PixelType.int8())
display(empty.multiply(empty)) # []
```

Was this helpful?
