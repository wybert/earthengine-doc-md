 
#  ee.Algorithms.GeometryConstructors.MultiLineString
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Constructs a MultiLineString from the given coordinates. 
Usage| Returns  
---|---  
`ee.Algorithms.GeometryConstructors.MultiLineString(coordinates,  _crs_, _geodesic_, _maxError_)`| Geometry  
Argument| Type| Details  
---|---|---  
`coordinates`| List| The list of LineStrings, or to wrap a single LineString, the list of Points or pairs of Numbers in x,y order.  
`crs`| Projection, default: null| The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326.  
`geodesic`| Boolean, default: null| If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`maxError`| ErrorMargin, default: null| Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state.  
Was this helpful?
