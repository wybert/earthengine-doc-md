 
#  AffineTransform
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
The affine transform. The six values form a 2x3 matrix:
```
( ( scaleX, shearX, translateX )
 ( shearY, scaleY, translateY ) )

```

specifying a transformation such that given a pixel location `(u, v)`, the corresponding location in the CRS is this matrix times the column vector `(u, v, 1)`. Pixel coordinates use the "PixelIsArea" raster space, i.e. `(0, 0)` is the top-left corner of the top-left pixel, and `(width, height)` is the bottom-right corner of the image. `(translateX, translateY)` is the origin (in the CRS) of the pixel grid. If there is no shear or rotation, then `(scaleX, scaleY)` is the pixel size. `scaleY` is often negative so that the `(0, 0)` pixel corner can represent the north-westernmost corner of the image.
JSON representation  
---  
```
{
 "scaleX": number,
 "shearX": number,
 "translateX": number,
 "shearY": number,
 "scaleY": number,
 "translateY": number
}
```
  
Fields  
---  
`scaleX` |  `number` The horizontal scale factor.  
`shearX` |  `number` The horizontal shear factor for some, though not all, transformations.  
`translateX` |  `number` The horizontal offset.  
`shearY` |  `number` The vertical shear factor for some, though not all, transformations.  
`scaleY` |  `number` The vertical scale factor.  
`translateY` |  `number` The vertical offset.  
