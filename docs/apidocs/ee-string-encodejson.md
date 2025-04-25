 
#  ee.String.encodeJSON 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-encodejson#examples)


Encodes an object to JSON. Supports primitives, lists, and dictionaries. 
Usage| Returns  
---|---  
`ee.String.encodeJSON(object)`| String  
Argument| Type| Details  
---|---|---  
`object`| Object| The object to encode.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-encodejson#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-encodejson#colab-python-sample) More
```
print('JSON-encoded ee.String',
ee.String.encodeJSON(ee.String('earth')));// "\"earth\""
print('JSON-encoded ee.Number',
ee.String.encodeJSON(ee.Number(1)));// "1"
print('JSON-encoded ee.List',
ee.String.encodeJSON(ee.List([1,2,3])));// "[1,2,3]"
print('JSON-encoded ee.Dictionary',
ee.String.encodeJSON(ee.Dictionary({lc_name:'grassland',lc_class:3})));
// "{\"lc_class\":3,\"lc_name\":\"grassland\"}"
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('JSON-encoded ee.String:',
   repr(ee.String.encodeJSON(ee.String('earth')).getInfo())) # '\"earth\"'
print('JSON-encoded ee.Number:',
   repr(ee.String.encodeJSON(ee.Number(1)).getInfo())) # '1'
print('JSON-encoded ee.List:',
   repr(ee.String.encodeJSON(ee.List([1, 2, 3])).getInfo())) # '[1,2,3]'
print('JSON-encoded ee.Dictionary:',
   repr(ee.String.encodeJSON(
     ee.Dictionary({'lc_name': 'grassland', 'lc_class': 3})).getInfo()))
# '{\"lc_class\":3,\"lc_name\":\"grassland\"}'
```

