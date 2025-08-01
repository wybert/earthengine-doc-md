 
#  REST Resource: projects.tables
Stay organized with collections  Save and categorize content based on your preferences. 
## Resource: Table
Information about a table.
JSON representation  
---  
```
{
  "name": string,
  "expression": {
    object (Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression))
  },
  "fileFormat": enum (TableFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.tables#Table.TableFileFormat)),
  "selectors": [
    string
  ],
  "filename": string
}
```
  
Fields  
---  
`name` |  `string` The resource name representing the thumbnail, of the form "projects/*/tables/**" (e.g. "projects/earthengine-legacy/tables/").  
`expression` |  `object (`Expression[](https://developers.google.com/earth-engine/reference/rest/v1beta/Expression)`)` The expression to compute. Must evaluate to a FeatureCollection.  
`fileFormat` |  `enum (`TableFileFormat[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.tables#Table.TableFileFormat)`)` The output encoding in which to generate the resulting table.  
`selectors[]` |  `string` Optional property fields to select from the specified table.  
`filename` |  `string` Optional filename of the resulting table.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.tables/create)`
|  Creates an ID that can be used to render "table" data.  
### `getFeatures[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.tables/getFeatures)`
|  Fetches `Table` features, the request includes the name of the Table to download from a previous `CreateTable` request.  
