 
#  ee.Geometry.BBox.disjoint
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-disjoint#examples)


Returns true if and only if the geometries are disjoint. 
Usage| Returns  
---|---  
`BBox.disjoint(right,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-disjoint#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-disjoint#colab-python-sample) More
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);
// Define other inputs.
varinputGeom=ee.Geometry.BBox(-122.085,37.415,-122.075,37.425);
// Apply the disjoint method to the BBox object.
varbBoxDisjoint=bBox.disjoint({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('bBox.disjoint(...) =',bBoxDisjoint);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(bBox,
{'color':'black'},
'Geometry [black]: bBox');
Map.addLayer(inputGeom,
{'color':'blue'},
'Parameter [blue]: inputGeom');
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
# Define other inputs.
input_geom = ee.Geometry.BBox(-122.085, 37.415, -122.075, 37.425)
# Apply the disjoint method to the BBox object.
bbox_disjoint = bbox.disjoint(right=input_geom, maxError=1)
# Print the result.
display('bbox.disjoint(...) =', bbox_disjoint)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

