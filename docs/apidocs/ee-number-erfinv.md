 
#  ee.Number.erfInv
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the inverse error function of the input. Usage | Returns  
---|---  
`Number.erfInv()` | Number  
Argument | Type | Details  
---|---|---  
this: `input` | Number | The input value.  
## Examples
### Code Editor (JavaScript)
```
print('Inverse error function of -1',
ee.Number(-1).erfInv());// -Infinity

print('Inverse error function of -0.001',
ee.Number(-0.001).erfInv());// -0.000886227

print('Inverse error function of 0',
ee.Number(0).erfInv());// 0

print('Inverse error function of 0.001',
ee.Number(0.001).erfInv());// 0.000886227

print('Inverse error function of 1',
ee.Number(1).erfInv());// Infinity
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('Inverse error function of -1:',
      ee.Number(-1).erfInv().getInfo())  # -Infinity

print('Inverse error function of -0.001:',
      ee.Number(-0.001).erfInv().getInfo())  # -0.000886227

print('Inverse error function of 0:',
      ee.Number(0).erfInv().getInfo())  # 0

print('Inverse error function of 0.001:',
      ee.Number(0.001).erfInv().getInfo())  # 0.000886227

print('Inverse error function of 1:',
      ee.Number(1).erfInv().getInfo())  # Infinity
```

