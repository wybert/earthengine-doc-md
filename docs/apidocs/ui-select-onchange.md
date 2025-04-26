 
#  ui.Select.onChange 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Registers a callback that's fired when an item is selected. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Select.onChange(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.select`| ui.Select| The ui.Select instance.  
`callback`| Function| The callback to fire when an item is selected. The callback is passed the currently selected value and the select widget.  
