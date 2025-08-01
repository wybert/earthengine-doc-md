 
#  ee.Geometry.Polygon.serialize
Stay organized with collections  Save and categorize content based on your preferences. 
Usage | Returns  
---|---  
`Polygon.serialize(_legacy_)`|  String  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The Geometry instance.  
`legacy` | Boolean, optional | Enables legacy format.  
## Examples
### Code Editor (JavaScript)
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);

// Apply the serialize method to the Polygon object.
varpolygonSerialize=polygon.serialize();

// Print the result to the console.
print('polygon.serialize(...) =',polygonSerialize);

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

# Apply the serialize method to the Polygon object.
polygon_serialize = polygon.serialize()

# Print the result.
display('polygon.serialize(...) =', polygon_serialize)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m
```

