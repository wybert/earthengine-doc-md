 
#  ee.FeatureCollection.getString
Stay organized with collections  Save and categorize content based on your preferences. 
Extract a property from a feature. Usage| Returns  
---|---  
`FeatureCollection.getString(property)`| String  
Argument| Type| Details  
---|---|---  
this: `object`| Element| The feature to extract the property from.  
`property`| String| The property to extract.  
## Examples
### Code Editor (JavaScript)
```
// A FeatureCollection with a string property value.
varfc=ee.FeatureCollection([]).set('string_property','Abies magnifica');
// Fetch the string property value as an ee.String object.
print('String property value as ee.String',fc.getString('string_property'));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A FeatureCollection with a string property value.
fc = ee.FeatureCollection([]).set('string_property', 'Abies magnifica')
# Fetch the string property value as an ee.String object.
print('String property value as ee.String:',
   fc.getString('string_property').getInfo())
```

