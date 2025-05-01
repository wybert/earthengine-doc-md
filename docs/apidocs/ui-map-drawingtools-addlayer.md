 
#  ui.Map.DrawingTools.addLayer 
Stay organized with collections  Save and categorize content based on your preferences. 
Adds a given list of ee.Geometry objects to the drawing tools as a geometry layer. 
Returns the new geometry layer.
Usage| Returns  
---|---  
`DrawingTools.addLayer(geometries,  _name_, _color_, _shown_, _locked_)`| ui.Map.GeometryLayer  
Argument| Type| Details  
---|---|---  
this: `ui.map.drawingtools`| ui.Map.DrawingTools| The ui.Map.DrawingTools instance.  
`geometries`| List| The geometries with which to initialize the layer.  
`name`| String, optional| The name of the layer.  
`color`| String, optional| The CSS color of shapes in the layer, for instance "white" or "#FFFFFF".  
`shown`| Boolean, optional| Whether to show the shapes in the layer. Defaults to true.  
`locked`| Boolean, optional| Whether to lock shape editing in the layer. Defaults to false.  
