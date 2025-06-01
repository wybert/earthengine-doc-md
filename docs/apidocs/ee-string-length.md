 
#  ee.String.length 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the length of a string. Usage| Returns  
---|---  
`String.length()`| Integer  
Argument| Type| Details  
---|---|---  
this: `string`| String| The string from which to get the length.  
## Examples
### Code Editor (JavaScript)
```
print(ee.String('').length());// 0
print(ee.String('abc123').length());// 6
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.String('').length().getInfo()) # 0
print(ee.String('abc123').length().getInfo()) # 6
```

