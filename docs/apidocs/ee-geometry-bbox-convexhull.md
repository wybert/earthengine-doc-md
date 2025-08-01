 
#  ee.Geometry.BBox.convexHull
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-convexhull#examples)


Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.
Usage | Returns  
---|---  
`BBox.convexHull(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Calculates the convex hull of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-convexhull#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-bbox-convexhull#colab-python-sample) More
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);

// Apply the convexHull method to the BBox object.
varbBoxConvexHull=bBox.convexHull({'maxError':1});

// Print the result to the console.
print('bBox.convexHull(...) =',bBoxConvexHull);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(bBox,
{'color':'black'},
'Geometry [black]: bBox');
Map.addLayer(bBoxConvexHull,
{'color':'red'},
'Result [red]: bBox.convexHull');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a BBox object.
bbox = ee.Geometry.BBox(-122.09, 37.42, -122.08, 37.43)

# Apply the convexHull method to the BBox object.
bbox_convex_hull = bbox.convexHull(maxError=1)

# Print the result.
display('bbox.convexHull(...) =', bbox_convex_hull)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m.add_layer(
    bbox_convex_hull, {'color': 'red'}, 'Result [red]: bbox.convexHull'
)
m
```

Was this helpful?
