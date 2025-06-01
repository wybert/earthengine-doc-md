 
#  ui.Map.setControlVisibility 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Sets the visibility of the controls on the map. 
Returns this ui.Map.
Usage| Returns  
---|---  
`Map.setControlVisibility( _all_, _layerList_, _zoomControl_, _scaleControl_, _mapTypeControl_, _fullscreenControl_, _drawingToolsControl_)`| ui.Map  
Argument| Type| Details  
---|---|---  
this: `ui.map`| ui.Map| The ui.Map instance.  
`all`| Boolean, optional| Whether to show all controls. False hides all controls; true shows all controls. Overridden by individually set parameters. Note that setting this explicitly will affect any additional controls added in the future.  
`layerList`| Boolean, optional| When false, hides the layer list panel or, when true, allows the layer list panel's visibility to be determined by the presence of layers in the list. The default is to show the list.  
`zoomControl`| Boolean, optional| Whether the zoom control is visible. Defaults to true.  
`scaleControl`| Boolean, optional| Whether to show the control which indicates the scale at the map's current zoom level. Defaults to true.  
`mapTypeControl`| Boolean, optional| Whether to show the control that allows the user to change the base map. Defaults to true.  
`fullscreenControl`| Boolean, optional| Whether to show the control that allows the user to make the map full-screen. Defaults to true.  
`drawingToolsControl`| Boolean, optional| Whether to show the control that allows the user to add or edit the geometry drawing tools. Defaults to true if the drawing tools were previously added to the map. Ignored if the drawing tools were not previously added to the map.  
