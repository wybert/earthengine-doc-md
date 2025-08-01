 
#  ee.Geometry.MultiLineString.centroid
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-centroid#examples)


Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.
Usage | Returns  
---|---  
`MultiLineString.centroid(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Calculates the centroid of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-centroid#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multilinestring-centroid#colab-python-sample) More
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);

// Apply the centroid method to the MultiLineString object.
varmultiLineStringCentroid=multiLineString.centroid({'maxError':1});

// Print the result to the console.
print('multiLineString.centroid(...) =',multiLineStringCentroid);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
Map.addLayer(multiLineStringCentroid,
{'color':'red'},
'Result [red]: multiLineString.centroid');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a MultiLineString object.
multilinestring = ee.Geometry.MultiLineString([
    [[-122.088, 37.418], [-122.086, 37.422], [-122.082, 37.418]],
    [[-122.087, 37.416], [-122.083, 37.416], [-122.082, 37.419]],
])

# Apply the centroid method to the MultiLineString object.
multilinestring_centroid = multilinestring.centroid(maxError=1)

# Print the result.
display('multilinestring.centroid(...) =', multilinestring_centroid)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
    multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m.add_layer(
    multilinestring_centroid,
    {'color': 'red'},
    'Result [red]: multilinestring.centroid',
)
m
```

Was this helpful?
