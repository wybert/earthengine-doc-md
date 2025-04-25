 
#  ee.Geometry.cutLines 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-cutlines#examples)


Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString. 
Usage| Returns  
---|---  
`Geometry.cutLines(distances,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Cuts the lines of this geometry.  
`distances`| List| Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| Projection of the result and distance measurements, or EPSG:4326 if unspecified.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-cutlines#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-cutlines#colab-python-sample) More
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
// Apply the cutLines method to the Geometry object.
vargeometryCutLines=geometry.cutLines({'distances':[10,100],'maxError':1});
// Print the result to the console.
print('geometry.cutLines(...) =',geometryCutLines);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(geometry,
{'color':'black'},
'Geometry [black]: geometry');
Map.addLayer(geometryCutLines,
{'color':'red'},
'Result [red]: geometry.cutLines');
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
# Apply the cutLines method to the Geometry object.
geometry_cut_lines = geometry.cutLines(distances=[10, 100], maxError=1)
# Print the result.
display('geometry.cutLines(...) =', geometry_cut_lines)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(geometry, {'color': 'black'}, 'Geometry [black]: geometry')
m.add_layer(
  geometry_cut_lines, {'color': 'red'}, 'Result [red]: geometry.cutLines'
)
m
```

Was this helpful?
