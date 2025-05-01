 
#  ee.ImageCollection.getInfo 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
An imperative function that returns all the known information about this collection via an AJAX call. 
Returns a collection description whose fields include:
- features: a list containing metadata about the images in the collection.
- bands: a dictionary describing the bands of the images in this collection.
- properties: an optional dictionary containing the collection's metadata properties.
Usage| Returns  
---|---  
`ImageCollection.getInfo( _callback_)`| ImageCollectionDescription  
Argument| Type| Details  
---|---|---  
this: `imagecollection`| ImageCollection| The ImageCollection instance.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously. If supplied, will be called with the first parameter if successful and the second if unsuccessful.  
