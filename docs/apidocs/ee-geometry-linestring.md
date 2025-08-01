 
#  ee.Geometry.LineString
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 LineStrings given an even number of arguments, e.g. ee.Geometry.LineString(aLng, aLat, bLng, bLat, ...).
Usage | Returns  
---|---  
`ee.Geometry.LineString(coords, _proj_, _geodesic_, _maxError_)`|  Geometry.LineString  
Argument | Type | Details  
---|---|---  
`coords` | List<Geometry>|List<List<Number>>|List<Number> | A list of at least two points. May be a list of coordinates in the GeoJSON 'LineString' format, a list of at least two ee.Geometry objects describing a point, or a list of at least four numbers defining the [x,y] coordinates of at least two points.  
`proj` | Projection, optional | The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs.  
`geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`maxError` | ErrorMargin, optional | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state.  
Was this helpful?
