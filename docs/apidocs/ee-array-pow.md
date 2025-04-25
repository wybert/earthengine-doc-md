 
#  ee.Array.pow 
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, raises the first value to the power of the second. Usage| Returns  
---|---  
`Array.pow(right)`| Array  
Argument| Type| Details  
---|---|---  
this: `left`| Array| The left-hand value.  
`right`| Array| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.pow(empty));// []
// [0.25,-0.5,1,-2,4,-8]
print(ee.Array([-2,-2,-2,-2,-2,-2]).pow([-2,-1,0,1,2,3]));
// [1,-1,1,-1,1,-1]
print(ee.Array([-1,-1,-1,-1,-1,-1]).pow([-2,-1,0,1,2,3]));
// print(ee.Array([0, 0, 0, 0, 0, 0]).pow([-2, -1, 0, 1, 2, 3]));
print(ee.Array([0,0,0,0]).pow([0,1,2,3]));
// [1,1,1,1,1,1]
print(ee.Array([1,1,1,1,1,1]).pow([-2,-1,0,1,2,3]));
// [0.25,0.5,1,2,4,8]
print(ee.Array([2,2,2,2,2,2]).pow([-2,-1,0,1,2,3]));
// [0.009999999776482582,
// 0.10000000149011612,
// 1,
// 10,
// 100,
// 1000]
print(ee.Array([10,10,10,10,10,10]).pow([-2,-1,0,1,2,3]));
// [0.009999999776482582,
// 0.10000000149011612,
// 1,
// 10,
// 100,
// 1000]
print(ee.Array([10,10,10,10,10,10],ee.PixelType.int32())
.pow([-2,-1,0,1,2,3]));
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
display(empty.pow(empty)) # []
# [0.25, -0.5, 1, -2, 4, -8]
display(ee.Array([-2, -2, -2, -2, -2, -2]).pow([-2, -1, 0, 1, 2, 3]))
# [1, -1, 1, -1, 1, -1]
display(ee.Array([-1, -1, -1, -1, -1, -1]).pow([-2, -1, 0, 1, 2, 3]))
# ['Infinity', 'Infinity', 1, 0, 0, 0]
display(ee.Array([0, 0, 0, 0, 0, 0]).pow([-2, -1, 0, 1, 2, 3]))
# [1, 0, 0, 0]
display(ee.Array([0, 0, 0, 0]).pow([0, 1, 2, 3]))
# [1, 1, 1, 1, 1, 1]
display(ee.Array([1, 1, 1, 1, 1, 1]).pow([-2, -1, 0, 1, 2, 3]))
# [0.25, 0.5, 1, 2, 4, 8]
display(ee.Array([2, 2, 2, 2, 2, 2]).pow([-2, -1, 0, 1, 2, 3]))
# [0.009999999776482582,
# 0.10000000149011612,
# 1,
# 10,
# 100,
# 1000]
display(ee.Array([10, 10, 10, 10, 10, 10]).pow([-2, -1, 0, 1, 2, 3]))
# [0.009999999776482582,
# 0.10000000149011612,
# 1,
# 10,
# 100,
# 1000]
display(ee.Array([10, 10, 10, 10, 10, 10], ee.PixelType.int32())
    .pow([-2, -1, 0, 1, 2, 3]))
```

