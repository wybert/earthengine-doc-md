 
#  ee.Array.cut
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-cut#examples)


Cut an array along one or more axes. 
Usage| Returns  
---|---  
`Array.cut(position)`| Array  
Argument| Type| Details  
---|---|---  
this: `array`| Array| The array to cut.  
`position`| List| Cut an array along one or more axes. The positions args specifies either a single value for each axis of the array, or -1, indicating the whole axis. The output will be an array that has the same dimensions as the input, with a length of 1 on each axis that was not -1 in the positions array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-cut#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-cut#colab-python-sample) More
```
print(ee.Array([9]).cut([0]));// [9]
print(ee.Array([9]).cut([-1]));// [9]
vararray1x3=ee.Array([0,1,2]);
print(array1x3.cut([-1]));// [0,1,2]
print(array1x3.cut([0]));// [0]
print(array1x3.cut([2]));// [2]
vararray2x3=ee.Array([[0,1,2],[3,4,5]]);
print(array2x3.cut([-1,-1]));// [[0,1,2],[3,4,5]]
print(array2x3.cut([-1,0]));// [[0],[3]]
print(array2x3.cut([1,-1]));// [[3,4,5]]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([9]).cut([0])) # [9]
display(ee.Array([9]).cut([-1])) # [9]
array1x3 = ee.Array([0, 1, 2])
display(array1x3.cut([-1])) # [0, 1, 2]
display(array1x3.cut([0])) # [0]
display(array1x3.cut([2])) # [2]
array2x3 = ee.Array([[0, 1, 2], [3, 4, 5]])
display(array2x3.cut([-1, -1])) # [[0, 1, 2], [3 , 4, 5]]
display(array2x3.cut([-1, 0])) # [[0], [3]]
display(array2x3.cut([1, -1])) # [[3, 4, 5]]
```

Was this helpful?
