 
#  ee.String.serialize 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-string-serialize#examples)


Returns the serialized representation of this object. 
Usage| Returns  
---|---  
`String.serialize( _legacy_)`| String  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`legacy`| Boolean, optional| Enables legacy format.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-string-serialize#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-string-serialize#colab-python-sample) More
```
print('Serialized representation of ee.String',ee.String('earth').serialize());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Serialized representation of ee.String:', ee.String('earth').serialize())
```

