 
#  ee.String 
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs a new String. Usage| Returns  
---|---  
`ee.String(string)`| String  
Argument| Type| Details  
---|---|---  
`string`| Object|String| A string or a computed object.  
## Examples
### Code Editor (JavaScript)
```
print(ee.String('I am a string'));// I am a string
// Strings can use emoji.
print(ee.String('🧲⚡️👀'));// 🧲⚡️👀
// Empty string.
varempty=ee.String('');
print(empty);// ''
print(empty.length());// 0
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print(ee.String('I am a string').getInfo()) # I am a string
# Strings can use emoji.
print(ee.String('🧲⚡️👀').getInfo()) # 🧲⚡️👀
# Empty string.
empty = ee.String('')
print(empty.getInfo()) # ''
print(empty.length().getInfo()) # 0
```

