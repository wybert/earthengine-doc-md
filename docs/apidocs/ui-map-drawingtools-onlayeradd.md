 
#  ui.Map.DrawingTools.onLayerAdd
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage | Returns  
---|---  
`DrawingTools.onLayerAdd(callback)` | String  
Argument | Type | Details  
---|---|---  
this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance.  
`callback` | Function | The callback to fire when a layer is added. The callback is passed two parameters: the added GeometryLayer and the ui.Map.DrawingTools widget that the event listener is bound to.  
Was this helpful?
