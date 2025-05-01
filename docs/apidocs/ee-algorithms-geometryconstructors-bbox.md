 
#  ee.Algorithms.GeometryConstructors.BBox 
Stay organized with collections  Save and categorize content based on your preferences. 
Constructs a rectangle whose edges are lines of latitude and longitude. 
The result is a planar WGS84 rectangle.
If (east - west) ≥ 360 then the longitude range will be normalized to -180 to +180; otherwise they will be treated as designating points on a circle (e.g., east may be numerically less than west).
Usage| Returns  
---|---  
`ee.Algorithms.GeometryConstructors.BBox(west, south, east, north)`| Geometry  
Argument| Type| Details  
---|---|---  
`west`| Float| The westernmost enclosed longitude. Will be adjusted to lie in the range -180 to 180.  
`south`| Float| The southernmost enclosed latitude. If less than -90 (south pole), will be treated as -90.  
`east`| Float| The easternmost enclosed longitude.  
`north`| Float| The northernmost enclosed latitude. If greater than +90 (north pole), will be treated as +90.  
