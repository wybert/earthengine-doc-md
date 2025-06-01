 
#  ee.Geometry.Rectangle.serialize 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the serialized representation of this object. 
Usage| Returns  
---|---  
`Rectangle.serialize( _legacy_)`| String  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The Geometry instance.  
`legacy`| Boolean, optional| Enables legacy format.  
## Examples
### Code Editor (JavaScript)
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);
// Apply the serialize method to the Rectangle object.
varrectangleSerialize=rectangle.serialize();
// Print the result to the console.
print('rectangle.serialize(...) =',rectangleSerialize);
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
# Apply the serialize method to the Rectangle object.
rectangle_serialize = rectangle.serialize()
# Print the result.
display('rectangle.serialize(...) =', rectangle_serialize)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m
```

