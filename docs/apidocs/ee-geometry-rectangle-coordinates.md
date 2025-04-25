 
#  ee.Geometry.Rectangle.coordinates 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-coordinates#examples)


Returns a GeoJSON-style list of the geometry's coordinates. 
Usage| Returns  
---|---  
`Rectangle.coordinates()`| List  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-coordinates#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-coordinates#colab-python-sample) More
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);
// Apply the coordinates method to the Rectangle object.
varrectangleCoordinates=rectangle.coordinates();
// Print the result to the console.
print('rectangle.coordinates(...) =',rectangleCoordinates);
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
# Apply the coordinates method to the Rectangle object.
rectangle_coordinates = rectangle.coordinates()
# Print the result.
display('rectangle.coordinates(...) =', rectangle_coordinates)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m
```

