 
#  Map.getZoom 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/map-getzoom#examples)


Returns the current zoom level of the map. 
Usage| Returns  
---|---  
`Map.getZoom()`| Number  
**No arguments.**
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/map-getzoom#code-editor-javascript-sample) More
```
// The default map in the Code Editor is a built-in ui.Map object called "Map".
// Let's refer to it as "defaultMap" for clarity.
vardefaultMap=Map;
// ui.Map objects can be constructed. Here, a new map is declared.
varnewMap=ui.Map({
center:{lat:0,lon:0,zoom:1},
style:{position:'bottom-right',width:'400px'}
});
// Add the newMap to the defaultMap.
defaultMap.add(newMap);
// You can set the viewport of a ui.Map to be centered on an object.
// Here, the defaultMap is centered on a point with a selected zoom level.
vargeom=ee.Geometry.Point(-122.0841,37.4223);
defaultMap.centerObject(geom,18);
defaultMap.addLayer(geom,{color:'orange'},'Googleplex');
// Map extent can be fetched using the ui.Map.getBounds method.
print('defaultMap bounds as a list',
defaultMap.getBounds());
print('defaultMap bounds as a dictionary',
ee.Dictionary.fromLists(['w','s','e','n'],defaultMap.getBounds()));
print('defaultMap bounds as GeoJSON',
defaultMap.getBounds({asGeoJSON:true}));
// Map center point can be fetched using the ui.Map.getCenter method.
print('defaultMap center as a Point geometry',defaultMap.getCenter());
// Map zoom level can be fetched using the ui.Map.getZoom method.
print('defaultMap zoom level',defaultMap.getZoom());
// Map scale can be fetched using the ui.Map.getScale method.
print('defaultMap approximate pixel scale',defaultMap.getScale());
```

Was this helpful?
