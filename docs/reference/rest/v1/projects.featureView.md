 
#  REST Resource: projects.featureView
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Resource: FeatureView](https://developers.google.com/earth-engine/reference/rest/v1/projects.featureView#resource:-featureview)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1/projects.featureView#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1/projects.featureView#create)


## Resource: FeatureView
Information about a FeatureView map.
JSON representation  
---  
```
{
  "name": string,
  "visualizationExpression": {
    object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression))
  },

  // Union field source can be only one of the following:
  "asset": string
  // End of list of possible types for union field source.
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the map, of the form "projects/*/featureViews/**" (e.g. "projects/earthengine-legacy/featureViews/").  
`visualizationExpression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1/Expression)`)` A set of FeatureView visualization options to apply to the tiles at serving-time. Based on the google.earthengine.datamaps.v1.MapOptions proto.  
Union field `source`. The source of this map's data. `source` can be only one of the following:  
`asset` |  `string` Earth Engine asset name for which to create a FeatureView.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1/projects.featureView/create)`
|  Create a FeatureView.  
Was this helpful?
