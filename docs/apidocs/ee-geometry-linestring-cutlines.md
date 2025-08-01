 
#  ee.Geometry.LineString.cutLines
Stay organized with collections  Save and categorize content based on your preferences. 
Converts LineString, MultiLineString, and LinearRing geometries into a MultiLineString by cutting them into parts no longer than the given distance along their length. All other geometry types will be converted to an empty MultiLineString. Usage | Returns  
---|---  
`LineString.cutLines(distances, _maxError_, _proj_)`|  Geometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | Cuts the lines of this geometry.  
`distances` | List | Distances along each LineString to cut the line into separate pieces, measured in units of the given proj, or meters if proj is unspecified.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | Projection of the result and distance measurements, or EPSG:4326 if unspecified.  
## Examples
### Code Editor (JavaScript)
```
// Define a LineString object.
varlineString=ee.Geometry.LineString([[-122.09,37.42],[-122.08,37.43]]);

// Apply the cutLines method to the LineString object.
varlineStringCutLines=lineString.cutLines({'distances':[10,100],'maxError':1});

// Print the result to the console.
print('lineString.cutLines(...) =',lineStringCutLines);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(lineString,
{'color':'black'},
'Geometry [black]: lineString');
Map.addLayer(lineStringCutLines,
{'color':'red'},
'Result [red]: lineString.cutLines');
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

# Apply the cutLines method to the LineString object.
linestring_cut_lines = linestring.cutLines(distances=[10, 100], maxError=1)

# Print the result.
display('linestring.cutLines(...) =', linestring_cut_lines)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(linestring, {'color': 'black'}, 'Geometry [black]: linestring')
m.add_layer(
    linestring_cut_lines, {'color': 'red'}, 'Result [red]: linestring.cutLines'
)
m
```

