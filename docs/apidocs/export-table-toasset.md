 
#  Export.table.toAsset
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a batch task to export a feature collection to an Earth Engine table asset. Tasks can be started from the Tasks tab. 
Usage| Returns  
---|---  
`Export.table.toAsset(collection,  _description_, _assetId_, _maxVertices_, _priority_)`|   
Argument|  Type| Details  
---|---|---  
`collection`| FeatureCollection| The feature collection to export.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportTableTask".  
`assetId`| String, optional| The destination asset ID.  
`maxVertices`| Number, optional| Max number of uncut vertices per geometry; geometries with more vertices will be cut into pieces smaller than this size.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
Was this helpful?
