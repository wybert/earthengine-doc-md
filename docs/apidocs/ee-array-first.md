 
#  ee.Array.first 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, selects the value of the first value. Usage| Returns  
---|---  
`Array.first(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.first(empty));// []
print(ee.Array([0]).first(0));// [0]
print(ee.Array([0,1,2]).first(1));// [0,1,2]
print(ee.Array([0,1,2]).first(ee.Array([3,4,5])));// [0,1,2]
print(ee.Array([3,4,5]).first(ee.Array([0,1,2])));// [3,4,5]
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
display(empty.first(empty)) # []
display(ee.Array([0]).first(0)) # [0]
display(ee.Array([0, 1, 2]).first(1)) # [0,1,2]
display(ee.Array([0, 1, 2]).first(ee.Array([3, 4, 5]))) # [0, 1, 2]
display(ee.Array([3, 4, 5]).first(ee.Array([0, 1, 2]))) # [3, 4, 5]
```

