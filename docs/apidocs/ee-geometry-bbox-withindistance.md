 
#  ee.Geometry.BBox.withinDistance
Stay organized with collections  Save and categorize content based on your preferences. 
Returns true if and only if the geometries are within a specified distance. Usage| Returns  
---|---  
`BBox.withinDistance(right, distance,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`distance`| Float| The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
### Code Editor (JavaScript)
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);
// Define other inputs.
varinputGeom=ee.Geometry.Point(-122.090,37.423);
// Apply the withinDistance method to the BBox object.
varbBoxWithinDistance=bBox.withinDistance({'right':inputGeom,'distance':500,'maxError':1});
// Print the result to the console.
print('bBox.withinDistance(...) =',bBoxWithinDistance);
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

### Colab (Python)
```
# Define a BBox object.
bbox = ee.Geometry.BBox(-122.09, 37.42, -122.08, 37.43)
# Define other inputs.
input_geom = ee.Geometry.Point(-122.090, 37.423)
# Apply the withinDistance method to the BBox object.
bbox_within_distance = bbox.withinDistance(
  right=input_geom, distance=500, maxError=1
)
# Print the result.
display('bbox.withinDistance(...) =', bbox_within_distance)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

