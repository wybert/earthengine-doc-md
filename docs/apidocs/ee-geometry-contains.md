 
#  ee.Geometry.contains
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-contains#examples)


Returns true if and only if one geometry contains the other. 
Usage| Returns  
---|---  
`Geometry.contains(right,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-contains#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-contains#colab-python-sample) More
```
// Define a Geometry object.
vargeometry=ee.Geometry({
'type':'Polygon',
'coordinates':
[[[-122.081,37.417],
[-122.086,37.421],
[-122.084,37.418],
[-122.089,37.416]]]
});
// Define other inputs.
varinputGeom=ee.Geometry.BBox(-122.085,37.415,-122.075,37.425);
// Apply the contains method to the Geometry object.
vargeometryContains=geometry.contains({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('geometry.contains(...) =',geometryContains);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
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
# Define a Geometry object.
geometry = ee.Geometry({
  'type': 'Polygon',
  'coordinates': [[
    [-122.081, 37.417],
    [-122.086, 37.421],
    [-122.084, 37.418],
    [-122.089, 37.416],
  ]],
})
# Define other inputs.
input_geom = ee.Geometry.BBox(-122.085, 37.415, -122.075, 37.425)
# Apply the contains method to the Geometry object.
geometry_contains = geometry.contains(right=input_geom, maxError=1)
# Print the result.
display('geometry.contains(...) =', geometry_contains)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

Was this helpful?
