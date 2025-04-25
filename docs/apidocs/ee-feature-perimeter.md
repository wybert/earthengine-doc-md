 
#  ee.Feature.perimeter 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the length of the perimeter of the polygonal parts of the geometry of a given feature. The perimeter of multi geometries is the sum of the perimeters of their components. 
Usage| Returns  
---|---  
`Feature.perimeter( _maxError_, _proj_)`| Float  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| The feature from which the geometry is taken.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters.  
