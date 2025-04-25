 
#  ee.Feature.withinDistance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns true if and only if the geometries of two features are within a specified distance. 
Usage| Returns  
---|---  
`Feature.withinDistance(right, distance,  _maxError_, _proj_)`| Boolean  
Argument| Type| Details  
---|---|---  
this: `left`| Element| The feature containing the geometry used as the left operand of the operation.  
`right`| Element| The feature containing the geometry used as the right operand of the operation.  
`distance`| Float| The distance threshold. If a projection is specified, the distance is in units of that projected coordinate system, otherwise it is in meters.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
Was this helpful?
