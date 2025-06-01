 
#  ee.Image.getMapId 
Stay organized with collections  Save and categorize content based on your preferences. 
An imperative function that returns a map ID and optional token, suitable for generating a Map overlay. 
Returns an object which may be passed to ee.data.getTileUrl or ui.Map.addLayer. Undefined if a callback was specified.
Usage| Returns  
---|---  
`Image.getMapId( _visParams_, _callback_)`| MapId|Object  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`visParams`| ImageVisualizationParameters, optional| The visualization parameters.  
`callback`| Function, optional| An async callback. If not supplied, the call is made synchronously.  
