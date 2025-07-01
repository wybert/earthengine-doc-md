 
#  ee.Feature
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Features can be constructed from one of the following arguments plus an optional dictionary of properties: 
- An ee.Geometry.
- A GeoJSON Geometry.
- A GeoJSON Feature.
- A computed object: reinterpreted as a geometry if properties are specified, and as a feature if they aren't.
Usage| Returns  
---|---  
`ee.Feature(geometry,  _properties_)`| Feature  
Argument| Type| Details  
---|---|---  
`geometry`| ComputedObject|Feature|Geometry|Object| A geometry or feature.  
`properties`| Object, optional| A dictionary of metadata properties. If the first parameter is a Feature (instead of a geometry), this is unused.  
## Examples
### Code Editor (JavaScript)
```
// Create the simplest possible feature.
print(ee.Feature(null));// Empty feature
// Demonstrate how to set a feature's id.
print(ee.Feature(null,{'id':'yada'}).id());// null
print(ee.Feature(null,{'system:index':'abc123'}).id());// abc123
// The simplest possible feature with a geometry.
varfeature=ee.Feature(ee.Geometry.Point([-114.318,38.985]));
Map.addLayer(feature);
Map.centerObject(feature,10);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create the simplest possible feature.
display(ee.Feature(None)) # Empty feature
# Demonstrate how to set a feature's id.
display(ee.Feature(None, {'id': 'yada'}).id()) # None
display(ee.Feature(None, {'system:index': 'abc123'}).id()) # abc123
# The simplest possible feature with a geometry.
feature = ee.Feature(ee.Geometry.Point([-114.318, 38.985]))
m = geemap.Map()
m.add_layer(feature)
m.center_object(feature, 10)
m
```

