 
#  ui.Map.DrawingTools.onLayerAdd 
Stay organized with collections  Save and categorize content based on your preferences. 
Registers a callback that's fired when a layer is added. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`DrawingTools.onLayerAdd(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.map.drawingtools`| ui.Map.DrawingTools| The ui.Map.DrawingTools instance.  
`callback`| Function| The callback to fire when a layer is added. The callback is passed two parameters: the added GeometryLayer and the ui.Map.DrawingTools widget that the event listener is bound to.  
