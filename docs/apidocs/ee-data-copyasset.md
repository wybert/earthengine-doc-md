 
#  ee.data.copyAsset 
Stay organized with collections  Save and categorize content based on your preferences. 
Copies the asset from sourceId into destinationId. Usage| Returns  
---|---  
`ee.data.copyAsset(sourceId, destinationId,  _overwrite_, _callback_)`  
Argument|  Type| Details  
---|---|---  
`sourceId`| String| The ID of the asset to copy.  
`destinationId`| String| The ID of the new asset created by copying.  
`overwrite`| Boolean, optional| Overwrite any existing destination asset ID.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously. The callback is passed an empty object and an error message, if any.  
