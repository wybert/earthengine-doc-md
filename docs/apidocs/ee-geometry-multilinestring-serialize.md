 
#  ee.Geometry.MultiLineString.serialize
Stay organized with collections  Save and categorize content based on your preferences. 
Usage | Returns  
---|---  
`MultiLineString.serialize(_legacy_)`|  String  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The Geometry instance.  
`legacy` | Boolean, optional | Enables legacy format.  
## Examples
### Code Editor (JavaScript)
```
// Define a MultiLineString object.
varmultiLineString=ee.Geometry.MultiLineString(
[[[-122.088,37.418],[-122.086,37.422],[-122.082,37.418]],
[[-122.087,37.416],[-122.083,37.416],[-122.082,37.419]]]);

// Apply the serialize method to the MultiLineString object.
varmultiLineStringSerialize=multiLineString.serialize();

// Print the result to the console.
print('multiLineString.serialize(...) =',multiLineStringSerialize);

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

# Apply the serialize method to the MultiLineString object.
multilinestring_serialize = multilinestring.serialize()

# Print the result.
display('multilinestring.serialize(...) =', multilinestring_serialize)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(
    multilinestring, {'color': 'black'}, 'Geometry [black]: multilinestring'
)
m
```

