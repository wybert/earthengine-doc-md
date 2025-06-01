 
#  REST Resource: projects.locations.assets 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Resource: EarthEngineAsset](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.assets#resource:-earthengineasset)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.assets#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.assets#create)


## Resource: EarthEngineAsset
Information about an Earth Engine asset.
JSON representation  
---  
```
{
 "type": enum (Type[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Type_1)),
 "name": string,
 "id": string,
 "updateTime": string,
 "properties": {
  object
 },
 "startTime": string,
 "endTime": string,
 "geometry": {
  object
 },
 "bands": [
  {
   object (ImageBand[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ImageBand))
  }
 ],
 "sizeBytes": string,
 "featureCount": string,
 "quota": {
  object (FolderQuota[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FolderQuota))
 },
 "tilesets": [
  {
   object (Tileset[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Tileset))
  }
 ],
 // Union field location can be only one of the following:
 "cloudStorageLocation": {
  object (CloudStorageLocation[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.CloudStorageLocation))
 },
 "featureViewAssetLocation": {
  object (FeatureViewLocation[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewLocation))
 }
 // End of list of possible types for union field location.
}
```
  
Fields  
---  
`type` |  `enum (`Type[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Type_1)`)` The type of the asset.  
`name` |  `string` The name of the asset. `name` is of the format "projects/*/assets/**" (e.g. "projects/earthengine-legacy/assets/users//").  
`id` |  `string` The ID of the asset. Equivalent to `name` without the "projects/*/assets/" prefix (e.g. "users//"). Note that this is intended for display purposes only. It should not be used as an input to another operation. Use `name` instead.  
`updateTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last-modified time of the asset.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`properties` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Key/value properties associated with the asset.  
`startTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp associated with the asset, if any, e.g. the time at which a satellite image was taken. For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the start of that interval.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the end of that interval (exclusive).Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`geometry` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The spatial footprint associated with the asset, if any, as a GeoJSON geometry object (see RFC 7946).  
`bands[]` |  `object (`ImageBand[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ImageBand)`)` Information about the data bands of the image asset. Omitted for non-image assets.  
`sizeBytes` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The size of a leaf asset (e.g. an image) in bytes.  
`featureCount` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The number of features in the asset, if applicable.  
`quota` |  `object (`FolderQuota[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FolderQuota)`)` The quota information associated with the folder asset, if any. Returned for top-level user-owned folder assets (e.g. "users/*" or "projects/*").  
`tilesets[]` |  `object (`Tileset[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Tileset)`)` The tilesets backing this image. Only present for external images, whose pixels are retrieved from storage not owned by Earth Engine.  
Union field `location`. Information about where and how the raster tiles are stored. `location` can be only one of the following:  
`cloudStorageLocation**(deprecated)**`|  `object (`CloudStorageLocation[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.CloudStorageLocation)`)` This item is deprecated! Deprecated. Use `image.importExternal` instead. See <https://developers.google.com/earth-engine/Earth_Engine_asset_from_cloud_geotiff> for more details.  
`featureViewAssetLocation` |  `object (`FeatureViewLocation[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewLocation)`)` The location of this FeatureView in EE.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.assets/create)`
|  Creates an asset.  
