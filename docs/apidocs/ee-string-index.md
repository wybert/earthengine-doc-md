 
#  ee.String.index
Stay organized with collections  Save and categorize content based on your preferences. 
Searches a string for the first occurrence of a substring. Returns the index of the first match, or -1. Usage | Returns  
---|---  
`String.index(pattern)` | Integer  
Argument | Type | Details  
---|---|---  
this: `target` | String | The string to search.  
`pattern` | String | The string to find.  
## Examples
### Code Editor (JavaScript)
```
print(ee.String('abc123').index(''));// 0
print(ee.String('abc123').index('c1'));// 2
print(ee.String('abc123').index('ZZ'));// -1

// index is case-sensitive.
print(ee.String('abc123').index('BC'));// -1
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.String('abc123').index('').getInfo())  # 0
print(ee.String('abc123').index('c1').getInfo())  # 2
print(ee.String('abc123').index('ZZ').getInfo())  # -1

# index is case-sensitive.
print(ee.String('abc123').index('BC').getInfo())  # -1
```

