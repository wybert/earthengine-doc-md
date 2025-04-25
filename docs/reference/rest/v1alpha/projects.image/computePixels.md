 
#  Method: projects.image.computePixels 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/computePixels#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/computePixels#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/computePixels#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/computePixels#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/computePixels#authorization-scopes)


Computes a tile of pixels by performing an arbitrary computation on image data.
Requests are limited to 48MB in uncompressed data per request, computed as the product of the request dimensions in pixels, the number of image bands requested, and the number of bytes per pixel for each band. Requests are also limited to at most 32K pixels in either dimension and at most 1024 bands. Requests exceeding these limits will result in an error code of 400 (BAD_REQUEST).
If successful, the response body contains the requested pixel data in the encoding specified in the `fileFormat` field of the request.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{project=projects/*}/image:computePixels`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.computations.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression))
 },
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageFileFormat)),
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1alpha/PixelGrid))
 },
 "bandIds": [
  string
 ],
 "visualizationOptions": {
  object (VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/VisualizationOptions))
 },
 "workloadTag": string
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression)`)` The expression to compute.  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageFileFormat)`)` The output file format in which to return the pixel values.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1alpha/PixelGrid)`)` Parameters describing how the image computed by `expression` should be reprojected and clipped. If not present, the full computed image is returned in its native projection.  
`bandIds[]` |  `string` If present, specifies a specific set of bands that will be selected from the result of evaluating `expression`. If not present, all bands resulting from `expression` will be selected.  
`visualizationOptions` |  `object (`VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/VisualizationOptions)`)` If present, a set of visualization options to apply to produce an 8-bit RGB visualization of the data.  
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
