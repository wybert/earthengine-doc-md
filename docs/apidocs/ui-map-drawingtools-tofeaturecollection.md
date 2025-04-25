 
#  ui.Map.DrawingTools.toFeatureCollection 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a feature collection in which each geometry in the drawing tools is a feature. 
Usage| Returns  
---|---  
`DrawingTools.toFeatureCollection(indexProperty)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `ui.map.drawingtools`| ui.Map.DrawingTools| The ui.Map.DrawingTools instance.  
`indexProperty`| String| A property with this name will be assigned to every feature in the returned collection. The value of the property will be a number that corresponds to the index of the geometry layer to which the geometry belongs.  
