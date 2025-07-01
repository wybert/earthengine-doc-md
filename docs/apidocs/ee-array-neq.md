 
#  ee.Array.neq
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-neq#examples)


On an element-wise basis, returns 1 if and only if the first value is not equal to the second. 
Usage| Returns  
---|---  
`Array.neq(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-neq#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-neq#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.neq(empty));// []
print(ee.Array([0]).neq(ee.Array([1])));// 1
print(ee.Array([1]).neq(ee.Array([1])));// 0
print(ee.Array([1.1]).neq(ee.Array([1.1])));// 0
print(ee.Array([1.1]).float().neq(ee.Array([1.1])));// 1
print(ee.Array([1.1]).double().neq(ee.Array([1.1])));// 0
print(ee.Array([1]).int8().neq(ee.Array([1])));// 0
print(ee.Array([1]).int8().neq(ee.Array([1]).int32()));// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.neq(empty)) # []
display(ee.Array([0]).neq(ee.Array([1]))); # 1
display(ee.Array([1]).neq(ee.Array([1]))); # 0
display(ee.Array([1.1]).neq(ee.Array([1.1]))) # 0
display(ee.Array([1.1]).float().neq(ee.Array([1.1]))) # 1
display(ee.Array([1.1]).double().neq(ee.Array([1.1]))) # 0
display(ee.Array([1]).int8().neq(ee.Array([1]))) # 0
display(ee.Array([1]).int8().neq(ee.Array([1]).int32())) # 0
```

