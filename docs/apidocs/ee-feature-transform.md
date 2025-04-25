 
#  ee.Feature.transform 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Transforms the geometry of a feature to a specific projection. 
Usage| Returns  
---|---  
`Feature.transform( _proj_, _maxError_)`| Feature  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| The feature the geometry of which is being converted.  
`proj`| Projection, optional| The target projection. Defaults to EPSG:4326. If this has a geographic CRS, the edges of the geometry will be interpreted as geodesics. Otherwise they will be interpreted as straight lines in the projection.  
`maxError`| ErrorMargin, default: null| The maximum projection error.  
