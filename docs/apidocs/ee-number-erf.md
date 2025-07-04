 
#  ee.Number.erf
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the error function of the input. Usage| Returns  
---|---  
`Number.erf()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
print('Error function of -10',ee.Number(-10).erf());// -1
print('Error function of -0.001',ee.Number(-0.001).erf());// -0.001128378
print('Error function of 0',ee.Number(0).erf());// 0
print('Error function of 0.001',ee.Number(0.001).erf());// 0.001128378
print('Error function of 10',ee.Number(10).erf());// 1
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('Error function of -10:', ee.Number(-10).erf().getInfo()) # -1
# -0.001128378
print('Error function of -0.001:', ee.Number(-0.001).erf().getInfo())
print('Error function of 0:', ee.Number(0).erf().getInfo()) # 0
# 0.001128378
print('Error function of 0.001:', ee.Number(0.001).erf().getInfo())
print('Error function of 10:', ee.Number(10).erf().getInfo()) # 1
```

