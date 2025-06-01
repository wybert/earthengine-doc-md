 
#  ee.Array.identity 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Creates a 2D identity matrix of the given size. Usage| Returns  
---|---  
`ee.Array.identity(size)`| Array  
Argument| Type| Details  
---|---|---  
`size`| Integer| The length of each axis.  
## Examples
### Code Editor (JavaScript)
```
// []
print(ee.Array.identity(0));
// [[1]]
print(ee.Array.identity(1));
// [[1,0],
// [0,1]]
print(ee.Array.identity(2));
// [[1,0,0],
// [0,1,0],
// [0,0,1]]
print(ee.Array.identity(3));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# []
display(ee.Array.identity(0))
# [[1]]
display(ee.Array.identity(1))
# [[1, 0],
# [0, 1]]
display(ee.Array.identity(2))
# [[1, 0, 0],
# [0, 1, 0],
# [0, 0, 1]]
display(ee.Array.identity(3))
```

