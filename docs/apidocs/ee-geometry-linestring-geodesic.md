 
#  ee.Geometry.LineString.geodesic 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-geodesic#examples)


If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. 
Usage| Returns  
---|---  
`LineString.geodesic()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-geodesic#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-geodesic#colab-python-sample) More
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);
// Apply the geodesic method to the LineString object.
varlineStringGeodesic=lineString.geodesic();
// Print the result to the console.
print('lineString.geodesic(...) =',lineStringGeodesic);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
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
# Apply the geodesic method to the LineString object.
linestring_geodesic = linestring.geodesic()
# Print the result.
display('linestring.geodesic(...) =', linestring_geodesic)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m
```

Was this helpful?
