 
#  ee.Geometry.MultiPoint.geometries 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-geometries#examples)


Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries. 
Usage| Returns  
---|---  
`MultiPoint.geometries()`| List  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-geometries#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-geometries#colab-python-sample) More
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);
// Apply the geometries method to the MultiPoint object.
varmultiPointGeometries=multiPoint.geometries();
// Print the result to the console.
print('multiPoint.geometries(...) =',multiPointGeometries);
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
# Apply the geometries method to the MultiPoint object.
multipoint_geometries = multipoint.geometries()
# Print the result.
display('multipoint.geometries(...) =', multipoint_geometries)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m
```

