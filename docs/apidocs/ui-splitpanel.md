 
#  ui.SplitPanel 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A widget containing two panels with a divider between them. The divider can be dragged, allowing the panels to be resized. One or both panels may be ui.Map objects. 
By default the layout initializes with a 50/50 split. The width and max/minWidth styles on the panels control the split sizing for horizontal orientations. Similarly, use height and max/minHeight for vertical. These can be given in pixels as '{n}px' or as a percentage of the containing SplitPanel as '{n}%'.
Note that the given size for the second panel will be ignored if the first panel size is specified, since the overall width of the split panel is controlled independently. Max/min sizes may be set for both panels.
Usage| Returns  
---|---  
`ui.SplitPanel( _firstPanel_, _secondPanel_, _orientation_, _wipe_, _style_)`| ui.SplitPanel  
Argument| Type| Details  
---|---|---  
`firstPanel`| ui.Panel, optional| The left or top panel. Defaults to a new instance of ui.Panel.  
`secondPanel`| ui.Panel, optional| The bottom or right panel. Defaults to a new instance of ui.Panel.  
`orientation`| String, optional| One of "horizontal" or "vertical". Defaults to "horizontal".  
`wipe`| Boolean, optional| Whether to enable the wiping effect. When this mode is enabled, both panels take up all available space, and dragging the divider doesn't set the size of the panels but rather determines how much of each panel is shown. This effect is analogous to a "wipe transition". This mode is useful for comparing two maps. Defaults to false.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this panel. Defaults to an empty object.  
Was this helpful?
