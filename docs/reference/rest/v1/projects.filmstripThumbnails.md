 
#  REST Resource: projects.filmstripThumbnails
Stay organized with collections  Save and categorize content based on your preferences. 
## Resource: FilmstripThumbnail
Information about a filmstrip thumbnail.
JSON representation  
---  
```
{
 "name": string,
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression))
 },
 "orientation": enum (Orientation[](https://developers.google.com/earth-engine/reference/rest/v1/projects.filmstripThumbnails#FilmstripThumbnail.Orientation)),
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileFormat)),
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid))
 }
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the filmstrip thumbnail, of the form "projects/*/filmstripThumbnails/**" (e.g. "projects/earthengine-legacy/filmstripThumbnails/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression)`)` The expression to compute. Must evaluate to an ImageCollection.  
`orientation` |  `enum (`Orientation[](https://developers.google.com/earth-engine/reference/rest/v1/projects.filmstripThumbnails#FilmstripThumbnail.Orientation)`)` How the images should be placed to form the filmstrip thumbnail.  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/ImageFileFormat)`)` The output encoding in which to generate the resulting image.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid)`)` An optional pixel grid describing how the images computed by `expression` are reprojected and clipped.  
### Orientation
Defines the orientation of a filmstrip thumbnail image.
Enums  
---  
`ORIENTATION_UNSPECIFIED` | Unspecified.  
`HORIZONTAL` | Horizontal: images are laid out side by side, from left to right.  
`VERTICAL` | Vertical: images are laid out from top to bottom.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1/projects.filmstripThumbnails/create)`
|  Creates an ID that can be used to render an image containing multiple images from a collection.  
### `getPixels[](https://developers.google.com/earth-engine/reference/rest/v1/projects.filmstripThumbnails/getPixels)`
|  Computes an image showing the result of a computation.  
