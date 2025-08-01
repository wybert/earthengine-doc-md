 
#  ee.Geometry.BBox.geodesic
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-geodesic#examples)


If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth.
Usage | Returns  
---|---  
`BBox.geodesic()` | Boolean  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry |   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-geodesic#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-geodesic#colab-python-sample) More
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);

// Apply the geodesic method to the BBox object.
varbBoxGeodesic=bBox.geodesic();

// Print the result to the console.
print('bBox.geodesic(...) =',bBoxGeodesic);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(bBox,
{'color':'black'},
'Geometry [black]: bBox');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a BBox object.
bbox = ee.Geometry.BBox(-122.09, 37.42, -122.08, 37.43)

# Apply the geodesic method to the BBox object.
bbox_geodesic = bbox.geodesic()

# Print the result.
display('bbox.geodesic(...) =', bbox_geodesic)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m
```

