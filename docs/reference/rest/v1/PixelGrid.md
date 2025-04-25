 
#  PixelGrid 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Defines a pixel grid on the surface of the Earth, via a map projection. If the projection has a standard code, then `crsCode` will be set (non-empty). If the projection is non-standard, then `crsWkt` will be set. If the post-projection transformation is affine, then `affineTransform` will be set.
JSON representation  
---  
```
{
 "dimensions": {
  object (GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions))
 },
 "affineTransform": {
  object (AffineTransform[](https://developers.google.com/earth-engine/reference/rest/v1/AffineTransform))
 },
 // Union field crs can be only one of the following:
 "crsCode": string,
 "crsWkt": string
 // End of list of possible types for union field crs.
}
```
  
Fields  
---  
`dimensions` |  `object (`GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions)`)` The dimensions of the pixel grid.  
`affineTransform` |  `object (`AffineTransform[](https://developers.google.com/earth-engine/reference/rest/v1/AffineTransform)`)` The affine transform.  
Union field `crs`. The coordinate reference system of the pixel grid, specified as a standard code where possible, and in WKT format otherwise. `crs` can be only one of the following:  
`crsCode` |  `string` A standard coordinate reference system code (e.g. "EPSG:4326").  
`crsWkt` |  `string` A coordinate reference system in WKT format ("Well-Known Text").  
