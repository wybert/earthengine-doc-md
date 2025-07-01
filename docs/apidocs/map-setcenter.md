 
#  Map.setCenter
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/map-setcenter#examples)


Centers the map view at a given coordinates with the given zoom level. 
Returns the map.
Usage| Returns  
---|---  
`Map.setCenter(lon, lat,  _zoom_)`| ui.Map  
Argument| Type| Details  
---|---|---  
`lon`| Number| The longitude of the center, in degrees.  
`lat`| Number| The latitude of the center, in degrees.  
`zoom`| Number, optional| The zoom level, from 0 to 24.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/map-setcenter#code-editor-javascript-sample) More
```
// Set the position and optional zoom level of the map. Latitude must be
// within [-85, 85].
Map.setCenter(-123.6,47.7,9);
```

