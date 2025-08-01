 
#  Method: projects.assets.listImages
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#path-parameters)
  * [Query parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#query-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#authorization-scopes)
  * [Image](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#image)


Lists the images in an image collection asset. This method allows the caller to apply spatiotemporal and metadata filters to an image collection.
### HTTP request
`GET https://earthengine.googleapis.com/v1alpha/{parent=projects/*/assets/**}:listImages`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The name of the image collection asset to list. `parent` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:
  * `earthengine.assets.get`

  
### Query parameters
Parameters  
---  
`pageSize` |  `integer` The maximum number of results per page. The server may return fewer assets than requested. If unspecified, the page size default depends on the EarthEngineAssetView, with higher limits for more restrictive views.  
`pageToken` |  `string` A token identifying a page of results the server should return. Typically, this is the value of `ListImagesResponse.next_page_token[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#body.ListImagesResponse.FIELDS.next_page_token)` returned from the previous call to the `assets.listImages` method.  
`startTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If present, filters results to those whose timestamp is at least this value (inclusive). Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` If present, filters results to those whose timestamp is less than this value (exclusive). Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`region` |  `string` If present, a geometry defining a query region, specified as a GeoJSON geometry string (see RFC 7946). Spatial intersection is accurate to one meter.  
`filter` |  `string` If present, specifies additional simple property filters.  
`view` |  `enum (`EarthEngineAssetView[](https://developers.google.com/earth-engine/reference/rest/v1alpha/EarthEngineAssetView)`)` Specifies which parts of the `Image` resource should be returned in the response. If unset the default is to return all properties.  
### Request body
The request body must be empty.
### Response body
Response message for EarthEngineService.ListImages.
If successful, the response body contains data with the following structure:
JSON representation  
---  
```
{
  "images": [
    {
      object (Image[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#Image))
    }
  ],
  "nextPageToken": string
}
```
  
Fields  
---  
`images[]` |  `object (`Image[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#Image)`)` The list of images matching the query.  
`nextPageToken` |  `string` A token to retrieve the next page of results. Pass this value in the `ListImagesRequest.page_token[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listImages#body.QUERY_PARAMETERS.page_token)` field in the subsequent call to the `assets.listImages` method to retrieve the next page of results.  
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/earthengine.readonly`
  * `           https://www.googleapis.com/auth/cloud-platform`
  * `           https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
## Image
Information about an Earth Engine image.
JSON representation  
---  
```
{
  "name": string,
  "id": string,
  "updateTime": string,
  "title": string,
  "description": string,
  "properties": {
    object
  },
  "startTime": string,
  "endTime": string,
  "geometry": {
    object
  },
  "bands": [
    {
      object (ImageBand[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.ImageBand))
    }
  ],
  "sizeBytes": string
}
```
  
Fields  
---  
`name` |  `string` The name of the image, if present. `name` is of the format "projects/*/assets/**" (e.g. "projects/earthengine-legacy/assets/users//"). This should typically be present for stored images, but will be the empty string for computed ones.  
`id` |  `string` The ID of the image, if present. Equivalent to `name` without the "projects/*/assets/" prefix (e.g. "users//"). This should typically be present for stored images, but will be the empty string for computed ones.  
`updateTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last-modified time of the image. Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`title` |  `string` The title of the asset.  
`description` |  `string` The description of the asset.  
`properties` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Key/value properties associated with the image.  
`startTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp associated with the image, if any, e.g. the time at which a satellite image was taken. For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the start of that interval. Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the end of that interval (exclusive). Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`geometry` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The spatial footprint associated with the image, if any, as a GeoJSON geometry object (see RFC 7946).  
`bands[]` |  `object (`ImageBand[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.ImageBand)`)` Information about the data bands of the image.  
`sizeBytes` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The size of a leaf asset (e.g. an image) in bytes. This should typically be non-zero for stored images, and zero for computed ones.  
