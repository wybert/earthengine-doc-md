 
#  Method: projects.assets.getIamPolicy 
Stay organized with collections  Save and categorize content based on your preferences. 
Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{resource=projects/*/assets/**}:getIamPolicy`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "options": {
  object (GetPolicyOptions[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions))
 }
}
```
  
Fields  
---  
`options` |  `object (`GetPolicyOptions[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/GetIamPolicyRequest#GetPolicyOptions)`)` OPTIONAL: A `GetPolicyOptions` object for specifying options to `assets.getIamPolicy`.  
### Response body
If successful, the response body contains an instance of `Policy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/Policy)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
