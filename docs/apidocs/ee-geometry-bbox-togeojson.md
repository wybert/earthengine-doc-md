 
#  ee.Geometry.BBox.toGeoJSON
Stay organized with collections  Save and categorize content based on your preferences. 
Usage | Returns  
---|---  
`BBox.toGeoJSON()` | GeoJSONGeometry  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The Geometry instance.  
## Examples
### Code Editor (JavaScript)
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);

// Apply the toGeoJSON method to the BBox object.
varbBoxToGeoJSON=bBox.toGeoJSON();

// Print the result to the console.
print('bBox.toGeoJSON(...) =',bBoxToGeoJSON);

// Display relevant geometries on the map.
Map.setCenter(-122.085,37.422,15);
Map.addLayer(bBox,
{'color':'black'},
'Geometry [black]: bBox');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define a BBox object.
bbox = ee.Geometry.BBox(-122.09, 37.42, -122.08, 37.43)

# Apply the toGeoJSON method to the BBox object.
bbox_to_geojson = bbox.toGeoJSON()

# Print the result.
display('bbox.toGeoJSON(...) =', bbox_to_geojson)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m
```

