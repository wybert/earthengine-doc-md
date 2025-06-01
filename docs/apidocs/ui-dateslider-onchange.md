 
#  ui.DateSlider.onChange 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when the slider's value changes. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`DateSlider.onChange(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.dateslider`| ui.DateSlider| The ui.DateSlider instance.  
`callback`| Function| The callback to fire when the slider's state changes. The callback is passed an ee.DateRange representing the slider's current value and the slider widget.  
