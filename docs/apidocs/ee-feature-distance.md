 
#  ee.Feature.distance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the minimum distance between the geometries of two features. 
Usage| Returns  
---|---  
`Feature.distance(right,  _maxError_, _proj_, _spherical_)`| Float  
Argument| Type| Details  
---|---|---  
this: `left`| Element| The feature containing the geometry used as the left operand of the operation.  
`right`| Element| The feature containing the geometry used as the right operand of the operation.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
`spherical`| Boolean, default: false| When proj is not specified, if true the calculation will be done on the unit sphere. If false the calculation will be elliptical, taking earth flattening into account. Ignored if proj is specified. Default is false.  
Was this helpful?
