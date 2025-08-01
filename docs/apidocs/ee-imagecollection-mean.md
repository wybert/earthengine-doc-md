 
#  ee.ImageCollection.mean
Stay organized with collections  Save and categorize content based on your preferences. 
Reduces an image collection by calculating the mean of all values at each pixel across the stack of all matching bands. Bands are matched by name. Usage | Returns  
---|---  
`ImageCollection.mean()` | Image  
Argument | Type | Details  
---|---|---  
this: `collection` | ImageCollection | The image collection to reduce.  
## Examples
### Code Editor (JavaScript)
```
// Sentinel-2 image collection for July 2021 intersecting a point of interest.
// Reflectance, cloud probability, and scene classification bands are selected.
varcol=ee.ImageCollection('COPERNICUS/S2_SR')
.filterDate('2021-07-01','2021-08-01')
.filterBounds(ee.Geometry.Point(-122.373,37.448))
.select('B.*|MSK_CLDPRB|SCL');

// Visualization parameters for reflectance RGB.
varvisRefl={
bands:['B11','B8','B3'],
min:0,
max:4000
};
Map.setCenter(-122.373,37.448,9);
Map.addLayer(col,visRefl,'Collection reference',false);

// Reduce the collection to a single image using a variety of methods.
varmean=col.mean();
Map.addLayer(mean,visRefl,'Mean (B11, B8, B3)');

varmedian=col.median();
Map.addLayer(median,visRefl,'Median (B11, B8, B3)');

varmin=col.min();
Map.addLayer(min,visRefl,'Min (B11, B8, B3)');

varmax=col.max();
Map.addLayer(max,visRefl,'Max (B11, B8, B3)');

varsum=col.sum();
Map.addLayer(sum,
{bands:['MSK_CLDPRB'],min:0,max:500},'Sum (MSK_CLDPRB)');

varproduct=col.product();
Map.addLayer(product,
{bands:['MSK_CLDPRB'],min:0,max:1e10},'Product (MSK_CLDPRB)');

// ee.ImageCollection.mode returns the most common value. If multiple mode
// values occur, the minimum mode value is returned.
varmode=col.mode();
Map.addLayer(mode,{bands:['SCL'],min:1,max:11},'Mode (pixel class)');

// ee.ImageCollection.count returns the frequency of valid observations. Here,
// image pixels are masked based on cloud probability to add valid observation
// variability to the collection. Note that pixels with no valid observations
// are masked out of the returned image.
varnotCloudCol=col.map(function(img){
returnimg.updateMask(img.select('MSK_CLDPRB').lte(10));
});
varcount=notCloudCol.count();
Map.addLayer(count,{min:1,max:5},'Count (not cloud observations)');

// ee.ImageCollection.mosaic composites images according to their position in
// the collection (priority is last to first) and pixel mask status, where
// invalid (mask value 0) pixels are filled by preceding valid (mask value >0)
// pixels.
varmosaic=notCloudCol.mosaic();
Map.addLayer(mosaic,visRefl,'Mosaic (B11, B8, B3)');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Sentinel-2 image collection for July 2021 intersecting a point of interest.
# Reflectance, cloud probability, and scene classification bands are selected.
col = (
    ee.ImageCollection('COPERNICUS/S2_SR')
    .filterDate('2021-07-01', '2021-08-01')
    .filterBounds(ee.Geometry.Point(-122.373, 37.448))
    .select('B.*|MSK_CLDPRB|SCL')
)

# Visualization parameters for reflectance RGB.
vis_refl = {'bands': ['B11', 'B8', 'B3'], 'min': 0, 'max': 4000}
m = geemap.Map()
m.set_center(-122.373, 37.448, 9)
m.add_layer(col, vis_refl, 'Collection reference', False)

# Reduce the collection to a single image using a variety of methods.
mean = col.mean()
m.add_layer(mean, vis_refl, 'Mean (B11, B8, B3)')

median = col.median()
m.add_layer(median, vis_refl, 'Median (B11, B8, B3)')

min = col.min()
m.add_layer(min, vis_refl, 'Min (B11, B8, B3)')

max = col.max()
m.add_layer(max, vis_refl, 'Max (B11, B8, B3)')

sum = col.sum()
m.add_layer(
    sum, {'bands': ['MSK_CLDPRB'], 'min': 0, 'max': 500}, 'Sum (MSK_CLDPRB)'
)

product = col.product()
m.add_layer(
    product,
    {'bands': ['MSK_CLDPRB'], 'min': 0, 'max': 1e10},
    'Product (MSK_CLDPRB)',
)

# ee.ImageCollection.mode returns the most common value. If multiple mode
# values occur, the minimum mode value is returned.
mode = col.mode()
m.add_layer(
    mode, {'bands': ['SCL'], 'min': 1, 'max': 11}, 'Mode (pixel class)'
)

# ee.ImageCollection.count returns the frequency of valid observations. Here,
# image pixels are masked based on cloud probability to add valid observation
# variability to the collection. Note that pixels with no valid observations
# are masked out of the returned image.
not_cloud_col = col.map(
    lambda img: img.updateMask(img.select('MSK_CLDPRB').lte(10))
)
count = not_cloud_col.count()
m.add_layer(count, {'min': 1, 'max': 5}, 'Count (not cloud observations)')

# ee.ImageCollection.mosaic composites images according to their position in
# the collection (priority is last to first) and pixel mask status, where
# invalid (mask value 0) pixels are filled by preceding valid (mask value >0)
# pixels.
mosaic = not_cloud_col.mosaic()
m.add_layer(mosaic, vis_refl, 'Mosaic (B11, B8, B3)')
m
```

