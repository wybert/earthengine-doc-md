 
#  Method: projects.image.import
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/import#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/import#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/import#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/import#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/import#authorization-scopes)


Imports an image.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{project=projects/*}/image:import`
The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.
### Path parameters
Parameters  
---  
`project` |  `string` The project id or project number of the Google Cloud Platform project that should be treated as the service consumer for this request. Format is `projects/{project-id}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `project`:
  * `earthengine.imports.create`

  
### Request body
The request body contains data with the following structure:
JSON representation  
---  
```
{
  "imageManifest": {
    object (ImageManifest[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageManifest))
  },
  "description": string,
  "overwrite": boolean,
  "requestId": string
}
```
  
Fields  
---  
`imageManifest` |  `object (`ImageManifest[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageManifest)`)` The image manifest.  
`description` |  `string` A human-readable name of the task.  
`overwrite` |  `boolean` Whether to allow overwriting an existing asset.  
`requestId` |  `string` A unique string used to detect duplicated requests. If more than one request is made by the same user with the same non-empty `requestId`, only one of those requests may successfully start a long-running operation. `requestId` may contain the characters a..z, A..Z, 0-9, or '-'. `requestId` may be at most 60 characters long.  
### Response body
If successful, the response body contains an instance of `Operation[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `           https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
