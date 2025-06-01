 
#  ee.Geometry.LinearRing.union 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the union of the two geometries. Usage| Returns  
---|---  
`LinearRing.union(right,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
### Code Editor (JavaScript)
```
// Define a LinearRing object.
varlinearRing=ee.Geometry.LinearRing(
[[-122.091,37.420],
[-122.085,37.422],
[-122.080,37.430]]);
// Define other inputs.
varinputGeom=ee.Geometry.BBox(-122.085,37.415,-122.075,37.425);
// Apply the union method to the LinearRing object.
varlinearRingUnion=linearRing.union({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('linearRing.union(...) =',linearRingUnion);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(linearRing,
{'color':'black'},
'Geometry [black]: linearRing');
Map.addLayer(inputGeom,
{'color':'blue'},
'Parameter [blue]: inputGeom');
Map.addLayer(linearRingUnion,
{'color':'red'},
'Result [red]: linearRing.union');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a LinearRing object.
linearring = ee.Geometry.LinearRing(
  [[-122.091, 37.420], [-122.085, 37.422], [-122.080, 37.430]]
)
# Define other inputs.
input_geom = ee.Geometry.BBox(-122.085, 37.415, -122.075, 37.425)
# Apply the union method to the LinearRing object.
linearring_union = linearring.union(right=input_geom, maxError=1)
# Print the result.
display('linearring.union(...) =', linearring_union)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linearring, {'color': 'black'}, 'Geometry [black]: linearring')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m.add_layer(
  linearring_union, {'color': 'red'}, 'Result [red]: linearring.union'
)
m
```

