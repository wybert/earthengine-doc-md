 
#  ee.Geometry.Rectangle.toGeoJSONString
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-togeojsonstring#examples)


Usage | Returns  
---|---  
`Rectangle.toGeoJSONString()` | String  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The Geometry instance.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-togeojsonstring#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-togeojsonstring#colab-python-sample) More
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);

// Apply the toGeoJSONString method to the Rectangle object.
varrectangleToGeoJSONString=rectangle.toGeoJSONString();

// Print the result to the console.
print('rectangle.toGeoJSONString(...) =',rectangleToGeoJSONString);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(rectangle,
{'color':'black'},
'Geometry [black]: rectangle');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a Rectangle object.
rectangle = ee.Geometry.Rectangle(-122.09, 37.42, -122.08, 37.43)

# Apply the toGeoJSONString method to the Rectangle object.
rectangle_to_geojson_string = rectangle.toGeoJSONString()

# Print the result.
display('rectangle.toGeoJSONString(...) =', rectangle_to_geojson_string)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m
```

