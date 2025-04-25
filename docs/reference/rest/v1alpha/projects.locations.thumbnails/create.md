 
#  Method: projects.locations.thumbnails.create 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails/create#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails/create#path-parameters)
  * [Query parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails/create#query-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails/create#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails/create#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails/create#authorization-scopes)


Creates an ID that can be used to render a "thumbnail" image.
This is used in conjunction with `GetThumbnailPixels`. A call to `thumbnails.create` provides an expression and some output options. The result of `thumbnails.create` is an ID that represents an image that is the result of evaluating that expression and applying those options. Subsequently, calls to `GetThumbnailPixels` can be made to get the image data for the entire resulting image. The ID will be valid for a moderate period (a few hours).
The most common use case for this pair of endpoints is to provide a complex expression via a POST to `thumbnails.create`, and then fetch the computed image via a GET to `GetThumbnailPixels`. This two-part process allows for use in more situations than `ComputePixels`. In particular: - the result of `ComputePixels` needs to be unwrapped to get the encoded image bytes. The result of `GetThumbnailPixels` can be displayed directly by a browser. - `ComputePixels` can only be called by an authorised user, using a properly-scoped OAuth token. `thumbnails.create` has the same restriction, but `GetThumbnailPixels` can be invoked with a URL containing an API key, so URLs invoking it can be used more broadly.
The result of evaluating the expression has to meet some reasonable requirements for the requested image format. In particular, JPEG or PNG format requires that there be one or three output bands, and clips values that are outside the 0-255 range.
The description "thumbnail" does not imply a restriction on the size of the computed image: the same restrictions as `ComputePixels` apply to `thumbnails.create`/`GetThumbnailPixels`. Requests are limited to 48MB in uncompressed data per request, computed as the product of the request dimensions in pixels, the number of image bands requested, and the number of bytes per pixel for each band. Requests are also limited to at most 32K pixels in either dimension and at most 1024 bands. Requests exceeding these limits will result in an error code of 400 (BAD_REQUEST).
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{parent=projects/*/locations/*}/thumbnails`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The parent of the thumbnail collection (e.g., "projects/*"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:
  * `earthengine.thumbnails.create`

  
### Query parameters
Parameters  
---  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Request body
The request body contains an instance of `Thumbnail[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails#Thumbnail)`.
### Response body
If successful, the response body contains a newly created instance of `Thumbnail[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.thumbnails#Thumbnail)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
