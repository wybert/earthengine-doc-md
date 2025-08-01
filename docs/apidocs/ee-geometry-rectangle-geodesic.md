 
#  ee.Geometry.Rectangle.geodesic
Stay organized with collections  Save and categorize content based on your preferences. 
If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. Usage | Returns  
---|---  
`Rectangle.geodesic()` | Boolean  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry |   
## Examples
### Code Editor (JavaScript)
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);

// Apply the geodesic method to the Rectangle object.
varrectangleGeodesic=rectangle.geodesic();

// Print the result to the console.
print('rectangle.geodesic(...) =',rectangleGeodesic);

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

# Apply the geodesic method to the Rectangle object.
rectangle_geodesic = rectangle.geodesic()

# Print the result.
display('rectangle.geodesic(...) =', rectangle_geodesic)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m
```

