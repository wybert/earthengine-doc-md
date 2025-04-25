 
#  ee.Geometry.Point.isUnbounded 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-isunbounded#examples)


Returns whether the geometry is unbounded. 
Usage| Returns  
---|---  
`Point.isUnbounded()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-isunbounded#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-isunbounded#colab-python-sample) More
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);
// Apply the isUnbounded method to the Point object.
varpointIsUnbounded=point.isUnbounded();
// Print the result to the console.
print('point.isUnbounded(...) =',pointIsUnbounded);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(point,
{'color':'black'},
'Geometry [black]: point');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a Point object.
point = ee.Geometry.Point(-122.082, 37.42)
# Apply the isUnbounded method to the Point object.
point_is_unbounded = point.isUnbounded()
# Print the result.
display('point.isUnbounded(...) =', point_is_unbounded)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m
```

