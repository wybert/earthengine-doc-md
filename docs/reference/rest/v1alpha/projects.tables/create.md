 
#  Method: projects.tables.create 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/create#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/create#path-parameters)
  * [Query parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/create#query-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/create#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/create#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/create#authorization-scopes)


Creates an ID that can be used to render "table" data.
This is used in conjunction with `tables.getFeatures`. A call to `tables.create` provides an expression and some output options. The result of `tables.create` is an ID that represents a table that is the result of evaluating that expression and applying those options. Subsequently, calls to `tables.getFeatures` can be made to get the table data for the entire resulting table. The ID will be valid for a moderate period (a few hours).
The most common use case for this pair of endpoints is to provide a complex expression via a POST to `tables.create`, and then fetch the computed table via a GET to `tables.getFeatures`. This two-part process allows for use in more situations than `ComputeFeatures`. In particular: - the result of `ComputeFeatures` requires pagination to get the entirety of the features. Additionally only individual `Feature`s are returned. - `ComputeFeatures` can only be called by an authorized user, using a properly-scoped OAuth token. `tables.create` has the same restriction, but `GetTableData` can be invoked with a URL containing an API key, so URLs invoking it can be used more broadly.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{parent=projects/*}/tables`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`parent` |  `string` Required. The parent of the location where the table will be created (e.g., "projects/*").  
### Query parameters
Parameters  
---  
`workloadTag` |  `string` User supplied tag to track this computation.  
### Request body
The request body contains an instance of `Table[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.tables#Table)`.
### Response body
If successful, the response body contains a newly created instance of `Table[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.tables#Table)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/earthengine.readonly`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/cloud-platform.read-only`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
