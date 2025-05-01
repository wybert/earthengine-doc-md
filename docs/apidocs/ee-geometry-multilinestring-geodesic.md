 
#  ee.Geometry.MultiLineString.geodesic 
Stay organized with collections  Save and categorize content based on your preferences. 
If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. Usage| Returns  
---|---  
`MultiLineString.geodesic()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
### Code Editor (JavaScript)
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);
// Apply the geodesic method to the MultiLineString object.
varmultiLineStringGeodesic=multiLineString.geodesic();
// Print the result to the console.
print('multiLineString.geodesic(...) =',multiLineStringGeodesic);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a MultiLineString object.
multilinestring = ee.Geometry.MultiLineString([
  [[-122.088, 37.418], [-122.086, 37.422], [-122.082, 37.418]],
  [[-122.087, 37.416], [-122.083, 37.416], [-122.082, 37.419]],
])
# Apply the geodesic method to the MultiLineString object.
multilinestring_geodesic = multilinestring.geodesic()
# Print the result.
display('multilinestring.geodesic(...) =', multilinestring_geodesic)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m
```

