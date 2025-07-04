 
#  ee.Number
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs a new Number. Usage| Returns  
---|---  
`ee.Number(number)`| Number  
Argument| Type| Details  
---|---|---  
`number`| Number|Object| A number or a computed object.  
## Examples
### Code Editor (JavaScript)
```
print(ee.Number(0));// 0
print(ee.Number(1));// 1
print(ee.Number(0.0));// 0
print(ee.Number(1.0));// 1
print(ee.Number(-1.0));// -1
print(ee.Number(Math.PI));// 3.141592653589793
print(ee.Number(1.2e-35));// 1.2e-35
print(ee.Number(3.4e10));// 34000000000
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
print(ee.Number(0).getInfo()) # 0
print(ee.Number(1).getInfo()) # 1
print(ee.Number(0.0).getInfo()) # 0
print(ee.Number(1.0).getInfo()) # 1
print(ee.Number(-1.0).getInfo()) # -1
print(ee.Number(math.pi).getInfo()) # 3.141592653589793
print(ee.Number(1.2e-35).getInfo()) # 1.2e-35
print(ee.Number(3.4e10).getInfo()) # 34000000000
```

