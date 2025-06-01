 
#  ee.Geometry.Polygon.toGeoJSONString 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-togeojsonstring#examples)


Returns a GeoJSON string representation of the geometry. 
Usage| Returns  
---|---  
`Polygon.toGeoJSONString()`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-togeojsonstring#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon-togeojsonstring#colab-python-sample) More
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);
// Apply the toGeoJSONString method to the Polygon object.
varpolygonToGeoJSONString=polygon.toGeoJSONString();
// Print the result to the console.
print('polygon.toGeoJSONString(...) =',polygonToGeoJSONString);
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
# Apply the toGeoJSONString method to the Polygon object.
polygon_to_geojson_string = polygon.toGeoJSONString()
# Print the result.
display('polygon.toGeoJSONString(...) =', polygon_to_geojson_string)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m
```

Was this helpful?
