 
#  ee.Geometry.MultiPoint.isUnbounded 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-isunbounded#examples)


Returns whether the geometry is unbounded. 
Usage| Returns  
---|---  
`MultiPoint.isUnbounded()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-isunbounded#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-isunbounded#colab-python-sample) More
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);
// Apply the isUnbounded method to the MultiPoint object.
varmultiPointIsUnbounded=multiPoint.isUnbounded();
// Print the result to the console.
print('multiPoint.isUnbounded(...) =',multiPointIsUnbounded);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPoint,
{'color':'black'},
'Geometry [black]: multiPoint');
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
# Apply the isUnbounded method to the MultiPoint object.
multipoint_is_unbounded = multipoint.isUnbounded()
# Print the result.
display('multipoint.isUnbounded(...) =', multipoint_is_unbounded)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m
```

