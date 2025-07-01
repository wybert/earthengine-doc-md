 
#  REST Resource: projects.thumbnails
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Resource: Thumbnail](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.thumbnails#resource:-thumbnail)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.thumbnails#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.thumbnails#create)
    * [getPixels](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.thumbnails#getpixels)


## Resource: Thumbnail
Information about a thumbnail.
JSON representation  
---  
```
{
 "name": string,
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression))
 },
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageFileFormat)),
 "bandIds": [
  string
 ],
 "visualizationOptions": {
  object (VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/VisualizationOptions))
 },
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1alpha/PixelGrid))
 },
 "filenamePrefix": string
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the thumbnail, of the form "projects/*/thumbnails/**" (e.g. "projects/earthengine-legacy/thumbnails/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression)`)` The expression to compute. Must evaluate to an Image.  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageFileFormat)`)` The output encoding in which to generate the resulting image.  
`bandIds[]` |  `string` If present, specifies a specific set of bands that will be selected from the result of evaluating `expression`. If not present, all bands resulting from `expression` will be selected.  
`visualizationOptions` |  `object (`VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/VisualizationOptions)`)` If present, a set of visualization options to apply to produce an 8-bit RGB visualization of the data.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1alpha/PixelGrid)`)` An optional pixel grid describing how the image computed by `expression` is reprojected and clipped.  
`filenamePrefix` |  `string` Only used when fileFormat is ZIPPED_GEO_TIFF or ZIPPED_GEO_TIFF_PER_BAND.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.thumbnails/create)`
|  Creates an ID that can be used to render a "thumbnail" image.  
### `getPixels[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.thumbnails/getPixels)`
|  Computes an image showing the result of a computation.  
Was this helpful?
