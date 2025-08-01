 
#  ee.Geometry.BBox.dissolve
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries. Usage | Returns  
---|---  
`BBox.dissolve(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The geometry to union.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
### Code Editor (JavaScript)
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);

// Apply the dissolve method to the BBox object.
varbBoxDissolve=bBox.dissolve({'maxError':1});

// Print the result to the console.
print('bBox.dissolve(...) =',bBoxDissolve);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(bBox,
{'color':'black'},
'Geometry [black]: bBox');
Map.addLayer(bBoxDissolve,
{'color':'red'},
'Result [red]: bBox.dissolve');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a BBox object.
bbox = ee.Geometry.BBox(-122.09, 37.42, -122.08, 37.43)

# Apply the dissolve method to the BBox object.
bbox_dissolve = bbox.dissolve(maxError=1)

# Print the result.
display('bbox.dissolve(...) =', bbox_dissolve)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m.add_layer(bbox_dissolve, {'color': 'red'}, 'Result [red]: bbox.dissolve')
m
```

