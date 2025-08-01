 
#  ee.Geometry.Polygon.type
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the GeoJSON type of the geometry. Usage | Returns  
---|---  
`Polygon.type()` | String  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry |   
## Examples
### Code Editor (JavaScript)
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);

// Apply the type method to the Polygon object.
varpolygonType=polygon.type();

// Print the result to the console.
print('polygon.type(...) =',polygonType);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(polygon,
{'color':'black'},
'Geometry [black]: polygon');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a Polygon object.
polygon = ee.Geometry.Polygon([[
    [-122.092, 37.424],
    [-122.086, 37.418],
    [-122.079, 37.425],
    [-122.085, 37.423],
]])

# Apply the type method to the Polygon object.
polygon_type = polygon.type()

# Print the result.
display('polygon.type(...) =', polygon_type)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m
```

