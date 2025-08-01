 
#  Method: projects.assets.copy
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/copy#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/copy#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/copy#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/copy#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/copy#authorization-scopes)


Copies an asset.
### HTTP request
`POST https://earthengine.googleapis.com/v1beta/{sourceName=projects/*/assets/**}:copy`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`sourceName` |  `string` The name of the asset to copy. `name` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). (e.g., "assets/users/[USER]/[ASSET]"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceName`:
  * `earthengine.assets.get`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
  "destinationName": string,
  "overwrite": boolean
}
```
  
Fields  
---  
`destinationName` |  `string` The destination name to which to copy the asset. `name` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `destinationName`:
  * `earthengine.assets.create`

  
`overwrite` |  `boolean` Whether to allow overwriting an existing asset.  
### Response body
If successful, the response body contains an instance of `EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets#EarthEngineAsset)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
