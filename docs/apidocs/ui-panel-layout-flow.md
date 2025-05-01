 
#  ui.Panel.Layout.flow 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a layout that places its widgets in a flow, either horizontal or vertical. 
By default, widgets take up their natural space within a flow layout panel. Set the "stretch" style property on an added widget to stretch it to fill available space in the relevant direction:
- horizontal, vertical, both
When multiple widgets are stretched, the available space is split equally among them. Panels are widgets themselves and can be stretched by specifying a "stretch" style property.
Usage| Returns  
---|---  
`ui.Panel.Layout.flow( _direction_, _wrap_)`| ui.Panel.Layout  
Argument| Type| Details  
---|---|---  
`direction`| String, optional| The direction of the flow. One of 'horizontal' or 'vertical'. Defaults to 'vertical'.  
`wrap`| Boolean, optional| Whether to wrap children in the layout if there are too many to show in one line. Defaults to false.  
