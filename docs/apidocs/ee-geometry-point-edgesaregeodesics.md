 
#  ee.Geometry.Point.edgesAreGeodesics 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-edgesaregeodesics#examples)


Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection. 
Usage| Returns  
---|---  
`Point.edgesAreGeodesics()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-edgesaregeodesics#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-point-edgesaregeodesics#colab-python-sample) More
```
// Define a Point object.
varpoint=ee.Geometry.Point(-122.082,37.42);
// Apply the edgesAreGeodesics method to the Point object.
varpointEdgesAreGeodesics=point.edgesAreGeodesics();
// Print the result to the console.
print('point.edgesAreGeodesics(...) =',pointEdgesAreGeodesics);
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
# Apply the edgesAreGeodesics method to the Point object.
point_edges_are_geodesics = point.edgesAreGeodesics()
# Print the result.
display('point.edgesAreGeodesics(...) =', point_edges_are_geodesics)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(point, {'color': 'black'}, 'Geometry [black]: point')
m
```

Was this helpful?
