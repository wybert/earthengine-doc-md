 
#  ee.Array.identity
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-identity#examples)


Creates a 2D identity matrix of the given size.
Usage | Returns  
---|---  
`ee.Array.identity(size)` | Array  
Argument | Type | Details  
---|---|---  
`size` | Integer | The length of each axis.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-identity#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-identity#colab-python-sample) More
```
// []
print(ee.Array.identity(0));

// [[1]]
print(ee.Array.identity(1));

// [[1,0],
//  [0,1]]
print(ee.Array.identity(2));

// [[1,0,0],
//  [0,1,0],
//  [0,0,1]]
print(ee.Array.identity(3));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# []
display(ee.Array.identity(0))

# [[1]]
display(ee.Array.identity(1))

# [[1, 0],
#  [0, 1]]
display(ee.Array.identity(2))

# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
display(ee.Array.identity(3))
```

