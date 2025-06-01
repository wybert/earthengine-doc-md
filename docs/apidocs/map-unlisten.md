 
#  Map.unlisten 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Deletes callbacks. 
Usage| Returns  
---|---  
`Map.unlisten( _idOrType_)`|   
Argument|  Type| Details  
---|---|---  
`idOrType`| String, optional| Either an ID returned by listen() when a callback was registered, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks registered with that event type are deleted. If nothing is passed, all callbacks are deleted.  
