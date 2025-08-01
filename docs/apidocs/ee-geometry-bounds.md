 
#  ee.Geometry.bounds
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the bounding rectangle of the geometry. Usage | Returns  
---|---  
`Geometry.bounds(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Return the bounding box of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
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

// Apply the bounds method to the Geometry object.
vargeometryBounds=geometry.bounds();

// Print the result to the console.
print('geometry.bounds(...) =',geometryBounds);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
Map.addLayer(geometryBounds,
{'color':'red'},
'Result [red]: geometry.bounds');
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

# Apply the bounds method to the Geometry object.
geometry_bounds = geometry.bounds()

# Print the result.
display('geometry.bounds(...) =', geometry_bounds)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m.add_layer(
    geometry_bounds, {'color': 'red'}, 'Result [red]: geometry.bounds'
)
m
```

