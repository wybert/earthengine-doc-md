 
#  ee.Feature.bounds 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns a feature containing the bounding box of the geometry of a given feature. 
Usage| Returns  
---|---  
`Feature.bounds( _maxError_, _proj_)`| Feature  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| The feature the bound of which is being calculated.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
