 
#  ee.Number.bitwiseNot
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-bitwisenot#examples)


Calculates the bitwise NOT of the input, in the smallest signed integer type that can hold the input. 
Usage| Returns  
---|---  
`Number.bitwiseNot()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-bitwisenot#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-bitwisenot#colab-python-sample) More
```
/**
 * Unsigned 8-bit type example.
 *
 * 25 as binary:  00011001
 * Flip each digit: 11100110
 *
 * 11100110 is signed 8-bit binary for -26.
 * (binary interpreted using smallest signed integer type containing the input).
 */
print(ee.Number(25).bitwiseNot());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
"""Unsigned 8-bit type example.
25 as binary:  00011001
Flip each digit: 11100110
11100110 is signed 8-bit binary for -26.
(binary interpreted using smallest signed integer type containing the input).
"""
print(ee.Number(25).bitwiseNot().getInfo())
```

Was this helpful?
