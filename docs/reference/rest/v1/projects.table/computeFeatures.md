 
#  Method: projects.table.computeFeatures
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/computeFeatures#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/computeFeatures#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/computeFeatures#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/computeFeatures#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/computeFeatures#authorization-scopes)


Computes a set of features by applying an arbitrary computation to features in one or more tables. Results are returned as a list of GeoJSON feature objects.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{project=projects/*}/table:computeFeatures`
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
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression))
 },
 "pageSize": integer,
 "pageToken": string,
 "workloadTag": string
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression)`)` The expression to compute.  
`pageSize` |  `integer` The maximum number of results per page. The server may return fewer features than requested. If unspecified, the page size default is 1000 results per page.  
`pageToken` |  `string` A token identifying a page of results the server should return. Typically, this is the value of `ComputeFeaturesResponse.next_page_token[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/computeFeatures#body.ComputeFeaturesResponse.FIELDS.next_page_token)` returned from the previous call to the `table.computeFeatures` method.  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Response body
Response message for EarthEngineService.ComputeFeatures.
If successful, the response body contains data with the following structure:
JSON representation  
---  
```
{
 "type": string,
 "features": [
  {
   object (Feature[](https://developers.google.com/earth-engine/reference/rest/v1/Feature))
  }
 ],
 "nextPageToken": string
}
```
  
Fields  
---  
`type` |  `string` Always contains the constant string "FeatureCollection", marking this as a GeoJSON FeatureCollection object.  
`features[]` |  `object (`Feature[](https://developers.google.com/earth-engine/reference/rest/v1/Feature)`)` The list of features matching the query, as a list of GeoJSON feature objects (see RFC 7946) containing the string "Feature" in a field named "type", the geometry in a field named "geometry", and key/value properties in a field named "properties".  
`nextPageToken` |  `string` A token to retrieve the next page of results. Pass this value in the `ComputeFeaturesRequest.page_token[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/computeFeatures#body.request_body.FIELDS.page_token)` field in the subsequent call to the `table.computeFeatures` method to retrieve the next page of results.  
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
