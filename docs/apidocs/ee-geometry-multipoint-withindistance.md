 
#  ee.Geometry.MultiPoint.withinDistance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-withindistance#examples)


Returns true if and only if the geometries are within a specified distance. 
Usage| Returns  
---|---  
`MultiPoint.withinDistance(right, distance,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`distance`| Float| The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-withindistance#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-withindistance#colab-python-sample) More
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);
// Define other inputs.
varinputGeom=ee.Geometry.Point(-122.090,37.423);
// Apply the withinDistance method to the MultiPoint object.
varmultiPointWithinDistance=multiPoint.withinDistance({'right':inputGeom,'distance':500,'maxError':1});
// Print the result to the console.
print('multiPoint.withinDistance(...) =',multiPointWithinDistance);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPoint,
{'color':'black'},
'Geometry [black]: multiPoint');
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
# Define a MultiPoint object.
multipoint = ee.Geometry.MultiPoint([[-122.082, 37.420], [-122.081, 37.426]])
# Define other inputs.
input_geom = ee.Geometry.Point(-122.090, 37.423)
# Apply the withinDistance method to the MultiPoint object.
multipoint_within_distance = multipoint.withinDistance(
  right=input_geom, distance=500, maxError=1
)
# Print the result.
display('multipoint.withinDistance(...) =', multipoint_within_distance)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

