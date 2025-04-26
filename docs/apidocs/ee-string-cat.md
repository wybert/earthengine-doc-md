 
#  ee.String.cat 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-cat#examples)


Concatenates two strings. 
Usage| Returns  
---|---  
`String.cat(string2)`| String  
Argument| Type| Details  
---|---|---  
this: `string1`| String| The first string.  
`string2`| String| The second string.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-cat#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-cat#colab-python-sample) More
```
print(ee.String('cat').cat(' bird'));// 'cat bird'
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print(ee.String('cat').cat(' bird').getInfo()) # 'cat bird'
```

