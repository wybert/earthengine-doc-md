 
#  ui.Slider.onSlide
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Registers a callback that's fired when the slider's state changes. The callback will be invoked repeatedly while the user is dragging the slider. 
Returns an ID which can be passed to unlisten() to unregister the callback.
Usage| Returns  
---|---  
`Slider.onSlide(callback)`| String  
Argument| Type| Details  
---|---|---  
this: `ui.slider`| ui.Slider| The ui.Slider instance.  
`callback`| Function| The callback to fire when the slider's state changes. The callback is passed the slider's current value.  
Was this helpful?
