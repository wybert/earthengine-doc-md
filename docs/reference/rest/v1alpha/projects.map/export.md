 
#  Method: projects.map.export
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#authorization-scopes)
  * [TileOptions](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#tileoptions)
  * [ZoomSubset](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#zoomsubset)


Initiates a batch process that computes a tiled map and writes the result to Google Cloud Storage.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{project=projects/*}/map:export`
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
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression))
 },
 "description": string,
 "tileOptions": {
  object (TileOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#TileOptions))
 },
 "tileExportOptions": {
  object (ImageFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageFileExportOptions))
 },
 "requestId": string,
 "workloadTag": string,
 "priority": integer
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression)`)` An expression that evaluates to the image to compute and export. The bounds of the image will be used to determine the set of map tiles to render. To control the exported region, clip the image prior to exporting.  
`description` |  `string` A human-readable name of the task.  
`tileOptions` |  `object (`TileOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#TileOptions)`)` Options describing the map tiles to generate.  
`tileExportOptions` |  `object (`ImageFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageFileExportOptions)`)` Options for where and in what form to export the map tiles. Cloud Storage is currently the only supported destination for map exports.  
`requestId` |  `string` A unique string used to detect duplicated requests. If more than one request is made by the same user with the same non-empty `requestId`, only one of those requests may successfully start a long-running operation. `requestId` may contain the characters a..z, A..Z, 0-9, or '-'. `requestId` may be at most 60 characters long.  
`workloadTag` |  `string` User supplied label to track this computation.  
`priority` |  `integer` Optional. The priority of the export task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100 if not set.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`
  * `      https://www.googleapis.com/auth/devstorage.full_control`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
## TileOptions
Options describing image or video map tiles to export.
JSON representation  
---  
```
{
 "startZoom": integer,
 "minZoom": integer,
 "skipEmpty": boolean,
 "skipEmptyTiles": boolean,
 "mapsApiKey": string,
 "dimensions": {
  object (GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GridDimensions))
 },
 "tileDimensions": {
  object (GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GridDimensions))
 },
 "stride": integer,
 "zoomSubset": {
  object (ZoomSubset[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#ZoomSubset))
 },
 // Union field end_zoom_or_scale can be only one of the following:
 "endZoom": integer,
 "maxZoom": integer,
 "scale": number
 // End of list of possible types for union field end_zoom_or_scale.
}
```
  
Fields  
---  
`startZoom` |  `integer` The zoom level to start generating map tiles for export. Defaults to zero.  
`minZoom**(deprecated)**`|  `integer` This item is deprecated! The zoom level to start generating map tiles for export. Defaults to zero.  
`skipEmpty` |  `boolean` If true, skip writing empty (i.e. fully-transparent) map tiles.  
`skipEmptyTiles**(deprecated)**`|  `boolean` This item is deprecated! If true, skip writing empty (i.e. fully-transparent) map tiles.  
`mapsApiKey` |  `string` Optional Google Maps Platform API Key for generated map tile viewer.  
`dimensions` |  `object (`GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GridDimensions)`)` The width and height of output video tiles, used only for exporting tiled video pyramids (ExportVideoMap).  
`tileDimensions**(deprecated)**`|  `object (`GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GridDimensions)`)` This item is deprecated! The width and height of output video tiles, used only for exporting tiled video pyramids (ExportVideoMap).  
`stride` |  `integer` Tile row and column stride. (ExportVideoMap) Set to 4 for sparse tiles (WebGL-only) or 1 (default) for maximum compatibility.  
`zoomSubset` |  `object (`ZoomSubset[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.map/export#ZoomSubset)`)` A subset of zoom levels for which to generate tiles. May only be specified in a call to `ExportVideoMap`.  
Union field `end_zoom_or_scale`. The zoom level or scale at which to stop generating map tiles for. One or the other of these must be specified. `end_zoom_or_scale` can be only one of the following:  
`endZoom` |  `integer` The zoom level to stop generating map tiles for.  
`maxZoom**(deprecated)**`|  `integer` This item is deprecated! The zoom level to stop generating map tiles for.  
`scale` |  `number` The max image resolution in meters per pixel. The scale will be converted to the most appropriate maximum zoom level at the equator.  
## ZoomSubset
A subset of zoom levels for which to generate tiles (ExportVideoMap), Start and end subsets are double precision values, allowing you to render a zoom level or levels incrementally. To render a whole pyramid with a start zoom of 12: startZoom=0, endZoom=12, don't set this message. To render levels 0-11 and the first 10% of level 12: startZoom=0, endZoom=12, subset = {min=0, max=12.1 } To render the next 10% of level 12: startZoom=0, endZoom=12, subset = {min=12.1, max=12.2 } To render the remaining 80% of level 12: startZoom=0, endZoom=12, subset = {min=12.2, max=13 } Also note that all export shards must have the same (full) pyramid size in start/endZoom.
JSON representation  
---  
```
{
 "start": number,
 "end": number,
 "min": number,
 "max": number
}
```
  
Fields  
---  
`start` |  `number` Starting zoom level subset for which to generate tiles (ExportVideoMap) Here, subset is a double precision value, allowing you to render a zoom level incrementally, so 12.1 for example is the first 10% of the tiles in zoom 12 in some unspecified but deterministic order.  
`end` |  `number` Ending zoom level subset for which to generate tiles (ExportVideoMap), allowing you to render a zoom level incrementally, up to but not including the maximum subset (if provided) in some unspecified but deterministic order.  
`min**(deprecated)**`|  `number` This item is deprecated! Starting zoom level subset for which to generate tiles (ExportVideoMap) Here, subset is a double precision value, allowing you to render a zoom level incrementally, so 12.1 for example is the first 10% of the tiles in zoom 12 in some unspecified but deterministic order.  
`max**(deprecated)**`|  `number` This item is deprecated! Ending zoom level subset for which to generate tiles (ExportVideoMap), allowing you to render a zoom level incrementally, up to but not including the maximum subset (if provided) in some unspecified but deterministic order.  
Was this helpful?
