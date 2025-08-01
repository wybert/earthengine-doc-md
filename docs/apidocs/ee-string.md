 
#  ee.String
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string#examples)


Usage | Returns  
---|---  
`ee.String(string)` | String  
Argument | Type | Details  
---|---|---  
`string` | Object|String | A string or a computed object.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string#colab-python-sample) More
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
```
print(ee.String('I am a string').getInfo())  # I am a string

# Strings can use emoji.
print(ee.String('🧲⚡️👀').getInfo())  # 🧲⚡️👀

# Empty string.
empty = ee.String('')
print(empty.getInfo())  # ''
print(empty.length().getInfo())  # 0
```

Was this helpful?
