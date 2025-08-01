 
#  ee.data.getTableDownloadId
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Returns a download id and token, or null if a callback is specified.
Usage | Returns  
---|---  
`ee.data.getTableDownloadId(params, _callback_)`|  DownloadId  
Argument | Type | Details  
---|---|---  
`params` | Object | An object containing table download options with the following possible values:  |  ` table: ` The feature collection to download.  
---  
` format: ` The download format, CSV, JSON, KML, KMZ or TF_RECORD.  
` selectors: ` List of strings of selectors that can be used to determine which attributes will be downloaded.  
` filename: ` The name of the file that will be downloaded.  
`callback` | Function, optional | An optional callback. If not supplied, the call is made synchronously.  
Was this helpful?
