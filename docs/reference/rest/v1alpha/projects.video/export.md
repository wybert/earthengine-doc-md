 
#  Method: projects.video.export
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Initiates a batch process that computes a video and writes the result to one of several destinations.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{project=projects/*}/video:export`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.exports.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
  "expression": {
    object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression))
  },
  "description": string,
  "videoOptions": {
    object (VideoOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.videoThumbnails#VideoThumbnail.VideoOptions))
  },
  "fileExportOptions": {
    object (VideoFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.video/export#VideoFileExportOptions))
  },
  "requestId": string,
  "workloadTag": string,
  "priority": integer
}
```
  
Fields  
---  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression)`)` An expression that evaluates to the video to compute and export, represented as an image collection.  
`description` |  `string` A human-readable name of the task.  
`videoOptions` |  `object (`VideoOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.videoThumbnails#VideoThumbnail.VideoOptions)`)` Basic options describing the video to generate.  
`fileExportOptions` |  `object (`VideoFileExportOptions[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.video/export#VideoFileExportOptions)`)` Options for where and in what form to export the video.  
`requestId` |  `string` A unique string used to detect duplicated requests. If more than one request is made by the same user with the same non-empty `requestId`, only one of those requests may successfully start a long-running operation. `requestId` may contain the characters a..z, A..Z, 0-9, or '-'. `requestId` may be at most 60 characters long.  
`workloadTag` |  `string` User supplied label to track this computation.  
`priority` |  `integer` Optional. The priority of the export task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100 if not set.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/cloud-platform`
  * `           https://www.googleapis.com/auth/devstorage.full_control`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
## VideoFileExportOptions
Options for exporting videos as files outside Earth Engine.
JSON representation  
---  
```
{
  "fileFormat": enum (VideoFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.videoThumbnails#VideoThumbnail.VideoFileFormat)),

  // Union field destination can be only one of the following:
  "driveDestination": {
    object (DriveDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/DriveDestination))
  },
  "cloudStorageDestination": {
    object (CloudStorageDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/CloudStorageDestination))
  },
  "gcsDestination": {
    object (GcsDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GcsDestination))
  }
  // End of list of possible types for union field destination.
}
```
  
Fields  
---  
`fileFormat` |  `enum (`VideoFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.videoThumbnails#VideoThumbnail.VideoFileFormat)`)` The file format in which to export the video(s). Currently only MP4 is supported.  
Union field `destination`. Where to write the results. `destination` can be only one of the following:  
`driveDestination` |  `object (`DriveDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/DriveDestination)`)` If specified, configures export to Google Drive.  
`cloudStorageDestination` |  `object (`CloudStorageDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/CloudStorageDestination)`)` If specified, configures export to Google Cloud Storage.  
`gcsDestination  
**(deprecated)**`|  `object (`GcsDestination[](https://developers.google.com/earth-engine/reference/rest/v1alpha/GcsDestination)`)` This item is deprecated! If specified, configures export to Google Cloud Storage.  
