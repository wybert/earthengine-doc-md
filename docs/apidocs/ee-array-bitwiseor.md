 
#  ee.Array.bitwiseOr
Stay organized with collections  Save and categorize content based on your preferences. 
On an element-wise basis, calculates the bitwise OR of the input values. Usage | Returns  
---|---  
`Array.bitwiseOr(right)` | Array  
Argument | Type | Details  
---|---|---  
this: `left` | Array | The left-hand value.  
`right` | Array | The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
varempty=ee.Array([],ee.PixelType.int8());
print(empty.bitwiseOr(empty));// []

print(ee.Array(0).bitwiseOr(ee.Array(0)));// 0
print(ee.Array(0).bitwiseOr(ee.Array(1)));// 1
print(ee.Array(1).bitwiseOr(ee.Array(0)));// 1
print(ee.Array(1).bitwiseOr(ee.Array(1)));// 1

print(ee.Array(0xFF).bitwiseOr(ee.Array(0xFFFF)));// 65535
print(ee.Array(0xFFFF).bitwiseOr(ee.Array(0xFF)));// 65535

print(ee.Array(-1).bitwiseOr(ee.Array(0xFF)));// -1
print(ee.Array(-2).bitwiseOr(ee.Array(-3)));// -1
print(ee.Array(-2).bitwiseOr(ee.Array(-4)));// -2

print(ee.Array([6,6]).bitwiseOr(ee.Array([1,11])));// [7,15]
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
display(empty.bitwiseOr(empty))  # []

display(ee.Array(0).bitwiseOr(ee.Array(0)))  # 0
display(ee.Array(0).bitwiseOr(ee.Array(1)))  # 1
display(ee.Array(1).bitwiseOr(ee.Array(0)))  # 1
display(ee.Array(1).bitwiseOr(ee.Array(1)))  # 1

display(ee.Array(0xFF).bitwiseOr(ee.Array(0xFFFF)))  # 65535
display(ee.Array(0xFFFF).bitwiseOr(ee.Array(0xFF)))  # 65535

display(ee.Array(-1).bitwiseOr(ee.Array(0xFF)))  # -1
display(ee.Array(-2).bitwiseOr(ee.Array(-3)))  # -1
display(ee.Array(-2).bitwiseOr(ee.Array(-4)))  # -2

display(ee.Array([6, 6]).bitwiseOr(ee.Array([1, 11])))  # [7, 15]
```

