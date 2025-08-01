 
#  ee.Number.firstNonZero
Stay organized with collections  Save and categorize content based on your preferences. 
Selects the first value if it is non-zero, and the second value otherwise. Usage | Returns  
---|---  
`Number.firstNonZero(right)` | Number  
Argument | Type | Details  
---|---|---  
this: `left` | Number | The left-hand value.  
`right` | Number | The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
print('First non-zero: 0, 5',ee.Number(0).firstNonZero(ee.Number(5)));// 5
print('First non-zero: 5, 0',ee.Number(5).firstNonZero(ee.Number(0)));// 5
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('First non-zero in [0, 5]:',
      ee.Number(0).firstNonZero(ee.Number(5)).getInfo())  # 5
print('First non-zero in [5, 0]:',
      ee.Number(5).firstNonZero(ee.Number(0)).getInfo())  # 5
```

