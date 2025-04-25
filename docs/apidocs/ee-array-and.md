 
#  ee.Array.and 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-and#examples)


On an element-wise basis, returns 1 if and only if both values are non-zero. 
Usage| Returns  
---|---  
`Array.and(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-and#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-and#colab-python-sample) More
```
// Element-wise boolean "and" operator.
// Both arrays must be the same dimensions.
vararrayNeither=ee.Array([0,0]);
vararrayFirst=ee.Array([1,0]);
vararraySecond=ee.Array([0,1]);
vararrayBoth=ee.Array([1,1]);
// Any non-zero value is true.
vararrayLarger=ee.Array([-2,2]);
print(arrayBoth.and(arrayLarger));// [1, 1]
print(arrayBoth.and(arrayNeither));// [0, 0]
print(arrayFirst.and(arraySecond));// [0, 0]
print(arraySecond.and(arrayFirst));// [0, 0]
print(arrayBoth.and(arrayFirst));// [1, 0]
print(arrayBoth.and(arraySecond));// [0, 1]
print(arrayNeither.and(arrayFirst));// [0, 0]
print(arrayNeither.and(arraySecond));// [0, 0]
// Works the same for all PixelTypes.
vararrayDouble=ee.Array([0.0,2.0],ee.PixelType.double());
print(arrayBoth.and(arrayDouble));// [0, 1]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Element-wise boolean "and" operator.
# Both arrays must be the same dimensions.
array_neither = ee.Array([0, 0])
array_first = ee.Array([1, 0])
array_second = ee.Array([0, 1])
array_both = ee.Array([1, 1])
# Any non-zero value is true.
array_larger = ee.Array([-2, 2])
display(array_both.And(array_larger)) # [1, 1]
display(array_both.And(array_neither)) # [0, 0]
display(array_first.And(array_second)) # [0, 0]
display(array_second.And(array_first)) # [0, 0]
display(array_both.And(array_first)) # [1, 0]
display(array_both.And(array_second)) # [0, 1]
display(array_neither.And(array_first)) # [0, 0]
display(array_neither.And(array_second)) # [0, 0]
# Works the same for all PixelTypes.
array_double = ee.Array([0.0, 2.0], ee.PixelType.double())
display(array_both.And(array_double)) # [0, 1]
```

