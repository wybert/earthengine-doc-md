 
#  ui.Checkbox.unlisten
Stay organized with collections  Save and categorize content based on your preferences. 
Deletes callbacks. Usage| Returns  
---|---  
`Checkbox.unlisten( _idOrType_)`|   
Argument|  Type| Details  
---|---|---  
this: `ui.widget`| ui.Widget| The ui.Widget instance.  
`idOrType`| String, optional| Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted.  
