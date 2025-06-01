 
#  ee.Number.serialize 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the serialized representation of this object. Usage| Returns  
---|---  
`Number.serialize( _legacy_)`| String  
Argument| Type| Details  
---|---|---  
this: `computedobject`| ComputedObject| The ComputedObject instance.  
`legacy`| Boolean, optional| Enables legacy format.  
## Examples
### Code Editor (JavaScript)
```
print('Serialized representation of ee.Number',ee.Number(10).serialize());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
print('Serialized representation of ee.Number:', ee.Number(10).serialize())
```

