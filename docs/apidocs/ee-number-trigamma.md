 
#  ee.Number.trigamma 
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the trigamma function of the input. Usage| Returns  
---|---  
`Number.trigamma()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
print('Trigamma for -100',ee.Number(-100).trigamma());// Infinity
print('Trigamma for 0.001',ee.Number(0.001).trigamma());// 1000001.642533195
print('Trigamma for 0.5',ee.Number(0.5).trigamma());// 4.934802200
print('Trigamma for 1',ee.Number(1).trigamma());// 1.644934066
print('Trigamma for 100',ee.Number(100).trigamma());// 0.010050166
print('Trigamma for 200',ee.Number(200).trigamma());// 0.005012520
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('Trigamma for -100:', ee.Number(-100).trigamma().getInfo()) # Infinity
# 1000001.642533195
print('Trigamma for 0.001:', ee.Number(0.001).trigamma().getInfo())
print('Trigamma for 0.5:', ee.Number(0.5).trigamma().getInfo()) # 4.934802200
print('Trigamma for 1:', ee.Number(1).trigamma().getInfo()) # 1.644934066
print('Trigamma for 100:', ee.Number(100).trigamma().getInfo()) # 0.010050166
print('Trigamma for 200:', ee.Number(200).trigamma().getInfo()) # 0.005012520
```

