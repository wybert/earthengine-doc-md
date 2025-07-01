 
#  ee.Array.subtract
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-subtract#examples)


On an element-wise basis, subtracts the second value from the first. 
Usage| Returns  
---|---  
`Array.subtract(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-subtract#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-subtract#colab-python-sample) More
```
print(ee.Array([10]).subtract(1));// [9]
print(ee.Array([-1,0,1]).subtract(2));// [-3,-2,-1]
print(ee.Array([-1,0,1]).subtract([-5,6,7]));// [4,-6,-6]
varempty=ee.Array([],ee.PixelType.int8());
print(empty.subtract(empty));// []
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([10]).subtract(1)) # [9]
display(ee.Array([-1, 0, 1]).subtract(2)) # [-3, -2, -1]
display(ee.Array([-1, 0, 1]).subtract([-5, 6, 7])) # [4, -6, -6]
empty = ee.Array([], ee.PixelType.int8())
display(empty.subtract(empty)) # []
```

Was this helpful?
