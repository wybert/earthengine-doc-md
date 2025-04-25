 
#  ee.data.getFeatureViewTilesKey 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Get a tiles key for a given map or asset. The tiles key can be passed to an instance of FeatureViewTileSource which can be rendered on a base map outside of the Code Editor. 
Returns the call results. Null if a callback is specified.
Usage| Returns  
---|---  
`ee.data.getFeatureViewTilesKey(params,  _callback_)`| FeatureViewTilesKey  
Argument| Type| Details  
---|---|---  
`params`| FeatureViewVisualizationParameters| The visualization parameters as a (client-side) JavaScript object. For FeatureView assets:  | ` assetId ` (string) The asset ID for which to obtain a tiles key.  
---  
` visParams ` (Object) The visualization parameters for this layer.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
