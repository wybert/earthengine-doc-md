 
#  ui.Map.setLocked 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Limits panning and zooming on the map. 
- To lock both panning and zooming, set locked to true and nothing else.
- To allow panning and limit the min and max zoom, set locked to false and supply the minZoom and maxZoom parameters.
- To disallow panning and limit min and max zoom, set locked to true and supply the minZoom and maxZoom parameters.
- To reset the map to default, set locked to false and nothing else.
Usage| Returns  
---|---  
`Map.setLocked(locked,  _minZoom_, _maxZoom_)`  
Argument|  Type| Details  
---|---|---  
this: `ui.map`| ui.Map| The ui.Map instance.  
`locked`| Boolean| Whether the map should be locked or not.  
`minZoom`| Number, optional| (optional) The minimum zoom for the map, between 0 and 24, inclusive.  
`maxZoom`| Number, optional| (optional) The maximum zoom for the map, between 0 and 24, inclusive.  
