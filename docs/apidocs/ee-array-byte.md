 
#  ee.Array.byte 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-byte#examples)


On an element-wise basis, casts the input value to an unsigned 8-bit integer. 
Usage| Returns  
---|---  
`Array.byte()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-byte#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-byte#colab-python-sample) More
```
// Clamps below at 0.
print(ee.Array([-1]).byte());// [0]
print(ee.Array([255]).byte());// [255]
// Clamps above at 255.
print(ee.Array([256]).byte());// [255]
// Rounds. [0,0,1,127,255,255]
print(ee.Array([-0.1,0.1,0.5,127.1,255.1,255.9]).byte());
// Requires an explicit PixelType if no data.
print(ee.Array([[],[]],ee.PixelType.float()).byte());// Empty [[], []]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Clamps below at 0.
display(ee.Array([-1]).byte()) # [0]
display(ee.Array([255]).byte()) # [255]
# Clamps above at 255.
display(ee.Array([256]).byte()) # [255]
# Rounds. [0, 0, 1, 127, 255, 255]
display(ee.Array([-0.1, 0.1, 0.5, 127.1, 255.1, 255.9]).byte())
# Requires an explicit PixelType if no data.
display(ee.Array([[], []], ee.PixelType.float()).byte()) # [[], []]
```

Was this helpful?
