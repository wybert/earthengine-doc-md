 
#  ui.root.add
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ui-root-add#examples)


Adds a widget to the root panel. 
Returns the root panel.
Usage| Returns  
---|---  
`ui.root.add(widget)`| ui.Panel  
Argument| Type| Details  
---|---|---  
`widget`| ui.Widget| The widget to be added.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ui-root-add#code-editor-javascript-sample) More
```
// Replace the default UI widgets with a few custom widgets.
ui.root.clear();
ui.root.add(
ui.Panel({
widgets:[
ui.Label('This is a custom user interface.'),
],
style:{border:'5px solid green'}
})
);
ui.root.add(ui.Map());
```

Was this helpful?
