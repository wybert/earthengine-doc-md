 
#  ui.Map.onClick
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage | Returns  
---|---  
`Map.onClick(callback)` | String  
Argument | Type | Details  
---|---|---  
this: `ui.map` | ui.Map | The ui.Map instance.  
`callback` | Function | The callback to fire when the map is clicked. The callback is passed an object containing the coordinates of the clicked point on the map (with keys lon and lat) and the map widget itself.  
Was this helpful?
