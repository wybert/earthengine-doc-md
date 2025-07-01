 
#  ui.Map.Layer
Stay organized with collections  Save and categorize content based on your preferences. 
A layer generated from an Earth Engine object for display on a ui.Map. 
Usage| Returns  
---|---  
`ui.Map.Layer( _eeObject_, _visParams_, _name_, _shown_, _opacity_)`| ui.Map.Layer  
Argument| Type| Details  
---|---|---  
`eeObject`| Collection|Feature|Image, optional| The object to add to the map. Defaults to an empty ee.Image.  
`visParams`| FeatureVisualizationParameters|ImageVisualizationParameters, optional| The visualization parameters. See ee.data.getMapId() docs.  
`name`| String, optional| The name of the layer.  
`shown`| Boolean, optional| Whether the layer is initially shown. Defaults to true.  
`opacity`| Number, optional| The layer's opacity represented as a number between 0 and 1. Defaults to 1.  
