 
#  ee.ImageCollection.distance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Produces a DOUBLE image where each pixel is the distance in meters from the pixel center to the nearest Point, LineString, or polygonal boundary in the collection. Note distance is also measured within interiors of polygons. Pixels that are not within 'searchRadius' meters of a geometry will be masked out. 
Distances are computed on a sphere, so there is a small error proportional to the latitude difference between each pixel and the nearest geometry.
Usage| Returns  
---|---  
`ImageCollection.distance( _searchRadius_, _maxError_)`| Image  
Argument| Type| Details  
---|---|---  
this: `features`| FeatureCollection| Feature collection from which to get features used to compute pixel distances.  
`searchRadius`| Float, default: 100000| Maximum distance in meters from each pixel to look for edges. Pixels will be masked unless there are edges within this distance.  
`maxError`| Float, default: 100| Maximum reprojection error in meters, only used if the input polylines require reprojection. If '0' is provided, then this operation will fail if projection is required.  
