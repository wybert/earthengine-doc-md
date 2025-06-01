 
#  ee.Geometry.serialize 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-serialize#examples)


Returns the serialized representation of this object. 
Usage| Returns  
---|---  
`Geometry.serialize( _legacy_)`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
`legacy`| Boolean, optional| Enables legacy format.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-serialize#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-serialize#colab-python-sample) More
```
// Define a Geometry object.
vargeometry=ee.Geometry({
'type':'Polygon',
'coordinates':
[[[-122.081,37.417],
[-122.086,37.421],
[-122.084,37.418],
[-122.089,37.416]]]
});
// Apply the serialize method to the Geometry object.
vargeometrySerialize=geometry.serialize();
// Print the result to the console.
print('geometry.serialize(...) =',geometrySerialize);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a Geometry object.
geometry = ee.Geometry({
  'type': 'Polygon',
  'coordinates': [[
    [-122.081, 37.417],
    [-122.086, 37.421],
    [-122.084, 37.418],
    [-122.089, 37.416],
  ]],
})
# Apply the serialize method to the Geometry object.
geometry_serialize = geometry.serialize()
# Print the result.
display('geometry.serialize(...) =', geometry_serialize)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m
```

