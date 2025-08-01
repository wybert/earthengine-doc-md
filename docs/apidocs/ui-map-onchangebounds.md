 
#  ui.Map.onChangeBounds
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage | Returns  
---|---  
`Map.onChangeBounds(callback)` | String  
Argument | Type | Details  
---|---|---  
this: `ui.map` | ui.Map | The ui.Map instance.  
`callback` | Function | The callback to fire when the map bounds change. The callback is passed two parameters: an object containing the coordinates of the new map center (with keys lon, lat, and zoom) and the map widget itself.  
