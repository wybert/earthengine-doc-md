 
#  ee.Geometry.toGeoJSONString 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a GeoJSON string representation of the geometry. Usage| Returns  
---|---  
`Geometry.toGeoJSONString()`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
## Examples
### Code Editor (JavaScript)
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
// Apply the toGeoJSONString method to the Geometry object.
vargeometryToGeoJSONString=geometry.toGeoJSONString();
// Print the result to the console.
print('geometry.toGeoJSONString(...) =',geometryToGeoJSONString);
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

### Colab (Python)
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
# Apply the toGeoJSONString method to the Geometry object.
geometry_to_geojson_string = geometry.toGeoJSONString()
# Print the result.
display('geometry.toGeoJSONString(...) =', geometry_to_geojson_string)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m
```

