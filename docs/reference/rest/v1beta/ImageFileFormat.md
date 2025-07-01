 
#  ImageFileFormat
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Selects an image file format in which to return a block of pixel data.
Enums  
---  
`IMAGE_FILE_FORMAT_UNSPECIFIED` | Unspecified.  
`JPEG` | JPEG. Intended for display purposes. Only supported for 8-bit RGB data, or data that is converted to 8-bit RGB via `visualization` parameters.  
`PNG` | PNG. Intended for display purposes. Only supported for 8-bit RGB data, or data that is converted to 8-bit RGB via `visualization` parameters.  
`AUTO_JPEG_PNG` | Automatically select JPEG or PNG depending on whether or not there is any transparency. Intended for display purposes. Only supported for 8-bit RGB data, or data that is converted to 8-bit RGB via `visualization` parameters.  
`NPY` | NumPy .npy format.  
`GEO_TIFF` | GeoTIFF format.  
`TF_RECORD_IMAGE` | TFRecord format. Only supported for image exports.  
`ZIPPED_GEO_TIFF` | A format which returns a GeoTIFF file wrapped in a zip file. This is only available when using CreateThumbnail.  
`ZIPPED_GEO_TIFF_PER_BAND` | A format which returns a GeoTIFF file for each band, wrapped in a zip file. This is only available when using CreateThumbnail.  
