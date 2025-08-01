 
#  ee.Geometry.MultiPolygon.distance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-distance#examples)


Returns the minimum distance between two geometries.
Usage | Returns  
---|---  
`MultiPolygon.distance(right, _maxError_, _proj_, _spherical_)`|  Float  
Argument | Type | Details  
---|---|---  
this: `left` | Geometry | The geometry used as the left operand of the operation.  
`right` | Geometry | The geometry used as the right operand of the operation.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
`spherical` | Boolean, default: false | If true, the calculation will be done on the unit sphere. If false, the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-distance#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-distance#colab-python-sample) More
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
varinputGeom=ee.Geometry.Point(-122.090,37.423);

// Apply the distance method to the MultiPolygon object.
varmultiPolygonDistance=multiPolygon.distance({'right':inputGeom,'maxError':1});

// Print the result to the console.
print('multiPolygon.distance(...) =',multiPolygonDistance);

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
input_geom = ee.Geometry.Point(-122.090, 37.423)

# Apply the distance method to the MultiPolygon object.
multipolygon_distance = multipolygon.distance(right=input_geom, maxError=1)

# Print the result.
display('multipolygon.distance(...) =', multipolygon_distance)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
    multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

Was this helpful?
