 
#  Method: projects.featureViews.tiles.get
Stay organized with collections  Save and categorize content based on your preferences. 
Computes a map tile image showing a portion of a FeatureView. The request includes values from a previous `CreateFeatureView` request.
### HTTP request
`GET https://earthengine.googleapis.com/v1beta/{parent=projects/*/featureViews/*}/tiles/{zoom}/{x}/{y}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` A map name from `FeatureView.name`.  
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
  * `           https://www.googleapis.com/auth/earthengine.readonly`
  * `           https://www.googleapis.com/auth/cloud-platform`
  * `           https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
