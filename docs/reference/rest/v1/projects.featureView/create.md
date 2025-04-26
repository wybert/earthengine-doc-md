 
#  Method: projects.featureView.create 
Stay organized with collections  Save and categorize content based on your preferences. 
Create a FeatureView.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{parent=projects/*}/featureView`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The parent of the map collection (e.g., "projects/*").  
### Query parameters
Parameters  
---  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Request body
The request body contains an instance of `FeatureView[](https://developers.google.com/earth-engine/reference/rest/v1/projects.featureView#FeatureView)`.
### Response body
If successful, the response body contains a newly created instance of `FeatureView[](https://developers.google.com/earth-engine/reference/rest/v1/projects.featureView#FeatureView)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
