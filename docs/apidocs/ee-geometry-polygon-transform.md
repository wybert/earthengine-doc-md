 
#  ee.Geometry.Polygon.transform
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Transforms the geometry to a specific projection. 
Usage| Returns  
---|---  
`Polygon.transform( _proj_, _maxError_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry to reproject.  
`proj`| Projection, optional| The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection.  
`maxError`| ErrorMargin, default: null| The maximum projection error.  
Was this helpful?
