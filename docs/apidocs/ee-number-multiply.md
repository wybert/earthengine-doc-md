 
#  ee.Number.multiply 
Stay organized with collections  Save and categorize content based on your preferences. 
Multiplies the first value by the second. Usage| Returns  
---|---  
`Number.multiply(right)`| Number  
Argument| Type| Details  
---|---|---  
this: `left`| Number| The left-hand value.  
`right`| Number| The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
print('5 * 10',ee.Number(5).multiply(ee.Number(10)));// 50
print('-5 * -10',ee.Number(-5).multiply(ee.Number(-10)));// 50
print('5 * 10.5',ee.Number(5).multiply(ee.Number(10.5)));// 52.5
print('5 * -10.5',ee.Number(5).multiply(ee.Number(-10.5)));// -52.5
print('0 * 10',ee.Number(0).multiply(ee.Number(10)));// 0
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('5 * 10:', ee.Number(5).multiply(ee.Number(10)).getInfo()) # 50
print('-5 * -10:', ee.Number(-5).multiply(ee.Number(-10)).getInfo()) # 50
print('5 * 10.5:', ee.Number(5).multiply(ee.Number(10.5)).getInfo()) # 52.5
print('5 * -10.5:', ee.Number(5).multiply(ee.Number(-10.5)).getInfo()) # -52.5
print('0 * 10:', ee.Number(0).multiply(ee.Number(10)).getInfo()) # 0
```

