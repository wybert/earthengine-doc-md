 
#  ee.Geometry.dissolve
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-dissolve#examples)


Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.
Usage | Returns  
---|---  
`Geometry.dissolve(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The geometry to union.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-dissolve#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-dissolve#colab-python-sample) More
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

// Apply the dissolve method to the Geometry object.
vargeometryDissolve=geometry.dissolve({'maxError':1});

// Print the result to the console.
print('geometry.dissolve(...) =',geometryDissolve);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
Map.addLayer(geometryDissolve,
{'color':'red'},
'Result [red]: geometry.dissolve');
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

# Apply the dissolve method to the Geometry object.
geometry_dissolve = geometry.dissolve(maxError=1)

# Print the result.
display('geometry.dissolve(...) =', geometry_dissolve)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m.add_layer(
    geometry_dissolve, {'color': 'red'}, 'Result [red]: geometry.dissolve'
)
m
```

Was this helpful?
