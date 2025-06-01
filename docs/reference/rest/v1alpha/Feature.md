 
#  Feature 
Stay organized with collections  Save and categorize content based on your preferences. 
A GeoJSON feature object (see RFC 7946) containing the string "Feature" in a field named "type", the geometry in a field named "geometry", and key/value properties in a field named "properties".
JSON representation  
---  
```
{
 "type": string,
 "geometry": value,
 "properties": value
}
```
  
Fields  
---  
`type` |  `string` This string is always present and equal to "Feature".  
`geometry` |  `value (`Value[](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The geometry of the feature. This will contain a `google.protobuf.Struct` if geometry is present for this feature. Otherwise, it will hold a `google.protobuf.NullValue`.  
`properties` |  `value (`Value[](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The properties of the feature. This will contain a `google.protobuf.Struct` if properties are present for this feature. Otherwise, it will hold a `google.protobuf.NullValue`.  
