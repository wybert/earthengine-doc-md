 
#  ee.Array.bitwiseNot
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-bitwisenot#examples)


On an element-wise basis, calculates the bitwise NOT of the input, in the smallest signed integer type that can hold the input. 
Usage| Returns  
---|---  
`Array.bitwiseNot()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-bitwisenot#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-bitwisenot#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.bitwiseNot());// []
print(ee.Array(0).bitwiseNot());// -1
print(ee.Array(1).bitwiseNot());// -2
print(ee.Array(0xFF).bitwiseNot());// -256
print(ee.Array(-1).bitwiseNot());// 0
print(ee.Array(-2).bitwiseNot());// 1
print(ee.Array(-3).bitwiseNot());// 2
print(ee.Array(0xFF).toInt64().bitwiseNot());// -256
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.bitwiseNot()) # []
display(ee.Array(0).bitwiseNot()) # -1
display(ee.Array(1).bitwiseNot()) # -2
display(ee.Array(0xFF).bitwiseNot()) # -256
display(ee.Array(-1).bitwiseNot()) # 0
display(ee.Array(-2).bitwiseNot()) # 1
display(ee.Array(-3).bitwiseNot()) # 2
display(ee.Array(0xFF).toInt64().bitwiseNot()) # -256
```

Was this helpful?
