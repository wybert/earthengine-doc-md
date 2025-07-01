 
#  ee.Number.floor
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the largest integer less than or equal to the input. Usage| Returns  
---|---  
`Number.floor()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
// Positive numbers.
print('Floor for 2.1',ee.Number(2.1).floor());// 2
print('Floor for 2.5',ee.Number(2.5).floor());// 2
print('Floor for 2.9',ee.Number(2.9).floor());// 2
// Negative numbers.
print('Floor for -2.1',ee.Number(-2.1).floor());// -3
print('Floor for -2.5',ee.Number(-2.5).floor());// -3
print('Floor for -2.9',ee.Number(-2.9).floor());// -3
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Positive numbers.
print('Floor for 2.1:', ee.Number(2.1).floor().getInfo()) # 2
print('Floor for 2.5:', ee.Number(2.5).floor().getInfo()) # 2
print('Floor for 2.9:', ee.Number(2.9).floor().getInfo()) # 2
# Negative numbers.
print('Floor for -2.1:', ee.Number(-2.1).floor().getInfo()) # -3
print('Floor for -2.5:', ee.Number(-2.5).floor().getInfo()) # -3
print('Floor for -2.9:', ee.Number(-2.9).floor().getInfo()) # -3
```

