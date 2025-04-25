 
#  Method: projects.assets.setIamPolicy 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Sets the access control policy on the specified resource. Replaces any existing policy.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{resource=projects/*/assets/**}:setIamPolicy`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "policy": {
  object (Policy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/Policy))
 }
}
```
  
Fields  
---  
`policy` |  `object (`Policy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/Policy)`)` REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Google Cloud services (such as Projects) might reject them.  
### Response body
If successful, the response body contains an instance of `Policy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/Policy)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
