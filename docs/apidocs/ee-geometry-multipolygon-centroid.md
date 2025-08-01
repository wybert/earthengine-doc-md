 
#  ee.Geometry.MultiPolygon.centroid
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-centroid#examples)


Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons.
Usage | Returns  
---|---  
`MultiPolygon.centroid(_maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Calculates the centroid of this geometry.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-centroid#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-centroid#colab-python-sample) More
```
// Define a MultiPolygon object.
varmultiPolygon=ee.Geometry.MultiPolygon(
[[[[-122.092,37.424],
[-122.086,37.418],
[-122.079,37.425],
[-122.085,37.423]]],
[[[-122.081,37.417],
[-122.086,37.421],
[-122.089,37.416]]]]);

// Apply the centroid method to the MultiPolygon object.
varmultiPolygonCentroid=multiPolygon.centroid({'maxError':1});

// Print the result to the console.
print('multiPolygon.centroid(...) =',multiPolygonCentroid);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPolygon,
{'color':'black'},
'Geometry [black]: multiPolygon');
Map.addLayer(multiPolygonCentroid,
{'color':'red'},
'Result [red]: multiPolygon.centroid');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a MultiPolygon object.
multipolygon = ee.Geometry.MultiPolygon([
    [[
        [-122.092, 37.424],
        [-122.086, 37.418],
        [-122.079, 37.425],
        [-122.085, 37.423],
    ]],
    [[[-122.081, 37.417], [-122.086, 37.421], [-122.089, 37.416]]],
])

# Apply the centroid method to the MultiPolygon object.
multipolygon_centroid = multipolygon.centroid(maxError=1)

# Print the result.
display('multipolygon.centroid(...) =', multipolygon_centroid)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
    multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m.add_layer(
    multipolygon_centroid,
    {'color': 'red'},
    'Result [red]: multipolygon.centroid',
)
m
```

Was this helpful?
