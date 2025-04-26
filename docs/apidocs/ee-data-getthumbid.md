 
#  ee.data.getThumbId 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Get a Thumbnail Id for a given asset. 
Returns the thumb ID and optional token, or null if a callback is specified.
Usage| Returns  
---|---  
`ee.data.getThumbId(params,  _callback_)`| ThumbnailId  
Argument| Type| Details  
---|---|---  
`params`| ThumbnailOptions| An object containing thumbnail options with the following possible values:  | ` image ` (ee.Image) The image to make a thumbnail.  
---  
` bands ` (array of strings) An array of band names.  
` format ` (string) The file format ("png", "jpg", "geotiff").  
` name ` (string): The base name.  
Use ee.Image.getThumbURL for region, dimensions, and visualization options support.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
Was this helpful?
