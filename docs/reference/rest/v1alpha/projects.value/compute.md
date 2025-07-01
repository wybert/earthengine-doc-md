 
#  Method: projects.value.compute
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Computes an arbitrary value. This will fail if the result of the Expression is not something that is expressible as a Value, or if its evaluation requires too many resources. While it is possible (and not an error) to compute any type of object here, in general any Expression producing results that are better suited to one of the other Compute* endpoints should use that endpoint instead (e.g., an Expression whose result is a set of features should use ComputeFeatures).
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{project=projects/*}/value:compute`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.computations.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression))
 },
 "workloadTag": string
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression)`)` The expression to compute.  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Response body
The results of an arbitrary computation.
If successful, the response body contains data with the following structure:
JSON representation  
---  
```
{
 "result": value
}
```
  
Fields  
---  
`result` |  `value (`Value[](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The results of computing the value of the expression.  
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
