 
#  ee.Algorithms.GeometryConstructors.MultiGeometry
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs a MultiGeometry from the given list of geometry elements. Usage| Returns  
---|---  
`ee.Algorithms.GeometryConstructors.MultiGeometry(geometries,  _crs_, _geodesic_, _maxError_)`| Geometry  
Argument| Type| Details  
---|---|---  
`geometries`| List| The list of geometries for the MultiGeometry.  
`crs`| Projection, default: null| The coordinate reference system of the coordinates. The default is the projection of the inputs, where Numbers are assumed to be EPSG:4326.  
`geodesic`| Boolean, default: null| If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. The default is the geodesic state of the inputs, or true if the inputs are numbers.  
`maxError`| ErrorMargin, default: null| Max error when input geometry must be reprojected to an explicitly requested result projection or geodesic state.  
