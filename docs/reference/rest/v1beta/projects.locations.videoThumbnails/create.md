 
#  Method: projects.locations.videoThumbnails.create 
Stay organized with collections  Save and categorize content based on your preferences. 
Creates an ID that can be used to render an image containing an animation of multiple images from a collection.
This is used in conjunction with `GetVideoThumbnailPixels`. A call to `videoThumbnails.create` provides an expression and some output options. The result of `videoThumbnails.create` is an ID that represents an image that is the result of evaluating that expression and applying those options. Subsequently, calls to `GetVideoThumbnailPixels` can be made to get an image showing all of the elements of an ImageCollection, animated from first to last. The ID will be valid for a moderate period (a few hours).
The request is limited to 512*512*100 pixels in total, across all Images in the ImageCollection. Requests exceeding these limits will result in an error code of 400 (BAD_REQUEST).
### HTTP request
`POST https://earthengine.googleapis.com/v1beta/{parent=projects/*/locations/*}/videoThumbnails`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The parent of the location where the video thumbnail will be created (e.g., "projects/*"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:
  * `earthengine.videothumbnails.create`

  
### Query parameters
Parameters  
---  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Request body
The request body contains an instance of `VideoThumbnail[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.videoThumbnails#VideoThumbnail)`.
### Response body
If successful, the response body contains a newly created instance of `VideoThumbnail[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.videoThumbnails#VideoThumbnail)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
