 
#  Method: projects.getConfig 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects/getConfig#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects/getConfig#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects/getConfig#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects/getConfig#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects/getConfig#authorization-scopes)


Gets the config state of a project.
### HTTP request
`GET https://earthengine.googleapis.com/v1alpha/{name=projects/*/config}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` Required. The project config to get, of the format "projects/*/config". Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:
  * `earthengine.computations.create`

  
### Request body
The request body must be empty.
### Response body
If successful, the response body contains an instance of `ProjectConfig[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ProjectConfig)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
