 
#  ee.Geometry.MultiPolygon.area 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-area#examples)


Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times). 
Usage| Returns  
---|---  
`MultiPolygon.area( _maxError_, _proj_)`| Float  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry input.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-area#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-multipolygon-area#colab-python-sample) More
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
// Apply the area method to the MultiPolygon object.
varmultiPolygonArea=multiPolygon.area({'maxError':1});
// Print the result to the console.
print('multiPolygon.area(...) =',multiPolygonArea);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPolygon,
{'color':'black'},
'Geometry [black]: multiPolygon');
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
# Apply the area method to the MultiPolygon object.
multipolygon_area = multipolygon.area(maxError=1)
# Print the result.
display('multipolygon.area(...) =', multipolygon_area)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multipolygon, {'color': 'black'}, 'Geometry [black]: multipolygon'
)
m
```

Was this helpful?
