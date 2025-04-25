 
#  Method: projects.operations.list 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/list#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/list#path-parameters)
  * [Query parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/list#query-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/list#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/list#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/list#authorization-scopes)


Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.
### HTTP request
`GET https://earthengine.googleapis.com/v1/{name=projects/*}/operations`
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
