 
#  ee.Array.slice 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-slice#examples)


Creates a subarray by slicing out each position along the given axis from the 'start' (inclusive) to 'end' (exclusive) by increments of 'step'. The result will have as many dimensions as the input, and the same length in all directions except the slicing axis, where the length will be the number of positions from 'start' to 'end' by 'step' that are in range of the input array's length along 'axis'. This means the result can be length 0 along the given axis if start=end, or if the start or end values are entirely out of range. 
Usage| Returns  
---|---  
`Array.slice( _axis_, _start_, _end_, _step_)`| Array  
Argument| Type| Details  
---|---|---  
this: `array`| Array| Array to slice.  
`axis`| Integer, default: 0| The axis to slice on.  
`start`| Integer, default: 0| The coordinate of the first slice (inclusive) along 'axis'. Negative numbers are used to position the start of slicing relative to the end of the array, where -1 starts at the last position on the axis, -2 starts at the next to last position, etc.  
`end`| Integer, default: null| The coordinate (exclusive) at which to stop taking slices. By default this will be the length of the given axis. Negative numbers are used to position the end of slicing relative to the end of the array, where -1 will exclude the last position, -2 will exclude the last two positions, etc.  
`step`| Integer, default: 1| The separation between slices along 'axis'; a slice will be taken at each whole multiple of 'step' from 'start' (inclusive) to 'end' (exclusive). Must be positive.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-slice#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-slice#colab-python-sample) More
```
vararray1x6=ee.Array([1,2,3,4,5,6]);
print(array1x6.slice());// [1,2,3,4,5,6]
print(array1x6.slice(0));// [1,2,3,4,5,6]
print(array1x6.slice(0,0,6,1));// [1,2,3,4,5,6]
print(array1x6.slice(0,0,10,1));// [1,2,3,4,5,6]
print(array1x6.slice(0,2));// [3,4,5,6]
print(array1x6.slice(0,5));// [6]
print(array1x6.slice(0,6));// []
print(array1x6.slice(0,0,2));// [1,2]
print(array1x6.slice(0,0,0));// []
// Negative start and end.
print(array1x6.slice(0,0,-3));// [1,2,3]
print(array1x6.slice(0,-2,6));// [5,6]
print(array1x6.slice(0,0,6,2));// [1,3,5]
print(array1x6.slice(0,0,6,3));// [1,4]
print(array1x6.slice(0,0,6,4));// [1,5]
print(array1x6.slice(0,0,6,6));// [1]
print(array1x6.slice(0,2,6,2));// [3,5]
vararray3x2=ee.Array([[1,2],[3,4],[5,6]]);
print(array3x2.slice());// [[1,2],[3,4],[5,6]]
print(array3x2.slice(0));// [[1,2],[3,4],[5,6]]
print(array3x2.slice(0,0));// [[1,2],[3,4],[5,6]]
print(array3x2.slice(0,0,1));// [[1,2]]
print(array3x2.slice(0,0,2));// [[1,2],[3,4]]
print(array3x2.slice(0,0,3,1));// [[1,2],[3,4],[5,6]]
print(array3x2.slice(0,0,3,2));// [[1,2],[5,6]]
print(array3x2.slice(0,1,3,2));// [[3,4]]
print(array3x2.slice(0,0,3,3));// [[1,2]]
print(array3x2.slice(1));// [[1,2],[3,4],[5,6]]
print(array3x2.slice(1,1));// [[2],[4],[6]]
print(array3x2.slice(1,0,1));// [[1],[3],[5]]
varempty=ee.Array([],ee.PixelType.int8());
print(empty.slice());// []
print(empty.slice(0));// []
print(empty.slice(0,0,0,1));// []
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
array1x6 = ee.Array([1, 2, 3, 4, 5, 6])
display(array1x6.slice()) # [1, 2, 3, 4, 5, 6]
display(array1x6.slice(0)) # [1, 2, 3, 4, 5, 6]
display(array1x6.slice(0, 0, 6, 1)) # [1, 2, 3, 4, 5, 6]
display(array1x6.slice(0, 0, 10, 1)) # [1, 2, 3, 4, 5, 6]
display(array1x6.slice(0, 2)) # [3, 4, 5, 6]
display(array1x6.slice(0, 5)) # [6]
display(array1x6.slice(0, 6)) # []
display(array1x6.slice(0, 0, 2)) # [1, 2]
display(array1x6.slice(0, 0, 0)) # []
# Negative start and end.
display(array1x6.slice(0, 0, -3)) # [1, 2, 3]
display(array1x6.slice(0, -2, 6)) # [5, 6]
display(array1x6.slice(0, 0, 6, 2)) # [1, 3, 5]
display(array1x6.slice(0, 0, 6, 3)) # [1, 4]
display(array1x6.slice(0, 0, 6, 4)) # [1, 5]
display(array1x6.slice(0, 0, 6, 6)) # [1]
display(array1x6.slice(0, 2, 6, 2)) # [3, 5]
array3x2 = ee.Array([[1, 2], [3, 4], [5, 6]])
display(array3x2.slice()) # [[1, 2], [3, 4], [5, 6]]
display(array3x2.slice(0)) # [[1, 2], [3, 4], [5, 6]]
display(array3x2.slice(0, 0)) # [[1, 2],[3, 4],[5, 6]]
display(array3x2.slice(0, 0, 1)) # [[1, 2]]
display(array3x2.slice(0, 0, 2)) # [[1, 2], [3, 4]]
display(array3x2.slice(0, 0, 3, 1)) # [[1, 2], [3, 4], [5, 6]]
display(array3x2.slice(0, 0, 3, 2)) # [[1, 2], [5, 6]]
display(array3x2.slice(0, 1, 3, 2)) # [[3, 4]]
display(array3x2.slice(0, 0, 3, 3)) # [[1, 2]]
display(array3x2.slice(1)) # [[1, 2], [3, 4], [5, 6]]
display(array3x2.slice(1, 1)) # [[2], [4], [6]]
display(array3x2.slice(1, 0, 1)) # [[1], [3], [5]]
empty = ee.Array([], ee.PixelType.int8())
display(empty.slice()) # []
display(empty.slice(0)) # []
display(empty.slice(0, 0, 0, 1)) # []
```

Was this helpful?
