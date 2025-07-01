 
#  Map.onChangeCenter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Registers a callback that's fired when the map center changes. This is fired during pan or when the map's center is changed programmatically. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Map.onChangeCenter(callback)`| String  
Argument| Type| Details  
---|---|---  
`callback`| Function| The callback to fire when the map center changes. The callback is passed two parameters: an object containing the coordinates of the new center (with keys lon and lat) and the map widget itself.  
