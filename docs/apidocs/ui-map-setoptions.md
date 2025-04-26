 
#  ui.Map.setOptions 
Stay organized with collections  Save and categorize content based on your preferences. 
Modifies the Google Maps basemap. Allows for: 1) Setting the current MapType. 2) Providing custom styles for the basemap (MapTypeStyles). 3) Setting the list of available mapTypesIds for the basemap. 
If called with no parameters, resets the map type to the Google Maps default.
Returns this ui.Map.
Usage| Returns  
---|---  
`Map.setOptions( _mapTypeId_, _styles_, _types_)`| ui.Map  
Argument| Type| Details  
---|---|---  
this: `ui.map`| ui.Map| The ui.Map instance.  
`mapTypeId`| String, optional| A mapTypeId to set the basemap to. Can be one of "ROADMAP", "SATELLITE", "HYBRID", or "TERRAIN" to select one of the standard Google Maps API map types, or one of the keys specified in the opt_styles dictionary. If left as null and only 1 style is specified in opt_styles, that style will be used.  
`styles`| Object, optional| A dictionary of custom MapTypeStyle objects keyed with a name that will appear in the map's Map Type Controls. See: https://developers.google.com/maps/documentation/javascript/reference#MapTypeStyle  
`types`| List, optional| A list of mapTypeIds to make available. If omitted, but opt_styles is specified, appends all of the style keys to the standard Google Maps API map types.  
## Examples
### Code Editor (JavaScript)
```
// Set the map to terrain with a string.
Map.setOptions('TERRAIN');
// Use a dictionary to add some typo protection.
varmapTypes={
HYBRID:'HYBRID',
ROADMAP:'ROADMAP',
SATELLITE:'SATELLITE',
TERRAIN:'TERRAIN'
};
Map.setOptions({mapTypeId:mapTypes.HYBRID});
Map.setOptions({mapTypeId:mapTypes.ROADMAP});
Map.setOptions({mapTypeId:mapTypes.SATELLITE});
Map.setOptions({mapTypeId:mapTypes.TERRAIN});
// Add a basemap that inverts the lightness to make a darker background.
Map.setOptions({
styles:
{'Inverted':[{featureType:'all',stylers:[{invert_lightness:true}]}]}
});
// Use types keyword to control map type visibility, e.g. show only 'Inverted'.
Map.setOptions({
styles:
{'Inverted':[{featureType:'all',stylers:[{invert_lightness:true}]}]},
types:['Inverted']
});
```

