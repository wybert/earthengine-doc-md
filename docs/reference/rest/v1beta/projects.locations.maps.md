 
#  REST Resource: projects.locations.maps
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Resource: EarthEngineMap](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.maps#resource:-earthenginemap)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.maps#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.maps#create)


## Resource: EarthEngineMap
Information about a map.
JSON representation  
---  
```
{
 "name": string,
 "expression": {
  object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression))
 },
 "fileFormat": enum (ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)),
 "bandIds": [
  string
 ],
 "visualizationOptions": {
  object (VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/VisualizationOptions))
 }
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the map, of the form "projects/*/maps/**" (e.g. "projects/earthengine-legacy/maps/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression)`)` The expression to compute.  
`fileFormat` |  `enum (`ImageFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/ImageFileFormat)`)` The output file format in which to generate the map tiles.  
`bandIds[]` |  `string` If present, specifies a specific set of bands that will be selected from the result of evaluating the given expression. If not present, all bands resulting from the expression will be selected.  
`visualizationOptions` |  `object (`VisualizationOptions[](https://developers.google.com/earth-engine/reference/rest/v1beta/VisualizationOptions)`)` If present, a set of visualization options to apply to produce an 8-bit RGB visualization of the data.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.maps/create)`
|  Creates an ID that can be used to render map tiles showing the results of a computation.  
Was this helpful?
