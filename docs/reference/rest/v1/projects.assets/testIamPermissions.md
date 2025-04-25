 
#  Method: projects.assets.testIamPermissions 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/testIamPermissions#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/testIamPermissions#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/testIamPermissions#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/testIamPermissions#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/testIamPermissions#authorization-scopes)


Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.
Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{resource=projects/*/assets/**}:testIamPermissions`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`resource` |  `string` REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "permissions": [
  string
 ]
}
```
  
Fields  
---  
`permissions[]` |  `string` The set of permissions to check for the `resource`. Permissions with wildcards (such as `*` or `storage.*`) are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions).  
### Response body
If successful, the response body contains an instance of `TestIamPermissionsResponse[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/TestIamPermissionsResponse)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
