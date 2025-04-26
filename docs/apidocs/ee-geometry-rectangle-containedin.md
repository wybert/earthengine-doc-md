 
#  ee.Geometry.Rectangle.containedIn 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns true if and only if one geometry is contained in the other. 
Usage| Returns  
---|---  
`Rectangle.containedIn(right,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
### Code Editor (JavaScript)
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);
// Define other inputs.
varinputGeom=ee.Geometry.BBox(-122.085,37.415,-122.075,37.425);
// Apply the containedIn method to the Rectangle object.
varrectangleContainedIn=rectangle.containedIn({'right':inputGeom,'maxError':1});
// Print the result to the console.
print('rectangle.containedIn(...) =',rectangleContainedIn);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(rectangle,
{'color':'black'},
'Geometry [black]: rectangle');
Map.addLayer(inputGeom,
{'color':'blue'},
'Parameter [blue]: inputGeom');
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
# Define other inputs.
input_geom = ee.Geometry.BBox(-122.085, 37.415, -122.075, 37.425)
# Apply the containedIn method to the Rectangle object.
rectangle_contained_in = rectangle.containedIn(right=input_geom, maxError=1)
# Print the result.
display('rectangle.containedIn(...) =', rectangle_contained_in)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m.add_layer(input_geom, {'color': 'blue'}, 'Parameter [blue]: input_geom')
m
```

