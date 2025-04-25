 
#  ee.Geometry.MultiPoint.toGeoJSON 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-togeojson#examples)


Returns a GeoJSON representation of the geometry. 
Usage| Returns  
---|---  
`MultiPoint.toGeoJSON()`| GeoJSONGeometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-togeojson#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-togeojson#colab-python-sample) More
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);
// Apply the toGeoJSON method to the MultiPoint object.
varmultiPointToGeoJSON=multiPoint.toGeoJSON();
// Print the result to the console.
print('multiPoint.toGeoJSON(...) =',multiPointToGeoJSON);
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
# Apply the toGeoJSON method to the MultiPoint object.
multipoint_to_geojson = multipoint.toGeoJSON()
# Print the result.
display('multipoint.toGeoJSON(...) =', multipoint_to_geojson)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m
```

