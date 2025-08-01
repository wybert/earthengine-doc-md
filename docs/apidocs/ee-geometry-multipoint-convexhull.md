 
#  ee.Geometry.MultiPoint.convexHull
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-convexhull#examples)


Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment.
Usage | Returns  
---|---  
`MultiPoint.convexHull(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Calculates the convex hull of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-convexhull#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-convexhull#colab-python-sample) More
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);

// Apply the convexHull method to the MultiPoint object.
varmultiPointConvexHull=multiPoint.convexHull({'maxError':1});

// Print the result to the console.
print('multiPoint.convexHull(...) =',multiPointConvexHull);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPoint,
{'color':'black'},
'Geometry [black]: multiPoint');
Map.addLayer(multiPointConvexHull,
{'color':'red'},
'Result [red]: multiPoint.convexHull');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a MultiPoint object.
multipoint = ee.Geometry.MultiPoint([[-122.082, 37.420], [-122.081, 37.426]])

# Apply the convexHull method to the MultiPoint object.
multipoint_convex_hull = multipoint.convexHull(maxError=1)

# Print the result.
display('multipoint.convexHull(...) =', multipoint_convex_hull)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m.add_layer(
    multipoint_convex_hull,
    {'color': 'red'},
    'Result [red]: multipoint.convexHull',
)
m
```

Was this helpful?
