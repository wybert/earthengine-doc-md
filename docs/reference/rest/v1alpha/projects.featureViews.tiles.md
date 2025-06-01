 
#  REST Resource: projects.featureViews.tiles 
Stay organized with collections  Save and categorize content based on your preferences. 
## Resource: HttpBody
Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page.
This message can be used both in streaming and non-streaming API methods in the request as well as the response.
It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body.
Example:
```
message GetResourceRequest {
 // A unique request id.
 string requestId = 1;
 // The raw HTTP body is bound to this field.
 google.api.HttpBody http_body = 2;
}
service ResourceService {
 rpc GetResource(GetResourceRequest)
  returns (google.api.HttpBody);
 rpc UpdateResource(google.api.HttpBody)
  returns (google.protobuf.Empty);
}

```

Example with streaming methods:
```
service CaldavService {
 rpc GetCalendar(stream google.api.HttpBody)
  returns (stream google.api.HttpBody);
 rpc UpdateCalendar(stream google.api.HttpBody)
  returns (stream google.api.HttpBody);
}

```

Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.
JSON representation  
---  
```
{
 "contentType": string,
 "data": string,
 "extensions": [
  {
   "@type": string,
   field1: ...,
   ...
  }
 ]
}
```
  
Fields  
---  
`contentType` |  `string` The HTTP Content-Type header value specifying the content type of the body.  
`data` |  `string (bytes[](https://developers.google.com/discovery/v1/type-format) format)` The HTTP request/response body as raw binary.A base64-encoded string.  
`extensions[]` |  `object` Application specific response metadata. Must be set in the first response for streaming APIs.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
## Methods  
---  
### `get[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.featureViews.tiles/get)`
|  Computes a map tile image showing a portion of a FeatureView.  
