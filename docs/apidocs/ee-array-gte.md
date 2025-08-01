 
#  ee.Array.gte
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-gte#examples)


On an element-wise basis, returns 1 if and only if the first value is greater than or equal to the second.
Usage | Returns  
---|---  
`Array.gte(right)` | Array  
Argument | Type | Details  
---|---|---  
this: `left` | Array | The left-hand value.  
`right` | Array | The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-gte#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-gte#colab-python-sample) More
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.gte(empty));// []

print(ee.Array([0]).gte([0]));// [1]
print(ee.Array([1]).gte([2]));// [0]
print(ee.Array([2]).gte([1]));// [1]

print(ee.Array([-1,0,1]).gte([-2,1,1]));// [1,0,1]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.gte(empty))  # []

display(ee.Array([0]).gte([0]))  # [1]
display(ee.Array([1]).gte([2]))  # [0]
display(ee.Array([2]).gte([1]))  # [1]

display(ee.Array([-1, 0, 1]).gte([-2, 1, 1]))  # [1, 0, 1]
```

Was this helpful?
