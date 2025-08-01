 
#  ee.Geometry.Rectangle.centroid
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-centroid#examples)


Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.
Usage | Returns  
---|---  
`Rectangle.centroid(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Calculates the centroid of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-centroid#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-centroid#colab-python-sample) More
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);

// Apply the centroid method to the Rectangle object.
varrectangleCentroid=rectangle.centroid({'maxError':1});

// Print the result to the console.
print('rectangle.centroid(...) =',rectangleCentroid);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(rectangle,
{'color':'black'},
'Geometry [black]: rectangle');
Map.addLayer(rectangleCentroid,
{'color':'red'},
'Result [red]: rectangle.centroid');
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

# Apply the centroid method to the Rectangle object.
rectangle_centroid = rectangle.centroid(maxError=1)

# Print the result.
display('rectangle.centroid(...) =', rectangle_centroid)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m.add_layer(
    rectangle_centroid, {'color': 'red'}, 'Result [red]: rectangle.centroid'
)
m
```

Was this helpful?
