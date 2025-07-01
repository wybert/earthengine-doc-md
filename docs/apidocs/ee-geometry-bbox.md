 
#  ee.Geometry.BBox
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Constructs a rectangle whose edges are lines of latitude and longitude. 
The result is a planar rectangle in EPSG:4326.
If (east - west) ≥ 360 then the longitude range will be normalized to -180 to
+180; otherwise they will be treated as designating points on a circle (e.g. east may be numerically less than west).
Usage| Returns  
---|---  
`ee.Geometry.BBox(west, south, east, north)`| Geometry.BBox  
Argument| Type| Details  
---|---|---  
`west`| Number| The westernmost enclosed longitude. Will be adjusted to lie in the range -180° to 180°.  
`south`| Number| The southernmost enclosed latitude. If less than -90° (south pole), will be treated as -90°.  
`east`| Number| The easternmost enclosed longitude.  
`north`| Number| The northernmost enclosed latitude. If greater than +90° (north pole), will be treated as +90°.  
