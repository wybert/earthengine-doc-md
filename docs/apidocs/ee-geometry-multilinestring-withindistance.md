 
#  ee.Geometry.MultiLineString.withinDistance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-withindistance#examples)


Returns true if and only if the geometries are within a specified distance. 
Usage| Returns  
---|---  
`MultiLineString.withinDistance(right, distance,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`distance`| Float| The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-withindistance#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-withindistance#colab-python-sample) More
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);
// Define other inputs.
varinputGeom=ee.Geometry.Point(-122.090,37.423);
// Apply the withinDistance method to the MultiLineString object.
varmultiLineStringWithinDistance=multiLineString.withinDistance({'right':inputGeom,'distance':500,'maxError':1});
// Print the result to the console.
print('multiLineString.withinDistance(...) =',multiLineStringWithinDistance);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
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
# Define a MultiLineString object.
multilinestring = ee.Geometry.MultiLineString([
  [[-122.088, 37.418], [-122.086, 37.422], [-122.082, 37.418]],
  [[-122.087, 37.416], [-122.083, 37.416], [-122.082, 37.419]],
])
# Define other inputs.
input_geom = ee.Geometry.Point(-122.090, 37.423)
# Apply the withinDistance method to the MultiLineString object.
multilinestring_within_distance = multilinestring.withinDistance(
  right=input_geom, distance=500, maxError=1
)
# Print the result.
display(
  'multilinestring.withinDistance(...) =', multilinestring_within_distance
)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

Was this helpful?
