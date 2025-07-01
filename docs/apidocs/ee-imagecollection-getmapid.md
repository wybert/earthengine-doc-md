 
#  ee.ImageCollection.getMapId
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
An imperative function that returns a map ID via a synchronous AJAX call. 
This mosaics the collection to a single image and return a map ID suitable for building a Google Maps overlay.
Returns returns a map ID and optional token, which may be passed to ee.data.getTileUrl or ui.Map.addLayer. Undefined if a callback was specified.
Usage| Returns  
---|---  
`ImageCollection.getMapId( _visParams_, _callback_)`| MapId|Object  
Argument| Type| Details  
---|---|---  
this: `imagecollection`| ImageCollection| The ImageCollection instance.  
`visParams`| Object, optional| The visualization parameters.  
`callback`| Function, optional| An async callback. If not supplied, the call is made synchronously.  
