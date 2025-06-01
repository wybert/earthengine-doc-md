 
#  ee.Geometry.MultiPoint.bounds 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the bounding rectangle of the geometry. Usage| Returns  
---|---  
`MultiPoint.bounds( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Return the bounding box of this geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
### Code Editor (JavaScript)
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);
// Apply the bounds method to the MultiPoint object.
varmultiPointBounds=multiPoint.bounds();
// Print the result to the console.
print('multiPoint.bounds(...) =',multiPointBounds);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPoint,
{'color':'black'},
'Geometry [black]: multiPoint');
Map.addLayer(multiPointBounds,
{'color':'red'},
'Result [red]: multiPoint.bounds');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a MultiPoint object.
multipoint = ee.Geometry.MultiPoint([[-122.082, 37.420], [-122.081, 37.426]])
# Apply the bounds method to the MultiPoint object.
multipoint_bounds = multipoint.bounds()
# Print the result.
display('multipoint.bounds(...) =', multipoint_bounds)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m.add_layer(
  multipoint_bounds, {'color': 'red'}, 'Result [red]: multipoint.bounds'
)
m
```

