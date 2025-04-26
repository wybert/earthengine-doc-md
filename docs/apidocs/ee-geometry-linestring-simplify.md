 
#  ee.Geometry.LineString.simplify 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-simplify#examples)


Simplifies the geometry to within a given error margin. Note that this does not respect the error margin requested by the consumer of this algorithm, unless maxError is explicitly specified to be null. 
This overrides the default Earth Engine policy for propagating error margins, so regardless of the geometry accuracy requested from the output, the inputs will be requested with the error margin specified in the arguments to this algorithm. This results in consistent rendering at all zoom levels of a rendered vector map, but at lower zoom levels (i.e. zoomed out), the geometry won't be simplified, which may harm performance.
Usage| Returns  
---|---  
`LineString.simplify(maxError,  _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry to simplify.  
`maxError`| ErrorMargin| The maximum amount of error by which the result may differ from the input.  
`proj`| Projection, default: null| If specified, the result will be in this projection. Otherwise it will be in the same projection as the input. If the error margin is in projected units, the margin will be interpreted as units of this projection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-simplify#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-simplify#colab-python-sample) More
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);
// Apply the simplify method to the LineString object.
varlineStringSimplify=lineString.simplify({'maxError':1});
// Print the result to the console.
print('lineString.simplify(...) =',lineStringSimplify);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
Map.addLayer(lineStringSimplify,
{'color':'red'},
'Result [red]: lineString.simplify');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a LineString object.
linestring = ee.Geometry.LineString([[-122.09, 37.42], [-122.08, 37.43]])
# Apply the simplify method to the LineString object.
linestring_simplify = linestring.simplify(maxError=1)
# Print the result.
display('linestring.simplify(...) =', linestring_simplify)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m.add_layer(
  linestring_simplify, {'color': 'red'}, 'Result [red]: linestring.simplify'
)
m
```

