 
#  Method: projects.updateConfig
Stay organized with collections  Save and categorize content based on your preferences. 
Updates the config state of a project.
### HTTP request
`PATCH https://earthengine.googleapis.com/v1beta/{projectConfig.name=projects/*/config}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`projectConfig.name` |  `string` Required. The project config name, of the format "projects/*/config".  
### Query parameters
Parameters  
---  
`updateMask` |  `string (`FieldMask[](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The list of fields to update. This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
### Request body
The request body contains an instance of `ProjectConfig[](https://developers.google.com/earth-engine/reference/rest/v1beta/ProjectConfig)`.
### Response body
If successful, the response body contains an instance of `ProjectConfig[](https://developers.google.com/earth-engine/reference/rest/v1beta/ProjectConfig)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
