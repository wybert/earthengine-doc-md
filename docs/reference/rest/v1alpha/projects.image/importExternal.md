 
#  Method: projects.image.importExternal 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [HTTP request](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/importExternal#http-request)
  * [Path parameters](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/importExternal#path-parameters)
  * [Request body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/importExternal#request-body)
  * [Response body](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/importExternal#response-body)
  * [Authorization scopes](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.image/importExternal#authorization-scopes)


Imports an external image.
### HTTP request
`POST https://earthengine.googleapis.com/v1alpha/{project=projects/*}/image:importExternal`
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
 "overwrite": boolean
}
```
  
Fields  
---  
`imageManifest` |  `object (`ImageManifest[](https://developers.google.com/earth-engine/reference/rest/v1alpha/ImageManifest)`)` The image manifest.  
`overwrite` |  `boolean` Whether to allow overwriting an existing asset.  
### Response body
If successful, the response body is empty.
### Authorization scopes
Requires one of the following OAuth scopes:
  * `https://www.googleapis.com/auth/earthengine`
  * `      https://www.googleapis.com/auth/cloud-platform`


For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).
