 
#  Method: projects.operations.get
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/get#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/get#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/get#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/get#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/get#authorization-scopes)


Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.
### HTTP request
`GET https://earthengine.googleapis.com/v1alpha/{name=projects/*/operations/**}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The name of the operation resource.  
### Request body
The request body must be empty.
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
Was this helpful?
