 
#  ee.Number.rightShift
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Calculates the signed right shift of v1 by v2 bits. 
Usage| Returns  
---|---  
`Number.rightShift(right)`| Number  
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
 * 20 as binary:  00010100
 * Right shift 2: 00000101
 *
 * 00000101 is binary for 5.
 */
print(ee.Number(20).rightShift(2));// 5
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
20 as binary:  00010100
Right shift 2: 00000101
00000101 is binary for 5.
"""
print(ee.Number(20).rightShift(2).getInfo()) # 5
```

