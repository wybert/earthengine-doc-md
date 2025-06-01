 
#  ee.Geometry.Point.coveringGrid 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns a collection of features that cover this geometry, where each feature is a rectangle in the grid defined by the given projection. 
Usage| Returns  
---|---  
`Point.coveringGrid(proj,  _scale_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The result is the grid cells that intersect with this region.  
`proj`| Projection| The projection in which to construct the grid. A feature is generated for each grid cell that intersects 'geometry', where cell corners are at integer-valued positions in the projection. If the projection is scaled in meters, the points will be on a grid of that size at the point of true scale.  
`scale`| Float, default: null| Overrides the scale of the projection, if provided. May be required if the projection isn't already scaled.  
