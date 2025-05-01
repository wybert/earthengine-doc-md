 
#  ee.Number.atan 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-atan#examples)


Computes the arctangent in radians of the input. 
Usage| Returns  
---|---  
`Number.atan()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-atan#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-atan#colab-python-sample) More
```
print('Arctangent of -1e13',ee.Number(-1e13).atan());// -1.570796326 (-π/2)
print('Arctangent of -1',ee.Number(-1).atan());// -0.785398163
print('Arctangent of 0',ee.Number(0).atan());// 0
print('Arctangent of 1',ee.Number(1).atan());// 0.785398163
print('Arctangent of 1e13',ee.Number(1e13).atan());// 1.570796326 (π/2)
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# -1.570796326 (-π/2)
print('Arctangent of -1e13:', ee.Number(-1e13).atan().getInfo())
print('Arctangent of -1:', ee.Number(-1).atan().getInfo()) # -0.785398163
print('Arctangent of 0:', ee.Number(0).atan().getInfo()) # 0
print('Arctangent of 1:', ee.Number(1).atan().getInfo()) # 0.785398163
# 1.570796326 (π/2)
print('Arctangent of 1e13:', ee.Number(1e13).atan().getInfo())
```

Was this helpful?
