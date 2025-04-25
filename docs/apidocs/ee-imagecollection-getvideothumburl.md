 
#  ee.ImageCollection.getVideoThumbURL 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Get the URL of an animated thumbnail for this ImageCollection. 
Returns a thumbnail URL, or undefined if a callback was specified.
Usage| Returns  
---|---  
`ImageCollection.getVideoThumbURL(params,  _callback_)`| Object|String  
Argument| Type| Details  
---|---|---  
this: `imagecollection`| ImageCollection| The ImageCollection instance.  
`params`| Object| Parameters identical to ee.data.getMapId, plus, optionally:  | ` dimensions ` (a number or pair of numbers in format WIDTHxHEIGHT) Maximum dimensions of the thumbnail to render, in pixels. If only one number is passed, it is used as the maximum, and the other dimension is computed by proportional scaling.  
---  
` region ` (E,S,W,N or GeoJSON) Geospatial region of the image to render. By default, the whole image.  
` format ` (string) Encoding format. Only 'gif' is accepted.  
` framesPerSecond ` (number) Animation speed.  
`callback`| Function, optional| An optional callback which handles the resulting URL string. If not supplied, the call is made synchronously.  
Was this helpful?
