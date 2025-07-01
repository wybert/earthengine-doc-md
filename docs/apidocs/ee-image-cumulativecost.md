 
#  ee.Image.cumulativeCost
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes a cumulative cost map based on an image containing costs to traverse each pixel and an image containing source locations. 
Each output band represents the cumulative cost over the corresponding input cost band.
Usage| Returns  
---|---  
`Image.cumulativeCost(source, maxDistance,  _geodeticDistance_)`| Image  
Argument| Type| Details  
---|---|---  
this: `cost`| Image| An image representing the cost to traverse each pixel. Masked pixels can't be traversed. When comparing pixel traversal costs, we use band-wise dictionary ordering. Ancillary cost bands are only considered when paths over primary bands are equal cost.  
`source`| Image| A single-band image representing the sources. A pixel value different from 0 defines a source pixel.  
`maxDistance`| Float| Maximum distance for computation, in meters.  
`geodeticDistance`| Boolean, default: true| If true, geodetic distance along the curved surface is used, assuming a spherical Earth of radius 6378137.0. If false, Euclidean distance in the 2D plane of the map projection is used (faster, but less accurate).  
Was this helpful?
