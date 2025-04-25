 
#  ee.Geometry.Rectangle.projection 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the projection of the geometry. Usage| Returns  
---|---  
`Rectangle.projection()`| Projection  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
### Code Editor (JavaScript)
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);
// Apply the projection method to the Rectangle object.
varrectangleProjection=rectangle.projection();
// Print the result to the console.
print('rectangle.projection(...) =',rectangleProjection);
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

### Colab (Python)
```
# Define a Rectangle object.
rectangle = ee.Geometry.Rectangle(-122.09, 37.42, -122.08, 37.43)
# Apply the projection method to the Rectangle object.
rectangle_projection = rectangle.projection()
# Print the result.
display('rectangle.projection(...) =', rectangle_projection)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m
```

