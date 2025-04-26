 
#  ee.Geometry.LinearRing.dissolve 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the union of the geometry. This leaves single geometries untouched, and unions multi geometries. Usage| Returns  
---|---  
`LinearRing.dissolve( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry to union.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the union will be performed in this projection. Otherwise it will be performed in a spherical coordinate system.  
## Examples
### Code Editor (JavaScript)
```
// Define a LinearRing object.
varlinearRing=ee.Geometry.LinearRing(
[[-122.091,37.420],
[-122.085,37.422],
[-122.080,37.430]]);
// Apply the dissolve method to the LinearRing object.
varlinearRingDissolve=linearRing.dissolve({'maxError':1});
// Print the result to the console.
print('linearRing.dissolve(...) =',linearRingDissolve);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(linearRing,
{'color':'black'},
'Geometry [black]: linearRing');
Map.addLayer(linearRingDissolve,
{'color':'red'},
'Result [red]: linearRing.dissolve');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a LinearRing object.
linearring = ee.Geometry.LinearRing(
  [[-122.091, 37.420], [-122.085, 37.422], [-122.080, 37.430]]
)
# Apply the dissolve method to the LinearRing object.
linearring_dissolve = linearring.dissolve(maxError=1)
# Print the result.
display('linearring.dissolve(...) =', linearring_dissolve)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linearring, {'color': 'black'}, 'Geometry [black]: linearring')
m.add_layer(
  linearring_dissolve, {'color': 'red'}, 'Result [red]: linearring.dissolve'
)
m
```

