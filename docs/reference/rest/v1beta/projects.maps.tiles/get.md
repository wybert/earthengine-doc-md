 
#  Method: projects.maps.tiles.get
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.maps.tiles/get#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.maps.tiles/get#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.maps.tiles/get#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.maps.tiles/get#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.maps.tiles/get#authorization-scopes)


Computes a map tile image showing a portion of a computation. The request includes values (a map ID and authorisation token) from a previous `CreateMap` request.
### HTTP request
`GET https://earthengine.googleapis.com/v1beta/{parent=projects/*/maps/*}/tiles/{zoom}/{x}/{y}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` A map name from `EarthEngineMap.name`.  
`zoom` |  `integer` The [zoom level][https://developers.google.com/maps/documentation/javascript/coordinates] of the requested map tile.  
`x` |  `integer` The [x coordinate][https://developers.google.com/maps/documentation/javascript/coordinates] of the requested map tile.  
`y` |  `integer` The [y coordinate][https://developers.google.com/maps/documentation/javascript/coordinates] of the requested map tile.  
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
