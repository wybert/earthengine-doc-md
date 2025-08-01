 
#  ee.Geometry.BBox.area
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the area of the geometry. Area of points and line strings is 0 and the area of multi geometries is the sum of the areas of their components (intersecting areas are counted multiple times). Usage | Returns  
---|---  
`BBox.area(_maxError_, _proj_)`|  Float  
Argument | Type | Details  
---|---|---  
this: `geometry` | Geometry | The geometry input.  
`maxError` | ErrorMargin, default: null | The maximum amount of error tolerated when performing any necessary reprojection.  
`proj` | Projection, default: null | If specified, the result will be in the units of the coordinate system of this projection. Otherwise it will be in square meters.  
## Examples
### Code Editor (JavaScript)
```
// Define a BBox object.
varbBox=ee.Geometry.BBox(-122.09,37.42,-122.08,37.43);

// Apply the area method to the BBox object.
varbBoxArea=bBox.area({'maxError':1});

// Print the result to the console.
print('bBox.area(...) =',bBoxArea);

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

# Apply the area method to the BBox object.
bbox_area = bbox.area(maxError=1)

# Print the result.
display('bbox.area(...) =', bbox_area)

# Display relevant geometries on the map.
m = geemap.Map()
m.set_center(-122.085, 37.422, 15)
m.add_layer(bbox, {'color': 'black'}, 'Geometry [black]: bbox')
m
```

