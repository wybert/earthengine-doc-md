 
#  ee.Image.getThumbURL 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Get a thumbnail URL for this image. 
Returns a thumbnail URL, or undefined if a callback was specified.
Usage| Returns  
---|---  
`Image.getThumbURL(params,  _callback_)`| Object|String  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`params`| Object| Parameters identical to ee.data.getMapId, plus, optionally:  | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of the thumbnail to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling.  
---  
` region ` Geospatial region of the image to render, it may be an ee.Geometry, GeoJSON, or an array of lat/lon points (E,S,W,N). If not set the default is the bounds image.  
` format ` (string) Either 'png' or 'jpg'.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
Was this helpful?
