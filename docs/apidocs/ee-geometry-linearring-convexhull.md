 
#  ee.Geometry.LinearRing.convexHull
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the convex hull of the given geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment. Usage| Returns  
---|---  
`LinearRing.convexHull( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Calculates the convex hull of this geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
## Examples
### Code Editor (JavaScript)
```
// Define a LinearRing object.
varlinearRing=ee.Geometry.LinearRing(
[[-122.091,37.420],
[-122.085,37.422],
[-122.080,37.430]]);
// Apply the convexHull method to the LinearRing object.
varlinearRingConvexHull=linearRing.convexHull({'maxError':1});
// Print the result to the console.
print('linearRing.convexHull(...) =',linearRingConvexHull);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(linearRing,
{'color':'black'},
'Geometry [black]: linearRing');
Map.addLayer(linearRingConvexHull,
{'color':'red'},
'Result [red]: linearRing.convexHull');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a LinearRing object.
linearring = ee.Geometry.LinearRing(
  [[-122.091, 37.420], [-122.085, 37.422], [-122.080, 37.430]]
)
# Apply the convexHull method to the LinearRing object.
linearring_convex_hull = linearring.convexHull(maxError=1)
# Print the result.
display('linearring.convexHull(...) =', linearring_convex_hull)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linearring, {'color': 'black'}, 'Geometry [black]: linearring')
m.add_layer(
  linearring_convex_hull,
  {'color': 'red'},
  'Result [red]: linearring.convexHull',
)
m
```

