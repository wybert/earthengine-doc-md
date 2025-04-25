 
#  ee.Image.reduceRegion 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion#examples)


Apply a reducer to all the pixels in a specific region. 
Either the reducer must have the same number of inputs as the input image has bands, or it must have a single input and will be repeated for each band.
Returns a dictionary of the reducer's outputs.
Usage| Returns  
---|---  
`Image.reduceRegion(reducer,  _geometry_, _scale_, _crs_, _crsTransform_, _bestEffort_, _maxPixels_, _tileScale_)`| Dictionary  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to reduce.  
`reducer`| Reducer| The reducer to apply.  
`geometry`| Geometry, default: null| The region over which to reduce data. Defaults to the footprint of the image's first band.  
`scale`| Float, default: null| A nominal scale in meters of the projection to work in.  
`crs`| Projection, default: null| The projection to work in. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale.  
`crsTransform`| List, default: null| The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with 'scale', and replaces any transform already set on the projection.  
`bestEffort`| Boolean, default: false| If the polygon would contain too many pixels at the given scale, compute and use a larger scale which would allow the operation to succeed.  
`maxPixels`| Long, default: 10000000| The maximum number of pixels to reduce.  
`tileScale`| Float, default: 1| A scaling factor between 0.1 and 16 used to adjust aggregation tile size; setting a larger tileScale (e.g., 2 or 4) uses smaller tiles and may enable computations that run out of memory with the default.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion#colab-python-sample) More
```
// A Landsat 8 surface reflectance image with SWIR1, NIR, and green bands.
varimg=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508')
.select(['SR_B6','SR_B5','SR_B3']);
// Santa Cruz Mountains ecoregion geometry.
vargeom=ee.FeatureCollection('EPA/Ecoregions/2013/L4')
.filter('us_l4name == "Santa Cruz Mountains"').geometry();
// Display layers on the map.
Map.setCenter(-122.08,37.22,9);
Map.addLayer(img,{min:10000,max:20000},'Landsat image');
Map.addLayer(geom,{color:'white'},'Santa Cruz Mountains ecoregion');
// Calculate median band values within Santa Cruz Mountains ecoregion. It is
// good practice to explicitly define "scale" (or "crsTransform") and "crs"
// parameters of the analysis to avoid unexpected results from undesired
// defaults when e.g. reducing a composite image.
varstats=img.reduceRegion({
reducer:ee.Reducer.median(),
geometry:geom,
scale:30,// meters
crs:'EPSG:3310',// California Albers projection
});
// A dictionary is returned; keys are band names, values are the statistic.
print('Median band values, Santa Cruz Mountains ecoregion',stats);
// You can combine reducers to calculate e.g. mean and standard deviation
// simultaneously. The output dictionary keys are the concatenation of the band
// names and statistic names, separated by an underscore.
varreducer=ee.Reducer.mean().combine({
reducer2:ee.Reducer.stdDev(),
sharedInputs:true
});
varmultiStats=img.reduceRegion({
reducer:reducer,
geometry:geom,
scale:30,
crs:'EPSG:3310',
});
print('Mean & SD band values, Santa Cruz Mountains ecoregion',multiStats);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Landsat 8 surface reflectance image with SWIR1, NIR, and green bands.
img = ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508').select(
  ['SR_B6', 'SR_B5', 'SR_B3']
)
# Santa Cruz Mountains ecoregion geometry.
geom = (
  ee.FeatureCollection('EPA/Ecoregions/2013/L4')
  .filter('us_l4name == "Santa Cruz Mountains"')
  .geometry()
)
# Display layers on the map.
m = geemap.Map()
m.set_center(-122.08, 37.22, 9)
m.add_layer(img, {'min': 10000, 'max': 20000}, 'Landsat image')
m.add_layer(geom, {'color': 'white'}, 'Santa Cruz Mountains ecoregion')
display(m)
# Calculate median band values within Santa Cruz Mountains ecoregion. It is
# good practice to explicitly define "scale" (or "crsTransform") and "crs"
# parameters of the analysis to avoid unexpected results from undesired
# defaults when e.g. reducing a composite image.
stats = img.reduceRegion(
  reducer=ee.Reducer.median(),
  geometry=geom,
  scale=30, # meters
  crs='EPSG:3310', # California Albers projection
)
# A dictionary is returned keys are band names, values are the statistic.
display('Median band values, Santa Cruz Mountains ecoregion', stats)
# You can combine reducers to calculate e.g. mean and standard deviation
# simultaneously. The output dictionary keys are the concatenation of the band
# names and statistic names, separated by an underscore.
reducer = ee.Reducer.mean().combine(
  reducer2=ee.Reducer.stdDev(), sharedInputs=True
)
multi_stats = img.reduceRegion(
  reducer=reducer,
  geometry=geom,
  scale=30,
  crs='EPSG:3310',
)
display('Mean & SD band values, Santa Cruz Mountains ecoregion', multi_stats)
```

Was this helpful?
