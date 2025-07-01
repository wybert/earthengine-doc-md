 
#  ee.Array.bitCount
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-array-bitcount#examples)


On an element-wise basis, calculates the number of one-bits in the 64-bit two's complement binary representation of the input. 
Usage| Returns  
---|---  
`Array.bitCount()`| Array  
Argument| Type| Details  
---|---|---  
this: `input`| Array| The input array.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-array-bitcount#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-array-bitcount#colab-python-sample) More
```
print(ee.Array([],ee.PixelType.int8()).bitCount());// []
print(ee.Array([0]).bitCount());// [0]
print(ee.Array([1]).bitCount());// [1]
print(ee.Array([2]).bitCount());// [1]
print(ee.Array([3]).bitCount());// [2]
print(ee.Array([0xFFFF]).bitCount());// [16]
print(ee.Array([1,2,3]).bitCount());// [1,1,2]
print(ee.Array([[0,1],[6,13]]).bitCount());// [[0,1],[2,3]]
// https://en.wikipedia.org/wiki/Two's_complement signed values.
print(ee.Array([-1]).bitCount());// [64]
print(ee.Array([-1],ee.PixelType.int8()).bitCount());// [64]
print(ee.Array([-2]).bitCount());// [63]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
display(ee.Array([], ee.PixelType.int8()).bitCount()) # []
display(ee.Array([0]).bitCount())    # [0]
display(ee.Array([1]).bitCount())    # [1]
display(ee.Array([2]).bitCount())    # [1]
display(ee.Array([3]).bitCount())    # [2]
display(ee.Array([0xFFFF]).bitCount())  # [16]
display(ee.Array([1, 2, 3]).bitCount()) # [1, 1, 2]
display(ee.Array([[0, 1], [6, 13]]).bitCount()) # [[0, 1], [2, 3]]
# https://en.wikipedia.org/wiki/Two's_complement signed values.
display(ee.Array([-1]).bitCount())            # [64]
display(ee.Array([-1], ee.PixelType.int8()).bitCount()) # [64]
display(ee.Array([-2]).bitCount())            # [63]
```

Was this helpful?
