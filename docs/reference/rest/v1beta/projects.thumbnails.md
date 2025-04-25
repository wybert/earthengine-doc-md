 
#  REST Resource: projects.thumbnails 
Stay organized with collections  Save and categorize content based on your preferences. 
## Resource: Thumbnail
Information about a thumbnail.
JSON representation  
---  
```
{
 "name": string,
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression))
 },
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)),
 "bandIds": [
  string
 ],
 "visualizationOptions": {
  object (VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/VisualizationOptions))
 },
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid))
 },
 "filenamePrefix": string
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the thumbnail, of the form "projects/*/thumbnails/**" (e.g. "projects/earthengine-legacy/thumbnails/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression)`)` The expression to compute. Must evaluate to an Image.  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)`)` The output encoding in which to generate the resulting image.  
`bandIds[]` |  `string` If present, specifies a specific set of bands that will be selected from the result of evaluating `expression`. If not present, all bands resulting from `expression` will be selected.  
`visualizationOptions` |  `object (`VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/VisualizationOptions)`)` If present, a set of visualization options to apply to produce an 8-bit RGB visualization of the data.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid)`)` An optional pixel grid describing how the image computed by `expression` is reprojected and clipped.  
`filenamePrefix` |  `string` Only used when fileFormat is ZIPPED_GEO_TIFF or ZIPPED_GEO_TIFF_PER_BAND.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.thumbnails/create)`
|  Creates an ID that can be used to render a "thumbnail" image.  
### `getPixels[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.thumbnails/getPixels)`
|  Computes an image showing the result of a computation.  
