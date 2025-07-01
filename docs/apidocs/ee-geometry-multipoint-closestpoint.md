 
#  ee.Geometry.MultiPoint.closestPoint
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the point on the right input that is nearest to the left input. If either input is empty, null is returned. If both inputs are unbounded, an arbitrary point is returned. If one input is unbounded, an arbitrary point in the bounded input is returned. 
Usage| Returns  
---|---  
`MultiPoint.closestPoint(right,  _maxError_, _proj_)`| Object  
Argument| Type| Details  
---|---|---  
this: `left`| Geometry| The geometry used as the left operand of the operation.  
`right`| Geometry| The geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
Was this helpful?
