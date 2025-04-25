 
#  ee.Geometry.MultiLineString.union 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-union#examples)


Returns the union of the two geometries. 
Usage| Returns  
---|---  
`MultiLineString.union(right,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-union#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-union#colab-python-sample) More
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);
// Define other inputs.
varinputGeom=ee.Geometry.BBox(-122.085,37.415,-122.075,37.425);
// Apply the union method to the MultiLineString object.
varmultiLineStringUnion=multiLineString.union({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('multiLineString.union(...) =',multiLineStringUnion);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
Map.addLayer(inputGeom,
{'color':'blue'},
'Parameter [blue]: inputGeom');
Map.addLayer(multiLineStringUnion,
{'color':'red'},
'Result [red]: multiLineString.union');
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
# Define other inputs.
input_geom = ee.Geometry.BBox(-122.085, 37.415, -122.075, 37.425)
# Apply the union method to the MultiLineString object.
multilinestring_union = multilinestring.union(right=input_geom, maxError=1)
# Print the result.
display('multilinestring.union(...) =', multilinestring_union)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m.add_layer(
  multilinestring_union,
  {'color': 'red'},
  'Result [red]: multilinestring.union',
)
m
```

Was this helpful?
