 
#  ee.Geometry.Point.distance
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the minimum distance between two geometries. Usage| Returns  
---|---  
`Point.distance(right,  _maxError_, _proj_, _spherical_)`| Float  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
`spherical`| Boolean, default: false| If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false.  
## Examples
### Code Editor (JavaScript)
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);
// Define other inputs.
varinputGeom=ee.Geometry.Point(-122.090,37.423);
// Apply the distance method to the Point object.
varpointDistance=point.distance({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('point.distance(...) =',pointDistance);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(point,
{'color':'black'},
'Geometry [black]: point');
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
# Define a Point object.
point = ee.Geometry.Point(-122.082, 37.42)
# Define other inputs.
input_geom = ee.Geometry.Point(-122.090, 37.423)
# Apply the distance method to the Point object.
point_distance = point.distance(right=input_geom, maxError=1)
# Print the result.
display('point.distance(...) =', point_distance)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

