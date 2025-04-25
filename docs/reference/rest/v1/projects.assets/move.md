 
#  Method: projects.assets.move 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Moves an asset.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{sourceName=projects/*/assets/**}:move`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`sourceName` |  `string` The name of the asset to move. `name` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceName`:
  * `earthengine.assets.delete`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "destinationName": string
}
```
  
Fields  
---  
`destinationName` |  `string` The destination name to which to move the asset. `name` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `destinationName`:
  * `earthengine.assets.create`

  
### Response body
If successful, the response body contains an instance of `EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
