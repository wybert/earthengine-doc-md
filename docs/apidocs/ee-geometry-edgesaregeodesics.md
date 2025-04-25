 
#  ee.Geometry.edgesAreGeodesics 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-edgesaregeodesics#examples)


Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection. 
Usage| Returns  
---|---  
`Geometry.edgesAreGeodesics()`| Boolean  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-edgesaregeodesics#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-edgesaregeodesics#colab-python-sample) More
```
// Define a Geometry object.
vargeometry=ee.Geometry({
'type':'Polygon',
'coordinates':
[[[-122.081,37.417],
[-122.086,37.421],
[-122.084,37.418],
[-122.089,37.416]]]
});
// Apply the edgesAreGeodesics method to the Geometry object.
vargeometryEdgesAreGeodesics=geometry.edgesAreGeodesics();
// Print the result to the console.
print('geometry.edgesAreGeodesics(...) =',geometryEdgesAreGeodesics);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a Geometry object.
geometry = ee.Geometry({
  'type': 'Polygon',
  'coordinates': [[
    [-122.081, 37.417],
    [-122.086, 37.421],
    [-122.084, 37.418],
    [-122.089, 37.416],
  ]],
})
# Apply the edgesAreGeodesics method to the Geometry object.
geometry_edges_are_geodesics = geometry.edgesAreGeodesics()
# Print the result.
display('geometry.edgesAreGeodesics(...) =', geometry_edges_are_geodesics)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m
```

Was this helpful?
