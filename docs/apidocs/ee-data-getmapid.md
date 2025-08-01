 
#  ee.data.getMapId
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns the mapId call results, which may be passed to ee.data.getTileUrl or ui.Map.addLayer. Null if a callback is specified.
Usage | Returns  
---|---  
`ee.data.getMapId(params, _callback_)`|  RawMapId  
Argument | Type | Details  
---|---|---  
`params` | ImageVisualizationParameters | The visualization parameters as a (client-side) JavaScript object. For Images and ImageCollections:  |  ` image ` (JSON string) The image to render.  
---  
` version ` (number) Version number of image (or latest).  
` bands ` (comma-separated strings) Comma-delimited list of band names to be mapped to RGB.  
` min ` (comma-separated numbers) Value (or one per band) to map onto 00.  
` max ` (comma-separated numbers) Value (or one per band) to map onto FF.  
` gain ` (comma-separated numbers) Gain (or one per band) to map onto 00-FF.  
` bias ` (comma-separated numbers) Offset (or one per band) to map onto 00-FF.  
` gamma ` (comma-separated numbers) Gamma correction factor (or one per band).  
` palette ` (comma-separated strings) List of CSS-style color strings (single-band previews only).  
` opacity ` (number) a number between 0 and 1 for opacity.  
` format ` (string) Either "jpg" or "png".  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
Was this helpful?
