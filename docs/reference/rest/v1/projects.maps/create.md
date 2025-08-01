 
#  Method: projects.maps.create
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.maps/create#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.maps/create#path-parameters)
  * [Query parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.maps/create#query-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.maps/create#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.maps/create#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.maps/create#authorization-scopes)


Creates an ID that can be used to render map tiles showing the results of a computation. The resulting ID should be used as part of `GetTile` requests.
This is used in conjunction with `GetTile`. A call to `maps.create` provides an expression and some output options. The result of `maps.create` is a map ID that represents an image that is the result of evaluating that expression and applying those options. Subsequently, calls to `GetTile` can be made to get image data for a tile of the resulting image, at any desired location and zoom. The map ID will be valid for a moderate period (a few hours).
The most common use case for this pair of endpoints is to populate a map viewport with a visualization of the output of some computation. In order for that to be possible, the computation output has to meet some reasonable requirements for the requested image format. In particular, JPEG or PNG format requires that there be one or three output bands, and clips values that are outside the 0-255 range.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{parent=projects/*}/maps`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The parent of the map collection (e.g., "projects/*"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:
  * `earthengine.maps.create`

  
### Query parameters
Parameters  
---  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Request body
The request body contains an instance of `EarthEngineMap[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.maps#EarthEngineMap)`.
### Response body
If successful, the response body contains a newly created instance of `EarthEngineMap[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.maps#EarthEngineMap)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/earthengine.readonly`
  * `           https://www.googleapis.com/auth/cloud-platform`
  * `           https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
