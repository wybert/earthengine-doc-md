 
#  ee.Number.log10 
Stay organized with collections  Save and categorize content based on your preferences. 
Computes the base-10 logarithm of the input. Usage| Returns  
---|---  
`Number.log10()`| Number  
Argument| Type| Details  
---|---|---  
this: `input`| Number| The input value.  
## Examples
### Code Editor (JavaScript)
```
print(ee.Number(0.1).log10());// -1
print(ee.Number(1).log10());// 0
print(ee.Number(10).log10());// 1
print(ee.Number(100).log10());// 2
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.Number(0.1).log10().getInfo()) # -1
print(ee.Number(1).log10().getInfo()) # 0
print(ee.Number(10).log10().getInfo()) # 1
print(ee.Number(100).log10().getInfo()) # 2
```

