 
#  ee.Feature.convexHull 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the feature with the geometry replaced by the convex hull of the original geometry. The convex hull of a single point is the point itself, the convex hull of collinear points is a line, and the convex hull of everything else is a polygon. Note that a degenerate polygon with all vertices on the same line will result in a line segment. Usage| Returns  
---|---  
`Feature.convexHull( _maxError_, _proj_)`| Feature  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| The feature containing the geometry whole hull is being calculated.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| The projection in which to perform the operation. If not specified, the operation will be performed in a spherical coordinate system, and linear distances will be in meters on the sphere.  
