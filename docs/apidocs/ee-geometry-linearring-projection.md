 
#  ee.Geometry.LinearRing.projection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Returns the projection of the geometry. 
Usage| Returns  
---|---  
`LinearRing.projection()`| Projection  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
### Code Editor (JavaScript)
```
// Define a LinearRing object.
varlinearRing=ee.Geometry.LinearRing(
[[-122.091,37.420],
[-122.085,37.422],
[-122.080,37.430]]);
// Apply the projection method to the LinearRing object.
varlinearRingProjection=linearRing.projection();
// Print the result to the console.
print('linearRing.projection(...) =',linearRingProjection);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(linearRing,
{'color':'black'},
'Geometry [black]: linearRing');
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
# Apply the projection method to the LinearRing object.
linearring_projection = linearring.projection()
# Print the result.
display('linearring.projection(...) =', linearring_projection)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linearring, {'color': 'black'}, 'Geometry [black]: linearring')
m
```

