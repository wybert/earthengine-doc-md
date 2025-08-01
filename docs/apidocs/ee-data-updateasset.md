 
#  ee.data.updateAsset
Stay organized with collections  Save and categorize content based on your preferences. 
The authenticated user must be a writer or owner of the asset.
Usage | Returns  
---|---  
`ee.data.updateAsset(assetId, asset, updateFields, _callback_)`|  Object  
Argument | Type | Details  
---|---|---  
`assetId` | String | The ID of the asset to update.  
`asset` | api.EarthEngineAsset | The updated version of the asset, containing only the new values of the fields to be updated. Only the "start_time", "end_time", and "properties" fields can be updated. If a value is named in "updateMask", but is unset in "asset", then that value will be deleted from the asset.  
`updateFields` | List<String> | A list of the field names to update. This may contain: "start_time" or "end_time" to update the corresponding timestamp, "properties.PROPERTY_NAME" to update a given property, or "properties" to update all properties. If the list is empty, all properties and both timestamps will be updated.  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
