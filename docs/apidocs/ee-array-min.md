 
#  ee.Array.min 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, selects the minimum of the first and second values. Usage| Returns  
---|---  
`Array.min(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.min(empty));// []
print(ee.Array([0,1,2,3]).min(ee.Array([-1,3,0,2])));// [-1,1,0,2]
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
empty = ee.Array([], ee.PixelType.int8())
display(empty.min(empty)) # []
# [-1, 1, 0, 2]
display(ee.Array([0, 1, 2, 3]).min(ee.Array([-1, 3, 0, 2])))
```

