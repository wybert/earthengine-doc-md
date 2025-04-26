 
#  ee.Geometry.LinearRing.geometries 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-geometries#examples)


Returns the list of geometries in a GeometryCollection, or a singleton list of the geometry for single geometries. 
Usage| Returns  
---|---  
`LinearRing.geometries()`| List  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry|   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-geometries#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-geometries#colab-python-sample) More
```
// Define a LinearRing object.
varlinearRing=ee.Geometry.LinearRing(
[[-122.091,37.420],
[-122.085,37.422],
[-122.080,37.430]]);
// Apply the geometries method to the LinearRing object.
varlinearRingGeometries=linearRing.geometries();
// Print the result to the console.
print('linearRing.geometries(...) =',linearRingGeometries);
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
# Apply the geometries method to the LinearRing object.
linearring_geometries = linearring.geometries()
# Print the result.
display('linearring.geometries(...) =', linearring_geometries)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linearring, {'color': 'black'}, 'Geometry [black]: linearring')
m
```

