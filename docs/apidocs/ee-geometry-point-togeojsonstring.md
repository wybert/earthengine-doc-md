 
#  ee.Geometry.Point.toGeoJSONString
Stay organized with collections  Save and categorize content based on your preferences. 
Usage | Returns  
---|---  
`Point.toGeoJSONString()` | String  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The Geometry instance.  
## Examples
### Code Editor (JavaScript)
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);

// Apply the toGeoJSONString method to the Point object.
varpointToGeoJSONString=point.toGeoJSONString();

// Print the result to the console.
print('point.toGeoJSONString(...) =',pointToGeoJSONString);

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

# Apply the toGeoJSONString method to the Point object.
point_to_geojson_string = point.toGeoJSONString()

# Print the result.
display('point.toGeoJSONString(...) =', point_to_geojson_string)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m
```

