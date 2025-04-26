 
#  ee.Geometry.MultiPoint 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Constructs an ee.Geometry describing a MultiPoint. 
For convenience, varargs may be used when all arguments are numbers. This allows creating EPSG:4326 MultiPoints given an even number of arguments, e.g. ee.Geometry.MultiPoint(aLng, aLat, bLng, bLat, ...).
Usage| Returns  
---|---  
`ee.Geometry.MultiPoint(coords,  _proj_)`| Geometry.MultiPoint  
Argument| Type| Details  
---|---|---  
`coords`| List| A list of points, each in the GeoJSON 'coordinates' format of a Point, or a list of the x,y coordinates in the given projection, or an ee.Geometry describing a point.  
`proj`| Projection, optional| The projection of this geometry. If unspecified, the default is the projection of the input ee.Geometry, or EPSG:4326 if there are no ee.Geometry inputs.  
