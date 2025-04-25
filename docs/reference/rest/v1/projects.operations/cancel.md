 
#  Method: projects.operations.cancel 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/cancel#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/cancel#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/cancel#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/cancel#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.operations/cancel#authorization-scopes)


Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use `Operations.GetOperation[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/get#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an `Operation.error[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.error)` value with a `google.rpc.Status.code[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Status.FIELDS.code)` of `1`, corresponding to `Code.CANCELLED`.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{name=projects/*/operations/**}:cancel`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The name of the operation resource to be cancelled.  
### Request body
The request body must be empty.
### Response body
If successful, the response body is an empty JSON object.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
Was this helpful?
