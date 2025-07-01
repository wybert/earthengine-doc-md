 
#  ee.data.listBuckets
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns top-level assets and folders for the Cloud Project or user. Leave the project field blank to use the current project. 
Usage| Returns  
---|---  
`ee.data.listBuckets( _project_, _callback_)`| api.ListAssetsResponse  
Argument| Type| Details  
---|---|---  
`project`| String, optional| Project to query, e.g. "projects/my-project". Defaults to current project. Use "projects/earthengine-legacy" for user home folders.  
`callback`| Function, optional| If not supplied, the call is made synchronously.  
Was this helpful?
