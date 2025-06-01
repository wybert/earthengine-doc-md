 
#  ee.Filter.bounds 
Stay organized with collections  Save and categorize content based on your preferences. 
Creates a filter that passes if the object's geometry intersects the given geometry. **Caution:** providing a large or complex collection as the `geometry` argument can result in poor performance. Collating the geometry of collections does not scale well; use the smallest collection (or geometry) that is required to achieve the desired outcome.
Returns the constructed filter.
Usage| Returns  
---|---  
`ee.Filter.bounds(geometry,  _errorMargin_)`| Filter  
Argument| Type| Details  
---|---|---  
`geometry`| ComputedObject|FeatureCollection|Geometry| The geometry, feature or collection to intersect with.  
`errorMargin`| ComputedObject|Number, optional| An optional error margin. If a number, interpreted as sphere surface meters.  
## Examples
### Code Editor (JavaScript)
```
// collection.filterBounds() is preferred.
// A Sentinel-2 surface reflectance image collection for 3 months in 2021.
varic=ee.ImageCollection('COPERNICUS/S2_SR')
.filterDate('2021-07-01','2021-10-01');
// A point geometry for the peak of Mount Shasta, California, USA.
vargeom=ee.Geometry.Point(-122.196,41.411);
print('Images intersecting point geometry',
ic.filter(ee.Filter.bounds(geom)));
// A feature collection of point geometries for mountain peaks.
varfc=ee.FeatureCollection([
ee.Feature(ee.Geometry.Point(-122.196,41.411),{mountain:'Mount Shasta'}),
ee.Feature(ee.Geometry.Point(-121.697,45.374),{mountain:'Mount Hood'})
]);
print('Images intersecting feature collection',
ic.filter(ee.Filter.bounds(fc)));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# collection.filterBounds() is preferred.
# A Sentinel-2 surface reflectance image collection for 3 months in 2021.
ic = ee.ImageCollection('COPERNICUS/S2_SR').filterDate('2021-07-01',
                            '2021-10-01')
# A point geometry for the peak of Mount Shasta, California, USA.
geom = ee.Geometry.Point(-122.196, 41.411)
print('Images intersecting point geometry:',
   ic.filter(ee.Filter.bounds(geom)).getInfo())
# A feature collection of point geometries for mountain peaks.
fc = ee.FeatureCollection([
  ee.Feature(ee.Geometry.Point(-122.196, 41.411),
        {'mountain': 'Mount Shasta'}),
  ee.Feature(ee.Geometry.Point(-121.697, 45.374),
        {'mountain': 'Mount Hood'})
])
print('Images intersecting feature collection:',
   ic.filter(ee.Filter.bounds(fc)).getInfo())
```

