 
#  ee.Feature.centroid 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a feature containing the point at the center of the highest-dimension components of the geometry of a feature. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons. 
Usage| Returns  
---|---  
`Feature.centroid( _maxError_, _proj_)`| Feature  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| Calculates the centroid of this feature's default geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
