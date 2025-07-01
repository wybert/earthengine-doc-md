 
#  ee.String.length
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-length#examples)


Returns the length of a string. 
Usage| Returns  
---|---  
`String.length()`| Integer  
Argument| Type| Details  
---|---|---  
this: `string`| String| The string from which to get the length.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-length#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-length#colab-python-sample) More
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
```
print(ee.String('').length().getInfo()) # 0
print(ee.String('abc123').length().getInfo()) # 6
```

Was this helpful?
