 
#  ee.Geometry.Polygon.dissolve
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries. Usage | Returns  
---|---  
`Polygon.dissolve(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The geometry to union.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
### Code Editor (JavaScript)
```
// Define a Polygon object.
varpolygon=ee.Geometry.Polygon(
[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]]);

// Apply the dissolve method to the Polygon object.
varpolygonDissolve=polygon.dissolve({'maxError':1});

// Print the result to the console.
print('polygon.dissolve(...) =',polygonDissolve);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(polygon,
{'color':'black'},
'Geometry [black]: polygon');
Map.addLayer(polygonDissolve,
{'color':'red'},
'Result [red]: polygon.dissolve');
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

# Apply the dissolve method to the Polygon object.
polygon_dissolve = polygon.dissolve(maxError=1)

# Print the result.
display('polygon.dissolve(...) =', polygon_dissolve)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(polygon, {'color': 'black'}, 'Geometry [black]: polygon')
m.add_layer(
    polygon_dissolve, {'color': 'red'}, 'Result [red]: polygon.dissolve'
)
m
```

