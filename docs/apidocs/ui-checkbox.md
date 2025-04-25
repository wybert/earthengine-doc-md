 
#  ui.Checkbox 
Stay organized with collections  Save and categorize content based on your preferences. 
A checkbox with a label. Usage| Returns  
---|---  
`ui.Checkbox( _label_, _value_, _onChange_, _disabled_, _style_)`| ui.Checkbox  
Argument| Type| Details  
---|---|---  
`label`| String, optional| The checkbox's label. Defaults to an empty string.  
`value`| Boolean, optional| Whether the checkbox is checked. A null value indicates that the checkbox is in an indeterminate state. Defaults to false.  
`onChange`| Function, optional| A callback to fire when the value of the checkbox changes. The callback is passed a boolean indicating whether the checkbox is now checked and the checkbox widget.  
`disabled`| Boolean, optional| Whether the checkbox is disabled. Defaults to false.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this widget. See style() documentation.  
