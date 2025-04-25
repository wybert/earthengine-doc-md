 
#  ee.Number.leftShift 
Stay organized with collections  Save and categorize content based on your preferences. 
Calculates the left shift of v1 by v2 bits. Usage| Returns  
---|---  
`Number.leftShift(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
/**
 * Unsigned 8-bit type example.
 *
 * 20 as binary: 00010100
 * Left shift 2: 01010000
 *
 * 01010000 is binary for 80.
 */
print(ee.Number(20).leftShift(2));// 80
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
"""Unsigned 8-bit type example.
20 as binary: 00010100
Left shift 2: 01010000
01010000 is binary for 80.
"""
print(ee.Number(20).leftShift(2).getInfo()) # 80
```

