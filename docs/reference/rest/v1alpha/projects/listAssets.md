 
#  Method: projects.listAssets
Stay organized with collections  Save and categorize content based on your preferences. 
Lists any container asset, such as a folder or collection.
### HTTP request
`GET https://earthengine.googleapis.com/v1alpha/{parent=projects/*}:listAssets`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The name of the container asset to list. `parent` is of the format "projects/*" or "projects/*/assets/**" (e.g., "projects/[PROJECT]" or "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are currently under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). If "projects/earthengine-legacy" is specified, the response will consist of a list of all top-level folders owned by the requesting user. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:
  * `earthengine.assets.get`
  * `earthengine.assets.list`

  
### Query parameters
Parameters  
---  
`pageSize` |  `integer` The maximum number of results per page. The server may return fewer assets than requested. If unspecified, the page size default depends on the EarthEngineAssetView, with higher limits for more restrictive views.  
`pageToken` |  `string` A token identifying a page of results the server should return. Typically this is the value of `ListAssetsResponse.next_page_token[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ListAssetsResponse#FIELDS.next_page_token)` returned from the previous call to the `projects.listAssets` method.  
`filter` |  `string` If present, specifies a filter. Filters are only applied to `ImageCollection` assets and are ignored for `Folder` assets. The fields `startTime`, `endTime`, and members of `properties` are recognized. The custom function `intersects(str)` is available, which allows filtering by geometry. An example date filter: ```
"startTime>\"2020-01-01T00:00:00+00:00\" AND
endTime<\"2020-02-01T00:00:00+00:00\""

```
An example property filter: ```
"properties.CLOUDY_PIXEL_PERCENTAGE<30"

```
An example geometry filter: ```
"intersects(\"{'type':'Point','coordinates':[1,2]}\")"
"intersects(\"{\\\"type\\\":\\\"Point\\\",\\\"coordinates\\\":[1,2]}\")"

```
See <https://google.aip.dev/160> for more details on the filter language.  
`view` |  `enum (`EarthEngineAssetView[](https://developers.google.com/earth-engine/reference/rest/v1alpha/EarthEngineAssetView)`)` Specifies which parts of the `EarthEngineAsset` resource should be returned in the response. Only applies to `ImageCollection` assets. All elements of `Folder` assets will be encoded in the `BASIC` view regardless of the value of this field.  
### Request body
The request body must be empty.
### Response body
If successful, the response body contains an instance of `ListAssetsResponse[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ListAssetsResponse)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/earthengine.readonly`
  * `           https://www.googleapis.com/auth/cloud-platform`
  * `           https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
