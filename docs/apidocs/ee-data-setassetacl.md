 
#  ee.data.setAssetAcl 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Sets the access control list of the asset with the given ID. 
The owner ACL cannot be changed, and the final ACL of the asset is constructed by merging the OWNER entries of the old ACL with the incoming ACL record.
The authenticated user must be a writer or owner of an asset to set its ACL.
Usage| Returns  
---|---  
`ee.data.setAssetAcl(assetId, aclUpdate,  _callback_)`|   
Argument|  Type| Details  
---|---|---  
`assetId`| String| The ID of the asset to set the ACL on.  
`aclUpdate`| AssetAclUpdate| The updated ACL.  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously. The callback is passed an empty object.  
