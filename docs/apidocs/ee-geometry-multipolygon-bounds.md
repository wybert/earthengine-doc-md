 
#  ee.Geometry.MultiPolygon.bounds
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the bounding rectangle of the geometry. Usage| Returns  
---|---  
`MultiPolygon.bounds( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Return the bounding box of this geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
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
// Apply the bounds method to the MultiPolygon object.
varmultiPolygonBounds=multiPolygon.bounds();
// Print the result to the console.
print('multiPolygon.bounds(...) =',multiPolygonBounds);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPolygon,
{'color':'black'},
'Geometry [black]: multiPolygon');
Map.addLayer(multiPolygonBounds,
{'color':'red'},
'Result [red]: multiPolygon.bounds');
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
# Apply the bounds method to the MultiPolygon object.
multipolygon_bounds = multipolygon.bounds()
# Print the result.
display('multipolygon.bounds(...) =', multipolygon_bounds)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m.add_layer(
  multipolygon_bounds, {'color': 'red'}, 'Result [red]: multipolygon.bounds'
)
m
```

