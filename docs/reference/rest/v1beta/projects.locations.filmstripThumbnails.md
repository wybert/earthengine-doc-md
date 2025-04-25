 
#  REST Resource: projects.locations.filmstripThumbnails 
Stay organized with collections  Save and categorize content based on your preferences. 
## Resource: FilmstripThumbnail
Information about a filmstrip thumbnail.
JSON representation  
---  
```
{
 "name": string,
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression))
 },
 "orientation": enum (Orientation[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.filmstripThumbnails#FilmstripThumbnail.Orientation)),
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)),
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid))
 }
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the filmstrip thumbnail, of the form "projects/*/filmstripThumbnails/**" (e.g. "projects/earthengine-legacy/filmstripThumbnails/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression)`)` The expression to compute. Must evaluate to an ImageCollection.  
`orientation` |  `enum (`Orientation[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.filmstripThumbnails#FilmstripThumbnail.Orientation)`)` How the images should be placed to form the filmstrip thumbnail.  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)`)` The output encoding in which to generate the resulting image.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid)`)` An optional pixel grid describing how the images computed by `expression` are reprojected and clipped.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.filmstripThumbnails/create)`
|  Creates an ID that can be used to render an image containing multiple images from a collection.  
