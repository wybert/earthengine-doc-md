 
#  ee.Geometry.MultiPolygon.dissolve 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-dissolve#examples)


Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries. 
Usage| Returns  
---|---  
`MultiPolygon.dissolve( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry to union.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-dissolve#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-dissolve#colab-python-sample) More
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
// Apply the dissolve method to the MultiPolygon object.
varmultiPolygonDissolve=multiPolygon.dissolve({'maxError':1});
// Print the result to the console.
print('multiPolygon.dissolve(...) =',multiPolygonDissolve);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPolygon,
{'color':'black'},
'Geometry [black]: multiPolygon');
Map.addLayer(multiPolygonDissolve,
{'color':'red'},
'Result [red]: multiPolygon.dissolve');
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
# Apply the dissolve method to the MultiPolygon object.
multipolygon_dissolve = multipolygon.dissolve(maxError=1)
# Print the result.
display('multipolygon.dissolve(...) =', multipolygon_dissolve)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m.add_layer(
  multipolygon_dissolve,
  {'color': 'red'},
  'Result [red]: multipolygon.dissolve',
)
m
```

Was this helpful?
