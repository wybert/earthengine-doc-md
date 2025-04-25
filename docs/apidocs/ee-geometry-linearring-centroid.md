 
#  ee.Geometry.LinearRing.centroid 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-centroid#examples)


Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons. 
Usage| Returns  
---|---  
`LinearRing.centroid( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Calculates the centroid of this geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-centroid#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linearring-centroid#colab-python-sample) More
```
// Define a LinearRing object.
varlinearRing=ee.Geometry.LinearRing(
[[-122.091,37.420],
[-122.085,37.422],
[-122.080,37.430]]);
// Apply the centroid method to the LinearRing object.
varlinearRingCentroid=linearRing.centroid({'maxError':1});
// Print the result to the console.
print('linearRing.centroid(...) =',linearRingCentroid);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(linearRing,
{'color':'black'},
'Geometry [black]: linearRing');
Map.addLayer(linearRingCentroid,
{'color':'red'},
'Result [red]: linearRing.centroid');
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
# Apply the centroid method to the LinearRing object.
linearring_centroid = linearring.centroid(maxError=1)
# Print the result.
display('linearring.centroid(...) =', linearring_centroid)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linearring, {'color': 'black'}, 'Geometry [black]: linearring')
m.add_layer(
  linearring_centroid, {'color': 'red'}, 'Result [red]: linearring.centroid'
)
m
```

