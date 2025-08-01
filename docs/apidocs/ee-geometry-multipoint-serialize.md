 
#  ee.Geometry.MultiPoint.serialize
Stay organized with collections  Save and categorize content based on your preferences. 
Usage | Returns  
---|---  
`MultiPoint.serialize(_legacy_)`|  String  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The Geometry instance.  
`legacy` | Boolean, optional | Enables legacy format.  
## Examples
### Code Editor (JavaScript)
```
// Define a MultiPoint object.
varmultiPoint=ee.Geometry.MultiPoint([[-122.082,37.420],[-122.081,37.426]]);

// Apply the serialize method to the MultiPoint object.
varmultiPointSerialize=multiPoint.serialize();

// Print the result to the console.
print('multiPoint.serialize(...) =',multiPointSerialize);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(multiPoint,
{'color':'black'},
'Geometry [black]: multiPoint');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a MultiPoint object.
multipoint = ee.Geometry.MultiPoint([[-122.082, 37.420], [-122.081, 37.426]])

# Apply the serialize method to the MultiPoint object.
multipoint_serialize = multipoint.serialize()

# Print the result.
display('multipoint.serialize(...) =', multipoint_serialize)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(multipoint, {'color': 'black'}, 'Geometry [black]: multipoint')
m
```

