 
#  ee.Geometry.MultiPolygon.disjoint 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns true if and only if the geometries are disjoint. Usage| Returns  
---|---  
`MultiPolygon.disjoint(right,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
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
// Define other inputs.
varinputGeom=ee.Geometry.BBox(-122.085,37.415,-122.075,37.425);
// Apply the disjoint method to the MultiPolygon object.
varmultiPolygonDisjoint=multiPolygon.disjoint({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('multiPolygon.disjoint(...) =',multiPolygonDisjoint);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPolygon,
{'color':'black'},
'Geometry [black]: multiPolygon');
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
# Define other inputs.
input_geom = ee.Geometry.BBox(-122.085, 37.415, -122.075, 37.425)
# Apply the disjoint method to the MultiPolygon object.
multipolygon_disjoint = multipolygon.disjoint(right=input_geom, maxError=1)
# Print the result.
display('multipolygon.disjoint(...) =', multipolygon_disjoint)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

