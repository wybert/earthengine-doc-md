 
#  ee.Geometry.MultiPoint.closestPoints
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a dictionary containing up to two entries representing a point on each input geometry that is closest to the other input geometry. If either geometry is empty, an empty dictionary is returned. If both geometries are unbounded, the dictionary has an arbitrary point for both 'left' and 'right'. If one geometry is unbounded, the dictionary has an arbitrary point contained in the bounded geometry for both 'left' and 'right'.
Usage | Returns  
---|---  
`MultiPoint.closestPoints(right, _maxError_, _proj_)`|  Object  
Argument | Type | Details  
---|---|---  
this: `left` | Geometry | The geometry used as the left operand of the operation.  
`right` | Geometry | The geometry used as the right operand of the operation.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
