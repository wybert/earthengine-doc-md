 
#  ee.Feature.cutLines 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString. 
Usage| Returns  
---|---  
`Feature.cutLines(distances,  _maxError_, _proj_)`| Feature  
Argument| Type| Details  
---|---|---  
this: `feature`| Element| Cuts the lines of this feature's default geometry.  
`distances`| List| Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| Projection of the result and distance measurements, or EPSG:4326 if unspecified.  
Was this helpful?
