 
#  ui.Map.DrawingTools.onShapeChange 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when a drawing mode shape is changed. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`DrawingTools.onShapeChange(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.map.drawingtools`| ui.Map.DrawingTools| The ui.Map.DrawingTools instance.  
`callback`| Function| The callback to fire when the shape is changed. The callback is passed two parameters: the drawing mode shape as a string (or null for cancel) and the ui.Map.DrawingTools widget that the event listener is bound to. The shape values are: 
  * point 
  * line 
  * polygon 
  * rectangle 
  * null 

  
Was this helpful?
