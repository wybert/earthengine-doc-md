 
#  REST Resource: projects.operations
Stay organized with collections  Save and categorize content based on your preferences. 
## Resource: Operation
This resource represents a long-running operation that is the result of a network API call.
JSON representation  
---  
```
{
  "name": string,
  "metadata": {
    "@type": string,
    field1: ...,
    ...
  },
  "done": boolean,

  // Union field result can be only one of the following:
  "error": {
    object (Status[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Status))
  },
  "response": {
    "@type": string,
    field1: ...,
    ...
  }
  // End of list of possible types for union field result.
}
```
  
Fields  
---  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`metadata` |  `object` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any. An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
Union field `result`. The operation result, which can be either an `error` or a valid `response`. If `done` == `false`, neither `error` nor `response` is set. If `done` == `true`, exactly one of `error` or `response` can be set. Some services might not provide the result. `result` can be only one of the following:  
`error` |  `object (`Status[](https://developers.google.com/earth-engine/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error result of the operation in case of failure or cancellation.  
`response` |  `object` The normal, successful response of the operation. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
## Methods  
---  
### `cancel[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/cancel)`
|  Starts asynchronous cancellation on a long-running operation.  
### `delete[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/delete)`
|  Deletes a long-running operation.  
### `get[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/get)`
|  Gets the latest state of a long-running operation.  
### `list[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/list)`
|  Lists operations that match the specified filter in the request.  
### `wait[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.operations/wait)`
|  Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
