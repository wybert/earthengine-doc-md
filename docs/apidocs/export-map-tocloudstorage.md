 
#  Export.map.toCloudStorage 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Creates a batch task to export an Image as a rectangular pyramid of map tiles for use with web map viewers. The map tiles will be accompanied by a reference index.html file that displays them using the Google Maps API, and an earth.html file for opening the map on Google Earth. 
Usage| Returns  
---|---  
`Export.map.toCloudStorage(image,  _description_, _bucket_, _fileFormat_, _path_, _writePublicTiles_, _maxZoom_, _scale_, _minZoom_, _region_, _skipEmptyTiles_, _mapsApiKey_, _bucketCorsUris_, _priority_)`  
Argument|  Type| Details  
---|---|---  
`image`| Image| The image to export as tiles.  
`description`| String, optional| A human-readable name of the task. Defaults to "myExportMapTask".  
`bucket`| String, optional| The destination bucket to write to.  
`fileFormat`| String, optional| The map tiles' file format, one of "auto", "png", or "jpg". Defaults to "auto", which means that opaque tiles will be encoded as "jpg" and tiles with transparency will be encoded as "png".  
`path`| String, optional| The string used as the output's path. A trailing "/" is optional. Defaults to the task's description.  
`writePublicTiles`| Boolean, optional| Whether to write public tiles instead of using the bucket's default object ACL. Defaults to true and requires invoker to be OWNER of bucket.  
`maxZoom`| Number, optional| The maximum zoom level of the map tiles to export.  
`scale`| Number, optional| The max image resolution in meters per pixel, as an alternative to "maxZoom". The scale will be converted to the most appropriate maximum zoom level at the equator.  
`minZoom`| Number, optional| The optional minimum zoom level of the map tiles to export. Defaults to zero.  
`region`| Geometry.LinearRing|Geometry.Polygon|String, optional| A LinearRing, Polygon, or coordinates representing region to export. These may be specified as the Geometry objects or coordinates serialized as a string. Map tiles will be produced in the rectangular region containing this geometry.  
`skipEmptyTiles`| Boolean, optional| If true, skip writing empty (i.e. fully-transparent) map tiles. Defaults to false. Only supported on GeoTIFF exports.  
`mapsApiKey`| String, optional| Used in index.html to initialize the Google Maps API. This removes the "development purposes only" message from the map.  
`bucketCorsUris`| List, optional| A list of domains (e.g. https://code.earthengine.google.com) that are allowed to retrieve the exported tiles from JavaScript. Setting the tiles to public is not enough to allow them to be accessible by a web page, so you must explicitly give domains access to the bucket. This is known as Cross-Origin-Resource-Sharing, or CORS. You can allow all domains to have access using "*", but this is generally discouraged. See https://cloud.google.com/storage/docs/cross-origin for more details.  
`priority`| Number, optional| The priority of the task within the project. Higher priority tasks are scheduled sooner. Must be an integer between 0 and 9999. Defaults to 100.  
Was this helpful?
