 
#  ee.Feature.area
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the area of the feature's default geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times). Usage| Returns  
---|---  
`Feature.area( _maxError_, _proj_)`| Float  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| The feature from which the geometry is taken.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters.  
