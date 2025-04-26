 
#  ee.data.createAsset 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates an asset from a JSON value. To create an empty image collection or folder, pass in a "value" object with a "type" key whose value is one of ee.data.AssetType.* (i.e. "ImageCollection" or "Folder"). 
Returns a description of the saved asset, including a generated ID, or null if a callback is specified.
Usage| Returns  
---|---  
`ee.data.createAsset(value,  _path_, _force_, _properties_, _callback_)`| Object  
Argument| Type| Details  
---|---|---  
`value`| Object| An object describing the asset to create.  
`path`| String, optional| An optional desired ID, including full path.  
`force`| Boolean, optional| Force overwrite.  
`properties`| Object, optional| The keys and values of the properties to set  
`callback`| Function, optional| An optional callback. If not supplied, the call is made synchronously.  
Was this helpful?
