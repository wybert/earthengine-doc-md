 
#  ee.Number.cos
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-number-cos#examples)


Computes the cosine of the input in radians. 
Usage| Returns  
---|---  
`Number.cos()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-number-cos#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-number-cos#colab-python-sample) More
```
// Input angle in radians.
print('Cosine of 0',ee.Number(0).cos());// 1
print('Cosine of π/2',ee.Number(Math.PI/2).cos());// 0 (nearly)
print('Cosine of π',ee.Number(Math.PI).cos());// -1
// Convert degrees to radians.
vardegrees=45;
varradians=degrees*(Math.PI/180);
print('Cosine of 45 degrees',ee.Number(radians).cos());// 0.707106781
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
print('Cosine of 0:', ee.Number(0).cos().getInfo()) # 1
print('Cosine of π/2:', ee.Number(math.pi/2).cos().getInfo()) # 0 (nearly)
print('Cosine of π:', ee.Number(math.pi).cos().getInfo()) # -1
# Convert degrees to radians.
degrees = 45
radians = degrees * (math.pi/180)
# 0.707106781
print('Cosine of 45 degrees:', ee.Number(radians).cos().getInfo())
```

Was this helpful?
