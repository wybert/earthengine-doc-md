 
#  ee.Image.reduceRegions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregions#examples)


Apply a reducer over the area of each feature in the given collection.
The reducer must have the same number of inputs as the input image has bands.
Returns the input features, each augmented with the corresponding reducer outputs.
Usage | Returns  
---|---  
`Image.reduceRegions(collection, reducer, _scale_, _crs_, _crsTransform_, _tileScale_, _maxPixelsPerRegion_)`|  FeatureCollection  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image to reduce.  
`collection` | FeatureCollection | The features to reduce over.  
`reducer` | Reducer | The reducer to apply.  
`scale` | Float, default: null | A nominal scale in meters of the projection to work in.  
`crs` | Projection, default: null | The projection to work in. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale.  
`crsTransform` | List, default: null | The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with 'scale', and will replace any transform already set on the projection.  
`tileScale` | Float, default: 1 | A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default.  
`maxPixelsPerRegion` | Long, default: null | The maximum number of pixels to reduce per region.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregions#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregions#colab-python-sample) More
```
// A Landsat 8 SR image with SWIR1, NIR, and green bands.
varimg=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508')
.select(['SR_B6','SR_B5','SR_B3']);

// Santa Cruz Mountains ecoregions feature collection.
varregionCol=ee.FeatureCollection('EPA/Ecoregions/2013/L4')
.filter('us_l4name == "Santa Cruz Mountains" || '+
'us_l4name == "San Mateo Coastal Hills" || '+
'us_l4name == "Leeward Hills"');

// Display layers on the map.
Map.setCenter(-122.08,37.22,9);
Map.addLayer(img,{min:10000,max:20000},'Landsat image');
Map.addLayer(regionCol,{color:'white'},'Santa Cruz Mountains ecoregions');

// Calculate median band values within Santa Cruz Mountains ecoregions. It is
// good practice to explicitly define "scale" (or "crsTransform") and "crs"
// parameters of the analysis to avoid unexpected results from undesired
// defaults when e.g. reducing a composite image.
varstats=img.reduceRegions({
collection:regionCol,
reducer:ee.Reducer.median(),
scale:30,// meters
crs:'EPSG:3310',// California Albers projection
});

// The input feature collection is returned with new properties appended.
// The new properties are the outcome of the region reduction per image band,
// for each feature in the collection. Region reduction property names
// are the same as the input image band names.
print('Median band values, Santa Cruz Mountains ecoregions',stats);

// You can combine reducers to calculate e.g. mean and standard deviation
// simultaneously. The resulting property names are the concatenation of the
// band names and statistic names, separated by an underscore.
varreducer=ee.Reducer.mean().combine({
reducer2:ee.Reducer.stdDev(),
sharedInputs:true
});
varmultiStats=img.reduceRegions({
collection:regionCol,
reducer:reducer,
scale:30,
crs:'EPSG:3310',
});
print('Mean & SD band values, Santa Cruz Mountains ecoregions',multiStats);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Landsat 8 SR image with SWIR1, NIR, and green bands.
img = ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508').select(
    ['SR_B6', 'SR_B5', 'SR_B3']
)

# Santa Cruz Mountains ecoregions feature collection.
region_col = ee.FeatureCollection('EPA/Ecoregions/2013/L4').filter(
    'us_l4name == "Santa Cruz Mountains" || '
    + 'us_l4name == "San Mateo Coastal Hills" || '
    + 'us_l4name == "Leeward Hills"'
)

# Display layers on the map.
m = geemap.Map()
m.set_center(-122.08, 37.22, 9)
m.add_layer(img, {'min': 10000, 'max': 20000}, 'Landsat image')
m.add_layer(
    region_col, {'color': 'white'}, 'Santa Cruz Mountains ecoregions'
)
display(m)

# Calculate median band values within Santa Cruz Mountains ecoregions. It is
# good practice to explicitly define "scale" (or "crsTransform") and "crs"
# parameters of the analysis to avoid unexpected results from undesired
# defaults when e.g. reducing a composite image.
stats = img.reduceRegions(
    collection=region_col,
    reducer=ee.Reducer.median(),
    scale=30,  # meters
    crs='EPSG:3310',  # California Albers projection
)

# The input feature collection is returned with new properties appended.
# The new properties are the outcome of the region reduction per image band,
# for each feature in the collection. Region reduction property names
# are the same as the input image band names.
display('Median band values, Santa Cruz Mountains ecoregions', stats)

# You can combine reducers to calculate e.g. mean and standard deviation
# simultaneously. The resulting property names are the concatenation of the
# band names and statistic names, separated by an underscore.
reducer = ee.Reducer.mean().combine(
    reducer2=ee.Reducer.stdDev(), sharedInputs=True
)
multi_stats = img.reduceRegions(
    collection=region_col,
    reducer=reducer,
    scale=30,
    crs='EPSG:3310',
)
display('Mean & SD band values, Santa Cruz Mountains ecoregions', multi_stats)
```

Was this helpful?
