 
#  ee.Number.eq
Stay organized with collections  Save and categorize content based on your preferences. 
Returns 1 if and only if the first value is equal to the second. Usage | Returns  
---|---  
`Number.eq(right)` | Number  
Argument | Type | Details  
---|---|---  
this: `left` | Number | The left-hand value.  
`right` | Number | The right-hand value.  
## Examples
### Code Editor (JavaScript)
```
print('1 equal to 1?',ee.Number(1).eq(ee.Number(1)));// 1
print('1.001 equal to 1?',ee.Number(1.001).eq(ee.Number(1)));// 0
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('1 equal to 1?', ee.Number(1).eq(ee.Number(1)).getInfo())  # 1
print('1.001 equal to 1?', ee.Number(1.001).eq(ee.Number(1)).getInfo())  # 0
```

