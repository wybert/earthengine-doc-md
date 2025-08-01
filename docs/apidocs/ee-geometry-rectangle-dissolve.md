 
#  ee.Geometry.Rectangle.dissolve
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-dissolve#examples)


Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries.
Usage | Returns  
---|---  
`Rectangle.dissolve(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The geometry to union.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-dissolve#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-dissolve#colab-python-sample) More
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);

// Apply the dissolve method to the Rectangle object.
varrectangleDissolve=rectangle.dissolve({'maxError':1});

// Print the result to the console.
print('rectangle.dissolve(...) =',rectangleDissolve);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(rectangle,
{'color':'black'},
'Geometry [black]: rectangle');
Map.addLayer(rectangleDissolve,
{'color':'red'},
'Result [red]: rectangle.dissolve');
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

# Apply the dissolve method to the Rectangle object.
rectangle_dissolve = rectangle.dissolve(maxError=1)

# Print the result.
display('rectangle.dissolve(...) =', rectangle_dissolve)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m.add_layer(
    rectangle_dissolve, {'color': 'red'}, 'Result [red]: rectangle.dissolve'
)
m
```

Was this helpful?
