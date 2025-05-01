 
#  ui.Map 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A Google map. 
Usage| Returns  
---|---  
`ui.Map( _center_, _onClick_, _style_)`| ui.Map  
Argument| Type| Details  
---|---|---  
`center`| Object, optional| An object containing the latitude ('lat'), longitude ('lon') and optionally the zoom level ('zoom') for the map.  
`onClick`| Function, optional| A callback fired when the map is clicked. The callback is passed an object containing the coordinates of the clicked point on the map (with keys lon and lat) and the map widget itself.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this map. See style() documentation.  
Was this helpful?
