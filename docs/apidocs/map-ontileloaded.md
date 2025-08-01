 
#  Map.onTileLoaded
Stay organized with collections  Save and categorize content based on your preferences. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage | Returns  
---|---  
`Map.onTileLoaded(callback)` | String  
Argument | Type | Details  
---|---|---  
`callback` | Function | Called with an array of per layer values. Each value is the fraction of tiles still pending: a value of 0 means there are no more tiles to load for the layer.  
