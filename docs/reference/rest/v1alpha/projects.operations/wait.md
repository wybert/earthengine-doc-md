 
#  Method: projects.operations.wait 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/wait#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/wait#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/wait#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/wait#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/wait#authorization-scopes)


Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state. If the operation is already done, the latest state is immediately returned. If the timeout specified is greater than the default HTTP/RPC timeout, the HTTP/RPC timeout is used. If the server does not support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Note that this method is on a best-effort basis. It may return the latest state before the specified timeout (including immediately), meaning even an immediate response is no guarantee that the operation is done.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{name=projects/*/operations/**}:wait`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` The name of the operation resource to wait on.  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "timeout": string
}
```
  
Fields  
---  
`timeout` |  `string (`Duration[](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
