 
#  Map.add
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/map-add#examples)


Adds an item to the map. Can also be used to add widgets like ui.Label as well as some non-widget objects like ui.Map.Layer. 
Returns the map.
Usage| Returns  
---|---  
`Map.add(item)`| ui.Map  
Argument| Type| Details  
---|---|---  
`item`| Object| The item to add.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/map-add#code-editor-javascript-sample) More
```
// The default map in the Code Editor is a built-in ui.Map object called "Map".
// Let's refer to it as "defaultMap" for clarity.
vardefaultMap=Map;
// ui.Map objects can be constructed. Here, a new map is declared.
varnewMap=ui.Map({
center:{lat:0,lon:0,zoom:1},
style:{position:'bottom-right',width:'400px'}
});
// Add the newMap to the defaultMap;
defaultMap.add(newMap);
// Other UI widgets can be added to ui.Map objects, for example labels:
defaultMap.add(ui.Label('Default Map',{position:'bottom-left'}));
newMap.add(ui.Label('New Map',{position:'bottom-left'}));
// ...selectors:
defaultMap.add(ui.Select(['This','That','Other']));
// ...or buttons:
defaultMap.add(ui.Button('Click me'));
// You can also add ui.Map.Layer objects. Here, an ee.Geometry object
// is converted to a map layer and added to the default map.
vargeom=ee.Geometry.Point(-122.0841,37.4223);
vargeomLayer=ui.Map.Layer(geom,{color:'orange'},'Googleplex');
defaultMap.add(geomLayer);
defaultMap.centerObject(geom,18);
```

Was this helpful?
