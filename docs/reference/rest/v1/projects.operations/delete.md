 
#  Method: projects.operations.delete 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/delete#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/delete#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/delete#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/delete#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/delete#authorization-scopes)


Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.
### HTTP request
`DELETE https://earthengine.googleapis.com/v1/{name=projects/*/operations/**}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The name of the operation resource to be deleted.  
### Request body
The request body must be empty.
### Response body
If successful, the response body is an empty JSON object.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
