 
#  ee.Array.argmax 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-argmax#examples)


Returns the position, as a list of indices in each array axis, of the maximum value in an array, or null if the array is empty. If there are multiple occurrences of the maximum, returns the position of the first. 
Usage| Returns  
---|---  
`Array.argmax()`| List  
Argument| Type| Details  
---|---|---  
this: `array`| Array|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-argmax#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-argmax#colab-python-sample) More
```
// Return the position of the maximum value in each dimension.
// Returns null if the array is empty.
print(ee.Array([],ee.PixelType.int8()).argmax());// null
print(ee.Array([9]).argmax());// [0]
print(ee.Array([0,-1,2,1]).argmax());// [2]
print(ee.Array([[3,4,2],[6,5,7]]).argmax());// [1, 2]
// Returns the first occurrence of the maximum.
print(ee.Array([1,1,1,9,9,9]).argmax());// [3]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Return the position of the maximum value in each dimension.
# Returns null if the array is empty.
display(ee.Array([], ee.PixelType.int8()).argmax()) # None
display(ee.Array([9]).argmax()) # [0]
display(ee.Array([0, -1, 2, 1]).argmax()) # [2]
display(ee.Array([[3, 4, 2], [6, 5, 7]]).argmax()) # [1, 2]
# Returns the first occurrence of the maximum.
display(ee.Array([1, 1, 1, 9, 9, 9]).argmax()) # [3]
```

