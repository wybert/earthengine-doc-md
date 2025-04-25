 
#  ee.Array.bitwiseAnd 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-bitwiseand#examples)


On an element-wise basis, calculates the bitwise AND of the input values. 
Usage| Returns  
---|---  
`Array.bitwiseAnd(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-bitwiseand#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-bitwiseand#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.bitwiseAnd(empty));// []
print(ee.Array(0).bitwiseAnd(ee.Array(0)));// 0
print(ee.Array(0).bitwiseAnd(ee.Array(1)));// 0
print(ee.Array(1).bitwiseAnd(ee.Array(0)));// 0
print(ee.Array(1).bitwiseAnd(ee.Array(1)));// 1
print(ee.Array(0xFF).bitwiseAnd(ee.Array(0xFFFF)));// 255
print(ee.Array(0xFFFF).bitwiseAnd(ee.Array(0xFF)));// 255
print(ee.Array(-1).bitwiseAnd(ee.Array(0xFF)));// 255
print(ee.Array(-1).bitwiseAnd(ee.Array(-2)));// -2
print(ee.Array([6,6]).bitwiseAnd(ee.Array([1,11])));// [0,2]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.bitwiseAnd(empty)) # []
display(ee.Array(0).bitwiseAnd(ee.Array(0))) # 0
display(ee.Array(0).bitwiseAnd(ee.Array(1))) # 0
display(ee.Array(1).bitwiseAnd(ee.Array(0))) # 0
display(ee.Array(1).bitwiseAnd(ee.Array(1))) # 1
display(ee.Array(0xFF).bitwiseAnd(ee.Array(0xFFFF))) # 255
display(ee.Array(0xFFFF).bitwiseAnd(ee.Array(0xFF))) # 255
display(ee.Array(-1).bitwiseAnd(ee.Array(0xFF))) # 255
display(ee.Array(-1).bitwiseAnd(ee.Array(-2))) # -2
display(ee.Array([6, 6]).bitwiseAnd(ee.Array([1, 11]))) # [0, 2]
```

Was this helpful?
