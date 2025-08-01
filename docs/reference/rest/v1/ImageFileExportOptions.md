 
#  ImageFileExportOptions
Stay organized with collections  Save and categorize content based on your preferences. 
Options for exporting images as files outside Earth Engine.
JSON representation  
---  
```
{
  "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileFormat)),

  // Union field destination can be only one of the following:
  "driveDestination": {
    object (DriveDestination[](https://developers.google.com/earth-engine/reference/rest/v1/DriveDestination))
  },
  "cloudStorageDestination": {
    object (CloudStorageDestination[](https://developers.google.com/earth-engine/reference/rest/v1/CloudStorageDestination))
  }
  // End of list of possible types for union field destination.

  // Union field format_options can be only one of the following:
  "geoTiffOptions": {
    object (GeoTiffImageExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions#GeoTiffImageExportOptions))
  },
  "tfRecordOptions": {
    object (TfRecordImageExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions#TfRecordImageExportOptions))
  }
  // End of list of possible types for union field format_options.
}
```
  
Fields  
---  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileFormat)`)` The file format in which to export the image(s).  
Union field `destination`. Where to write the results. `destination` can be only one of the following:  
`driveDestination` |  `object (`DriveDestination[](https://developers.google.com/earth-engine/reference/rest/v1/DriveDestination)`)` If specified, configures export to Google Drive.  
`cloudStorageDestination` |  `object (`CloudStorageDestination[](https://developers.google.com/earth-engine/reference/rest/v1/CloudStorageDestination)`)` If specified, configures export to Google Cloud Storage.  
Union field `format_options`. File-format-specific options. `format_options` can be only one of the following:  
`geoTiffOptions` |  `object (`GeoTiffImageExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions#GeoTiffImageExportOptions)`)` File-format-specific options for `GEO_TIFF` exports.  
`tfRecordOptions` |  `object (`TfRecordImageExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions#TfRecordImageExportOptions)`)` File-format-specific options for `TF_RECORD_IMAGE` exports.  
## GeoTiffImageExportOptions
Options for encoding images as GeoTIFF files.
JSON representation  
---  
```
{
  "cloudOptimized": boolean,
  "tileDimensions": {
    object (GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions))
  },
  "skipEmptyFiles": boolean,
  "tileSize": integer,
  "noData": {
    object (Number[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions#Number))
  }
}
```
  
Fields  
---  
`cloudOptimized` |  `boolean` If true, generates 'cloud optimized' GeoTIFF files for more efficient access in cloud environments (see www.cogeo.org).  
`tileDimensions` |  `object (`GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions)`)` Optional explicit dimensions in pixels into which to split the image if it is too large to fit in a single file. This must be set to a multiple of the tile size, by default is 256.  
`skipEmptyFiles` |  `boolean` If true, skip writing empty (i.e. fully-masked) image files.  
`tileSize` |  `integer` Optional. Optional parameter setting the output tile size. This parameter is the side dimension in pixels of intermediate output tiles. The default tile size is 256, which corresponds to a 256x256 tile.  
`noData` |  `object (`Number[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileExportOptions#Number)`)` Optional. Optional no data value. Only `noData.float_value` is currently supported.  
## Number
A number.
JSON representation  
---  
```
{

  // Union field value can be only one of the following:
  "floatValue": number,
  "integerValue": string
  // End of list of possible types for union field value.
}
```
  
Fields  
---  
Union field `value`. The value. `value` can be only one of the following:  
`floatValue` |  `number` A double-precision floating point value.  
`integerValue` |  `string (int64[](https://developers.google.com/discovery/v1/type-format) format)` An 64-bit integer value.  
## TfRecordImageExportOptions
Options for encoding images as TFRecord files.
JSON representation  
---  
```
{
  "tileDimensions": {
    object (GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions))
  },
  "marginDimensions": {
    object (GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions))
  },
  "compress": boolean,
  "maxSizeBytes": string,
  "defaultValue": number,
  "tensorDepths": {
    string: integer,
    ...
  },
  "sequenceData": boolean,
  "collapseBands": boolean,
  "maxMaskedRatio": number
}
```
  
Fields  
---  
`tileDimensions` |  `object (`GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions)`)` Dimensions tiled over the export area, covering every pixel in the bounding box exactly once (except when the patch dimensions do not evenly divide the bounding box in which case border tiles along the greatest x/y edges will be dropped). Dimensions must be > 0.  
`marginDimensions` |  `object (`GridDimensions[](https://developers.google.com/earth-engine/reference/rest/v1/GridDimensions)`)` If specified, tiles will be buffered by the margin dimensions both positively and negatively, resulting in overlap between neighboring patches.  
`compress` |  `boolean` If true, compresses the .tfrecord files with gzip and appends the ".gz" suffix.  
`maxSizeBytes` |  `string (Int64Value[](https://developers.google.com/discovery/v1/type-format) format)` Maximum size, in bytes, for an exported .tfrecord (before compression). A smaller file size will result in greater sharding (and, thus, more output files). Defaults to 1GiB.  
`defaultValue` |  `number` The value set in each band of a pixel that is partially or completely masked, and, the value set at each value in an output 3D feature made from an array band where the array length at the source pixel was less than the depth of the feature value. The fractional part is dropped for integer type bands, and clamped to the range of the band type. Defaults to 0.  
`tensorDepths` |  `map (key: string, value: integer)` Mapping from the names of input array bands to the depth of the 3D tensors they create. Arrays will be truncated, or padded with default values to fit the shape specified. For each array band, this must have a corresponding entry. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`sequenceData` |  `boolean` If true, each pixel is output as a SequenceExample mapping scalar bands to the context and array bands to the example’s sequences. The SequenceExamples are output in row-major order of pixels in each patch, and then by row-major order of area patches in the file sequence.  
`collapseBands` |  `boolean` If true, all bands will be combined into a single 3D tensor, taking on the name of the first band in the image. All bands are promoted to bytes, int64s, then floats in that order depending on the type furthest in that sequence within all bands. Array bands are allowed as long as tensorDepths is specified.  
`maxMaskedRatio` |  `number` Maximum allowed proportion of masked pixels in a patch. Patches which exceed this allowance will be dropped rather than written to files. If this field is set to anything but 1, the JSON sidecar will not be produced. Defaults to 1.  
