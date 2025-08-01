 
#  ee.Geometry.MultiLineString.dissolve
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-dissolve#examples)


Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.
Usage | Returns  
---|---  
`MultiLineString.dissolve(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The geometry to union.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-dissolve#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-dissolve#colab-python-sample) More
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);

// Apply the dissolve method to the MultiLineString object.
varmultiLineStringDissolve=multiLineString.dissolve({'maxError':1});

// Print the result to the console.
print('multiLineString.dissolve(...) =',multiLineStringDissolve);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
Map.addLayer(multiLineStringDissolve,
{'color':'red'},
'Result [red]: multiLineString.dissolve');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a MultiLineString object.
multilinestring = ee.Geometry.MultiLineString([
    [[-122.088, 37.418], [-122.086, 37.422], [-122.082, 37.418]],
    [[-122.087, 37.416], [-122.083, 37.416], [-122.082, 37.419]],
])

# Apply the dissolve method to the MultiLineString object.
multilinestring_dissolve = multilinestring.dissolve(maxError=1)

# Print the result.
display('multilinestring.dissolve(...) =', multilinestring_dissolve)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
    multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m.add_layer(
    multilinestring_dissolve,
    {'color': 'red'},
    'Result [red]: multilinestring.dissolve',
)
m
```

Was this helpful?
