 
#  ee.String.decodeJSON 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-decodejson#examples)


Decodes a JSON string. 
Usage| Returns  
---|---  
`String.decodeJSON()`| Object  
Argument| Type| Details  
---|---|---  
this: `string`| String| The string to decode.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-decodejson#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-decodejson#colab-python-sample) More
```
vardata=ee.Dictionary(ee.String('{"a": "abc", "b": 1}').decodeJSON());
print(data);
print(data.get('a'));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
data = ee.Dictionary(ee.String('{"a": "abc", "b": 1}').decodeJSON())
print(data.getInfo())
print(data.get('a').getInfo())
```

Was this helpful?
