 
#  Table Manifest Upload
Stay organized with collections  Save and categorize content based on your preferences. 
If you need more flexibility uploading tables into Google Earth Engine (EE) than the [Code Editor UI](https://developers.google.com/earth-engine/table_upload) or the `upload` command of the ['earthengine' command-line tool](https://developers.google.com/earth-engine/command_line#upload) provide, you can do so by describing a table upload using a JSON file known as a "manifest" and using the `upload table --manifest` command of the command-line tool.
## One-time setup
  1. Manifest uploads only work with files located in [Google Cloud Storage](https://cloud.google.com/storage/getting-started/). To start using Google Cloud Storage, [create a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects), if you don't already have one. Note that setup requires specifying a credit card for billing. EE itself isn't charging anyone at this point, but transferring files to Google Cloud Storage before uploading them to EE will have [a small cost](https://cloud.google.com/storage/pricing). For typical upload data sizes (tens or hundreds of gigabytes), the cost will be quite low.
  2. Within your project, [turn on the Cloud Storage API](https://cloud.google.com/apis/docs/enable-disable-apis) and [create a bucket](https://cloud.google.com/storage/docs/creating-buckets).
  3. [Install the Earth Engine Python client](https://developers.google.com/earth-engine/python_install). It includes the `earthengine` command-line tool, which we will use for uploading data.
  4. For automated uploads, you may want to use a [Google Cloud service account](https://cloud.google.com/iam/docs/understanding-service-accounts) associated with your project. You don't need a service account for testing, but when you have a moment, please start familiarizing yourself with using them.


## Asset IDs and names
For assets in Cloud projects, use `projects/my_cloud_project/assets/my_asset`.
For older legacy projects, the asset name in the manifest needs to be slightly different from the asset ID visible elsewhere in Earth Engine. To upload assets whose asset IDs start with `users/some_user` or `projects/some_project`, the asset name in the manifest must have the string `projects/earthengine-legacy/assets/` prepended to the ID. For example, EE asset ID `users/username/my_table` should be uploaded using the name `projects/earthengine-legacy/assets/users/username/my_table`.
Yes, this means that IDs like `projects/some_projects/some_asset` get converted into names where `projects` is mentioned twice: `projects/earthengine-legacy/assets/projects/some_projects/some_asset`. This is confusing but necessary to conform to the Google Cloud API standards.
## Using manifests
The simplest possible manifest is shown below. It uploads a file named `small.csv` from a Google Cloud Storage bucket named `gs://earthengine-test`.
```
{
  "name": "projects/some-project-id/assets/some-asset-id",
  "sources": [
    {
      "uris": [
        "gs://earthengine-test/small.csv"
      ]
    }
  ]
}
```

To use it, save it to a file named `manifest.json` and run:
```
earthengineuploadtable--manifest/path/to/manifest.json
```

(The file `gs://earthengine-test/small.csv` exists and is publicly readable-you can use it for testing.)
For shapefile uploads, specify just the .shp file; the other files will be detected automatically.
### Multiple sources
It's possible to specify multiple CSV or shapefile sources, with one file per source. In this case, each CSV file must have the same structure. For example, we have two CSV files, `region1.csv` and `region2.csv`:
id | shape  
---|---  
1 | {"type":"Point","coordinates":[-119,36]}  
2 | {"type":"Point","coordinates":[-118,37]}  
3 | {"type":"Point","coordinates":[-117,38]}  
id | shape  
---|---  
4 | {"type":"Point","coordinates":[-112,40]}  
5 | {"type":"Point","coordinates":[-111,41]}  
6 | {"type":"Point","coordinates":[-110,42]}  
They have the same structure, but different contents. They've been uploaded into a Cloud storage bucket: `gs://earthengine-test/region1.csv` and `gs://earthengine-test/region2.csv`. To ingest them as an Earth Engine asset, create a manifest with two entries in the `sources` list, like this:
```
{
"name":"projects/some-project-id/assets/some-asset-id",
"sources":[
{
"uris":[
"gs://earthengine-test/region1.csv"
]
},
{
"uris":[
"gs://earthengine-test/region2.csv"
]
}
]
}
```

## Start and end time
All assets should specify start and end time to give more context to the data, especially if they are included into collections. These fields are not required, but we highly recommend using them whenever possible.
Start and end time usually mean the time of the observation, not the time when the source file was produced.
The end time is treated as an exclusive boundary for simplicity. For example, for assets spanning exactly one day, use the midnight of two consecutive days (for example, 1980-01-31T00:00:00 and 1980-02-01T00:00:00) for the start and end time. If the asset has no duration, set end time to be the same as start time. Represent times in manifests as [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) strings. We recommend assuming that end time is exclusive (for example, midnight of the next day for daily assets) to simplify the date values.
Example:
```
{
  "name": "projects/some-project-id/assets/some-asset-id",
  "sources": [
    {
      "uris": [
        "gs://bucket/table_20190612.csv"
      ]
    }
  ],
  "startTime": "1980-01-31T00:00:00Z",
  "endTime": "1980-02-01T00:00:00Z"
}
```

## Manifest structure reference
The following JSON structure includes all possible table upload manifest fields. Find field definitions in the following [ Manifest field definitions section.](https://developers.google.com/earth-engine/guides/table_manifest#manifest_field_definitions)
```
{
  "name": _<string>_,
  "sources": [
    {
      "uris": [
        _<string>_
      ],
      "charset": _<string>_,
      "maxErrorMeters": _<double>_,
      "maxVertices": _<int32>_,
      "crs": _<string>_,
      "geodesic": _<boolean>_,
      "primaryGeometryColumn": _<string>_,
      "xColumn": _<string>_,
      "yColumn": _<string>_,
      "dateFormat": _<string>_,
      "csvDelimiter": _<string>_,
      "csvQualifier": _<string>_,
    }
  ],
  "uriPrefix": _<string>_,
  "startTime": {
    "seconds": _<integer>_
  },
  "endTime": {
    "seconds": _<integer>_
  },
  "properties": {
    _<unspecified>_
  }
}
```

## Manifest field definitions
#### name
`string`
The name of the asset to be created. `name` is of the format "projects/*/assets/**" (for example, `projects/earthengine-legacy/assets/users/USER/ASSET`).
#### sources
`list`
A list of fields defining the properties of a table file and its sidecars. See the following `sources` dictionary element fields for more information.
#### sources[i].uris
`list`
A list of the URIs of the data to ingest. Currently, only Google Cloud Storage URIs are supported. Each URI must be specified in the following format: `gs://bucket-id/object-id`. The primary object should be the first element of the list, and sidecars listed afterwards. Each URI is prefixed with `TableManifest.uri_prefix` if set.
#### sources[i].charset
`string`
The name of the default charset to use for decoding strings. If empty, the charset "UTF-8" is assumed by default.
#### sources[i].maxErrorMeters
`double`
The max allowed error in meters when transforming geometry between coordinate systems. If empty, the max error is 1 meter by default.
#### sources[i].maxVertices
`int32`
The max number of vertices. If not zero, geometry will be subdivided into spatially disjoint pieces, each under this limit. 
#### sources[i].crs
`string`
The default CRS code or WKT string specifying the coordinate reference system of any geometry that does not have one specified. If left blank, the default will be [EPSG:4326](https://epsg.io/4326). For CSV/TFRecord sources only. 
#### sources[i].geodesic
`boolean`
The default strategy for interpreting edges in geometry that do not have one otherwise specified. If false, edges are straight in the projection. If true, edges are curved to follow the shortest path on the surface of the Earth. When blank, defaults to false if the CRS is a projected coordinate system. For CSV/TFRecord sources only. 
#### sources[i].primaryGeometryColumn
`string`
The geometry column to use as a row's primary geometry when there is more than one geometry column.
If left blank and more than one geometry column exists, the first geometry column encountered is used. For CSV/TFRecord sources only. 
#### sources[i].xColumn
`string`
The name of the numeric x coordinate column for deducing point geometry. If the `yColumn` is also specified, and both columns contain numeric values, then a point geometry column will be constructed with x,y values in the coordinate system given in the CRS. If left blank and the CRS does _not_ specify a projected coordinate system, defaults to "longitude". If left blank and the CRS _does_ specify a projected coordinate system, defaults to an empty string and no point geometry is generated.
A generated point geometry column will be named `{xColumn}_{yColumn}_N` where N is appended such that `{xColumn}_{yColumn}_N` is unique if a column named `{xColumn}_{yColumn}` already exists. For CSV/TFRecord sources only. 
#### sources[i].yColumn
`string`
The name of the numeric y coordinate column for deducing point geometry. If the `xColumn` is also specified, and both columns contain numeric values, then a point geometry column will be constructed with x,y values in the coordinate system given in the CRS. If left blank and the CRS does _not_ specify a projected coordinate system, defaults to "latitude". If left blank and the CRS _does_ specify a projected coordinate system, defaults to an empty string and no point geometry is generated.
A generated point geometry column will be named `{xColumn}_{yColumn}_N` where N is appended such that `{xColumn}_{yColumn}_N` is unique if a column named `{xColumn}_{yColumn}` already exists. For CSV/TFRecord sources only. 
#### sources[i].dateFormat
`string`
A format with which to parse fields encoding dates. The format pattern must be as described in the [Joda-Time DateTimeFormat class documentation](http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html). If left blank, dates will be imported as strings. For CSV/TFRecord sources only. 
#### sources[i].csvDelimiter
`string`
When ingesting CSV files, a single character used as a delimiter between column values in a row. If left blank, defaults to `','`. For CSV sources only. 
#### sources[i].csvQualifier
`string`
When ingesting CSV files, a character that surrounds column values (a.k.a. "quote character"). If left blank, defaults to `"`. For CSV sources only.
If a column value is not surrounded by qualifiers, leading and tailing whitespace is trimmed. For example: 
```
    ..., test,...            <== this value is not qualified
becomes the string value:
    "test"                   <== leading whitespace is stripped
```
while: ```
    ...," test",...          <== this value IS qualified with quotes
becomes the string value:
    " test"                  <== leading whitespace remains!
```

#### uriPrefix
`string`
An optional prefix prepended to all `uris` defined in the manifest.
#### startTime
`integer`
The timestamp associated with the asset, if any. This typically corresponds to the time at which data were collected. For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the start of that interval. Specified as as seconds and (optionally) nanoseconds since the epoch (1970-01-01). Assumed to be in the UTC time zone.
#### endTime
`integer`
For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the end of that interval (exclusive). Specified as as seconds and (optionally) nanoseconds since the epoch (1970-01-01). Assumed to be in the UTC time zone.
#### properties
`dictionary`
An arbitrary flat dictionary of key-value pairs. Keys must be strings and values can be either numbers or strings. List values are not yet supported for user-uploaded assets.
#### columnDataTypeOverrides
`dictionary`
If the automatic type detection is not working correctly, use this field with column names as keys and one of the following constants as values: COLUMN_DATA_TYPE_STRING, COLUMN_DATA_TYPE_NUMERIC, COLUMN_DATA_TYPE_LONG.
## Limitations
### JSON manifest size
The JSON manifest file size limit is 10 MB. If you have many files to upload, consider ways to reduce the number of characters needed to describe the dataset. For example, use the [`uriPrefix`](https://developers.google.com/earth-engine/guides/table_manifest#uriprefix) field to eliminate the need to provide the GCP bucket path for each URI in the [`uris`](https://developers.google.com/earth-engine/guides/table_manifest#sources\[i\].uris) list. If further size reduction is needed, try shortening the filenames.
