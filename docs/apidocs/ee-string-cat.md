 
#  ee.String.cat 
Stay organized with collections  Save and categorize content based on your preferences. 
Concatenates two strings. Usage| Returns  
---|---  
`String.cat(string2)`| String  
Argument| Type| Details  
---|---|---  
this: `string1`| String| The first string.  
`string2`| String| The second string.  
## Examples
### Code Editor (JavaScript)
```
print(ee.String('cat').cat(' bird'));// 'cat bird'
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.String('cat').cat(' bird').getInfo()) # 'cat bird'
```

