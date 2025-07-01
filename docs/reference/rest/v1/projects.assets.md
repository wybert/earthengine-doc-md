 
#  REST Resource: projects.assets
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Resource: EarthEngineAsset](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#resource:-earthengineasset)
    * [CloudStorageLocation](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#cloudstoragelocation)
    * [FeatureViewLocation](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#featureviewlocation)
    * [FeatureViewOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#featureviewoptions)
    * [FeatureViewAttribute](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#featureviewattribute)
    * [Type](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#type)
    * [FeatureViewIngestionTimeParameters](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#featureviewingestiontimeparameters)
    * [ThinningOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#thinningoptions)
    * [ThinningStrategy](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#thinningstrategy)
    * [RankingOptions](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#rankingoptions)
    * [RankingRule](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#rankingrule)
    * [RankByOneThingRule](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#rankbyonethingrule)
    * [RankByAttributeRule](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#rankbyattributerule)
    * [RankByMinVisibleLodRule](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#rankbyminvisiblelodrule)
    * [RankByGeometryTypeRule](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#rankbygeometrytyperule)
    * [RankByMinZoomLevelRule](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#rankbyminzoomlevelrule)
    * [Direction](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#direction)
    * [Type](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#type_1)
    * [ImageBand](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#imageband)
    * [PixelDataType](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#pixeldatatype)
    * [Precision](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#precision)
    * [MissingData](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#missingdata)
    * [FolderQuota](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#folderquota)
    * [Tileset](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#tileset)
    * [ImageSource](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#imagesource)
    * [DataType](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#datatype)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#methods)
    * [copy](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#copy)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#create)
    * [delete](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#delete)
    * [get](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#get)
    * [getIamPolicy](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#getiampolicy)
    * [getPixels](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#getpixels)
    * [listAssets](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#listassets)
    * [listFeatures](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#listfeatures)
    * [move](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#move)
    * [patch](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#patch)
    * [setIamPolicy](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#setiampolicy)
    * [testIamPermissions](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#testiampermissions)


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
### CloudStorageLocation
The location of an asset on Cloud Storage.
JSON representation  
---  
```
{
 "uris": [
  string
 ]
}
```
  
Fields  
---  
`uris[]` |  `string` The URIs of the data. Only Google Cloud Storage URIs are supported. Each URI must be specified in the following format: "gs://bucket-id/object-id". Only one URI is currently supported. If more than one URI is specified an `INALID_ARGUMENT` error is returned.  
### FeatureViewLocation
A FeatureView EE asset.
JSON representation  
---  
```
{
 "assetOptions": {
  object (FeatureViewOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewOptions))
 }
}
```
  
Fields  
---  
`assetOptions` |  `object (`FeatureViewOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewOptions)`)` Ingest-time options for FeatureView assets.  
### FeatureViewOptions
Ingest-time options for FeatureView assets.
JSON representation  
---  
```
{
 "featureViewAttributes": [
  {
   object (FeatureViewAttribute[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewAttribute))
  }
 ],
 "ingestionTimeParameters": {
  object (FeatureViewIngestionTimeParameters[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewIngestionTimeParameters))
 }
}
```
  
Fields  
---  
`featureViewAttributes[]` |  `object (`FeatureViewAttribute[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewAttribute)`)` Attributes in the FeatureView asset, comprising a schema for the asset. These are the attributes that features in this asset can have. Each attribute has a name and a type.  
`ingestionTimeParameters` |  `object (`FeatureViewIngestionTimeParameters[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.FeatureViewIngestionTimeParameters)`)` FeatureView ingestion time parameters.  
### FeatureViewAttribute
A FeatureView attribute and its type.
JSON representation  
---  
```
{
 "name": string,
 "type": enum (Type[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Type))
}
```
  
Fields  
---  
`name` |  `string` Name of the attribute.  
`type` |  `enum (`Type[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Type)`)` Type of the attribute.  
### Type
These types are a mirror of those found in geo/enterprise/layers/public/data_source_schema.proto.
Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`INTEGER` | A 64 bit integer value.  
`BOOLEAN` | True/False Boolean value.  
`DOUBLE` | A double precision floating point number.  
`STRING` | A string of unbounded length.  
`DATE_TIME` | A date/time, represented as a signed 64-bit integer in microseconds since the epoch, and therefore supporting the time period from 290,308 BCE through 294,247 CE.  
### FeatureViewIngestionTimeParameters
FeatureView ingestion time parameters. These parameters must be specified at ingestion time and cannot be updated on the fly for a FeatureView.
JSON representation  
---  
```
{
 "thinningOptions": {
  object (ThinningOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ThinningOptions))
 },
 "rankingOptions": {
  object (RankingOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankingOptions))
 }
}
```
  
Fields  
---  
`thinningOptions` |  `object (`ThinningOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ThinningOptions)`)` The maximum number of feature bounding boxes that are allowed to intersect a tile. This number must be nonnegative.  
`rankingOptions` |  `object (`RankingOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankingOptions)`)` Options for assigning z-order ranks and thinning ranks to features.  
### ThinningOptions
Thinning options that control the density at which features are displayed per tile.
JSON representation  
---  
```
{
 "maxFeaturesPerTile": integer,
 "thinningStrategy": enum (ThinningStrategy[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ThinningStrategy))
}
```
  
Fields  
---  
`maxFeaturesPerTile` |  `integer` The maximum number of feature bounding boxes that are allowed to intersect a tile. This number must be nonnegative.  
`thinningStrategy` |  `enum (`ThinningStrategy[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ThinningStrategy)`)` The feature thinning strategy that should be used.  
### ThinningStrategy
Thinning strategy for features.
Enums  
---  
`UNKNOWN_THINNING_STRATEGY` | Unknown thinning strategy.  
`GLOBALLY_CONSISTENT` | When thinning at a particular LOD, globally-consistent thinning means that if a feature is removed by thinning, then all other features with equal or worse thinning rank will also be removed.  
`HIGHER_DENSITY` | When thinning, try to come as close as possible to the maxFeaturesPerTile limit for each tile. We will prefer better-ranked features over worse-ranked features, but will sometimes discard better- ranked features if that helps us achieve higher feature density.We guarantee that the strategy is deterministic, and that the set of post-thinned features will be a superset of those generated by globally- consistent thinning.  
### RankingOptions
Ranking options for z-order and thinning.
JSON representation  
---  
```
{
 "zOrderRankingRule": {
  object (RankingRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankingRule))
 },
 "thinningRankingRule": {
  object (RankingRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankingRule))
 }
}
```
  
Fields  
---  
`zOrderRankingRule` |  `object (`RankingRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankingRule)`)` Ranking rule for assigning z-order ranks to features.  
`thinningRankingRule` |  `object (`RankingRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankingRule)`)` Ranking rule for assigning thinning ranks to features.  
### RankingRule
Ranking rules that control how features are ranked for thinning and z-order.
JSON representation  
---  
```
{
 "rankByOneThingRule": [
  {
   object (RankByOneThingRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByOneThingRule))
  }
 ]
}
```
  
Fields  
---  
`rankByOneThingRule[]` |  `object (`RankByOneThingRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByOneThingRule)`)` An ordered list of zero or more rank-by-one-thing (such as an attr) rules, which are used as primary, secondary, ... ranking keys for setting thinning_rank in each RankedFeature.  
### RankByOneThingRule
An individual ranking rule to control rank for thinning and z-order.
JSON representation  
---  
```
{
 // Union field rule can be only one of the following:
 "rankByAttributeRule": {
  object (RankByAttributeRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByAttributeRule))
 },
 "rankByMinVisibleLodRule": {
  object (RankByMinVisibleLodRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByMinVisibleLodRule))
 },
 "rankByGeometryTypeRule": {
  object (RankByGeometryTypeRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByGeometryTypeRule))
 },
 "rankByMinZoomLevelRule": {
  object (RankByMinZoomLevelRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByMinZoomLevelRule))
 }
 // End of list of possible types for union field rule.
 "direction": enum (Direction[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Direction))
}
```
  
Fields  
---  
Union field `rule`. The type of ranking rule to use. `rule` can be only one of the following:  
`rankByAttributeRule` |  `object (`RankByAttributeRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByAttributeRule)`)` Rank by feature attribute value.  
`rankByMinVisibleLodRule**(deprecated)**`|  `object (`RankByMinVisibleLodRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByMinVisibleLodRule)`)` This item is deprecated! Rank by the min lod at which the feature geometry is first visible. A feature with any points is always visible at all LODs. Deprecated: please use rankByMinZoomLevelRule instead.  
`rankByGeometryTypeRule` |  `object (`RankByGeometryTypeRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByGeometryTypeRule)`)` Rank by geometry type. Precedence of types, high to low: polygon, polyline, point, none. In features with multiple types, the highest takes priority.  
`rankByMinZoomLevelRule` |  `object (`RankByMinZoomLevelRule[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.RankByMinZoomLevelRule)`)` Rank by the min zoom level at which the feature geometry is first visible. A feature with any points is always visible at all LODs.  
`direction` |  `enum (`Direction[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Direction)`)` Whether the rank by this one thing should be ASCENDING (lower values first, i.e. more important) or DESCENDING (high values first, i.e. more important). In other words, ASCENDING means use directly the ordering described in the RankByAttributeRule (or other) submessage documentation below, and DESCENDING means reverse that ordering.  
### RankByAttributeRule
Rank by feature attribute value.
JSON representation  
---  
```
{
 "attributeName": string
}
```
  
Fields  
---  
`attributeName` |  `string` Rank by the value of the attribute with the given name. This is mostly the natural ordering of the values of the given type, with some subtleties and clarifications: - for integer attrs, lower values come before higher values - for double attrs, lower values come before higher values with NaN considered to be lower than all other values including minus infinity - for boolean attrs, false is considered to come before true - for date_time attrs, earlier values come before later ones - string attrs are ranked lexicographically - an attr whose value has not been set is considered to have the default value of the given type (0 for integer, false for boolean, etc.).  
### RankByMinVisibleLodRule
This type has no fields.
Rank by the min lod at which the feature geometry is first visible. A feature with any points is always visible at all LODs.
### RankByGeometryTypeRule
This type has no fields.
Rank by geometry type. Precedence of types, high to low: polygon, polyline, point, none. In features with multiple types, the highest takes priority.
### RankByMinZoomLevelRule
This type has no fields.
Rank by the min zoom level at which the feature geometry is first visible. A feature with any points is always visible at all LODs.
### Direction
Whether to order a list from low to high (ASCENDING) or from high to low (DESCENDING).
Enums  
---  
`DIRECTION_UNSPECIFIED` | No ranking direction specified.  
`ASCENDING` | Ascending order.  
`DESCENDING` | Descending order.  
### Type
Types of asset.
Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified.  
`IMAGE` | Image.  
`IMAGE_COLLECTION` | Image collection.  
`TABLE` | Table.  
`FOLDER` | Folder.  
`CLASSIFIER` | Classifier.  
`FEATURE_VIEW` | FeatureView asset.  
### ImageBand
Information about a single data band of an image asset.
JSON representation  
---  
```
{
 "id": string,
 "dataType": {
  object (PixelDataType[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.PixelDataType))
 },
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid))
 },
 "pyramidingPolicy": enum (PyramidingPolicy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/PyramidingPolicy)),
 "missingData": {
  object (MissingData[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.MissingData))
 }
}
```
  
Fields  
---  
`id` |  `string` The ID of the band.  
`dataType` |  `object (`PixelDataType[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.PixelDataType)`)` The numeric type of the band.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid)`)` The pixel grid of the band.  
`pyramidingPolicy` |  `enum (`PyramidingPolicy[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/PyramidingPolicy)`)` The pyramiding policy of the band.  
`missingData` |  `object (`MissingData[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.MissingData)`)` The value(s) denoting missing data.  
### PixelDataType
Specifies the numeric type of the pixels in an image band.
JSON representation  
---  
```
{
 "precision": enum (Precision[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Precision)),
 "range": {
  object (DoubleRange[](https://developers.google.com/earth-engine/reference/rest/v1/DoubleRange))
 },
 "dimensionsCount": integer
}
```
  
Fields  
---  
`precision` |  `enum (`Precision[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.Precision)`)` The numeric precision of the type.  
`range` |  `object (`DoubleRange[](https://developers.google.com/earth-engine/reference/rest/v1/DoubleRange)`)` The range of the numeric type, if any. Typically absent for floating-point types.  
`dimensionsCount` |  `integer` The number of dimensions in an array-valued data type, or zero to indicate an ordinary scalar type.  
### Precision
Specifies the precision of a numeric data type.
Enums  
---  
`PRECISION_UNSPECIFIED` | Unspecified.  
`INT` | The data type has integer precision. Note that this could represent differently sized integers.  
`FLOAT` | The data type has 32-bit floating point precision.  
`DOUBLE` | The data type has 64-bit floating point (double) precision.  
### MissingData
A list of values which represent no data.
JSON representation  
---  
```
{
 "values": [
  number
 ]
}
```
  
Fields  
---  
`values[]` |  `number` Values which represent no data.  
### FolderQuota
Describes the current usage and limits of a top-level folder.
JSON representation  
---  
```
{
 "sizeBytes": string,
 "maxSizeBytes": string,
 "assetCount": string,
 "maxAssets": string
}
```
  
Fields  
---  
`sizeBytes` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The size of the folder in bytes.  
`maxSizeBytes` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The maximum size of the folder in bytes.  
`assetCount` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The number of assets stored in the folder.  
`maxAssets` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of assets that can be stored in the folder.  
### Tileset
A set of ImageSources that can be referenced with a unique ID.
JSON representation  
---  
```
{
 "id": string,
 "sources": [
  {
   object (ImageSource[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ImageSource))
  }
 ],
 "dataType": enum (DataType[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.DataType)),
 "crs": string
}
```
  
Fields  
---  
`id` |  `string` The ID of the tileset. Must be unique among tilesets specified in the ImageManifest. This ID is discarded during the processing step; it is only used to link a Tileset to a band. The empty string is a valid ID.  
`sources[]` |  `object (`ImageSource[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.ImageSource)`)` The sources which comprise this tileset.  
`dataType` |  `enum (`DataType[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets#EarthEngineAsset.DataType)`)` An optional data type for the band. If specified, no check is done to verify that the type of every input file matches. `dataType` must match the type of every input file, except for cases where the input type is ambiguous (e.g. `Byte` can be `INT8` or `UINT8`).  
`crs` |  `string` The coordinate reference system of the pixel grid, specified as a standard code where possible, and in WKT format otherwise.  
### ImageSource
An image file and its sidecars.
JSON representation  
---  
```
{
 "uris": [
  string
 ],
 "affineTransform": {
  object (AffineTransform[](https://developers.google.com/earth-engine/reference/rest/v1/AffineTransform))
 },
 "dimensions": {
  object (GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions))
 }
}
```
  
Fields  
---  
`uris[]` |  `string` The URIs of the data to import. Currently, only Google Cloud Storage URIs are supported. Each URI must be specified in the following format: "gs://bucket-id/object-id". The primary object should be the first element of the list, and sidecars listed afterwards. Each URI is prefixed with `ImageManifest.uri_prefix` if set.  
`affineTransform` |  `object (`AffineTransform[](https://developers.google.com/earth-engine/reference/rest/v1/AffineTransform)`)` An optional affine transform. Should only be specified if the data from `uris` (including any sidecars) isn't sufficient to place the pixels.  
`dimensions` |  `object (`GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions)`)` Raster dimensions in pixels. Used only when 'skipMetadataRead' is set.  
### DataType
Specifies the numeric data type.
Enums  
---  
`DATA_TYPE_UNSPECIFIED` | Unspecified.  
`INT8` | 8-bit signed integer.  
`UINT8` | 8-bit unsigned integer.  
`INT16` | 16-bit signed integer.  
`UINT16` | 16-bit unsigned integer.  
`INT32` | 32-bit signed integer.  
`UINT32` | 32-bit unsigned integer.  
`FLOAT` | 32-bit float.  
`DOUBLE` | 64-bit float.  
## Methods  
---  
### `copy[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/copy)`
|  Copies an asset.  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/create)`
|  Creates an asset.  
### `delete[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/delete)`
|  Deletes an asset.  
### `get[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/get)`
|  Gets detailed information about an asset.  
### `getIamPolicy[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/getIamPolicy)`
|  Gets the access control policy for a resource.  
### `getPixels[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/getPixels)`
|  Fetches pixels from an image asset.  
### `listAssets[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/listAssets)`
|  Lists any container asset, such as a folder or collection.  
### `listFeatures[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/listFeatures)`
|  Lists the features in a table asset.  
### `move[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/move)`
|  Moves an asset.  
### `patch[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/patch)`
|  Updates an asset.  
### `setIamPolicy[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/setIamPolicy)`
|  Sets the access control policy on the specified resource.  
### `testIamPermissions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.assets/testIamPermissions)`
|  Returns permissions that a caller has on the specified resource.  
