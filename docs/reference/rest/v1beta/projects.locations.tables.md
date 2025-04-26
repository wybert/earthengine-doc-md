 
#  REST Resource: projects.locations.tables 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Resource: Table](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.tables#resource:-table)
    * [TableFileFormat](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.tables#tablefileformat)
  * [Methods](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.tables#methods)
    * [create](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.tables#create)


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
### TableFileFormat
Selects a tabular file format in which to encode a table of features.
Enums  
---  
`TABLE_FILE_FORMAT_UNSPECIFIED` | Unspecified.  
`CSV` | Comma-separated value format.  
`GEO_JSON` | GeoJSON FeatureCollection format. See <http://geojson.org/>.  
`KML` | Keyhole Markup Language format.  
`KMZ` | Zip-compressed Keyhole Markup Language format.  
`SHP` | Shapefile format.  
`TF_RECORD_TABLE` | TFRecord format.  
## Methods  
---  
### `create[](https://developers.google.com/earth-engine/reference/rest/v1beta/projects.locations.tables/create)`
|  Creates an ID that can be used to render "table" data.  
Was this helpful?
