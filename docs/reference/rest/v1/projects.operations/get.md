 
#  Method: projects.operations.get
Stay organized with collections  Save and categorize content based on your preferences. 
Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.
### HTTP request
`GET https://earthengine.googleapis.com/v1/{name=projects/*/operations/**}`
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
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
