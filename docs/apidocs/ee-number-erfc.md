 
#  ee.Number.erfc 
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the complementary error function of the input. Usage| Returns  
---|---  
`Number.erfc()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
print('Complementary error function of -10',
ee.Number(-10).erfc());// 2
print('Complementary error function of -0.001',
ee.Number(-0.001).erfc());// 1.001128378
print('Complementary error function of 0',
ee.Number(0).erfc());// 1
print('Complementary error function of 0.001',
ee.Number(0.001).erfc());// 0.998871621
print('Complementary error function of 10',
ee.Number(10).erfc());// 2.088487583e-45
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('Complementary error function of -10:',
   ee.Number(-10).erfc().getInfo()) # 2
print('Complementary error function of -0.001:',
   ee.Number(-0.001).erfc().getInfo()) # 1.001128378
print('Complementary error function of 0:',
   ee.Number(0).erfc().getInfo()) # 1
print('Complementary error function of 0.001:',
   ee.Number(0.001).erfc().getInfo()) # 0.998871621
print('Complementary error function of 10:',
   ee.Number(10).erfc().getInfo()) # 2.088487583e-45
```

