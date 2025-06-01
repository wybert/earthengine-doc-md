 
#  ee.FeatureCollection.getNumber 
Stay organized with collections  Save and categorize content based on your preferences. 
Extract a property from a feature. Usage| Returns  
---|---  
`FeatureCollection.getNumber(property)`| Number  
Argument| Type| Details  
---|---|---  
this: `object`| Element| The feature to extract the property from.  
`property`| String| The property to extract.  
## Examples
### Code Editor (JavaScript)
```
// A FeatureCollection with a number property value.
varfc=ee.FeatureCollection([]).set('number_property',1.5);
// Fetch the number property value as an ee.Number object.
print('Number property value as ee.Number',fc.getNumber('number_property'));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A FeatureCollection with a number property value.
fc = ee.FeatureCollection([]).set('number_property', 1.5)
# Fetch the number property value as an ee.Number object.
print('Number property value as ee.Number:',
   fc.getNumber('number_property').getInfo())
```

