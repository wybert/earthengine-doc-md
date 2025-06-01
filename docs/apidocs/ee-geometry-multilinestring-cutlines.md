 
#  ee.Geometry.MultiLineString.cutLines 
Stay organized with collections  Save and categorize content based on your preferences. 
Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString. Usage| Returns  
---|---  
`MultiLineString.cutLines(distances,  _maxError_, _proj_)`| Geometry  
Argument| Type| Details  
---|---|---  
this: `geometry`| Geometry| Cuts the lines of this geometry.  
`distances`| List| Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified.  
`maxError`| ErrorMargin, default: null| The maximum amount of error tolerated when performing any necessary reprojection.  
`proj`| Projection, default: null| Projection of the result and distance measurements, or EPSG:4326 if unspecified.  
## Examples
### Code Editor (JavaScript)
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);
// Apply the cutLines method to the MultiLineString object.
varmultiLineStringCutLines=multiLineString.cutLines({'distances':[10,100],'maxError':1});
// Print the result to the console.
print('multiLineString.cutLines(...) =',multiLineStringCutLines);
// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiLineString,
{'color':'black'},
'Geometry [black]: multiLineString');
Map.addLayer(multiLineStringCutLines,
{'color':'red'},
'Result [red]: multiLineString.cutLines');
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
# Apply the cutLines method to the MultiLineString object.
multilinestring_cut_lines = multilinestring.cutLines(
  distances=[10, 100], maxError=1
)
# Print the result.
display('multilinestring.cutLines(...) =', multilinestring_cut_lines)
# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
  multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m.add_layer(
  multilinestring_cut_lines,
  {'color': 'red'},
  'Result [red]: multilinestring.cutLines',
)
m
```

