 
#  ee.Number.tan 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-tan#examples)


Computes the tangent of the input in radians. 
Usage| Returns  
---|---  
`Number.tan()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-tan#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-tan#colab-python-sample) More
```
// Input angle in radians.
print('Tangent of 0',ee.Number(0).tan());// 0
print('Tangent of π/2',ee.Number(Math.PI/2).tan());// 16331239353195370
print('Tangent of π',ee.Number(Math.PI).tan());// 0 (nearly)
// Convert degrees to radians.
vardegrees=45;
varradians=degrees*(Math.PI/180);
print('Tangent of 45 degrees',ee.Number(radians).tan());// 1 (nearly)
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
print('Tangent of 0:', ee.Number(0).tan().getInfo()) # 0
print('Tangent of π/2:',
   ee.Number(math.pi/2).tan().getInfo()) # 16331239353195370
print('Tangent of π:', ee.Number(math.pi).tan().getInfo()) # 0 (nearly)
# Convert degrees to radians.
degrees = 45
radians = degrees * (math.pi/180)
print('Tangent of 45 degrees:',
   ee.Number(radians).tan().getInfo()) # 1 (nearly)
```

Was this helpful?
