 
#  ee.Array.abs 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-abs#examples)


On an element-wise basis, computes the absolute value of the input. 
Usage| Returns  
---|---  
`Array.abs()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-abs#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-abs#colab-python-sample) More
```
print(ee.Array([-1]).abs());// [1]
print(ee.Array([-2,0,2]).abs());// [2,0,2]
print(ee.Array([[-3.1,-2],[-1,0]]).abs());// [[3.1,2],[1,0]]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([-1]).abs()) # [1]
display(ee.Array([-2, 0, 2]).abs()) # [2, 0, 2]
display(ee.Array([[-3.1, -2], [-1, 0]]).abs()) # [[3.1, 2], [1, 0]]
```

