 
#  Export.table.toBigQuery 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a batch task to export a FeatureCollection to BigQuery. Tasks can be started from the Tasks tab. 
Note that this feature is in Preview, and the API and behavior may change significantly. For more information, see https://developers.google.com/earth-engine/guides/export_to_bigquery
Usage| Returns  
---|---  
`Export.table.toBigQuery(collection,  _description_, _table_, _overwrite_, _append_, _selectors_, _maxVertices_, _priority_)`|   
Argument|  Type| Details  
---|---|---  
`collection`| FeatureCollection| The feature collection to export.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportTableTask".  
`table`| String, optional| The fully-qualifed BigQuery destination table in the following format: "project_id.dataset_id.table_id".  
`overwrite`| Boolean, optional| Whether the existing table should be overwritten by the result of this export. Defaults to false. The `overwrite` and `append` parameters cannot be `true` simultaneously. The export fails if the table already exists and both `overwrite` and `append` are `false`.  
`append`| Boolean, optional| Whether table data should be appended if the table already exists and has a compatible schema. Defaults to false. The `overwrite` and `append` parameters cannot be `true` simultaneously. The export fails if the table already exists and both `overwrite` and `append` are `false`.  
`selectors`| List, optional| A list of properties to include in the export; either a single string with comma-separated names or a list of strings.  
`maxVertices`| Number, optional| Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
