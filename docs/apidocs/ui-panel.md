 
#  ui.Panel 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A widget that can hold other widgets. Use panels to construct complex combinations of nested widgets. 
Panels can be added to ui.root but not printed to the console with print().
Usage| Returns  
---|---  
`ui.Panel( _widgets_, _layout_, _style_)`| ui.Panel  
Argument| Type| Details  
---|---|---  
`widgets`| List, optional| The list of widgets or a single widget to add to the panel. Defaults to an empty array.  
`layout`| String|ui.Panel.Layout, optional| The layout to use for this panel. If a string is passed in, it's taken as a shortcut to the layout constructor with that name. Defaults to 'flow'.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this widget. See style() documentation.  
Was this helpful?
