 
#  Method: projects.tables.getFeatures
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Fetches `Table` features, the request includes the name of the Table to download from a previous `tables.create` request.
### HTTP request
`GET https://earthengine.googleapis.com/v1/{name=projects/*/tables/*}:getFeatures`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` Required. A table name from `Table.name`.  
### Request body
The request body must be empty.
### Response body
If successful, the response is a generic HTTP response whose format is defined by the method.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
