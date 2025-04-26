 
#  ee.Geometry.Point.serialize 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the serialized representation of this object. Usage| Returns  
---|---  
`Point.serialize( _legacy_)`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
`legacy`| Boolean, optional| Enables legacy format.  
## Examples
### Code Editor (JavaScript)
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);
// Apply the serialize method to the Point object.
varpointSerialize=point.serialize();
// Print the result to the console.
print('point.serialize(...) =',pointSerialize);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(point,
{'color':'black'},
'Geometry [black]: point');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a Point object.
point = ee.Geometry.Point(-122.082, 37.42)
# Apply the serialize method to the Point object.
point_serialize = point.serialize()
# Print the result.
display('point.serialize(...) =', point_serialize)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m
```

