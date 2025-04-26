 
#  ee.Number.leftShift 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-leftshift#examples)


Calculates the left shift of v1 by v2 bits. 
Usage| Returns  
---|---  
`Number.leftShift(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-leftshift#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-leftshift#colab-python-sample) More
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
```
"""Unsigned 8-bit type example.
20 as binary: 00010100
Left shift 2: 01010000
01010000 is binary for 80.
"""
print(ee.Number(20).leftShift(2).getInfo()) # 80
```

