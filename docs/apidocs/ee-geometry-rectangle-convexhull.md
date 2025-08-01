 
#  ee.Geometry.Rectangle.convexHull
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-convexhull#examples)


Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.
Usage | Returns  
---|---  
`Rectangle.convexHull(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Calculates the convex hull of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-convexhull#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-rectangle-convexhull#colab-python-sample) More
```
// Define a Rectangle object.
varrectangle=ee.Geometry.Rectangle(-122.09,37.42,-122.08,37.43);

// Apply the convexHull method to the Rectangle object.
varrectangleConvexHull=rectangle.convexHull({'maxError':1});

// Print the result to the console.
print('rectangle.convexHull(...) =',rectangleConvexHull);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(rectangle,
{'color':'black'},
'Geometry [black]: rectangle');
Map.addLayer(rectangleConvexHull,
{'color':'red'},
'Result [red]: rectangle.convexHull');
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

# Apply the convexHull method to the Rectangle object.
rectangle_convex_hull = rectangle.convexHull(maxError=1)

# Print the result.
display('rectangle.convexHull(...) =', rectangle_convex_hull)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(rectangle, {'color': 'black'}, 'Geometry [black]: rectangle')
m.add_layer(
    rectangle_convex_hull,
    {'color': 'red'},
    'Result [red]: rectangle.convexHull',
)
m
```

