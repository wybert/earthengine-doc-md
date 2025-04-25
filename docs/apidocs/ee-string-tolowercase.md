 
#  ee.String.toLowerCase 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-tolowercase#examples)


Converts all of the characters in a string to lower case. 
Usage| Returns  
---|---  
`String.toLowerCase()`| String  
Argument| Type| Details  
---|---|---  
this: `string`| String| The string to convert to lower case.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-tolowercase#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-tolowercase#colab-python-sample) More
```
vars=ee.String('AaBbCc123');
print(s.toLowerCase());// aabbcc123
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
s = ee.String('AaBbCc123')
print(s.toLowerCase().getInfo()) # aabbcc123
```

Was this helpful?
