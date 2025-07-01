 
#  ee.Array.not
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-not#examples)


On an element-wise basis, returns 0 if the input is non-zero, and 1 otherwise. 
Usage| Returns  
---|---  
`Array.not()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-not#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-not#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.not());// []
print(ee.Array([0]).not());// [1]
print(ee.Array([1]).not());// [0]
print(ee.Array([-1,-0.1,0,0.1,1]).not());// [0,0,1,0,0]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.Not()) # []
display(ee.Array([0]).Not()) # [1]
display(ee.Array([1]).Not()) # [0]
display(ee.Array([-1, -0.1, 0, 0.1, 1]).Not()) # [0, 0, 1, 0, 0]
```

Was this helpful?
