 
#  ee.Geometry.LineString.area
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-area#examples)


Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times).
Usage | Returns  
---|---  
`LineString.area(_maxError_, _proj_)`|  Float  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The geometry input.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-area#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-geometry-linestring-area#colab-python-sample) More
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);

// Apply the area method to the LineString object.
varlineStringArea=lineString.area({'maxError':1});

// Print the result to the console.
print('lineString.area(...) =',lineStringArea);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
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

# Apply the area method to the LineString object.
linestring_area = linestring.area(maxError=1)

# Print the result.
display('linestring.area(...) =', linestring_area)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m
```

Was this helpful?
