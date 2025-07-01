 
#  ee.Feature.dissolve
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a feature containing the union of the geometry of a feature. This leaves single geometries untouched, and unions multi geometries. 
Usage| Returns  
---|---  
`Feature.dissolve( _maxError_, _proj_)`| Element  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| The feature the geometry of which is being unioned.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
Was this helpful?
