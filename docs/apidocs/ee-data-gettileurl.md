 
#  ee.data.getTileUrl 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Generate a URL for map tiles from a Map ID and coordinates. If formatTileUrl is not present, we generate it by using or guessing the urlFormat string, and add urlFormat and formatTileUrl to `id` for future use. 
Returns the tile URL.
Usage| Returns  
---|---  
`ee.data.getTileUrl(id, x, y, z)`| String  
Argument| Type| Details  
---|---|---  
`id`| RawMapId| The Map ID to generate tiles for.  
`x`| Number| The tile x coordinate.  
`y`| Number| The tile y coordinate.  
`z`| Number| The tile zoom level.  
