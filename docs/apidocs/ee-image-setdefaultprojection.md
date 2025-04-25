 
#  ee.Image.setDefaultProjection 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Set a default projection to be applied to this image. The projection's resolution may be overridden by later operations. 
Usage| Returns  
---|---  
`Image.setDefaultProjection(crs,  _crsTransform_, _scale_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to reproject.  
`crs`| Projection| The CRS to project the image to.  
`crsTransform`| List, default: null| The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with the scale option, and replaces any transform already on the projection.  
`scale`| Float, default: null| If scale is specified, then the projection is scaled by dividing the specified scale value by the nominal size of a meter in the specified projection. If scale is not specified, then the scale of the given projection will be used.  
Was this helpful?
