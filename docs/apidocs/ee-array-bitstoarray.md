 
#  ee.Array.bitsToArray
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-bitstoarray#examples)


Converts the bits of an integer to an Array. The array has as many elements as the position of the highest set bit, or a single 0 for a value of 0. 
Usage| Returns  
---|---  
`ee.Array.bitsToArray(input)`| Array  
Argument| Type| Details  
---|---|---  
`input`| Number| The integer to transform.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-bitstoarray#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-bitstoarray#colab-python-sample) More
```
print(ee.Array.bitsToArray(0));// [0]
print(ee.Array.bitsToArray(1));// [1]
print(ee.Array.bitsToArray(5));// [1, 0 , 1]
print(ee.Array.bitsToArray(0xFF));// [1,1,1,1,1,1,1,1]
print(ee.Array.bitsToArray(-1));// Array of 64 "1" values
print(ee.Array.bitsToArray(-1).toInt8());// Array of 64 "1" values
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array.bitsToArray(0)) # [0]
display(ee.Array.bitsToArray(1)) # [1]
display(ee.Array.bitsToArray(5)) # [1, 0 , 1]
display(ee.Array.bitsToArray(0xFF)) # [1, 1, 1, 1, 1, 1, 1, 1]
display(ee.Array.bitsToArray(-1)) # Array of 64 "1" values
display(ee.Array.bitsToArray(-1).toInt8()) # Array of 64 "1" values
```

