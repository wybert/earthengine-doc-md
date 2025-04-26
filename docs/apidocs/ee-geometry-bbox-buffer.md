 
#  ee.Geometry.BBox.buffer 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-buffer#examples)


Returns the input buffered by a given distance. If the distance is positive, the geometry is expanded, and if the distance is negative, the geometry is contracted. 
Usage| Returns  
---|---  
`BBox.buffer(distance,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry being buffered.  
`distance`| Float| The distance of the buffering, which may be negative. If no projection is specified, the unit is meters. Otherwise the unit is in the coordinate system of the projection.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when approximating the buffering circle and performing any necessary reprojection. If unspecified, defaults to 1% of the distance.  
`proj`| Projection, default: null| If specified, the buffering will be performed in this projection and the distance will be interpreted as units of the coordinate system of this projection. Otherwise the distance is interpereted as meters and the buffering is performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-buffer#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-buffer#colab-python-sample) More
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);
// Apply the buffer method to the BBox object.
varbBoxBuffer=bBox.buffer({'distance':100});
// Print the result to the console.
print('bBox.buffer(...) =',bBoxBuffer);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(bBox,
{'color':'black'},
'Geometry [black]: bBox');
Map.addLayer(bBoxBuffer,
{'color':'red'},
'Result [red]: bBox.buffer');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a BBox object.
bbox = ee.Geometry.BBox(-122.09, 37.42, -122.08, 37.43)
# Apply the buffer method to the BBox object.
bbox_buffer = bbox.buffer(distance=100)
# Print the result.
display('bbox.buffer(...) =', bbox_buffer)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m.add_layer(bbox_buffer, {'color': 'red'}, 'Result [red]: bbox.buffer')
m
```

Was this helpful?
