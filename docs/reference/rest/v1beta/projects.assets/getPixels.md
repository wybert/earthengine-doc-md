 
#  Method: projects.assets.getPixels
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/getPixels#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/getPixels#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/getPixels#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/getPixels#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets/getPixels#authorization-scopes)


Fetches pixels from an image asset. This custom method allows the caller to request an arbitrary tile of pixels from an image, optionally specifying the bands and map projection. Masked or missing data will be encoded as zeroes.
Requests are limited to 48MB in uncompressed data per request, computed as the product of the request dimensions in pixels, the number of image bands requested, and the number of bytes per pixel for each band. Requests are also limited to at most 32K pixels in either dimension and at most 1024 bands. Requests exceeding these limits will result in an error code of 400 (BAD_REQUEST).
If successful, the response body contains the requested pixel data in the encoding specified in the `fileFormat` field of the request.
### HTTP request
`POST https://earthengine.googleapis.com/v1beta/{name=projects/*/assets/**}:getPixels`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` Required. The name of the image asset from which to get pixels. `name` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:
  * `earthengine.assets.get`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)),
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid))
 },
 "region": {
  object
 },
 "bandIds": [
  string
 ],
 "visualizationOptions": {
  object (VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/VisualizationOptions))
 },
 "workloadTag": string
}
```
  
Fields  
---  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)`)` The output file format in which to return the pixel values.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid)`)` Parameters describing the pixel grid in which to fetch data. Defaults to the native pixel grid of the data.  
`region` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` If present, the region of data to return, specified as a GeoJSON geometry object (see RFC 7946). Since the returned image is always rectangular, the bounding box of the given geometry in the output coordinate system will actually be used. If `grid.dimensions` is also specified then the grid will finally be rescaled to the requested size.  
`bandIds[]` |  `string` If present, specifies a specific set of bands from which to get pixels. Bands are identified by id, as indicated by the `id` field of an ImageBand proto.  
`visualizationOptions` |  `object (`VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/VisualizationOptions)`)` If present, a set of visualization options to apply to produce an 8-bit RGB visualization of the data, rather than returning the raw data.  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Response body
If successful, the response is a generic HTTP response whose format is defined by the method.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
Was this helpful?
