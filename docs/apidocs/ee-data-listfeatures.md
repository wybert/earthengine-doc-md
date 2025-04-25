 
#  ee.data.listFeatures 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
List features for a given table asset. 
Returns the call results. Null if a callback is specified.
Usage| Returns  
---|---  
`ee.data.listFeatures(asset, params,  _callback_)`| api.ListFeaturesResponse  
Argument| Type| Details  
---|---|---  
`asset`| String| The table asset ID to query.  
`params`| api.ProjectsAssetsListFeaturesNamedParameters| An object containing request parameters with the following possible values:  | ` pageSize ` (number): An optional maximum number of results per page, default is 1000.  
---  
` pageToken ` (string): An optional token identifying a page of results the server should return, usually taken from the response object.  
` region ` (string): If present, a geometry defining a query region, specified as a GeoJSON geometry string (see RFC 7946).  
` filter ` (comma-separated strings): If present, specifies additional simple property filters (see https://google.aip.dev/160).  
`callback`| Function, optional| An optional callback, called with two parameters: the first is the resulting list of features and the second is an error string on failure. If not supplied, the call is made synchronously.  
