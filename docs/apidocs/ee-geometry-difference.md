 
#  ee.Geometry.difference
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the result of subtracting the 'right' geometry from the 'left' geometry. Usage | Returns  
---|---  
`Geometry.difference(right, _maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `left` | Geometry | The geometry used as the left operand of the operation.  
`right` | Geometry | The geometry used as the right operand of the operation.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
### Code Editor (JavaScript)
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

// Apply the difference method to the Geometry object.
vargeometryDifference=geometry.difference({'right':inputGeom,'maxError':1});

// Print the result to the console.
print('geometry.difference(...) =',geometryDifference);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
Map.addLayer(inputGeom,
{'color':'blue'},
'Parameter [blue]: inputGeom');
Map.addLayer(geometryDifference,
{'color':'red'},
'Result [red]: geometry.difference');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
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

# Apply the difference method to the Geometry object.
geometry_difference = geometry.difference(right=input_geom, maxError=1)

# Print the result.
display('geometry.difference(...) =', geometry_difference)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m.add_layer(
    geometry_difference, {'color': 'red'}, 'Result [red]: geometry.difference'
)
m
```

