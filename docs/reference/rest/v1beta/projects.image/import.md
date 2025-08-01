 
#  Method: projects.image.import
Stay organized with collections  Save and categorize content based on your preferences. 
Imports an image.
### HTTP request
`POST https://earthengine.googleapis.com/v1beta/{project=projects/*}/image:import`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.imports.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
  "imageManifest": {
    object (ImageManifest[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#ImageManifest))
  },
  "description": string,
  "overwrite": boolean,
  "requestId": string
}
```
  
Fields  
---  
`imageManifest` |  `object (`ImageManifest[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#ImageManifest)`)` The image manifest.  
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
## ImageManifest
Describes how the EarthEngine service should compose an image from a set of files.
JSON representation  
---  
```
{
  "name": string,
  "properties": {
    object
  },
  "uriPrefix": string,
  "tilesets": [
    {
      object (Tileset[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets#EarthEngineAsset.Tileset))
    }
  ],
  "bands": [
    {
      object (TilesetBand[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#TilesetBand))
    }
  ],
  "maskBands": [
    {
      object (TilesetMaskBand[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#TilesetMaskBand))
    }
  ],
  "footprint": {
    object (PixelFootprint[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#PixelFootprint))
  },
  "missingData": {
    object (MissingData[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets#EarthEngineAsset.MissingData))
  },
  "pyramidingPolicy": enum (PyramidingPolicy),
  "startTime": string,
  "endTime": string,
  "skipMetadataRead": boolean,
  "memo": string
}
```
  
Fields  
---  
`name` |  `string` The name of the asset to be created. `name` is of the format "projects/*/assets/**" (e.g. "projects/earthengine-legacy/assets/users//"). All user-owned assets are under the project "earthengine-legacy" (e.g. "projects/earthengine-legacy/assets/users/foo/bar"). All other assets are under the project "earthengine-public" (e.g. "projects/earthengine-public/assets/LANDSAT").  
`properties` |  `object (`Struct[](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Additional properties of the asset. The property names "system:time_start" and "system:time_end" are deprecated. Use the fields `startTime` and `endTime` instead.  
`uriPrefix` |  `string` The optional prefix prepended to all `uri`s defined in this manifest.  
`tilesets[]` |  `object (`Tileset[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets#EarthEngineAsset.Tileset)`)` The tilesets. Each tileset must have a unique ID.  
`bands[]` |  `object (`TilesetBand[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#TilesetBand)`)` The bands. The band order of the asset is the same as the order of `bands`.  
`maskBands[]` |  `object (`TilesetMaskBand[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#TilesetMaskBand)`)` The mask bands.  
`footprint` |  `object (`PixelFootprint[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#PixelFootprint)`)` The footprint in pixel coordinates (not in lat/lng coordinates). If empty, the footprint is by default the entire image. See `PixelGrid` for a more detailed description of pixel coordinates.  
`missingData` |  `object (`MissingData[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets#EarthEngineAsset.MissingData)`)` The values which represent no data in all bands of the image. Applies to all bands which do not specify their own `missingData`.  
`pyramidingPolicy` |  `enum (`PyramidingPolicy`)` The pyramiding policy. If unspecified, the policy MEAN is applied by default. Applies to all bands which do not specify their own `pyramidingPolicy`.  
`startTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp associated with the asset, if any, e.g. the time at which a satellite image was taken. For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the start of that interval. Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`Timestamp[](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the end of that interval (exclusive). Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`skipMetadataRead` |  `boolean` Whether to skip reading metadata from files using GDAL. When this field is true, tilesets should contain complete GDAL metadata: data type, crs, transform, file dimensions, and no data value.  
`memo` |  `string` Freeform field to store user notes. Not used in ingestion.  
## TilesetBand
Represents a single band sourced from a tileset.
JSON representation  
---  
```
{
  "id": string,
  "tilesetId": string,
  "tilesetBandIndex": integer,
  "missingData": {
    object (MissingData[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets#EarthEngineAsset.MissingData))
  },
  "pyramidingPolicy": enum (PyramidingPolicy)
}
```
  
Fields  
---  
`id` |  `string` The ID of the band.  
`tilesetId` |  `string` The ID of the tileset corresponding to the band.  
`tilesetBandIndex` |  `integer` The zero-based band index from the tileset corresponding to the band. E.g. if 1, then the pixels of the band are are the pixels of the band at index 1 of the tileset (in `ImageManifest.tilesets`) with ID `tilesetId`.  
`missingData` |  `object (`MissingData[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.assets#EarthEngineAsset.MissingData)`)` The values which represent no data in the band. If `MissingData` is set with no `values`, then any nodata value present for the files corresponding to this `TilesetBand` will be ignored.  
`pyramidingPolicy` |  `enum (`PyramidingPolicy`)` The pyramiding policy.  
## TilesetMaskBand
Represents a single mask band sourced from a tileset.
JSON representation  
---  
```
{
  "tilesetId": string,
  "bandIds": [
    string
  ]
}
```
  
Fields  
---  
`tilesetId` |  `string` The ID of the Tileset corresponding to the mask band. The last band of the Tileset is always used as the mask band.  
`bandIds[]` |  `string` The IDs of bands that the mask band applies to. If empty, the mask band is applied to all bands in the asset. Each band may only have one corresponding mask band. If any of these bands have an internal mask, the internal mask is ignored in favor of this mask band.  
## PixelFootprint
A footprint of all valid pixels in an image.
JSON representation  
---  
```
{
  "points": [
    {
      object (GridPoint[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#GridPoint))
    }
  ],
  "bandId": string
}
```
  
Fields  
---  
`points[]` |  `object (`GridPoint[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.image/import#GridPoint)`)` A ring which forms the exterior of a simple polygon that must contain the centers of all valid pixels of the image. This must be a linear ring: the last point must be equal to the first. Coordinates are in the projection of the band specified by `bandId`. Note: Use non-integer coordinates such as the center of each pixel because footprint is taken to include a pixel iff the pixel (a 1x1 rectangle) intersects the footprint. To avoid accidentally selecting neighboring pixels, don't use integer-valued coordinates, because those are the boundaries between pixels. Drawing the footprint along the pixel centers prevents including unintended pixels, which can cause errors when intended pixels are abutting a map boundary such as the antimeridian or a pole. For example, for a 2x2 image with all 4 valid pixels the following is one possible ring: [{"x": 0.5, "y": 0.5}, {"x": 0.5, "y": 1.5}, {"x": 1.5, "y": 1.5}, {"x": 1.5, "y": 0.5}, {"x": 0.5, "y": 0.5}]  
`bandId` |  `string` The ID of the band whose CRS defines the coordinates of the footprint. If empty, the first band is used.  
## GridPoint
A two-dimensional point or vector.
JSON representation  
---  
```
{
  "x": number,
  "y": number
}
```
  
Fields  
---  
`x` |  `number` The x coordinate value.  
`y` |  `number` The y coordinate value.  
