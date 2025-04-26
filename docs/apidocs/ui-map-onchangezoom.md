 
#  ui.Map.onChangeZoom 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Registers a callback that's fired when the map zoom level changes. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Map.onChangeZoom(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.map`| ui.Map| The ui.Map instance.  
`callback`| Function| The callback to fire when the map zoom change. The callback is passed two parameters: the new zoom level and the map widget itself.  
