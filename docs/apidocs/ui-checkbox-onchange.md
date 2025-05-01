 
#  ui.Checkbox.onChange 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when the value of the checkbox changes. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Checkbox.onChange(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.checkbox`| ui.Checkbox| The ui.Checkbox instance.  
`callback`| Function| The callback to fire when the value of the checkbox changes. The callback is passed a boolean indicating whether the checkbox is now checked and the checkbox widget.  
