 
#  ee.Image.getInfo 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
An imperative function that returns information about this image via an AJAX call. 
Returns a description of the image. Includes:
- bands - a list containing metadata about the bands in the collection.
- properties - a dictionary containing the image's metadata properties.
Usage| Returns  
---|---  
`Image.getInfo( _callback_)`| ImageDescription  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful.  
Was this helpful?
