 
#  Image Manifest Upload
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
If you need more flexibility uploading images into Google Earth Engine (EE) than the [Code Editor UI](https://developers.google.com/earth-engine/image_upload) or the `upload` command of the ['earthengine' command-line tool](https://developers.google.com/earth-engine/command_line#upload) provide, you can do so by describing an image upload using a JSON file known as a "manifest" and using the `upload image --manifest` command of the command-line tool.
See a complete example in [this Colab notebook](https://github.com/google/earthengine-community/blob/master/guides/linked/Uploading_image_tiles_as_a_single_asset_using_a_manifest.ipynb) which demonstrates uploading image tiles as a single asset using a manifest. 
## One-time setup
  1. Manifest uploads only work with files located in [Google Cloud Storage](https://cloud.google.com/storage/getting-started/). To start using Google Cloud Storage, [create a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects), if you don't already have one. Note that setup requires specifying a credit card for billing. EE itself isn't charging anyone at this point, but transferring files to Google Cloud Storage before uploading them to EE will have [a small cost](https://cloud.google.com/storage/pricing). For typical upload data sizes (tens or hundreds of gigabytes), the cost will be quite low.
  2. Within your project, [turn on the Cloud Storage API](https://cloud.google.com/apis/docs/enable-disable-apis) and [create a bucket](https://cloud.google.com/storage/docs/creating-buckets).
  3. [Install the Earth Engine Python client](https://developers.google.com/earth-engine/python_install). It includes the `earthengine` command-line tool, which we will use for uploading data.
  4. For automated uploads, you may want to use a [Google Cloud service account](https://cloud.google.com/iam/docs/understanding-service-accounts) associated with your project. You don't need a service account for testing, but when you have a moment, please start familiarizing yourself with using them.


Very large source files (100 GB or more) might be uploaded faster if they are broken down into multiple tiles.
## Asset IDs and names
For Cloud project-owned assets, use this convention for asset names: `projects/some-project-id/assets/some-asset-id`.
Learn about asset names for legacy project and user-owned assets
For older legacy projects, the asset name in the manifest needs to be slightly different from the asset ID visible elsewhere in Earth Engine. To upload assets whose asset IDs start with `users/some_user` or `projects/some_project`, the asset name in the manifest must have the string `projects/earthengine-legacy/assets/` prepended to the ID. For example, EE asset ID `users/username/my_geotiff` should be uploaded using the name `projects/earthengine-legacy/assets/users/username/my_geotiff`.
Yes, this means that IDs like `projects/some_projects/some_asset` get converted into names where `projects` is mentioned twice: `projects/earthengine-legacy/assets/projects/some_projects/some_asset`. This is confusing but necessary to conform to the Google Cloud API standards.
## Using manifests
A basic manifest is shown in the following code block. It uploads a file named `small.tif` from a Google Cloud Storage bucket named `gs://earthengine-test`.
```
{
 "name": "projects/some-project-id/assets/some-asset-id",
 "tilesets": [
  {
   "sources": [
    {
     "uris": [
      "gs://earthengine-test/small.tif"
     ]
    }
   ]
  }
 ]
}
```

To use it, save it to a file named `manifest.json` and run:
`earthengine upload image --manifest /path/to/manifest.json`
(The file `gs://earthengine-test/small.tif` exists and is publicly readable-you can use it for testing.)
## Tilesets
The somewhat complicated manifest structure of JSON is necessary to give enough flexibility to address a common upload challenge: how to describe all possible ways of combining pixels from multiple source files into a single asset. Specifically, there are two independent ways of grouping files together:
  * Mosaics. Sometimes multiple files represent multiple tiles (for example, each tile is a 1x1 degree square). Such files must be **_mosaiced (merged together)_** into the same band in an EE asset.
  * Separate bands. Sometimes, multiple files represent multiple bands. Such files must be **_stacked together_** as bands in an EE asset.


(Both ways might have to be used at the same time, but that is a rare situation.)
To describe these options, manifests introduce the notion of a **_tileset_**. A single tileset corresponds to a single GDAL source. Because of this, all sources in a single tileset must have the same GDAL structure (number and type of bands, projection, transform, missing value). Since a GDAL source can have multiple bands, one tileset may contain data for multiple EE bands.
For **_mosaic ingestion_** , the manifest will look like this:
```
{
 "name": "projects/some-project-id/assets/some-asset-id",
 "tilesets": [
  {
   "sources": [
    {
     "uris": [
      "gs://bucket/N30W22.tif"
     ]
    },
    {
     "uris": [
      "gs://bucket/N31W22.tif"
     ]
    }
   ]
  }
 ]
}
```

For **_separate bands_** , the manifest will look like this (you also need to add a `bands` section as explained below):
```
{
 "name": "projects/some-project-id/assets/some-asset-id",
 "bands": ...,
 "tilesets": [
  {
   "id": "tileset_for_band1",
   "sources": [
    {
     "uris": [
      "gs://bucket/band1.tif"
     ]
    }
   ]
  },
  {
   "id": "tileset_for_band2",
   "sources": [
    {
     "uris": [
      "gs://bucket/band2.tif"
     ]
    }
   ]
  }
 ]
}
```

Note that in the case of separate bands we have to give each tileset a different tileset ID for clarity. The tileset ID can be an arbitrary string - these strings are not kept in the uploaded asset. Tileset IDs are only used in ingestion to distinguish stacked tilesets from each other.
## Bands
The second important concept is matching source files to EE asset bands. This is done using the `bands` section of the manifest.
The `bands` section can be omitted, in which case the bands are created first from the files in the first tileset, then from the next tileset, and so on. By default, the bands are named "b1", "b2", etc. To override the default band names, include a "bands" section at the end, like this:
```
{
 "name": "projects/earthengine-legacy/assets/users/username/some_folder/some_id",
 "tilesets": [
  {
   "sources": [
    {
     "uris": [
      "gs://bucket/rgb.tif"
     ]
    }
   ]
  }
 ],
 "bands": [
  {
   "id": "R",
   "tilesetBandIndex": 0
  },
  {
   "id": "G",
   "tilesetBandIndex": 1
  },
  {
   "id": "B",
   "tilesetBandIndex": 2
  }
 ]
}
```

The number of EE bands must be the same as the total number of bands in all tilesets.
If you don't want to ingest all the bands from a file, you can use the `tilesetBandIndex` field to indicate which of the GDAL bands should be ingested. The first band has tilesetBandIndex of 0.
Example:
Suppose the source file has four bands: "tmin", "tmin_error", "tmax", "tmax_error". We only want to ingest "tmin" and "tmax". Relevant manifest sections will look like this:
```
{
 "name": "projects/earthengine-legacy/assets/users/username/some_folder/some_id",
 "tilesets": [
  {
   "id": "temperature",
   "sources": [
    {
     "uris": [
      "gs://bucket/temperature.tif"
     ]
    }
   ]
  }
 ],
 "bands": [
  {
   "id": "tmin",
   "tilesetBandIndex": 0,
   "tilesetId": "temperature"
  },
  {
   "id": "tmax",
   "tilesetBandIndex": 2,
   "tilesetId": "temperature"
  }
 ]
}
```

## Mask bands
Band masking is controlled by the `maskBands` component of the manifest. Three possible mask configurations are supported (but the mask band is always assumed to be the last band in a certain file).
  1. Mask for **all** data bands in the **same** file.
  2. Mask for **all** data bands coming from all **other** files.
  3. Mask for **some** data bands.


1. The most common case is a single GeoTIFF whose last band is used as mask for the other bands. This only works for GeoTIFFs of type Byte. Use the following manifest:
```
{
 "name": "projects/earthengine-legacy/assets/users/username/some_folder/some_id",
 "tilesets": [
  {
   "id": "data_tileset",
   "sources": [
    {
     "uris": [
      "gs://bucket/data_file.tif"
     ]
    }
   ]
  }
 ],
 "bands": [
  {
   "id": "data_band",
   "tilesetId": "data_tileset"
  },
  {
   "id": "qa_band",
   "tilesetId": "data_tileset"
  }
 ],
 "maskBands": [
  {
   "tilesetId": "data_tileset"
  }
 ]
}
```

2. To use a mask GeoTIFF as a mask for all bands in another GeoTIFF, use the following manifest:
```
{
 "name": "projects/earthengine-legacy/assets/users/username/some_folder/some_id",
 "tilesets": [
  {
   "id": "data_tileset",
   "sources": [
    {
     "uris": [
      "gs://bucket/data_file.tif"
     ]
    }
   ]
  },
  {
   "id": "mask_tileset",
   "sources": [
    {
     "uris": [
      "gs://bucket/mask_file.tif"
     ]
    }
   ]
  }
 ],
 "bands": [
  {
   "id": "data_band",
   "tilesetId": "data_tileset"
  },
  {
   "id": "qa_band",
   "tilesetId": "data_tileset"
  }
 ],
 "maskBands": [
  {
   "tilesetId": "mask_tileset"
  }
 ]
}
```

3. To use a GeoTIFF as a mask for a specific band in another file, use the following manifest (the difference with the previous case is that the `bandIds` field in `maskBands` is set):
```
{
 "name": "projects/earthengine-legacy/assets/users/username/some_folder/some_id",
 "tilesets": [
  {
   "id": "data_tileset",
   "sources": [
    {
     "uris": [
      "gs://bucket/data_file.tif"
     ]
    }
   ]
  },
  {
   "id": "mask_tileset",
   "sources": [
    {
     "uris": [
      "gs://bucket/mask_file.tif"
     ]
    }
   ]
  }
 ],
 "bands": [
  {
   "id": "data_band",
   "tilesetId": "data_tileset"
  },
  {
   "id": "qa_band",
   "tilesetId": "data_tileset"
  }
 ],
 "maskBands": [
  {
   "tilesetId": "mask_tileset",
   "bandIds": ["data_band"]
  }
 ]
}
```

In the last example, we are working with two bands from the `data_tileset` tileset, but are only applying a mask to one of the bands (`data_band`), as designated by the `bandIds` field of the only provided `maskBands` list object.
Note that only the last band of the tileset mentioned in `maskBands` is used as the mask band.
## Pyramiding policy
When Earth Engine constructs [image pyramids](https://developers.google.com/earth-engine/scale#image-pyramids) during ingestion, it has to repeatedly reduce 2x2-pixel grids into a single pixel, transforming the pixel value in some fashion. By default, pixel values are averaged, which is the right thing to do in most cases when the raster band represents more-or-less continuous data. However, there are two situations when relying on the default will produce incorrect results, in which case the `pyramidingPolicy` field in the band definition must be set (if not set, its value is assumed to be "MEAN" by default).
For classification of raster images (for land cover classification, for example) the most logical way of pyramiding pixels is to take the majority of the four values to produce the next one. This is done using the "MODE" pyramiding policy:
```
{
 "name": "projects/earthengine-legacy/assets/users/username/some_folder/some_id",
 "tilesets": [
  {
   "sources": [
    {
     "uris": [
      "gs://bucket/landcover.tif"
     ]
    }
   ]
  }
 ],
 "bands": [
  {
   "id": "landcover",
   "pyramidingPolicy": "MODE"
  }
 ]
}
```

For raster bands where neither "MEAN" nor "MODE" make sense (for example, bitpacked pixels), the "SAMPLE" pyramiding policy should be used. "SAMPLE" always takes the value of the upper left-hand pixel from each 2x2 grid. The following example assigns the "MEAN" pyramiding policy to a band representing a continuous variable ("NDVI") and "SAMPLE" to the data's "QA" band.
```
{
 "name": "projects/earthengine-legacy/assets/users/username/some_folder/some_id",
 "tilesets": [
  {
   "sources": [
    {
     "uris": [
      "gs://bucket/ndvi.tif"
     ]
    }
   ]
  }
 ],
 "bands": [
  {
   "id": "NDVI",
   "tilesetBandIndex": 0,
   "pyramidingPolicy": "MEAN"
  },
  {
   "id": "QA",
   "tilesetBandIndex": 1,
   "pyramidingPolicy": "SAMPLE"
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
 "tilesets": [
  {
   "sources": [
    {
     "uris": [
      "gs://bucket/img_20190612.tif"
     ]
    }
   ]
  }
 ],
 "startTime": "1980-01-31T00:00:00Z",
 "endTime": "1980-02-01T00:00:00Z"
}
```

## Manifest structure reference
The following JSON structure includes all possible image upload manifest fields. Find field definitions in the following [ Manifest field definitions section.](https://developers.google.com/earth-engine/guides/image_manifest#manifest_field_definitions)
```
{
"name":_<string>_,
"tilesets":[
  {
   "dataType": _<string>_,
   "id": _<string>_,
   "crs": _<string>_,
   "sources": [
    {
     "uris": [
      _<string__>_
],
"affineTransform":{
"scaleX":_<double>_,
"shearX":_<double>_,
"translateX":_<double>_,
"shearY":_<double>_,
"scaleY":_<double>_,
"translateY":_<double>_
}
}
]
}
],
"bands":[
  {
   "id": _<string>_,
   "tilesetId": _<string>_,
   "tilesetBandIndex": _<int32>_,
   "missingData": {
    "values": [_<double__>_]
},
"pyramindingPolicy":_<string>_
}
],
"maskBands":[
  {
   "tilesetId": _<string>_,
   "bandIds": [
    _<string__>_
]
}
],
"footprint":{
"points":[
   {
    "x": _<double>_,
    "y": _<double__>_
   }
],
"bandId":_<string>_
},
"missingData":{
"values":[_<double>_]
},
"pyramidingPolicy":_<string>_,
"uriPrefix":_<string>_,
"startTime":{
"seconds":_<integer>_
},
"endTime":{
"seconds":_<integer>_
},
"properties":{
_<unspecified>_
}
}
```

## Manifest field definitions
#### name
`string`
The name of the asset to be created. `name` is of the format "projects/*/assets/**" (for example, "projects/earthengine-legacy/assets/users/USER/ASSET").
#### tilesets
`list`
A list of dictionaries that define properties for tile sets. See the following `tilesets` dictionary element fields for more information.
#### tilesets[i].dataType
`string`
Specifies the numeric data type of the data. The default is the type that GDAL reports, in which case there is no need to define.
Data type | Value  
---|---  
Unspecified | "DATA_TYPE_UNSPECIFIED"  
8-bit signed integer | "INT8"  
8-bit unsigned integer | "UINT8"  
16-bit signed integer | "INT16"  
16-bit unsigned integer | "UINT16"  
32-bit signed integer | "INT32"  
32-bit unsigned integer | "UINT32"  
32-bit float | "FLOAT32"  
64-bit float | "FLOAT64"  
#### tilesets[i].id
`string`
The ID of the tileset. Must be unique among tilesets specified in the asset manifest. This ID is discarded during the processing step; it is only used to link a tileset to a band. The empty string is a valid ID.
#### tilesets[i].crs
`string`
The coordinate reference system of the pixel grid, specified as a standard code where possible (for example, EPSG code), and in WKT format otherwise.
#### tilesets[i].sources
`list`
A list of dictionaries defining the properties of an image file and its sidecars. See the following `sources` dictionary element fields for more information.
#### tilesets[i].sources[j].uris
`list`
A list of the URIs of the data to ingest. Only Google Cloud Storage URIs are supported. Each URI must be specified in the following format: `gs://bucket-id/object-id`. The primary object should be the first element of the list, and sidecars listed afterwards. Each URI is prefixed with `ImageManifest.uriPrefix` if set.
#### tilesets[i].sources[j].affineTransform
`dictionary`
An optional affine transform. Should only be specified if the data from `uris` (including any sidecars) isn't sufficient to place the pixels. Provided as a dictionary with the following keys: "scaleX", "shearX", "translateX", "shearY", "scaleY", "translateY". See [ this reference](https://docs.oracle.com/javase/8/docs/api/java/awt/geom/AffineTransform.html) for more information.
Example keys and values:
```
{
 "scaleX": 0.1,
 "shearX": 0.0,
 "translateX": -180.0,
 "shearY": 0.0,
 "scaleY": -0.1,
 "translateY": 90.0
}
```

#### bands
`list`
A list of dictionaries defining the properties of a single band sourced from a tileset. Note that the band order of the asset is the same as the order of `bands`. See the following `bands` dictionary element fields for more information.
#### bands[i].id
`string`
The ID (name) of the band.
#### bands[i].tilesetId
`string`
The ID of the tileset corresponding to the band.
#### bands[i].tilesetBandIndex
`int32`
The zero-based band index from the tileset corresponding to the band.
#### bands[i].missingData.values
`list`
A list of values (double type) which represent no data in the band.
#### bands[i].pyramidingPolicy
`string`
The pyramiding policy. See [ this link](https://developers.google.com/earth-engine/scale#image-pyramids) for more information. Options include:
  * "MEAN" (default)
  * "MODE"
  * "SAMPLE"


#### maskBands
`list`
A list of dictionaries defining the properties of a single mask band sourced from a tileset. At most 1 mask band may be provided. See the following `maskBands` dictionary element fields for more information.
#### maskBands[i].tilesetId
`string`
The ID of the tileset corresponding to the mask band. The last band of the tileset is always used as the mask band.
#### maskBands[i].bandIds
`list of strings`
List of the IDs of bands that the mask band applies to. If empty, the mask band is applied to all bands in the asset. Each band may only have one corresponding mask band.
#### footprint
`dictionary`
A dictionary defining the properties of the footprint of all valid pixels in an image. If empty, the default footprint is the entire image. See the following `footprint` dictionary element fields for more information.
#### footprint.points
`list`
A list of points defining a footprint of all valid pixels in an image. A point is defined by a dictionary with "x" and "y" keys having float values. A list of points are to describe a ring which forms the exterior of a simple polygon that must contain the centers of all valid pixels of the image. This must be a linear ring: the last point must be equal to the first. Coordinates are in the projection of the band specified by `bandId`.
Note: Use non-integer coordinates such as the center of each pixel because `footprint` is taken to include a pixel if the pixel (a 1x1 rectangle) intersects the footprint. To avoid accidentally selecting neighboring pixels, don't use integer-valued coordinates, because those are the boundaries between pixels. Drawing the footprint along the pixel centers prevents including unintended pixels, which can cause errors when intended pixels are abutting a map boundary such as the antimeridian or a pole.
For example, for a 2x2 image with all four valid pixels, the following is one possible ring:
```
[
 {
  "x": 0.5,
  "y": 0.5
 },
 {
  "x": 0.5,
  "y": 1.5
 },
 {
  "x": 1.5,
  "y": 1.5
 },
 {
  "x": 1.5,
  "y": 0.5
 },
 {
  "x": 0.5,
  "y": 0.5
 }
]
```

#### footprint.bandId
`string`
The ID of the band whose CRS defines the coordinates of the footprint. If empty, the first band is used.
#### missingData.values
`list`
A list of values (double type) which represent no data in all bands of the image. Applies to all bands which don't specify their own `missingData`.
#### pyramidingPolicy
`string`
The pyramiding policy. If unspecified, the policy "MEAN" is applied by default. Applies to all bands which don't specify their own. See [ this link](https://developers.google.com/earth-engine/scale#image-pyramids) for more information. Options include:
  * "MEAN" (default)
  * "MODE"
  * "SAMPLE"


#### uriPrefix
`string`
An optional prefix prepended to all `uris` defined in the manifest.
#### startTime
`integer`
The timestamp associated with the asset, if any. This typically corresponds to the time at which a satellite image was taken. For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the start of that interval. Specified as as seconds and (optionally) nanoseconds since the epoch (1970-01-01). Assumed to be in the UTC time zone.
#### endTime
`integer`
For assets that correspond to an interval of time, such as average values over a month or year, this timestamp corresponds to the end of that interval (exclusive). Specified as as seconds and (optionally) nanoseconds since the epoch (1970-01-01). Assumed to be in the UTC time zone.
#### properties
`dictionary`
An arbitrary flat dictionary of key-value pairs. Keys must be strings and values can be either numbers or strings. List values are not yet supported for user-uploaded assets.
## Limitations
### JSON manifest size
The JSON manifest file size limit is 10 MB. If you have many files to upload, consider ways to reduce the number of characters needed to describe the dataset. For example, use the [`uriPrefix`](https://developers.google.com/earth-engine/guides/image_manifest#uriprefix) field to eliminate the need to provide the Google Cloud bucket path for each URI in the [`uris`](https://developers.google.com/earth-engine/guides/image_manifest#tilesets) list. If further size reduction is needed, try shortening the filenames.
### Image file format
Each image file must be a TIFF image. If the CRS is not specified in the manifest, then the file must be a GeoTIFF with an embedded CRS.
TIFF files can be compressed with DEFLATE, JPEG-XL/JXL, LERC, LERC_DEFLATE, LERC_ZSTD, LZMA, LZW, WEBP, or ZSTD.
Recommendations for the best upload experience for large files:
  * **Best choice:** ZSTD offers a good balance of speed and compression.
  * **Avoid:** LZMA can be very slow despite good compression.
  * **Uncompressed files:** Will result in larger files and longer upload times.
  * **Lossy compression (e.g., JPEG):** May alter pixel values. Use lossless compression (e.g., DEFLATE, LZMA, LZW, ZSTD) unless you understand the potential impact on your data.


