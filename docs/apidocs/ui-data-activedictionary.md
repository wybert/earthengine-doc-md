 
#  ui.data.ActiveDictionary
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A dictionary-like container for data for use in UI components. 
When a property of a ui.data.ActiveDictionary (e.g. myButton.style()) is updated, the component it belongs to is automatically updated. For example, myButton.style().set('color', 'red') would change the color of button's text to red.
Usage| Returns  
---|---  
`ui.data.ActiveDictionary( _object_, _allowedProperties_)`| ui.data.ActiveDictionary  
Argument| Type| Details  
---|---|---  
`object`| Object, optional| A JavaScript object with properties and values to initialize this object with.  
`allowedProperties`| List, optional| An array of allowed properties for this object. If undefined, then any property is allowed.  
Was this helpful?
