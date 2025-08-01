 
#  Method: projects.assets.listFeatures
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#path-parameters)
  * [Query parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#query-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#authorization-scopes)


Lists the features in a table asset. This method allows the caller to apply spatiotemporal and property filters to a table. Results are returned as a list of GeoJSON feature objects.
### HTTP request
`GET https://earthengine.googleapis.com/v1alpha/{asset=projects/*/assets/**}:listFeatures`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`asset` |  `string` Required. The name of the table asset to list. `asset` is of the format "projects/*/assets/**" (e.g., "projects/earthengine-legacy/assets/users/[USER]/[ASSET]"). All user-owned assets are under the project "earthengine-legacy" (e.g., "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g., "projects/earthengine-public/assets/LANDSAT"). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `asset`:
  * `earthengine.assets.get`

  
### Query parameters
Parameters  
---  
`pageSize` |  `integer` The maximum number of results per page. The server may return fewer assets than requested. If unspecified, the page size default is 1000 results per page.  
`pageToken` |  `string` A token identifying a page of results the server should return. Typically, this is the value of `ListFeaturesResponse.next_page_token[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#body.ListFeaturesResponse.FIELDS.next_page_token)` returned from the previous call to the `assets.listFeatures` method.  
`region` |  `string` If present, a geometry defining a query region, specified as a GeoJSON geometry string (see RFC 7946).  
`filter` |  `string` If present, specifies additional simple property filters.  
### Request body
The request body must be empty.
### Response body
Response message for EarthEngineService.ListFeatures.
If successful, the response body contains data with the following structure:
JSON representation  
---  
```
{
  "type": string,
  "features": [
    {
      object (Feature[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Feature))
    }
  ],
  "nextPageToken": string
}
```
  
Fields  
---  
`type` |  `string` Always contains the constant string "FeatureCollection", marking this as a GeoJSON FeatureCollection object.  
`features[]` |  `object (`Feature[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Feature)`)` The list of features matching the query, as a list of GeoJSON feature objects (see RFC 7946) containing the string "Feature" in a field named "type", the geometry in a field named "geometry", and key/value properties in a field named "properties".  
`nextPageToken` |  `string` A token to retrieve the next page of results. Pass this value in the `ListFeaturesRequest.page_token[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/listFeatures#body.QUERY_PARAMETERS.page_token)` field in the subsequent call to the `assets.listFeatures` method to retrieve the next page of results.  
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/earthengine.readonly`
  * `           https://www.googleapis.com/auth/cloud-platform`
  * `           https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
