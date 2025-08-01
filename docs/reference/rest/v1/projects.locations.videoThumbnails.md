 
#  REST Resource: projects.locations.videoThumbnails
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
## Resource: VideoThumbnail
Information about a video thumbnail.
JSON representation  
---  
```
{
  "name": string,
  "expression": {
    object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression))
  },
  "videoOptions": {
    object (VideoOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.videoThumbnails#VideoThumbnail.VideoOptions))
  },
  "fileFormat": enum (VideoFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.videoThumbnails#VideoThumbnail.VideoFileFormat)),
  "grid": {
    object (PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid))
  }
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the video thumbnail, of the form "projects/*/videoThumbnails/**" (e.g. "projects/earthengine-legacy/videoThumbnails/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression)`)` The expression to compute. Must evaluate to an ImageCollection.  
`videoOptions` |  `object (`VideoOptions[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.videoThumbnails#VideoThumbnail.VideoOptions)`)` Options for the animation.  
`fileFormat` |  `enum (`VideoFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.videoThumbnails#VideoThumbnail.VideoFileFormat)`)` The output encoding in which to generate the resulting video thumbnail. Currently only GIF is supported.  
`grid` |  `object (`PixelGrid[](https://developers.google.com/earth-engine/reference/rest/v1/PixelGrid)`)` An optional pixel grid describing how the images computed by `expression` are reprojected and clipped.  
### VideoOptions
Basic options for generating videos.
JSON representation  
---  
```
{
  "framesPerSecond": number,
  "maxFrames": integer,
  "maxPixelsPerFrame": string
}
```
  
Fields  
---  
`framesPerSecond` |  `number` The frame rate of the exported video. Must be a value between 0.1 and 120. Defaults to 5.0.  
`maxFrames` |  `integer` The maximum number of video frames to compute and export. This is a safety guard to prevent you from accidentally starting a larger export than you had intended. The default value is 1000 frames, but you can set the value explicitly to raise or lower this limit.  
`maxPixelsPerFrame` |  `string (Int64Value[](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of pixels to compute and export per frame. This is a safety guard to prevent you from accidentally starting a larger export than you had intended. The default value is 1e8 pixels, but you can set the value explicitly to raise or lower this limit.  
### VideoFileFormat
Selects a video file format in which to encode a sequence of images.
Enums  
---  
`VIDEO_FILE_FORMAT_UNSPECIFIED` | Unspecified.  
`MP4` | MPEG-4 Part 14 format.  
`GIF` | Animated GIF.  
`VP9` | WEBM/VP9  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1/projects.locations.videoThumbnails/create)`
|  Creates an ID that can be used to render an image containing an animation of multiple images from a collection.  
