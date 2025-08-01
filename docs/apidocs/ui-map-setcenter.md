 
#  ui.Map.setCenter
Stay organized with collections  Save and categorize content based on your preferences. 
Returns this ui.Map.
Usage | Returns  
---|---  
`Map.setCenter(lon, lat, _zoom_)`|  ui.Map  
Argument | Type | Details  
---|---|---  
this: `ui.map` | ui.Map | The ui.Map instance.  
`lon` | Number | The longitude of the center, in degrees.  
`lat` | Number | The latitude of the center, in degrees.  
`zoom` | Number, optional | The zoom level, from 0 to 24.  
## Examples
### Code Editor (JavaScript)
```
// Define a ui.Map widget.
varmap=ui.Map();

// Set the position and optional zoom level of the map. Latitude must be
// within [-85, 85].
map.setCenter({lon:-123.6,lat:47.7,zoom:9});
print(map);
```

