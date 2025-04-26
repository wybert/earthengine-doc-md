 
#  Method: projects.videoThumbnails.getPixels 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.videoThumbnails/getPixels#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.videoThumbnails/getPixels#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.videoThumbnails/getPixels#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.videoThumbnails/getPixels#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.videoThumbnails/getPixels#authorization-scopes)


Computes an image showing the result of a computation. The request includes values (an ID and authorisation token) from a previous `videoThumbnails.create` request.
### HTTP request
`GET https://earthengine.googleapis.com/v1/{name=projects/*/videoThumbnails/*}:getPixels`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`name` |  `string` Required. A video thumbnail name from `VideoThumbnail.name`.  
### Request body
The request body must be empty.
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
