 
#  ee.Geometry.LineString.toGeoJSONString
Stay organized with collections  Save and categorize content based on your preferences. 
Usage | Returns  
---|---  
`LineString.toGeoJSONString()` | String  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The Geometry instance.  
## Examples
### Code Editor (JavaScript)
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);

// Apply the toGeoJSONString method to the LineString object.
varlineStringToGeoJSONString=lineString.toGeoJSONString();

// Print the result to the console.
print('lineString.toGeoJSONString(...) =',lineStringToGeoJSONString);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a LineString object.
linestring = ee.Geometry.LineString([[-122.09, 37.42], [-122.08, 37.43]])

# Apply the toGeoJSONString method to the LineString object.
linestring_to_geojson_string = linestring.toGeoJSONString()

# Print the result.
display('linestring.toGeoJSONString(...) =', linestring_to_geojson_string)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m
```

