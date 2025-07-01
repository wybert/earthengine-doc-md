 
#  ee.Geometry.LineString.centroid
Stay organized with collections  Save and categorize content based on your preferences. 
Returns a point at the center of the highest-dimension components of the geometry. Lower-dimensional components are ignored, so the centroid of a geometry containing two polygons, three lines and a point is equivalent to the centroid of a geometry containing just the two polygons. Usage| Returns  
---|---  
`LineString.centroid( _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Calculates the centroid of this geometry.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in EPSG:4326.  
## Examples
### Code Editor (JavaScript)
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);
// Apply the centroid method to the LineString object.
varlineStringCentroid=lineString.centroid({'maxError':1});
// Print the result to the console.
print('lineString.centroid(...) =',lineStringCentroid);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
Map.addLayer(lineStringCentroid,
{'color':'red'},
'Result [red]: lineString.centroid');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a LineString object.
linestring = ee.Geometry.LineString([[-122.09, 37.42], [-122.08, 37.43]])
# Apply the centroid method to the LineString object.
linestring_centroid = linestring.centroid(maxError=1)
# Print the result.
display('linestring.centroid(...) =', linestring_centroid)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m.add_layer(
  linestring_centroid, {'color': 'red'}, 'Result [red]: linestring.centroid'
)
m
```

