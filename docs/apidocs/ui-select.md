 
#  ui.Select 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A printable select menu with a callback. 
Usage| Returns  
---|---  
`ui.Select( _items_, _placeholder_, _value_, _onChange_, _disabled_, _style_)`| ui.Select  
Argument| Type| Details  
---|---|---  
`items`| List, optional| The list of options to add to the select. Defaults to an empty array.  
`placeholder`| String, optional| The placeholder shown when no value is selected. Defaults to "Select a value...".  
`value`| String, optional| The select's value. Defaults to null.  
`onChange`| Function, optional| The callback to fire when an item is selected. The callback is passed the currently selected value and the select widget.  
`disabled`| Boolean, optional| Whether the select is disabled. Defaults to false.  
`style`| Object, optional| An object of allowed CSS styles with their values to be set for this widget. See style() documentation.  
