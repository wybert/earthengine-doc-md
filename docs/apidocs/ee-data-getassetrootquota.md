 
#  ee.data.getAssetRootQuota 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns quota usage details for the asset root with the given ID. 
Usage notes:
- The id _must_ be a root folder like "users/foo" (not "users/foo/bar").
- The authenticated user must own the asset root to see its quota usage.
Usage| Returns  
---|---  
`ee.data.getAssetRootQuota(rootId,  _callback_)`| AssetQuotaDetails  
Argument| Type| Details  
---|---|---  
`rootId`| String| The ID of the asset root to check, e.g. "users/foo".  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
