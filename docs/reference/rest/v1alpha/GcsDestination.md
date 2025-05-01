 
#  GcsDestination 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [TilePermissions](https://developers.google.com/earth-engine/reference/rest/v1alpha/GcsDestination#tilepermissions)


This item is deprecated!
Configuration for a destination in Google Cloud Storage.
JSON representation  
---  
```
{
 "bucket": string,
 "filenamePrefix": string,
 "permissions": enum (TilePermissions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GcsDestination#TilePermissions)),
 "bucketCorsUris": [
  string
 ]
}
```
  
Fields  
---  
`bucket` |  `string` The Google Cloud Storage destination bucket.  
`filenamePrefix` |  `string` The string used as the prefix for each output file. A trailing "/" indicates a path. The filenames of the exported files will be constructed from this prefix, the coordinates of each file in a mosaic (if any), and a file extension corresponding to the file format.  
`permissions` |  `enum (`TilePermissions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GcsDestination#TilePermissions)`)` Specifies the permissions to set on the exported tiles. If unspecified, defaults to DEFAULT_OBJECT_ACL.  
`bucketCorsUris[]` |  `string` Optional list of URIs to whitelist for the CORS settings on the bucket. Used to enable websites to access exported files via JavaScript.  
## TilePermissions
Permissions to set on exported map tiles.
Enums  
---  
`TILE_PERMISSIONS_UNSPECIFIED` | Unspecified.  
`PUBLIC` | Write public tiles. Requires the caller to be an OWNER of the bucket.  
`DEFAULT_OBJECT_ACL` | Write tiles using the bucket's default object ACL.  
