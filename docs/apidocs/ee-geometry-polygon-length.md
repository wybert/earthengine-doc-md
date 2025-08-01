 
#  ee.Geometry.Polygon.length
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the length of the linear parts of the geometry. Polygonal parts are ignored. The length of multi geometries is the sum of the lengths of their components. Usage | Returns  
---|---  
`Polygon.length(_maxError_, _proj_)`|  Float  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The input geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in meters.  
## Examples
### Code Editor (JavaScript)
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);

// Apply the length method to the Polygon object.
varpolygonLength=polygon.length();

// Print the result to the console.
print('polygon.length(...) =',polygonLength);

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

# Apply the length method to the Polygon object.
polygon_length = polygon.length()

# Print the result.
display('polygon.length(...) =', polygon_length)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m
```

