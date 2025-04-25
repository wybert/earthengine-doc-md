 
#  ee.Geometry.MultiLineString.toGeoJSONString 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-togeojsonstring#examples)


Returns a GeoJSON string representation of the geometry. 
Usage| Returns  
---|---  
`MultiLineString.toGeoJSONString()`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-togeojsonstring#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-togeojsonstring#colab-python-sample) More
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);
// Apply the toGeoJSONString method to the MultiLineString object.
varmultiLineStringToGeoJSONString=multiLineString.toGeoJSONString();
// Print the result to the console.
print('multiLineString.toGeoJSONString(...) =',multiLineStringToGeoJSONString);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a MultiLineString object.
multilinestring = ee.Geometry.MultiLineString([
  [[-122.088, 37.418], [-122.086, 37.422], [-122.082, 37.418]],
  [[-122.087, 37.416], [-122.083, 37.416], [-122.082, 37.419]],
])
# Apply the toGeoJSONString method to the MultiLineString object.
multilinestring_to_geojson_string = multilinestring.toGeoJSONString()
# Print the result.
display(
  'multilinestring.toGeoJSONString(...) =', multilinestring_to_geojson_string
)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m
```

Was this helpful?
