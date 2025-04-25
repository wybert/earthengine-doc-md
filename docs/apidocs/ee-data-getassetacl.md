 
#  ee.data.getAssetAcl 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the access control list of the asset with the given ID. 
The authenticated user must be a writer or owner of an asset to see its ACL.
Usage| Returns  
---|---  
`ee.data.getAssetAcl(assetId,  _callback_)`| AssetAcl  
Argument| Type| Details  
---|---|---  
`assetId`| String| The ID of the asset to check.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
