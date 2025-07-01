 
#  ee.Geometry.BBox.edgesAreGeodesics
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-edgesaregeodesics#examples)


Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection. 
Usage| Returns  
---|---  
`BBox.edgesAreGeodesics()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-edgesaregeodesics#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-edgesaregeodesics#colab-python-sample) More
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);
// Apply the edgesAreGeodesics method to the BBox object.
varbBoxEdgesAreGeodesics=bBox.edgesAreGeodesics();
// Print the result to the console.
print('bBox.edgesAreGeodesics(...) =',bBoxEdgesAreGeodesics);
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
# Apply the edgesAreGeodesics method to the BBox object.
bbox_edges_are_geodesics = bbox.edgesAreGeodesics()
# Print the result.
display('bbox.edgesAreGeodesics(...) =', bbox_edges_are_geodesics)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m
```

Was this helpful?
