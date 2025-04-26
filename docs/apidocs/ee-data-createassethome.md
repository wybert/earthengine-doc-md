 
#  ee.data.createAssetHome 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Attempts to create a home root folder (e.g. "users/joe") for the current user. This results in an error if the user already has a home root folder or the requested ID is unavailable. 
Usage| Returns  
---|---  
`ee.data.createAssetHome(requestedId,  _callback_)`|   
Argument|  Type| Details  
---|---|---  
`requestedId`| String| The requested ID of the home folder (e.g. "users/joe").  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
