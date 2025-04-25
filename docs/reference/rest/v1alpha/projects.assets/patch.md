 
#  Method: projects.assets.patch 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/patch#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/patch#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/patch#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/patch#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets/patch#authorization-scopes)


Updates an asset. There are a number of constraints on the update operation:
  * Only the `title`, `description`, `startTime`, `endTime`, and `properties` fields of the asset can be updated.
  * Naming `"properties"` in `updateMask` results in all user-defined properties of the asset being replaced by the properties in `asset`.
  * Naming `"title"`, `"description"`, `"startTime"` or `"endTime"` in `updateMask` and not providing a value in `asset` results in that field becoming unset.
  * It is possible to update individual properties by naming them in `updateMask`, like `"properties.my_property_name"`. The property's value will be set to the corresponding value from `asset.properties`. If there is no corresponding value in `asset.properties`, or if there is a value but it is a `NullValue`, the property will be deleted from the asset.
  * Properties can be set only to string or number values, or deleted by specifying a `NullValue`.
  * Supplying an empty `updateMask` will result in the asset's timestamps and properties all being replaced by the values in `asset`.


### HTTP request
`PATCH https://earthengine.googleapis.com/v1alpha/{asset.name=projects/*/assets/**}`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`asset.name` |  `string` The name of the asset. `name` is of the format "projects/*/assets/**" (e.g. "projects/earthengine-legacy/assets/users//").  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
 "asset": {
  "cloudStorageLocation": {
   "uris": [
    string
   ]
  },
  "gcsLocation": {
   "uris": [
    string
   ]
  },
  "featureViewAssetLocation": {
   "assetOptions": {
    object (FeatureViewOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.FeatureViewOptions))
   }
  },
  "type": enum (Type[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.Type_1)),
  "name": string,
  "id": string,
  "updateTime": string,
  "title": string,
  "description": string,
  "properties": {
   "fields": {
    string: value,
    ...
   }
  },
  "startTime": string,
  "endTime": string,
  "geometry": {
   "fields": {
    string: value,
    ...
   }
  },
  "bands": [
   {
    "id": string,
    "dataType": {
     object (PixelDataType[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.PixelDataType))
    },
    "grid": {
     object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1alpha/PixelGrid))
    },
    "pyramidingPolicy": enum (PyramidingPolicy),
    "missingData": {
     object (MissingData[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.MissingData))
    }
   }
  ],
  "sizeBytes": string,
  "featureCount": string,
  "quota": {
   "sizeBytes": string,
   "maxSizeBytes": string,
   "assetCount": string,
   "maxAssets": string,
   "maxAssetCount": string
  },
  "tilesets": [
   {
    "id": string,
    "sources": [
     {
      object (ImageSource[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.ImageSource))
     }
    ],
    "dataType": enum (DataType[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.DataType)),
    "crs": string
   }
  ]
 },
 "updateMask": string
}
```
  
Fields  
---  
`asset.type` |  `enum (`Type[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.Type_1)`)` The type of the asset.  
`asset.id` |  `string` The ID of the asset. Equivalent to `name` without the "projects/*/assets/" prefix (e.g. "users//"). Note that this is intended for display purposes only. It should not be used as an input to another operation. Use `name` instead.  
`asset.updateTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last-modified time of the asset.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`asset.title**(deprecated)**`|  `string` The title of the asset.  
`asset.description**(deprecated)**`|  `string` The description of the asset.  
`asset.properties` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Key/value properties associated with the asset.  
`asset.startTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp associated with the asset, if any, e.g. the time at which a satellite image was taken. For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the start of that interval.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`asset.endTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the end of that interval (exclusive).Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`asset.geometry` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The spatial footprint associated with the asset, if any, as a GeoJSON geometry object (see RFC 7946).  
`asset.bands[]` |  `object (`ImageBand[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.ImageBand)`)` Information about the data bands of the image asset. Omitted for non-image assets.  
`asset.sizeBytes` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The size of a leaf asset (e.g. an image) in bytes.  
`asset.featureCount` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The number of features in the asset, if applicable.  
`asset.quota` |  `object (`FolderQuota[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.FolderQuota)`)` The quota information associated with the folder asset, if any. Returned for top-level user-owned folder assets (e.g. "users/*" or "projects/*").  
`asset.tilesets[]` |  `object (`Tileset[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.Tileset)`)` The tilesets backing this image. Only present for external images, whose pixels are retrieved from storage not owned by Earth Engine.  
`updateMask` |  `string (`FieldMask[](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The update mask specifying which fields of the asset to update.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
Union field `location`. Information about where and how the raster tiles are stored. `location` can be only one of the following:  
`asset.cloudStorageLocation**(deprecated)**`|  `object (`CloudStorageLocation[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.CloudStorageLocation)`)` Deprecated. Use `image.importExternal` instead. See <https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff> for more details.  
`asset.gcsLocation**(deprecated)**`|  `object (`GcsLocation[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.GcsLocation)`)` Deprecated. Use `image.importExternal` instead. See <https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff> for more details.  
`asset.featureViewAssetLocation` |  `object (`FeatureViewLocation[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset.FeatureViewLocation)`)` The location of this FeatureView in EE.  
### Response body
If successful, the response body contains an instance of `EarthEngineAsset[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.assets#EarthEngineAsset)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
Was this helpful?
