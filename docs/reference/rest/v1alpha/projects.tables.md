 
#  REST Resource: projects.tables
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Resource: Table](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables#resource:-table)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables#create)
    * [getFeatures](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables#getfeatures)


## Resource: Table
Information about a table.
JSON representation  
---  
```
{
  "name": string,
  "expression": {
    object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression))
  },
  "fileFormat": enum (TableFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.tables#Table.TableFileFormat)),
  "selectors": [
    string
  ],
  "filename": string
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the thumbnail, of the form "projects/*/tables/**" (e.g. "projects/earthengine-legacy/tables/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1alpha/Expression)`)` The expression to compute. Must evaluate to a FeatureCollection.  
`fileFormat` |  `enum (`TableFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.locations.tables#Table.TableFileFormat)`)` The output encoding in which to generate the resulting table.  
`selectors[]` |  `string` Optional property fields to select from the specified table.  
`filename` |  `string` Optional filename of the resulting table.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/create)`
|  Creates an ID that can be used to render "table" data.  
### `getFeatures[](https://developers.google.com/earth-engine/reference/rest/v1alpha/projects.tables/getFeatures)`
|  Fetches `Table` features, the request includes the name of the Table to download from a previous `CreateTable` request.  
Was this helpful?
