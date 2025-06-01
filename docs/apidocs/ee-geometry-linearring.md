 
#  ee.Geometry.LinearRing 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Constructs an ee.Geometry describing a LinearRing. If the last point is not equal to the first, a duplicate of the first point will be added at the end. 
For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 LinearRings given an even number of arguments, e.g. ee.Geometry.LinearRing(aLng, aLat, bLng, bLat, ..., aLng, aLat).
Usage| Returns  
---|---  
`ee.Geometry.LinearRing(coords,  _proj_, _geodesic_, _maxError_)`| Geometry.LinearRing  
Argument| Type| Details  
---|---|---  
`coords`| List| A list of points in the ring. May be a list of coordinates in the GeoJSON 'LinearRing' format, a list of at least three ee.Geometry objects describing a point, or a list of at least six numbers defining the [x,y] coordinates of at least three points.  
`proj`| Projection, optional| The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs.  
`geodesic`| Boolean, optional| If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`maxError`| ErrorMargin, optional| Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state.  
Was this helpful?
