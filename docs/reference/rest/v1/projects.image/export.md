 
#  Method: projects.image.export
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#authorization-scopes)
  * [ImageAssetExportOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#imageassetexportoptions)


Initiates a batch process that computes an image and writes the result to one of several destinations.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{project=projects/*}/image:export`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.exports.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
  "expression": {
    object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression))
  },
  "description": string,
  "maxPixels": string,
  "grid": {
    object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid))
  },
  "requestId": string,
  "workloadTag": string,
  "priority": integer,

  // Union field export_options can be only one of the following:
  "fileExportOptions": {
    object (ImageFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions))
  },
  "assetExportOptions": {
    object (ImageAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#ImageAssetExportOptions))
  }
  // End of list of possible types for union field export_options.
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression)`)` An expression that evaluates to the image to compute and export.  
`description` |  `string` A human-readable name of the task.  
`maxPixels` |  `string (Int64Value[](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of pixels to compute and export. This is a safety guard to prevent you from accidentally starting a larger export than you had intended. The default value is 1e8 pixels, but you can set the value explicitly to raise or lower this limit.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid)`)` Parameters describing how the image computed by `expression` should be reprojected and clipped. If not present, the full computed image is returned in its native projection.  
`requestId` |  `string` A unique string used to detect duplicated requests. If more than one request is made by the same user with the same non-empty `requestId`, only one of those requests may successfully start a long-running operation. `requestId` may contain the characters a..z, A..Z, 0-9, or '-'. `requestId` may be at most 60 characters long.  
`workloadTag` |  `string` User supplied label to track this computation.  
`priority` |  `integer` Optional. The priority of the export task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100 if not set.  
Union field `export_options`. Options describing where and how to store the results. `export_options` can be only one of the following:  
`fileExportOptions` |  `object (`ImageFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions)`)` If specified, configures export as a file.  
`assetExportOptions` |  `object (`ImageAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.image/export#ImageAssetExportOptions)`)` If specified, configures export as an Earth Engine asset.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/cloud-platform`
  * `           https://www.googleapis.com/auth/devstorage.full_control`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
## ImageAssetExportOptions
Options for saving images as Earth Engine assets.
JSON representation  
---  
```
{
  "pyramidingPolicy": enum (PyramidingPolicy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/PyramidingPolicy)),
  "pyramidingPolicyOverrides": {
    string: enum (PyramidingPolicy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/PyramidingPolicy)),
    ...
  },

  // Union field destination can be only one of the following:
  "earthEngineDestination": {
    object (EarthEngineDestination[](https://developers.google.com/earth-engine/reference/rest/v1/EarthEngineDestination))
  }
  // End of list of possible types for union field destination.
}
```
  
Fields  
---  
`pyramidingPolicy` |  `enum (`PyramidingPolicy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/PyramidingPolicy)`)` The pyramiding policy to apply by default to all bands.  
`pyramidingPolicyOverrides` |  `map (key: string, value: enum (`PyramidingPolicy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/PyramidingPolicy)`))` Specific per-band pyramid policy overrides. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `destination`. Where to write the results. `destination` can be only one of the following:  
`earthEngineDestination` |  `object (`EarthEngineDestination[](https://developers.google.com/earth-engine/reference/rest/v1/EarthEngineDestination)`)` If specified, configures export to Earth Engine.  
Was this helpful?
