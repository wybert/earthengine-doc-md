 
#  ee.Array.get
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-get#examples)


Extracts the value at the given position from the input array. 
Usage| Returns  
---|---  
`Array.get(position)`| Number  
Argument| Type| Details  
---|---|---  
this: `array`| Array| The array to extract from.  
`position`| List| The coordinates of the element to get.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-get#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-get#colab-python-sample) More
```
print(ee.Array([9]).get([0]));// 9
print(ee.Array([8,7,6]).get([2]));// 6
vararray=ee.Array([[0,1,2],[3,4,5]]);
print(array.get([0,0]));// 0
print(array.get([0,1]));// 1
print(array.get([1,0]));// 3
print(array.get([1,2]));// 5
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([9]).get([0])) # 9
display(ee.Array([8, 7, 6]).get([2])) # 6
array = ee.Array([[0, 1, 2], [3, 4, 5]])
display(array.get([0, 0])) # 0
display(array.get([0, 1])) # 1
display(array.get([1, 0])) # 3
display(array.get([1, 2])) # 5
```

Was this helpful?
