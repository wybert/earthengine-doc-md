 
#  ee.Geometry.BBox.toGeoJSONString 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-togeojsonstring#examples)


Returns a GeoJSON string representation of the geometry. 
Usage| Returns  
---|---  
`BBox.toGeoJSONString()`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-togeojsonstring#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-togeojsonstring#colab-python-sample) More
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);
// Apply the toGeoJSONString method to the BBox object.
varbBoxToGeoJSONString=bBox.toGeoJSONString();
// Print the result to the console.
print('bBox.toGeoJSONString(...) =',bBoxToGeoJSONString);
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
# Apply the toGeoJSONString method to the BBox object.
bbox_to_geojson_string = bbox.toGeoJSONString()
# Print the result.
display('bbox.toGeoJSONString(...) =', bbox_to_geojson_string)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m
```

