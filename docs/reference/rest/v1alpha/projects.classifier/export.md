 
#  Method: projects.classifier.export
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#authorization-scopes)
  * [ClassifierAssetExportOptions](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#classifierassetexportoptions)


Initiates a batch process that computes a classifier and saves it as an Earth Engine asset.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{project=projects/*}/classifier:export`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` Required. The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.exports.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression))
 },
 "description": string,
 "requestId": string,
 "assetExportOptions": {
  object (ClassifierAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#ClassifierAssetExportOptions))
 },
 "workloadTag": string,
 "priority": integer
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression)`)` Required. An expression that evaluates to an Earth Engine Classifier to compute and export.  
`description` |  `string` Optional. An optional human-readable name of the task.  
`requestId` |  `string` Optional. A unique string used to detect duplicated requests. If more than one request is made by the same user with the same non-empty `requestId`, only one of those requests may successfully start a long-running operation. `requestId` may contain the characters a..z, A..Z, 0-9, or '-'. `requestId` may be at most 60 characters long.  
`assetExportOptions` |  `object (`ClassifierAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.classifier/export#ClassifierAssetExportOptions)`)` Required. Configures the export as an Earth Engine asset.  
`workloadTag` |  `string` Optional. User supplied label to track this computation.  
`priority` |  `integer` Optional. The priority of the export task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100 if not set.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
## ClassifierAssetExportOptions
Options for saving tables as Earth Engine assets.
JSON representation  
---  
```
{
 // Union field destination can be only one of the following:
 "earthEngineDestination": {
  object (EarthEngineDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/EarthEngineDestination))
 }
 // End of list of possible types for union field destination.
}
```
  
Fields  
---  
Union field `destination`. Where to write the results. `destination` can be only one of the following:  
`earthEngineDestination` |  `object (`EarthEngineDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/EarthEngineDestination)`)` If specified, configures export to Earth Engine.  
Was this helpful?
