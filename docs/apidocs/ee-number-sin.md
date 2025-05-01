 
#  ee.Number.sin 
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the sine of the input in radians. Usage| Returns  
---|---  
`Number.sin()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
// Input angle in radians.
print('Sine of 0',ee.Number(0).sin());// 0
print('Sine of π/2',ee.Number(Math.PI/2).sin());// 1
print('Sine of 3π/2',ee.Number(3*Math.PI/2).sin());// -1
// Convert degrees to radians.
vardegrees=45;
varradians=degrees*(Math.PI/180);
print('Sine of 45 degrees',ee.Number(radians).sin());// 0.707106781
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
importmath
# Input angle in radians.
print('Sine of 0:', ee.Number(0).sin().getInfo()) # 0
print('Sine of π/2:', ee.Number(math.pi/2).sin().getInfo()) # 1
print('Sine of 3π/2:', ee.Number(3*math.pi/2).sin().getInfo()) # -1
# Convert degrees to radians.
degrees = 45
radians = degrees * (math.pi/180)
print('Sine of 45 degrees:', ee.Number(radians).sin().getInfo()) # 0.707106781
```

