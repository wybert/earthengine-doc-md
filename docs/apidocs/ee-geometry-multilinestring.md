 
#  ee.Geometry.MultiLineString 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Constructs an ee.Geometry describing a MultiLineString. 
For convenience, varargs may be used when all arguments are numbers. This allows creating geodesic EPSG:4326 MultiLineStrings with a single LineString, given an even number of arguments, e.g. ee.Geometry.MultiLineString(aLng, aLat, bLng, bLat, ...).
Usage| Returns  
---|---  
`ee.Geometry.MultiLineString(coords,  _proj_, _geodesic_, _maxError_)`| Geometry.MultiLineString  
Argument| Type| Details  
---|---|---  
`coords`| List| A list of linestrings. May be a list of coordinates in the GeoJSON 'MultiLineString' format, a list of at least two ee.Geometry objects describing a LineString, or a list of numbers defining a single linestring.  
`proj`| Projection, optional| The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs.  
`geodesic`| Boolean, optional| If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`maxError`| ErrorMargin, optional| Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state.  
Was this helpful?
