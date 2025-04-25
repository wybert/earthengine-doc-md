 
#  ee.Feature.geometry 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the geometry of a given feature in a given projection. 
Usage| Returns  
---|---  
`Feature.geometry( _maxError_, _proj_, _geodesics_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| The feature from which the geometry is taken.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the geometry will be in this projection. If unspecified, the geometry will be in its default projection.  
`geodesics`| Boolean, default: null| If true, the geometry will have geodesic edges. If false, it will have edges as straight lines in the specified projection. If null, the edge interpretation will be the same as the original geometry. This argument is ignored if proj is not specified.  
Was this helpful?
