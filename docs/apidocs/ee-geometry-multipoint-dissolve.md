 
#  ee.Geometry.MultiPoint.dissolve 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-dissolve#examples)


Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries. 
Usage| Returns  
---|---  
`MultiPoint.dissolve( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry to union.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-dissolve#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-dissolve#colab-python-sample) More
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);
// Apply the dissolve method to the MultiPoint object.
varmultiPointDissolve=multiPoint.dissolve({'maxError':1});
// Print the result to the console.
print('multiPoint.dissolve(...) =',multiPointDissolve);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPoint,
{'color':'black'},
'Geometry [black]: multiPoint');
Map.addLayer(multiPointDissolve,
{'color':'red'},
'Result [red]: multiPoint.dissolve');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a MultiPoint object.
multipoint = ee.Geometry.MultiPoint([[-122.082, 37.420], [-122.081, 37.426]])
# Apply the dissolve method to the MultiPoint object.
multipoint_dissolve = multipoint.dissolve(maxError=1)
# Print the result.
display('multipoint.dissolve(...) =', multipoint_dissolve)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m.add_layer(
  multipoint_dissolve, {'color': 'red'}, 'Result [red]: multipoint.dissolve'
)
m
```

