 
#  ee.Geometry.Point.geodesic
Stay organized with collections  Save and categorize content based on your preferences. 
If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. Usage | Returns  
---|---  
`Point.geodesic()` | Boolean  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry |   
## Examples
### Code Editor (JavaScript)
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);

// Apply the geodesic method to the Point object.
varpointGeodesic=point.geodesic();

// Print the result to the console.
print('point.geodesic(...) =',pointGeodesic);

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

# Apply the geodesic method to the Point object.
point_geodesic = point.geodesic()

# Print the result.
display('point.geodesic(...) =', point_geodesic)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m
```

