 
#  ee.String.trim 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-trim#examples)


Returns a string whose value is the original string, with any leading and trailing whitespace removed. 
Usage| Returns  
---|---  
`String.trim()`| String  
Argument| Type| Details  
---|---|---  
this: `string`| String| The string to trim.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-trim#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-trim#colab-python-sample) More
```
vars=ee.String('\t\n\r abc\t\n\r ');
print(s.trim());// "abc"
vars=ee.String(' a\t\n\r b ');
print(s.trim());// "a\t\n\r b"
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
s = ee.String('\t\n\r abc\t\n\r ')
print(s.trim().getInfo()) # "abc"
s = ee.String(' a\t\n\r b ')
print(s.trim().getInfo()) # "a\t\n\r b"
```

Was this helpful?
