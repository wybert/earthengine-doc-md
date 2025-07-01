 
#  Export.video.toDrive
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a batch task to export an ImageCollection as a video to Drive. The collection must only contain RGB images. Tasks can be started from the Tasks tab. "crsTransform", "scale", and "dimensions" are mutually exclusive. 
Usage| Returns  
---|---  
`Export.video.toDrive(collection,  _description_, _folder_, _fileNamePrefix_, _framesPerSecond_, _dimensions_, _region_, _scale_, _crs_, _crsTransform_, _maxPixels_, _maxFrames_, _priority_)`|   
Argument|  Type| Details  
---|---|---  
`collection`| ImageCollection| The image collection to export.  
`description`| String, optional| A human-readable name of the task. May contain letters, numbers, -, _ (no spaces). Defaults to "myExportVideoTask".  
`folder`| String, optional| The Google Drive Folder that the export will reside in. Note: (a) if the folder name exists at any level, the output is written to it, (b) if duplicate folder names exist, output is written to the most recently modified folder, (c) if the folder name does not exist, a new folder will be created at the root, and (d) folder names with separators (e.g. 'path/to/file') are interpreted as literal strings, not system paths. Defaults to Drive root.  
`fileNamePrefix`| String, optional| The filename prefix. May contain letters, numbers, -, _ (no spaces). Defaults to the description.  
`framesPerSecond`| Number, optional| The framerate of the exported video. Must be a value between 0.1 and 100. Defaults to 1.  
`dimensions`| Number|String, optional| The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers.  
`region`| Geometry.LinearRing|Geometry.Polygon|String, optional| A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string.  
`scale`| Number, optional| Resolution in meters per pixel.  
`crs`| String, optional| CRS to use for the exported image. Defaults to the Google Maps Mercator projection, SR-ORG:6627.  
`crsTransform`| String, optional| Affine transform to use for the exported image. Requires "crs" to be defined.  
`maxPixels`| Number, optional| Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit.  
`maxFrames`| Number, optional| Set the maximum number of frames to export. By default, a maximum of 1000 frames may be exported. By setting this explicitly, you may raise or lower this limit.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
Was this helpful?
