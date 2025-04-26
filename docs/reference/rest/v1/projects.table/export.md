 
#  Method: projects.table.export 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#authorization-scopes)
  * [TableFileExportOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#tablefileexportoptions)
  * [TableAssetExportOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#tableassetexportoptions)
  * [FeatureViewAssetExportOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#featureviewassetexportoptions)
  * [FeatureViewDestination](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#featureviewdestination)
  * [BigQueryExportOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#bigqueryexportoptions)
  * [BigQueryDestination](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#bigquerydestination)


Initiates a batch process that computes a table and writes the result to one of several destinations.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{project=projects/*}/table:export`
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
 "selectors": [
  string
 ],
 "requestId": string,
 "maxErrorMeters": number,
 "maxVertices": integer,
 "workloadTag": string,
 "priority": integer,
 // Union field export_options can be only one of the following:
 "fileExportOptions": {
  object (TableFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#TableFileExportOptions))
 },
 "assetExportOptions": {
  object (TableAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#TableAssetExportOptions))
 },
 "featureViewExportOptions": {
  object (FeatureViewAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#FeatureViewAssetExportOptions))
 },
 "bigqueryExportOptions": {
  object (BigQueryExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#BigQueryExportOptions))
 }
 // End of list of possible types for union field export_options.
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression)`)` An expression that evaluates to the table to compute and export.  
`description` |  `string` A human-readable name of the task.  
`selectors[]` |  `string` An explicit list of columns to include in the result.  
`requestId` |  `string` A unique string used to detect duplicated requests. If more than one request is made by the same user with the same non-empty `requestId`, only one of those requests may successfully start a long-running operation. `requestId` may contain the characters a..z, A..Z, 0-9, or '-'. `requestId` may be at most 60 characters long.  
`maxErrorMeters` |  `number` The max allowed error in meters when transforming geometry between coordinate systems. If empty, the max error is 1 meter by default.  
`maxVertices` |  `integer` Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size.  
`workloadTag` |  `string` User supplied label to track this computation.  
`priority` |  `integer` Optional. The priority of the export task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100 if not set.  
Union field `export_options`. Options describing where and how to store the results. `export_options` can be only one of the following:  
`fileExportOptions` |  `object (`TableFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#TableFileExportOptions)`)` If specified, configures export as a file.  
`assetExportOptions` |  `object (`TableAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#TableAssetExportOptions)`)` If specified, configures export as an Earth Engine asset.  
`featureViewExportOptions` |  `object (`FeatureViewAssetExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#FeatureViewAssetExportOptions)`)` If specified, configures export as a FeatureView map.  
`bigqueryExportOptions` |  `object (`BigQueryExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#BigQueryExportOptions)`)` If specified, configures export of tabular data to BigQuery.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/devstorage.full_control`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
## TableFileExportOptions
Options for exporting tables as files outside Earth Engine.
JSON representation  
---  
```
{
 "fileFormat": enum (TableFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.tables#Table.TableFileFormat)),
 // Union field destination can be only one of the following:
 "driveDestination": {
  object (DriveDestination[](https://developers.google.com/earth-engine/reference/rest/v1/DriveDestination))
 },
 "cloudStorageDestination": {
  object (CloudStorageDestination[](https://developers.google.com/earth-engine/reference/rest/v1/CloudStorageDestination))
 }
 // End of list of possible types for union field destination.
}
```
  
Fields  
---  
`fileFormat` |  `enum (`TableFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.tables#Table.TableFileFormat)`)` The file format in which to export the table(s).  
Union field `destination`. Where to write the results. `destination` can be only one of the following:  
`driveDestination` |  `object (`DriveDestination[](https://developers.google.com/earth-engine/reference/rest/v1/DriveDestination)`)` If specified, configures export to Google Drive.  
`cloudStorageDestination` |  `object (`CloudStorageDestination[](https://developers.google.com/earth-engine/reference/rest/v1/CloudStorageDestination)`)` If specified, configures export to Google Cloud Storage.  
## TableAssetExportOptions
Options for saving tables as Earth Engine assets.
JSON representation  
---  
```
{
 // Union field destination can be only one of the following:
 "earthEngineDestination": {
  object (EarthEngineDestination[](https://developers.google.com/earth-engine/reference/rest/v1/EarthEngineDestination))
 }
 // End of list of possible types for union field destination.
}
```
  
Fields  
---  
Union field `destination`. Where to write the results. `destination` can be only one of the following:  
`earthEngineDestination` |  `object (`EarthEngineDestination[](https://developers.google.com/earth-engine/reference/rest/v1/EarthEngineDestination)`)` If specified, configures export to Earth Engine.  
## FeatureViewAssetExportOptions
Options for saving tables or FeatureCollections as FeatureView maps.
JSON representation  
---  
```
{
 "ingestionTimeParameters": {
  object (FeatureViewIngestionTimeParameters[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewIngestionTimeParameters))
 },
 // Union field destination can be only one of the following:
 "featureViewDestination": {
  object (FeatureViewDestination[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#FeatureViewDestination))
 }
 // End of list of possible types for union field destination.
}
```
  
Fields  
---  
`ingestionTimeParameters` |  `object (`FeatureViewIngestionTimeParameters[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewIngestionTimeParameters)`)` The FeatureView ingestion time parameters. These parameters must be specified at ingestion time and cannot be updated on the fly.  
Union field `destination`. Where to write the results. `destination` can be only one of the following:  
`featureViewDestination` |  `object (`FeatureViewDestination[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#FeatureViewDestination)`)` If specified, configures export to FeatureViews.  
## FeatureViewDestination
Configuration for an Earth Engine FeatureView destination.
JSON representation  
---  
```
{
 "name": string,
 "assetVersion": integer
}
```
  
Fields  
---  
`name` |  `string` Required. The FeatureView asset ID. The server generates a map name from the ID.  
`assetVersion` |  `integer` The FeatureView asset version to create. Used for aliasing versions with assets. If not set, 0 will be used.  
## BigQueryExportOptions
Options for exporting tabular data to BigQuery.
JSON representation  
---  
```
{
 // Union field destination can be only one of the following:
 "bigqueryDestination": {
  object (BigQueryDestination[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#BigQueryDestination))
 }
 // End of list of possible types for union field destination.
}
```
  
Fields  
---  
Union field `destination`. Where to write the data. `destination` can be only one of the following:  
`bigqueryDestination` |  `object (`BigQueryDestination[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/export#BigQueryDestination)`)` If specified, configures export to BigQuery.  
## BigQueryDestination
Configuration for a destination in BigQuery.
JSON representation  
---  
```
{
 "table": string,
 "overwrite": boolean,
 "append": boolean
}
```
  
Fields  
---  
`table` |  `string` Required. The BigQuery destination table reference in the following format: "projectId.dataset_id.table_id".If the referenced resource does not exist, new table will be created. This applies if "append" and "overwrite" parameters are both false as well.If the referenced resource does exist and has compatible schema, one of the "overwrite" and "append" parameters has to be true, otherwise the task will fail.If referenced resource exists and schema is not compatible with the existing one, task will also fail.  
`overwrite` |  `boolean` Specifies if the table data should be overwritten if the table already exists and has a compatible schema.The `overwrite` and `append` parameters cannot be `true` simultaneously.  
`append` |  `boolean` Specifies if the table data should be appended if the table already exists and has a compatible schema.The `overwrite` and `append` parameters cannot be `true` simultaneously.  
