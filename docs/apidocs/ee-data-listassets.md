 
#  ee.data.listAssets 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a list of the contents in an asset collection or folder, in an object that includes an `assets` array and an optional `nextPageToken`. 
Usage| Returns  
---|---  
`ee.data.listAssets(parent,  _params_, _callback_)`| api.ListAssetsResponse  
Argument| Type| Details  
---|---|---  
`parent`| String| The ID of the collection or folder to list.  
`params`| api.ProjectsAssetsListAssetsNamedParameters, optional| An object containing optional request parameters with the following possible values:  | ` pageSize ` (string) The number of results to return. If not specified, all results are returned.  
---  
` pageToken ` (string) The token for the page of results to return.  
` filter ` (string) An additional filter query to apply. Example query: `properties.my_property>=1 AND properties.my_property<2 AND startTime >= "2019-01-01T00:00:00.000Z" AND endTime < "2020-01-01T00:00:00.000Z" AND intersects("{'type':'Point','coordinates':[0,0]}")` See https://google.aip.dev/160 for how to construct a query.  
` view ` (string) Specifies how much detail is returned in the list. Either "FULL" (default) for all image properties or "BASIC".  
`callback`| Function, optional| If not supplied, the call is made synchronously.  
Was this helpful?
