 
#  ee.Geometry.Point.bounds
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the bounding rectangle of the geometry. Usage | Returns  
---|---  
`Point.bounds(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Return the bounding box of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
### Code Editor (JavaScript)
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);

// Apply the bounds method to the Point object.
varpointBounds=point.bounds();

// Print the result to the console.
print('point.bounds(...) =',pointBounds);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(point,
{'color':'black'},
'Geometry [black]: point');
Map.addLayer(pointBounds,
{'color':'red'},
'Result [red]: point.bounds');
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

# Apply the bounds method to the Point object.
point_bounds = point.bounds()

# Print the result.
display('point.bounds(...) =', point_bounds)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m.add_layer(point_bounds, {'color': 'red'}, 'Result [red]: point.bounds')
m
```

