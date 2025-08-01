 
#  ee.Geometry.MultiPolygon
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 MultiPolygons with a single Polygon with a single LinearRing given an even number of arguments, e.g. ee.Geometry.MultiPolygon(aLng, aLat, bLng, bLat, ..., aLng, aLat).
Usage | Returns  
---|---  
`ee.Geometry.MultiPolygon(coords, _proj_, _geodesic_, _maxError_, _evenOdd_)`|  Geometry.MultiPolygon  
Argument | Type | Details  
---|---|---  
`coords` | List<Geometry>|List<List<List<List<Number>>>>|List<Number> | A list of polygons. May be a list of coordinates in the GeoJSON 'MultiPolygon' format, a list of ee.Geometry objects describing a Polygon, or a list of numbers defining a single polygon boundary.  
`proj` | Projection, optional | The projection of this geometry. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326.  
`geodesic` | Boolean, optional | If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`maxError` | ErrorMargin, optional | Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state.  
`evenOdd` | Boolean, optional | If true, polygon interiors will be determined by the even/odd rule, where a point is inside if it crosses an odd number of edges to reach a point at infinity. Otherwise polygons use the left- inside rule, where interiors are on the left side of the shell's edges when walking the vertices in the given order. If unspecified, defaults to true.  
Was this helpful?
