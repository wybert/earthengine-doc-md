 
#  Map.setZoom 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/map-setzoom#examples)


Sets the zoom level of the map. 
Returns this ui.Map.
Usage| Returns  
---|---  
`Map.setZoom(zoom)`| ui.Map  
Argument| Type| Details  
---|---|---  
`zoom`| Number| The zoom level, from 0 to 24, to set for the map.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/map-setzoom#code-editor-javascript-sample) More
```
// See the entire world.
Map.setZoom(1);
// See the smallest region possible.
Map.setZoom(24);
// The most recent zoom is the one the view will have.
Map.setZoom(12);
```

