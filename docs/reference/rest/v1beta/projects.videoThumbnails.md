 
#  REST Resource: projects.videoThumbnails 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Resource: VideoThumbnail](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.videoThumbnails#resource:-videothumbnail)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.videoThumbnails#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.videoThumbnails#create)
    * [getPixels](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.videoThumbnails#getpixels)


## Resource: VideoThumbnail
Information about a video thumbnail.
JSON representation  
---  
```
{
 "name": string,
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression))
 },
 "videoOptions": {
  object (VideoOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.videoThumbnails#VideoThumbnail.VideoOptions))
 },
 "fileFormat": enum (VideoFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.videoThumbnails#VideoThumbnail.VideoFileFormat)),
 "grid": {
  object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid))
 }
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the video thumbnail, of the form "projects/*/videoThumbnails/**" (e.g. "projects/earthengine-legacy/videoThumbnails/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression)`)` The expression to compute. Must evaluate to an ImageCollection.  
`videoOptions` |  `object (`VideoOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.videoThumbnails#VideoThumbnail.VideoOptions)`)` Options for the animation.  
`fileFormat` |  `enum (`VideoFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.videoThumbnails#VideoThumbnail.VideoFileFormat)`)` The output encoding in which to generate the resulting video thumbnail. Currently only GIF is supported.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1beta/PixelGrid)`)` An optional pixel grid describing how the images computed by `expression` are reprojected and clipped.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.videoThumbnails/create)`
|  Creates an ID that can be used to render an image containing an animation of multiple images from a collection.  
### `getPixels[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.videoThumbnails/getPixels)`
|  Computes an image showing the result of a computation.  
