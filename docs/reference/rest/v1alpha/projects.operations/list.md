 
#  Method: projects.operations.list 
Stay organized with collections  Save and categorize content based on your preferences. 
Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.
### HTTP request
`GET https://earthengine.googleapis.com/v1alpha/{name=projects/*}/operations`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The name of the operation's parent resource.  
### Query parameters
Parameters  
---  
`filter` |  `string` The standard list filter.  
`pageSize` |  `integer` The standard list page size.  
`pageToken` |  `string` The standard list page token.  
### Request body
The request body must be empty.
### Response body
If successful, the response body contains an instance of `ListOperationsResponse[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
