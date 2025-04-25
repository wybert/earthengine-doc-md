 
#  Export.table.toCloudStorage 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a batch task to export a FeatureCollection as a table to Google Cloud Storage. Tasks can be started from the Tasks tab. 
Usage| Returns  
---|---  
`Export.table.toCloudStorage(collection,  _description_, _bucket_, _fileNamePrefix_, _fileFormat_, _selectors_, _maxVertices_, _priority_)`  
Argument|  Type| Details  
---|---|---  
`collection`| FeatureCollection| The feature collection to export.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportTableTask".  
`bucket`| String, optional| The Cloud Storage destination bucket.  
`fileNamePrefix`| String, optional| The string used as the output's prefix. A trailing "/" indicates a path. Defaults to the description.  
`fileFormat`| String, optional| The output format: "CSV" (default), "GeoJSON", "KML", "KMZ", "SHP", or "TFRecord".  
`selectors`| List, optional| A list of properties to include in the export; either a single string with comma-separated names or a list of strings.  
`maxVertices`| Number, optional| Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
Was this helpful?
