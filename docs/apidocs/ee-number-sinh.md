 
#  ee.Number.sinh 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-sinh#examples)


Computes the hyperbolic sine of the input. 
Usage| Returns  
---|---  
`Number.sinh()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-sinh#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-sinh#colab-python-sample) More
```
// Input angle in radians.
print('Hyperbolic sine of -5',ee.Number(-5).sinh());// -74.203210577
print('Hyperbolic sine of -1',ee.Number(-1).sinh());// -1.175201193
print('Hyperbolic sine of 0',ee.Number(0).sinh());// 0
print('Hyperbolic sine of 1',ee.Number(1).sinh());// 1.175201193
print('Hyperbolic sine of 5',ee.Number(5).sinh());// 74.203210577
// Convert degrees to radians.
vardegrees=45;
varradians=degrees*(Math.PI/180);
print('Hyperbolic sine of 45 degrees',
ee.Number(radians).sinh());// 0.868670961
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
print('Hyperbolic sine of -5:', ee.Number(-5).sinh().getInfo()) # -74.203210577
print('Hyperbolic sine of -1:', ee.Number(-1).sinh().getInfo()) # -1.175201193
print('Hyperbolic sine of 0:', ee.Number(0).sinh().getInfo()) # 0
print('Hyperbolic sine of 1:', ee.Number(1).sinh().getInfo()) # 1.175201193
print('Hyperbolic sine of 5:', ee.Number(5).sinh().getInfo()) # 74.203210577
# Convert degrees to radians.
degrees = 45
radians = degrees * (math.pi/180)
print('Hyperbolic sine of 45 degrees:',
   ee.Number(radians).sinh().getInfo()) # 0.868670961
```

