 
#  ee.Geometry.MultiLineString.area 
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times). Usage| Returns  
---|---  
`MultiLineString.area( _maxError_, _proj_)`| Float  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| The geometry input.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters.  
## Examples
### Code Editor (JavaScript)
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);
// Apply the area method to the MultiLineString object.
varmultiLineStringArea=multiLineString.area({'maxError':1});
// Print the result to the console.
print('multiLineString.area(...) =',multiLineStringArea);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a MultiLineString object.
multilinestring = ee.Geometry.MultiLineString([
  [[-122.088, 37.418], [-122.086, 37.422], [-122.082, 37.418]],
  [[-122.087, 37.416], [-122.083, 37.416], [-122.082, 37.419]],
])
# Apply the area method to the MultiLineString object.
multilinestring_area = multilinestring.area(maxError=1)
# Print the result.
display('multilinestring.area(...) =', multilinestring_area)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m
```

