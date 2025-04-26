 
#  Map.setOptions 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/map-setoptions#examples)


Modifies the Google Maps basemap. Allows for: 
1) Setting the current MapType. 2) Providing custom styles for the basemap (MapTypeStyles). 3) Setting the list of available mapTypesIds for the basemap.
If called with no parameters, resets the map type to the google default.
Returns the map.
Usage| Returns  
---|---  
`Map.setOptions( _mapTypeId_, _styles_, _types_)`| ui.Map  
Argument| Type| Details  
---|---|---  
`mapTypeId`| String, optional| A mapTypeId to set the basemap to. Can be one of "ROADMAP", "SATELLITE", "HYBRID" or "TERRAIN" to select one of the standard Google Maps API map types, or one of the keys specified in the opt_styles dictionary. If left as null and only 1 style is specified in opt_styles, that style will be used.  
`styles`| Object, optional| A dictionary of custom MapTypeStyle objects keyed with a name that will appear in the map's Map Type Controls. See: https://developers.google.com/maps/documentation/javascript/reference#MapTypeStyle  
`types`| List, optional| A list of mapTypeIds to make available. If omitted, but opt_styles is specified, appends all of the style keys to the standard Google Maps API map types.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/map-setoptions#code-editor-javascript-sample) More
```
// Types
Map.setOptions('HYBRID');
Map.setOptions('ROADMAP');
Map.setOptions('SATELLITE');
Map.setOptions('TERRAIN');
```

