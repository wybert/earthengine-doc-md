 
#  ui.Map.DrawingTools.onLayerConfig 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired after a layer's name or color is changed. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`DrawingTools.onLayerConfig(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.map.drawingtools`| ui.Map.DrawingTools| The ui.Map.DrawingTools instance.  
`callback`| Function| The callback to fire after a layer is configured. The callback is passed two parameters: the configured GeometryLayer and the ui.Map.DrawingTools widget that the event listener is bound to.  
Was this helpful?
