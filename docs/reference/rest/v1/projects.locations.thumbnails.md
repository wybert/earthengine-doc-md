 
#  REST Resource: projects.locations.thumbnails
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Resource: Thumbnail](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.thumbnails#resource:-thumbnail)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.thumbnails#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.thumbnails#create)


## Resource: Thumbnail
Information about a thumbnail.
JSON representation  
---  
```
{
 "name": string,
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression))
 },
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileFormat)),
 "bandIds": [
  string
 ],
 "visualizationOptions": {
  object (VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1/VisualizationOptions))
 },
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid))
 },
 "filenamePrefix": string
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the thumbnail, of the form "projects/*/thumbnails/**" (e.g. "projects/earthengine-legacy/thumbnails/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression)`)` The expression to compute. Must evaluate to an Image.  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileFormat)`)` The output encoding in which to generate the resulting image.  
`bandIds[]` |  `string` If present, specifies a specific set of bands that will be selected from the result of evaluating `expression`. If not present, all bands resulting from `expression` will be selected.  
`visualizationOptions` |  `object (`VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1/VisualizationOptions)`)` If present, a set of visualization options to apply to produce an 8-bit RGB visualization of the data.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid)`)` An optional pixel grid describing how the image computed by `expression` is reprojected and clipped.  
`filenamePrefix` |  `string` Only used when fileFormat is ZIPPED_GEO_TIFF or ZIPPED_GEO_TIFF_PER_BAND.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.thumbnails/create)`
|  Creates an ID that can be used to render a "thumbnail" image.  
