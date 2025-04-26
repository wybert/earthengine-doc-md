 
#  ee.FeatureCollection.randomPoints 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Generates points that are uniformly random in the given geometry. If the geometry is two-dimensional (polygon or multi-polygon) then the returned points are uniformly distributed on the given region of the sphere. If the geometry is one-dimensional (linestrings), the returned points are interpolated uniformly along the geometry's edges. If the geometry has dimension zero (points), the returned points are sampled uniformly from the input points. If a multi-geometry of mixed dimension is given, points are sampled from the component geometries with the highest dimension. Usage| Returns  
---|---  
`ee.FeatureCollection.randomPoints(region,  _points_, _seed_, _maxError_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
`region`| Geometry| The region to generate points for.  
`points`| Integer, default: 1000| The number of points to generate.  
`seed`| Long, default: 0| A seed for the random number generator.  
`maxError`| ErrorMargin, optional| The maximum amount of error tolerated when performing any necessary reprojection.  
## Examples
### Code Editor (JavaScript)
```
// An ee.Geometry to constrain the geographic bounds of random points.
varregion=ee.Geometry.Rectangle(
{coords:[-113.5,40.0,-110.2,41.9],geodesic:false});
// Generate 50 random points with the region.
varrandomPoints=ee.FeatureCollection.randomPoints(
{region:region,points:50,seed:0,maxError:1});
print('Random points from within the defined region',randomPoints);
Map.setCenter(-111.802,40.979,7);
Map.addLayer(region,{color:'yellow'},'Region');
Map.addLayer(randomPoints,{color:'black'},'Random points');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# An ee.Geometry to constrain the geographic bounds of random points.
region = ee.Geometry.Rectangle(
  coords=[-113.5, 40.0, -110.2, 41.9], proj='EPSG:4326', geodesic=False
)
# Generate 50 random points with the region.
random_points = ee.FeatureCollection.randomPoints(
  region=region, points=50, seed=0, maxError=1
)
display('Random points from within the defined region', random_points)
m = geemap.Map()
m.set_center(-111.802, 40.979, 7)
m.add_layer(region, {'color': 'yellow'}, 'Region')
m.add_layer(random_points, {'color': 'black'}, 'Random points')
m
```

