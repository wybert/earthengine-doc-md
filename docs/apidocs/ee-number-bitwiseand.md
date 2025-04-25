 
#  ee.Number.bitwiseAnd 
Stay organized with collections  Save and categorize content based on your preferences. 
Calculates the bitwise AND of the input values. Usage| Returns  
---|---  
`Number.bitwiseAnd(right)`| Number  
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
 * 25 as binary:  00011001
 * 21 as binary:  00010101
 * Both digits 1?: 00010001
 *
 * 00010001 is unsigned 8-bit binary for 17.
 */
print(ee.Number(25).bitwiseAnd(21));
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
25 as binary:  00011001
21 as binary:  00010101
Both digits 1?: 00010001
00010001 is unsigned 8-bit binary for 17.
"""
print(ee.Number(25).bitwiseAnd(21).getInfo())
```

