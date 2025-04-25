 
#  ee.Geometry.Polygon.distance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-distance#examples)


Returns the minimum distance between two geometries. 
Usage| Returns  
---|---  
`Polygon.distance(right,  _maxError_, _proj_, _spherical_)`| Float  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
`spherical`| Boolean, default: false| When proj is not specified, if true the calculation will be done on the unit sphere. If false the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-distance#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-distance#colab-python-sample) More
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);
// Define other inputs.
varinputGeom=ee.Geometry.Point(-122.090,37.423);
// Apply the distance method to the Polygon object.
varpolygonDistance=polygon.distance({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('polygon.distance(...) =',polygonDistance);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(polygon,
{'color':'black'},
'Geometry [black]: polygon');
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
# Define a Polygon object.
polygon = ee.Geometry.Polygon([[
  [-122.092, 37.424],
  [-122.086, 37.418],
  [-122.079, 37.425],
  [-122.085, 37.423],
]])
# Define other inputs.
input_geom = ee.Geometry.Point(-122.090, 37.423)
# Apply the distance method to the Polygon object.
polygon_distance = polygon.distance(right=input_geom, maxError=1)
# Print the result.
display('polygon.distance(...) =', polygon_distance)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

