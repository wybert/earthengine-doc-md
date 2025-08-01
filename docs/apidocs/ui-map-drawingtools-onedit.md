 
#  ui.Map.DrawingTools.onEdit
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage | Returns  
---|---  
`DrawingTools.onEdit(callback)` | String  
Argument | Type | Details  
---|---|---  
this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance.  
`callback` | Function | The callback to fire when a shape is edited. The callback is passed three parameters: the edited ee.Geometry, the GeometryLayer to which the edited geometry belongs, and the ui.Map.DrawingTools widget that the event listener is bound to.  
