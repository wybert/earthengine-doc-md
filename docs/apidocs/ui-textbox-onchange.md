 
#  ui.Textbox.onChange 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Registers a callback that's called when text in the textbox changes. 
In particular, the callback is called when:
- The user types a new value and then either the textbox loses focus or the user presses enter.
- A new value is set programmatically with set('value', newValue).
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Textbox.onChange(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.textbox`| ui.Textbox| The ui.Textbox instance.  
`callback`| Function| The callback to fire when the text changes. The callback is passed the text currently in the textbox and the textbox widget.  
