 
#  ee.Number.asin 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-asin#examples)


Computes the arcsine in radians of the input. 
Usage| Returns  
---|---  
`Number.asin()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-asin#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-asin#colab-python-sample) More
```
// The domain of arcsine is [-1,1], inputs outside the domain are invalid.
print('Arcsine of -1',ee.Number(-1).asin());// -1.570796326 (-π/2)
print('Arcsine of 0',ee.Number(0).asin());// 0
print('Arcsine of 1',ee.Number(1).asin());// 1.570796326 (π/2)
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The domain of arcsine is [-1,1], inputs outside the domain are invalid.
print('Arcsine of -1:', ee.Number(-1).asin().getInfo()) # -1.570796326 (-π/2)
print('Arcsine of 0:', ee.Number(0).asin().getInfo()) # 0
print('Arcsine of 1:', ee.Number(1).asin().getInfo()) # 1.570796326 (π/2)
```

