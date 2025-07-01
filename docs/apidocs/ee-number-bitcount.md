 
#  ee.Number.bitCount
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-bitcount#examples)


Calculates the number of one-bits in the 64-bit two's complement binary representation of the input. 
Usage| Returns  
---|---  
`Number.bitCount()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-bitcount#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-bitcount#colab-python-sample) More
```
print(ee.Number(0).bitCount());// [0]
print(ee.Number(1).bitCount());// [1]
print(ee.Number(2).bitCount());// [1]
print(ee.Number(3).bitCount());// [2]
print(ee.Number(0xFFFF).bitCount());// [16]
// https://en.wikipedia.org/wiki/Two's_complement signed values.
print(ee.Number(-1).bitCount());// [64]
print(ee.Number(-1,ee.PixelType.int8()).bitCount());// [64]
print(ee.Number(-2).bitCount());// [63]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.Number(0).bitCount().getInfo())    # [0]
print(ee.Number(1).bitCount().getInfo())    # [1]
print(ee.Number(2).bitCount().getInfo())    # [1]
print(ee.Number(3).bitCount().getInfo())    # [2]
print(ee.Number(0xFFFF).bitCount().getInfo()) # [16]
# https://en.wikipedia.org/wiki/Two's_complement signed values.
print(ee.Number(-1).bitCount().getInfo())            # [64]
print(ee.Number(-1).toInt8().bitCount().getInfo())       # [64]
print(ee.Number(-2).bitCount().getInfo())            # [63]
```

Was this helpful?
