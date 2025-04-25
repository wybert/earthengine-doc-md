 
#  Map.onIdle 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when the map stops moving. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Map.onIdle(callback)`| String  
Argument| Type| Details  
---|---|---  
`callback`| Function| The callback to fire when the map becomes idle. The callback is passed two parameters: an object containing the coordinates of the map center (with keys lon, lat, and zoom) and the map widget itself.  
