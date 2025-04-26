 
#  ee.Geometry.MultiPolygon.toGeoJSONString 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a GeoJSON string representation of the geometry. Usage| Returns  
---|---  
`MultiPolygon.toGeoJSONString()`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
## Examples
### Code Editor (JavaScript)
```
// Define a MultiPolygon object.
varmultiPolygon=ee.Geometry.MultiPolygon(
[[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]],
[[[-122.081,37.417],
[-122.086,37.421],
[-122.089,37.416]]]]);
// Apply the toGeoJSONString method to the MultiPolygon object.
varmultiPolygonToGeoJSONString=multiPolygon.toGeoJSONString();
// Print the result to the console.
print('multiPolygon.toGeoJSONString(...) =',multiPolygonToGeoJSONString);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPolygon,
{'color':'black'},
'Geometry [black]: multiPolygon');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a MultiPolygon object.
multipolygon = ee.Geometry.MultiPolygon([
  [[
    [-122.092, 37.424],
    [-122.086, 37.418],
    [-122.079, 37.425],
    [-122.085, 37.423],
  ]],
  [[[-122.081, 37.417], [-122.086, 37.421], [-122.089, 37.416]]],
])
# Apply the toGeoJSONString method to the MultiPolygon object.
multipolygon_to_geojson_string = multipolygon.toGeoJSONString()
# Print the result.
display('multipolygon.toGeoJSONString(...) =', multipolygon_to_geojson_string)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m
```

