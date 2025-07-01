 
#  ui.Map.CloudStorageLayer
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A layer generated from Cloud Storage tiles for display on a ui.Map. 
Usage| Returns  
---|---  
`ui.Map.CloudStorageLayer(bucket, path, maxZoom,  _suffix_, _name_, _shown_, _opacity_)`| ui.Map.CloudStorageLayer  
Argument| Type| Details  
---|---|---  
`bucket`| String| The bucket that contains the tiles.  
`path`| String| The path to this layer's tiles, relative to the bucket. A trailing "/" is optional.  
`maxZoom`| Number| The maximum zoom level for which there are tiles.  
`suffix`| String, optional| The tile source file suffix, if any.  
`name`| String, optional| The name of the layer.  
`shown`| Boolean, optional| Whether the layer is initially shown. Defaults to true.  
`opacity`| Number, optional| The layer's opacity represented as a number between 0 and 1. Defaults to 1.  
Was this helpful?
