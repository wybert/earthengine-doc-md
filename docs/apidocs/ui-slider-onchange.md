 
#  ui.Slider.onChange 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when the slider's state changes. If the change is due to the user dragging the slider, the event will not fire until the drag completes. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Slider.onChange(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.slider`| ui.Slider| The ui.Slider instance.  
`callback`| Function| The callback to fire when the slider's state changes. The callback is passed the slider's current value and the slider widget.  
