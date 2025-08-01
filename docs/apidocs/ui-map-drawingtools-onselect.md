 
#  ui.Map.DrawingTools.onSelect
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage | Returns  
---|---  
`DrawingTools.onSelect(callback)` | String  
Argument | Type | Details  
---|---|---  
this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance.  
`callback` | Function | The callback to fire when a shape is selected. The callback is passed three parameters: the selected ee.Geometry, the GeometryLayer to which the selected geometry belongs, and the ui.Map.DrawingTools widget that the event listener is bound to.  
