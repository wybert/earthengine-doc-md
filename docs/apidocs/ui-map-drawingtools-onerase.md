 
#  ui.Map.DrawingTools.onErase
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when a shape is erased. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`DrawingTools.onErase(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.map.drawingtools`| ui.Map.DrawingTools| The ui.Map.DrawingTools instance.  
`callback`| Function| The callback to fire when a shape is erased. The callback is passed three parameters: the removed ee.Geometry, the GeometryLayer from which the geometry was removed, and the ui.Map.DrawingTools widget that the event listener is bound to.  
Was this helpful?
