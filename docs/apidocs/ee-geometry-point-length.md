 
#  ee.Geometry.Point.length
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components. Usage | Returns  
---|---  
`Point.length(_maxError_, _proj_)`|  Float  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The input geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters.  
## Examples
### Code Editor (JavaScript)
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);

// Apply the length method to the Point object.
varpointLength=point.length();

// Print the result to the console.
print('point.length(...) =',pointLength);

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

# Apply the length method to the Point object.
point_length = point.length()

# Print the result.
display('point.length(...) =', point_length)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m
```

