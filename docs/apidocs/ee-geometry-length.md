 
#  ee.Geometry.length
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-length#examples)


Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components.
Usage | Returns  
---|---  
`Geometry.length(_maxError_, _proj_)`|  Float  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The input geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-length#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-length#colab-python-sample) More
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

// Apply the length method to the Geometry object.
vargeometryLength=geometry.length();

// Print the result to the console.
print('geometry.length(...) =',geometryLength);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
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

# Apply the length method to the Geometry object.
geometry_length = geometry.length()

# Print the result.
display('geometry.length(...) =', geometry_length)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m
```

Was this helpful?
