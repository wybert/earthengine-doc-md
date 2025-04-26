 
#  ee.Geometry.MultiPolygon.buffer 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-buffer#examples)


Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted. 
Usage| Returns  
---|---  
`MultiPolygon.buffer(distance,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry being buffered.  
`distance`| Float| The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance.  
`proj`| Projection, default: null| If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-buffer#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-buffer#colab-python-sample) More
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
// Apply the buffer method to the MultiPolygon object.
varmultiPolygonBuffer=multiPolygon.buffer({'distance':100});
// Print the result to the console.
print('multiPolygon.buffer(...) =',multiPolygonBuffer);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPolygon,
{'color':'black'},
'Geometry [black]: multiPolygon');
Map.addLayer(multiPolygonBuffer,
{'color':'red'},
'Result [red]: multiPolygon.buffer');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
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
# Apply the buffer method to the MultiPolygon object.
multipolygon_buffer = multipolygon.buffer(distance=100)
# Print the result.
display('multipolygon.buffer(...) =', multipolygon_buffer)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m.add_layer(
  multipolygon_buffer, {'color': 'red'}, 'Result [red]: multipolygon.buffer'
)
m
```

