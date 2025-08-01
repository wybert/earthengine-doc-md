 
#  ui.Map.DrawingTools.unlisten
Stay organized with collections  Save and categorize content based on your preferences. 
Usage | Returns  
---|---  
`DrawingTools.unlisten(_idOrType_)`|   
Argument | Type | Details  
---|---|---  
this: `ui.map.drawingtools` | ui.Map.DrawingTools | The ui.Map.DrawingTools instance.  
`idOrType` | String, optional | Either an ID returned by an onEventType() function during callback registration, an event type, or nothing. If an ID is passed, the corresponding callback is deleted. If an event type is passed, all callbacks for that type are deleted. If nothing is passed, all callbacks are deleted.  
