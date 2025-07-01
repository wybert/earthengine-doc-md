 
#  ui.Panel.style
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ui-panel-style#examples)


Returns the widget's style ActiveDictionary, which can be modified to update the widget's styles. 
Properties which behave like their CSS counterparts:
- height, maxHeight, minHeight (e.g. '100px')
- width, maxWidth, minWidth (e.g. '100px')
- padding, margin (e.g. '4px 4px 4px 4px' or simply '4px')
- color, backgroundColor (e.g. 'red' or '#FF0000')
- border (e.g. '1px solid black')
- borderColor (e.g. 'red black blue #FF0000')
- borderRadius (e.g. '10px')
- borderStyle (e.g. 'solid dashed none dotted')
- borderWidth (e.g. '1px 0px 1px 0px')
- fontSize (e.g. '24px')
- fontStyle (e.g. 'italic')
- fontWeight (e.g. 'bold' or '100')
- fontFamily (e.g. 'monospace' or 'serif')
- textAlign (e.g. 'left' or 'center')
- textDecoration (e.g. 'underline' or 'line-through')
- whiteSpace (e.g. 'nowrap' or 'pre')
- shown (true or false)
Supported custom layout properties (see ui.Panel.Layout documentation):
- stretch ('horizontal', 'vertical', 'both')
- position ('top-right', 'top-center', 'top-left', 'bottom-right', ...)
Usage| Returns  
---|---  
`Panel.style()`| ui.data.ActiveDictionary  
Argument| Type| Details  
---|---|---  
this: `ui.widget`| ui.Widget| The ui.Widget instance.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ui-panel-style#code-editor-javascript-sample) More
```
// Define a UI widget and add it to the map.
varwidget=ui.Panel({style:{width:'400px',height:'200px'}});
Map.add(widget);
// View the UI widget's style properties; an ActiveDictionary.
print(widget.style());
// ActiveDictionaries are mutable; set a style property.
widget.style().set('backgroundColor','lightgray');
print(widget.style());
// Define the UI widget's style ActiveDictionary as a variable.
varwidgetStyle=widget.style();
print(widgetStyle);
// Set the UI widget's style properties from the ActiveDictionary variable.
widgetStyle.set({border:'5px solid darkgray'});
print(widgetStyle);
```

Was this helpful?
