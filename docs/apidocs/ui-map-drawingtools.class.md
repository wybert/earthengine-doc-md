 
#  ui.Map.DrawingTools 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A set of tools for drawing on a map. 
Usage| Returns  
---|---  
`ui.Map.DrawingTools( _layers_, _shape_, _selected_, _shown_, _linked_)`| ui.Map.DrawingTools  
Argument| Type| Details  
---|---|---  
`layers`| List, optional| An array of geometry layers with which to initialize the drawing tools.  
`shape`| String, optional| The shape to draw. One of the following: point, line, polygon, or rectangle. Defaults to polygon.  
`selected`| ui.Map.GeometryLayer, optional| The selected geometry layer. Defaults to null.  
`shown`| Boolean, optional| When false, hides the drawing tools or, when true, shows the shape selecter and allows the list panel's visibility to be determined by the presence of geometry layers in the list. Defaults to true.  
`linked`| Boolean, optional| Whether the drawing tools are linked to the geometries in the imports pane. When false, the tools do not display imported geometries. Defaults to false.  
