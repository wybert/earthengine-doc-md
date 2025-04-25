 
#  ee.Number.tanh 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-tanh#examples)


Computes the hyperbolic tangent of the input. 
Usage| Returns  
---|---  
`Number.tanh()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-tanh#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-tanh#colab-python-sample) More
```
// Input angle in radians.
print('Hyperbolic tangent of -5',ee.Number(-5).tanh());// -0.999909204
print('Hyperbolic tangent of -1',ee.Number(-1).tanh());// -0.761594155
print('Hyperbolic tangent of 0',ee.Number(0).tanh());// 0
print('Hyperbolic tangent of 1',ee.Number(1).tanh());// 0.761594155
print('Hyperbolic tangent of 5',ee.Number(5).tanh());// 0.999909204
// Convert degrees to radians.
vardegrees=45;
varradians=degrees*(Math.PI/180);
print('Hyperbolic tangent of 45 degrees',
ee.Number(radians).tanh());// 0.655794202
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importmath
# Input angle in radians.
print('Hyperbolic tangent of -5:',
   ee.Number(-5).tanh().getInfo()) # -0.999909204
print('Hyperbolic tangent of -1:',
   ee.Number(-1).tanh().getInfo()) # -0.761594155
print('Hyperbolic tangent of 0:', ee.Number(0).tanh().getInfo()) # 0
print('Hyperbolic tangent of 1:', ee.Number(1).tanh().getInfo()) # 0.761594155
print('Hyperbolic tangent of 5:', ee.Number(5).tanh().getInfo()) # 0.999909204
# Convert degrees to radians.
degrees = 45
radians = degrees * (math.pi/180)
print('Hyperbolic tangent of 45 degrees:',
   ee.Number(radians).tanh().getInfo()) # 0.655794202
```

Was this helpful?
