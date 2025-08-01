 
#  ee.Image.loadZarrV2Array
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Loads a Zarr v2 array as an Image. The array attributes (.zattrs) must contain the field '_ARRAY_DIMENSIONS', which is a list of the names of each dimension (e.g., ['time', 'y', 'x']). There must be at least two dimensions, with the final two representing Y and X respectively (e.g., ['lat', 'lon']). The supported compression codecs are 'blosc', 'gzip', 'lz4', 'zlib', and 'zstd'. The supported blosc meta-compression codecs are 'lz4', lz4hc', 'zlib', and 'zstd' ('blosclz' is not supported).
Usage | Returns  
---|---  
`ee.Image.loadZarrV2Array(uri, proj, _starts_, _ends_)`|  Image  
Argument | Type | Details  
---|---|---  
`uri` | String | The Cloud Storage URI of the .zarray file to load. A .zmetadata file must be present in the parent directory of the array's directory (e.g., for 'gs://b/o/.zarray', 'gs://b/.zmetadata' must be present). The bucket metadata must be accessible (requires the `storage.buckets.get` permission which is provided by the role "Storage Legacy Bucket Reader" among others, see https://cloud.google.com/storage/docs/access-control/iam-roles) and the bucket must be located in the US multi-region, a dual-region including US-CENTRAL1, or the US-CENTRAL1 region.  
`proj` | Projection | The projection of the array.  
`starts` | List, default: null | The indices (inclusive) at which to start taking slices along each non-spatial dimension. If null, slices will start at index 0 for all non-spatial dimensions. If specified, this list must have a length equal to the number of non-spatial dimensions (total dimensions - 2). An individual element within the list may be null, which defaults to 0 for that dimension. Negative indices are counted from the end of the dimension (e.g., -1 is the last element).  
`ends` | List, default: null | The indices (exclusive) at which to stop taking slices along each non-spatial dimension. If null, slices will extend to the end of each corresponding non-spatial dimension (i.e., defaults to the length of the dimension). If specified, this list must have a length equal to the number of non-spatial dimensions (total dimensions - 2). An individual element within the list may be null, which also defaults to the length of that dimension. Negative indices are counted from the end of the dimension (e.g., -1 is the last element).  
Was this helpful?
