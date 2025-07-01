 
#  Method: projects.assets.create
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/create#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/create#path-parameters)
  * [Query parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/create#query-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/create#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/create#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/create#authorization-scopes)


Creates an asset.
The following asset types are createable: * `FOLDER`: No fields in `asset` may be specified. * `IMAGE`: To create a COG-backed asset, use `image.importExternal` instead. See <https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff> for more details. * `IMAGE_COLLECTION`: Only the fields `startTime`, `endTime`, and `properties` may be specified.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{parent=projects/*}/assets`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The parent of the asset collection (e.g., "projects/*"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:
  * `earthengine.assets.create`

  
### Query parameters
Parameters  
---  
`assetId` |  `string` The ID of the asset to create. Equivalent to name but without the "projects/*/assets" (e.g., users/[USER]/[ASSET]).  
`overwrite` |  `boolean` Whether to allow overwriting an image asset.  
### Request body
The request body contains an instance of `EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset)`.
### Response body
If successful, the response body contains a newly created instance of `EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
Was this helpful?
