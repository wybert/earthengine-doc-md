 
#  ee.Geometry.Polygon.isUnbounded 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-isunbounded#examples)


Returns whether the geometry is unbounded. 
Usage| Returns  
---|---  
`Polygon.isUnbounded()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-isunbounded#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-isunbounded#colab-python-sample) More
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);
// Apply the isUnbounded method to the Polygon object.
varpolygonIsUnbounded=polygon.isUnbounded();
// Print the result to the console.
print('polygon.isUnbounded(...) =',polygonIsUnbounded);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(polygon,
{'color':'black'},
'Geometry [black]: polygon');
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
# Apply the isUnbounded method to the Polygon object.
polygon_is_unbounded = polygon.isUnbounded()
# Print the result.
display('polygon.isUnbounded(...) =', polygon_is_unbounded)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m
```

Was this helpful?
