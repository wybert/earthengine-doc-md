 
#  ee.Geometry.MultiPoint.edgesAreGeodesics
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-edgesaregeodesics#examples)


Returns true if the geometry edges, if any, are geodesics along a spherical model of the earth; if false, any edges are straight lines in the projection.
Usage | Returns  
---|---  
`MultiPoint.edgesAreGeodesics()` | Boolean  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry |   
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-edgesaregeodesics#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipoint-edgesaregeodesics#colab-python-sample) More
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);

// Apply the edgesAreGeodesics method to the MultiPoint object.
varmultiPointEdgesAreGeodesics=multiPoint.edgesAreGeodesics();

// Print the result to the console.
print('multiPoint.edgesAreGeodesics(...) =',multiPointEdgesAreGeodesics);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPoint,
{'color':'black'},
'Geometry [black]: multiPoint');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a MultiPoint object.
multipoint = ee.Geometry.MultiPoint([[-122.082, 37.420], [-122.081, 37.426]])

# Apply the edgesAreGeodesics method to the MultiPoint object.
multipoint_edges_are_geodesics = multipoint.edgesAreGeodesics()

# Print the result.
display('multipoint.edgesAreGeodesics(...) =', multipoint_edges_are_geodesics)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m
```

Was this helpful?
