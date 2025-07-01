 
#  Method: projects.assets.get
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/get#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/get#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/get#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/get#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/get#authorization-scopes)


Gets detailed information about an asset.
### HTTP request
`GET https://earthengine.googleapis.com/v1/{name=projects/*/assets/**}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` Required. The name of the asset to get. `name` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:
  * `earthengine.assets.get`

  
### Request body
The request body must be empty.
### Response body
If successful, the response body contains an instance of `EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
Was this helpful?
