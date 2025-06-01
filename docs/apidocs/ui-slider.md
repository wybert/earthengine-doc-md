 
#  ui.Slider 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A draggable target that ranges linearly between two numeric values. The value of the slider is displayed as a label alongside it. 
Usage| Returns  
---|---  
`ui.Slider( _min_, _max_, _value_, _step_, _onChange_, _direction_, _disabled_, _style_)`| ui.Slider  
Argument| Type| Details  
---|---|---  
`min`| Number, optional| The minimum value. Defaults to 0.  
`max`| Number, optional| The maximum value. Defaults to 1.  
`value`| Number, optional| The initial value. Defaults to 0.  
`step`| Number, optional| The step size for the slider. Defaults to 0.01.  
`onChange`| Function, optional| A callback to fire when the slider's state changes. The callback is passed the slider's current value and the slider widget.  
`direction`| String, optional| The direction of the slider. One of 'horizontal' or 'vertical'. Defaults to 'horizontal'.  
`disabled`| Boolean, optional| Whether the slider is disabled. Defaults to false.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this widget. See style() documentation.  
