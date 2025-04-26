 
#  ee.Number.clamp 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-clamp#examples)


Clamps the value to lie within the range of min to max. 
Usage| Returns  
---|---  
`Number.clamp(min, max)`| Number  
Argument| Type| Details  
---|---|---  
this: `number`| Number|   
`min`| Float| The minimum value to clamp to.  
`max`| Float| The maximum value to clamp to.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-clamp#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-clamp#colab-python-sample) More
```
// Numbers within range are unaffected.
print('100 clamped to range [0,255]',ee.Number(100).clamp(0,255));// 100
// Numbers greater than max in range are set to max.
print('259 clamped to range [0,255]',ee.Number(259).clamp(0,255));// 255
// Numbers less than min in range are set to min.
print('-259 clamped to range [0,255]',ee.Number(-259).clamp(0,255));// 0
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Numbers within range are unaffected.
# 100
print('100 clamped to range [0,255]:', ee.Number(100).clamp(0, 255).getInfo())
# Numbers greater than max in range are set to max.
# 255
print('259 clamped to range [0,255]:', ee.Number(259).clamp(0, 255).getInfo())
# Numbers less than min in range are set to min.
# 0
print('-259 clamped to range [0,255]:', ee.Number(-259).clamp(0, 255).getInfo())
```

