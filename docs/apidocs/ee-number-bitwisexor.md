 
#  ee.Number.bitwiseXor 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-bitwisexor#examples)


Calculates the bitwise XOR of the input values. 
Usage| Returns  
---|---  
`Number.bitwiseXor(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-bitwisexor#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-bitwisexor#colab-python-sample) More
```
/**
 * Unsigned 8-bit type example.
 *
 * 25 as binary:     00011001
 * 21 as binary:     00010101
 * Only one digit is 1?: 00001100
 *
 * 00001100 is unsigned 8-bit binary for 12.
 */
print(ee.Number(25).bitwiseXor(21));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
"""Unsigned 8-bit type example.
25 as binary:     00011001
21 as binary:     00010101
Only one digit is 1?: 00001100
00001100 is unsigned 8-bit binary for 12.
"""
print(ee.Number(25).bitwiseXor(21).getInfo())
```

Was this helpful?
