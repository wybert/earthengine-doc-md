 
#  Method: projects.table.import
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#authorization-scopes)
  * [TableManifest](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#tablemanifest)
  * [TableSource](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#tablesource)


Imports a table.
### HTTP request
`POST https://earthengine.googleapis.com/v1/{project=projects/*}/table:import`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.assets.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
  "tableManifest": {
    object (TableManifest[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#TableManifest))
  },
  "description": string,
  "overwrite": boolean,
  "requestId": string
}
```
  
Fields  
---  
`tableManifest` |  `object (`TableManifest[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#TableManifest)`)` The table manifest.  
`description` |  `string` A human-readable name of the task.  
`overwrite` |  `boolean` Whether to allow overwriting an existing asset.  
`requestId` |  `string` A unique string used to detect duplicated requests. If more than one request is made by the same user with the same non-empty `requestId`, only one of those requests may successfully start a long-running operation. `requestId` may contain the characters a..z, A..Z, 0-9, or '-'. `requestId` may be at most 60 characters long.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
## TableManifest
Describes how the EarthEngine service should compose a table from a set of files.
JSON representation  
---  
```
{
  "name": string,
  "properties": {
    object
  },
  "uriPrefix": string,
  "sources": [
    {
      object (TableSource[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#TableSource))
    }
  ],
  "startTime": string,
  "endTime": string,
  "csvColumnDataTypeOverrides": {
    string: enum (CsvColumnDataType[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/CsvColumnDataType)),
    ...
  },
  "columnDataTypeOverrides": {
    string: enum (ColumnDataType[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ColumnDataType)),
    ...
  },
  "memo": string
}
```
  
Fields  
---  
`name` |  `string` The name of the asset to be created. `name` is of the format "projects/*/assets/**" (e.g. "projects/earthengine-legacy/assets/users//"). All user-owned assets are under the project "earthengine-legacy" (e.g. "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g. "projects/earthengine-public/assets/LANDSAT").  
`properties` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Additional properties of the asset. The property names "system:time_start" and "system:time_end" are deprecated. Use the fields `startTime` and `endTime` instead.  
`uriPrefix` |  `string` The optional prefix prepended to all `uri`s defined in this manifest.  
`sources[]` |  `object (`TableSource[](https://developers.google.com/earth-engine/reference/rest/v1/projects.table/import#TableSource)`)` The sources which comprise this table.  
`startTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp associated with the asset, if any, e.g. the time at which a satellite image was taken. For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the start of that interval. Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the end of that interval (exclusive). Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`csvColumnDataTypeOverrides  
**(deprecated)**`|  `map (key: string, value: enum (`CsvColumnDataType[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/CsvColumnDataType)`))` This item is deprecated! Use columnDataTypeOverrides instead. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`columnDataTypeOverrides` |  `map (key: string, value: enum (`ColumnDataType[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ColumnDataType)`))` A map from column name to the type to use for that column. Columns not specified here will have their type inferred, such that number columns become numbers, WKT columns become geometry, etc. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`memo` |  `string` Freeform field to store user notes. Not used in ingestion.  
## TableSource
A table file.
JSON representation  
---  
```
{
  "uris": [
    string
  ],
  "charset": string,
  "maxErrorMeters": number,
  "maxVertices": integer,
  "crs": string,
  "geodesic": boolean,
  "primaryGeometryColumn": string,
  "xColumn": string,
  "yColumn": string,
  "dateFormat": string,
  "csvDelimiter": string,
  "csvQualifier": string
}
```
  
Fields  
---  
`uris[]` |  `string` The URIs of the data to import. Currently only Google Cloud Storage URIs are supported. Each URI must be specified in the following format: "gs://bucket-id/object-id". The primary object should be the first element of the list, sidecar files are inferred from the filepath of the primary object. Only one URI is currently supported. If more than one URI is specified an `INALID_ARGUMENT` error is returned.  
`charset` |  `string` The name of the default charset to use for decoding strings. If empty, the charset "utf-8" is assumed by default.  
`maxErrorMeters` |  `number` The max allowed error in meters when transforming geometry between coordinate systems. If empty, the max error is 1 meter by default.  
`maxVertices` |  `integer` The max number of vertices. If not zero, geometry will be subdivided into spatially disjoint pieces which are each under this limit.  
`crs` |  `string` The default CRS code or WKT string specifying the coordinate reference system of any geometry that does not have one specified. If left blank, the default will be EPSG:4326: <https://epsg.io/4326>. For CSV/TFRecord sources only.  
`geodesic` |  `boolean` The default strategy for interpreting edges in geometry that do not have one otherwise specified. If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. When blank, defaults to false if 'crs' is a projected coordinate system. For CSV/TFRecord sources only.  
`primaryGeometryColumn` |  `string` The geometry column to use as a row's primary geometry when there is more than one geometry column. If left blank and more than one geometry column exists, the first geometry column encountered is used. For CSV/TFRecord sources only.  
`xColumn` |  `string` The name of the numeric x coordinate column for deducing point geometry. If the yColumn is also specified, and both columns contain number values, then a point geometry column will be constructed with x,y values in the coordinate system given in 'crs'. If left blank and 'crs' does _not_ specify a projected coordinate system, defaults to "longitude". If left blank and 'crs' _does_ specify a projected coordinate system, defaults to "" and no point geometry is generated. A generated point geometry column will be named {xColumn}_{yColumn}_N where N is appended such that {xColumn}_{yColumn}_N is unique if a column named {xColumn}_{yColumn} already exists. For CSV/TFRecord sources only.  
`yColumn` |  `string` The name of the numeric y coordinate column for deducing point geometry. If the xColumn is also specified, and both columns contain number values, then a point geometry column will be constructed with x,y values in the coordinate system given in 'crs'. If left blank and 'crs' does _not_ specify a projected coordinate system, defaults to "latitude". If left blank and 'crs' _does_ specify a projected coordinate system, defaults to "" and no point geometry is generated. A generated point geometry column will be named {xColumn}_{yColumn}_N where N is appended such that {xColumn}_{yColumn}_N is unique if a column named {xColumn}_{yColumn} already exists. For CSV/TFRecord sources only.  
`dateFormat` |  `string` A format with which to parse fields encoding dates. The format pattern must be as described at <http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html>. If left blank, dates will be imported as strings. For CSV/TFRecord sources only.  
`csvDelimiter` |  `string` When ingesting CSV files, a single character used as a delimiter between column values in a row. If left blank, defaults to ','. For CSV sources only.  
`csvQualifier` |  `string` When ingesting CSV files, a character that surrounds column values (a.k.a. "quote character"). If left blank, defaults to '"'. For CSV sources only. If a column value is not surrounded by qualifiers, leading and tailing whitespace is trimmed. For example: ..., test,... <== this value is not qualified becomes the string value: "test" <== whitespace is stripped where: ...," test",... <== this value IS qualified with quotes becomes the string value: " test" <== whitespace remains!  
