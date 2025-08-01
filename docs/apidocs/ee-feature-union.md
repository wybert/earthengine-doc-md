 
#  ee.Feature.union
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a feature containing the union of the geometries of two features. Usage | Returns  
---|---  
`Feature.union(right, _maxError_, _proj_)`|  Feature  
Argument | Type | Details  
---|---|---  
this: `left` | Element | The feature containing the geometry used as the left operand of the operation. The properties of the result will be copied from this object.  
`right` | Element | The feature containing the geometry used as the right operand of the operation. The properties of this object are ignored.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
