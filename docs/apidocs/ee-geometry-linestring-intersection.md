 
#  ee.Geometry.LineString.intersection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-intersection#examples)


Returns the intersection of the two geometries. 
Usage| Returns  
---|---  
`LineString.intersection(right,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-intersection#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-intersection#colab-python-sample) More
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);
// Define other inputs.
varinputGeom=ee.Geometry.BBox(-122.085,37.415,-122.075,37.425);
// Apply the intersection method to the LineString object.
varlineStringIntersection=lineString.intersection({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('lineString.intersection(...) =',lineStringIntersection);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
Map.addLayer(inputGeom,
{'color':'blue'},
'Parameter [blue]: inputGeom');
Map.addLayer(lineStringIntersection,
{'color':'red'},
'Result [red]: lineString.intersection');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a LineString object.
linestring = ee.Geometry.LineString([[-122.09, 37.42], [-122.08, 37.43]])
# Define other inputs.
input_geom = ee.Geometry.BBox(-122.085, 37.415, -122.075, 37.425)
# Apply the intersection method to the LineString object.
linestring_intersection = linestring.intersection(right=input_geom, maxError=1)
# Print the result.
display('linestring.intersection(...) =', linestring_intersection)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m.add_layer(
  linestring_intersection,
  {'color': 'red'},
  'Result [red]: linestring.intersection',
)
m
```

Was this helpful?
