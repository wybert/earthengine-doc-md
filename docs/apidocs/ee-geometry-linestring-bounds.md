 
#  ee.Geometry.LineString.bounds 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-bounds#examples)


Returns the bounding rectangle of the geometry. 
Usage| Returns  
---|---  
`LineString.bounds( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Return the bounding box of this geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-bounds#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-bounds#colab-python-sample) More
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);
// Apply the bounds method to the LineString object.
varlineStringBounds=lineString.bounds();
// Print the result to the console.
print('lineString.bounds(...) =',lineStringBounds);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
Map.addLayer(lineStringBounds,
{'color':'red'},
'Result [red]: lineString.bounds');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a LineString object.
linestring = ee.Geometry.LineString([[-122.09, 37.42], [-122.08, 37.43]])
# Apply the bounds method to the LineString object.
linestring_bounds = linestring.bounds()
# Print the result.
display('linestring.bounds(...) =', linestring_bounds)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m.add_layer(
  linestring_bounds, {'color': 'red'}, 'Result [red]: linestring.bounds'
)
m
```

Was this helpful?
