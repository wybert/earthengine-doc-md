 
#  ee.Geometry.convexHull 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-convexhull#examples)


Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment. 
Usage| Returns  
---|---  
`Geometry.convexHull( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Calculates the convex hull of this geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-convexhull#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-convexhull#colab-python-sample) More
```
// Define a Geometry object.
vargeometry=ee.Geometry({
'type':'Polygon',
'coordinates':
[[[-122.081,37.417],
[-122.086,37.421],
[-122.084,37.418],
[-122.089,37.416]]]
});
// Apply the convexHull method to the Geometry object.
vargeometryConvexHull=geometry.convexHull({'maxError':1});
// Print the result to the console.
print('geometry.convexHull(...) =',geometryConvexHull);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
Map.addLayer(geometryConvexHull,
{'color':'red'},
'Result [red]: geometry.convexHull');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a Geometry object.
geometry = ee.Geometry({
  'type': 'Polygon',
  'coordinates': [[
    [-122.081, 37.417],
    [-122.086, 37.421],
    [-122.084, 37.418],
    [-122.089, 37.416],
  ]],
})
# Apply the convexHull method to the Geometry object.
geometry_convex_hull = geometry.convexHull(maxError=1)
# Print the result.
display('geometry.convexHull(...) =', geometry_convex_hull)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m.add_layer(
  geometry_convex_hull, {'color': 'red'}, 'Result [red]: geometry.convexHull'
)
m
```

Was this helpful?
