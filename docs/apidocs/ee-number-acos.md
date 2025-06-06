 
#  ee.Number.acos 
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the arccosine in radians of the input. Usage| Returns  
---|---  
`Number.acos()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
// The domain of arccosine is [-1,1], inputs outside the domain are invalid.
print('Arccosine of -1',ee.Number(-1).acos());// 3.141592653 (π)
print('Arccosine of 0',ee.Number(0).acos());// 1.570796326 (π/2)
print('Arccosine of 1',ee.Number(1).acos());// 0
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# The domain of arccosine is [-1,1], inputs outside the domain are invalid.
print('Arccosine of -1:', ee.Number(-1).acos().getInfo()) # 3.141592653 (π)
print('Arccosine of 0:', ee.Number(0).acos().getInfo()) # 1.570796326 (π/2)
print('Arccosine of 1:', ee.Number(1).acos().getInfo()) # 0
```

