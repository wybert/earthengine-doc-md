 
#  ee.Number.cosh 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-cosh#examples)


Computes the hyperbolic cosine of the input. 
Usage| Returns  
---|---  
`Number.cosh()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-cosh#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-cosh#colab-python-sample) More
```
// Input angle in radians.
print('Hyperbolic cosine of -5',ee.Number(-5).cosh());// 74.209948524
print('Hyperbolic cosine of -1',ee.Number(-1).cosh());// 1.543080634
print('Hyperbolic cosine of 0',ee.Number(0).cosh());// 1
print('Hyperbolic cosine of 1',ee.Number(1).cosh());// 1.543080634
print('Hyperbolic cosine of 5',ee.Number(5).cosh());// 74.209948524
// Convert degrees to radians.
vardegrees=45;
varradians=degrees*(Math.PI/180);
print('Hyperbolic cosine of 45 degrees',
ee.Number(radians).cosh());// 1.324609089
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
print('Hyperbolic cosine of -5:',
   ee.Number(-5).cosh().getInfo()) # 74.209948524
print('Hyperbolic cosine of -1:', ee.Number(-1).cosh().getInfo()) # 1.543080634
print('Hyperbolic cosine of 0:', ee.Number(0).cosh().getInfo()) # 1
print('Hyperbolic cosine of 1:', ee.Number(1).cosh().getInfo()) # 1.543080634
print('Hyperbolic cosine of 5:', ee.Number(5).cosh().getInfo()) # 74.209948524
# Convert degrees to radians.
degrees = 45
radians = degrees * (math.pi/180)
print('Hyperbolic cosine of 45 degrees:',
   ee.Number(radians).cosh().getInfo()) # 1.324609089
```

Was this helpful?
