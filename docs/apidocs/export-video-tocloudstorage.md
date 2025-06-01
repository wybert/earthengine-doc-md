 
#  Export.video.toCloudStorage 
Stay organized with collections  Save and categorize content based on your preferences. 
Creates a batch task to export an ImageCollection as a video to Google Cloud Storage. The collection must only contain RGB images. Tasks can be started from the Tasks tab. "crsTransform", "scale", and "dimensions" are mutually exclusive. Usage| Returns  
---|---  
`Export.video.toCloudStorage(collection,  _description_, _bucket_, _fileNamePrefix_, _framesPerSecond_, _dimensions_, _region_, _scale_, _crs_, _crsTransform_, _maxPixels_, _maxFrames_, _priority_)`|   
Argument|  Type| Details  
---|---|---  
`collection`| ImageCollection| The image collection to export.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportVideoTask".  
`bucket`| String, optional| The Cloud Storage destination bucket.  
`fileNamePrefix`| String, optional| The string used as the output's prefix. A trailing "/" indicates a path. Defaults to the description.  
`framesPerSecond`| Number, optional| The framerate of the exported video. Must be a value between 0.1 and 100. Defaults to 1.  
`dimensions`| Number|String, optional| The dimensions to use for the exported image. Takes either a single positive integer as the maximum dimension or "WIDTHxHEIGHT" where WIDTH and HEIGHT are each positive integers.  
`region`| Geometry.LinearRing|Geometry.Polygon|String, optional| A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string.  
`scale`| Number, optional| Resolution in meters per pixel.  
`crs`| String, optional| CRS to use for the exported image. Defaults to the Google Maps Mercator projection, SR-ORG:6627.  
`crsTransform`| String, optional| Affine transform to use for the exported image. Requires "crs" to be defined.  
`maxPixels`| Number, optional| Restrict the number of pixels in the export. By default, you will see an error if the export exceeds 1e8 pixels. Setting this value explicitly allows one to raise or lower this limit.  
`maxFrames`| Number, optional| Set the maximum number of frames to export. By default, a maximum of 1000 frames may be exported. By setting this explicitly, you may raise or lower this limit.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
