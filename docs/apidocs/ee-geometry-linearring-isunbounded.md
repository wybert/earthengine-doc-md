 
#  ee.Geometry.LinearRing.isUnbounded 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-isunbounded#examples)


Returns whether the geometry is unbounded. 
Usage| Returns  
---|---  
`LinearRing.isUnbounded()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-isunbounded#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-isunbounded#colab-python-sample) More
```
// Define a LinearRing object.
varlinearRing=ee.Geometry.LinearRing(
[[-122.091,37.420],
[-122.085,37.422],
[-122.080,37.430]]);
// Apply the isUnbounded method to the LinearRing object.
varlinearRingIsUnbounded=linearRing.isUnbounded();
// Print the result to the console.
print('linearRing.isUnbounded(...) =',linearRingIsUnbounded);
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
```
# Define a LinearRing object.
linearring = ee.Geometry.LinearRing(
  [[-122.091, 37.420], [-122.085, 37.422], [-122.080, 37.430]]
)
# Apply the isUnbounded method to the LinearRing object.
linearring_is_unbounded = linearring.isUnbounded()
# Print the result.
display('linearring.isUnbounded(...) =', linearring_is_unbounded)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linearring, {'color': 'black'}, 'Geometry [black]: linearring')
m
```

Was this helpful?
