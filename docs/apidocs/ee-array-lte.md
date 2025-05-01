 
#  ee.Array.lte 
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, returns 1 if and only if the first value is less than or equal to the second. Usage| Returns  
---|---  
`Array.lte(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.lte(empty));// []
print(ee.Array([0]).lte([0]));// [1]
print(ee.Array([1]).lte([2]));// [1]
print(ee.Array([2]).lte([1]));// [0]
print(ee.Array([-1,0,1]).lte([-2,1,1]));// [0,1,1]
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
display(empty.lte(empty)) # []
display(ee.Array([0]).lte([0])) # [1]
display(ee.Array([1]).lte([2])) # [1]
display(ee.Array([2]).lte([1])) # [0]
display(ee.Array([-1, 0, 1]).lte([-2, 1, 1])) # [0, 1, 1]
```

