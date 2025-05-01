 
#  ee.ImageCollection.bounds 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Constructs a bounding box around the geometries in a collection. 
Usage| Returns  
---|---  
`ImageCollection.bounds( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection whose bounds will be constructed.  
`maxError`| ErrorMargin, optional| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, optional| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
