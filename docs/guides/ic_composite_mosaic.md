 
#  Compositing and Mosaicking 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
In general, compositing refers to the process of combining spatially overlapping images into a single image based on an aggregation function. Mosaicking refers to the process of spatially assembling image datasets to produce a spatially continuous image. In Earth Engine, these terms are used interchangeably, though both compositing and mosaicking are supported. For example, consider the task of compositing multiple images in the same location. For example, using one National Agriculture Imagery Program (NAIP) Digital Orthophoto Quarter Quadrangle (DOQQ) at different times, the following example demonstrates making a maximum value composite:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#colab-python-sample) More
```
// Load three NAIP quarter quads in the same location, different times.
varnaip2004_2012=ee.ImageCollection('USDA/NAIP/DOQQ')
.filterBounds(ee.Geometry.Point(-71.08841,42.39823))
.filterDate('2004-07-01','2012-12-31')
.select(['R','G','B']);
// Temporally composite the images with a maximum value function.
varcomposite=naip2004_2012.max();
Map.setCenter(-71.12532,42.3712,12);
Map.addLayer(composite,{},'max value composite');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load three NAIP quarter quads in the same location, different times.
naip_2004_2012 = (
  ee.ImageCollection('USDA/NAIP/DOQQ')
  .filterBounds(ee.Geometry.Point(-71.08841, 42.39823))
  .filterDate('2004-07-01', '2012-12-31')
  .select(['R', 'G', 'B'])
)
# Temporally composite the images with a maximum value function.
composite = naip_2004_2012.max()
m.set_center(-71.12532, 42.3712, 12)
m.add_layer(composite, {}, 'max value composite')
m
```

Consider the need to mosaic four different DOQQs at the same time, but different locations. The following example demonstrates that using `imageCollection.mosaic()`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#colab-python-sample) More
```
// Load four 2012 NAIP quarter quads, different locations.
varnaip2012=ee.ImageCollection('USDA/NAIP/DOQQ')
.filterBounds(ee.Geometry.Rectangle(-71.17965,42.35125,-71.08824,42.40584))
.filterDate('2012-01-01','2012-12-31');
// Spatially mosaic the images in the collection and display.
varmosaic=naip2012.mosaic();
Map.setCenter(-71.12532,42.3712,12);
Map.addLayer(mosaic,{},'spatial mosaic');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load four 2012 NAIP quarter quads, different locations.
naip_2012 = (
  ee.ImageCollection('USDA/NAIP/DOQQ')
  .filterBounds(
    ee.Geometry.Rectangle(-71.17965, 42.35125, -71.08824, 42.40584)
  )
  .filterDate('2012-01-01', '2012-12-31')
)
# Spatially mosaic the images in the collection and display.
mosaic = naip_2012.mosaic()
m = geemap.Map()
m.set_center(-71.12532, 42.3712, 12)
m.add_layer(mosaic, {}, 'spatial mosaic')
```

Note that there is some overlap in the DOQQs in the previous example. The `mosaic()` method composites overlapping images according to their order in the collection (last on top). To control the source of pixels in a mosaic (or a composite), use image masks. For example, the following uses thresholds on spectral indices to mask the image data in a mosaic:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#colab-python-sample) More
```
// Load a NAIP quarter quad, display.
varnaip=ee.Image('USDA/NAIP/DOQQ/m_4207148_nw_19_1_20120710');
Map.setCenter(-71.0915,42.3443,14);
Map.addLayer(naip,{},'NAIP DOQQ');
// Create the NDVI and NDWI spectral indices.
varndvi=naip.normalizedDifference(['N','R']);
varndwi=naip.normalizedDifference(['G','N']);
// Create some binary images from thresholds on the indices.
// This threshold is designed to detect bare land.
varbare1=ndvi.lt(0.2).and(ndwi.lt(0.3));
// This detects bare land with lower sensitivity. It also detects shadows.
varbare2=ndvi.lt(0.2).and(ndwi.lt(0.8));
// Define visualization parameters for the spectral indices.
varndviViz={min:-1,max:1,palette:['FF0000','00FF00']};
varndwiViz={min:0.5,max:1,palette:['00FFFF','0000FF']};
// Mask and mosaic visualization images. The last layer is on top.
varmosaic=ee.ImageCollection([
// NDWI > 0.5 is water. Visualize it with a blue palette.
ndwi.updateMask(ndwi.gte(0.5)).visualize(ndwiViz),
// NDVI > 0.2 is vegetation. Visualize it with a green palette.
ndvi.updateMask(ndvi.gte(0.2)).visualize(ndviViz),
// Visualize bare areas with shadow (bare2 but not bare1) as gray.
bare2.updateMask(bare2.and(bare1.not())).visualize({palette:['AAAAAA']}),
// Visualize the other bare areas as white.
bare1.updateMask(bare1).visualize({palette:['FFFFFF']}),
]).mosaic();
Map.addLayer(mosaic,{},'Visualization mosaic');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a NAIP quarter quad, display.
naip = ee.Image('USDA/NAIP/DOQQ/m_4207148_nw_19_1_20120710')
m = geemap.Map()
m.set_center(-71.0915, 42.3443, 14)
m.add_layer(naip, {}, 'NAIP DOQQ')
# Create the NDVI and NDWI spectral indices.
ndvi = naip.normalizedDifference(['N', 'R'])
ndwi = naip.normalizedDifference(['G', 'N'])
# Create some binary images from thresholds on the indices.
# This threshold is designed to detect bare land.
bare_1 = ndvi.lt(0.2).And(ndwi.lt(0.3))
# This detects bare land with lower sensitivity. It also detects shadows.
bare_2 = ndvi.lt(0.2).And(ndwi.lt(0.8))
# Mask and mosaic visualization images. The last layer is on top.
mosaic = ee.ImageCollection([
  # NDWI > 0.5 is water. Visualize it with a blue palette.
  ndwi.updateMask(ndwi.gte(0.5)).visualize(
    min=0.5, max=1, palette=['00FFFF', '0000FF']
  ),
  # NDVI > 0.2 is vegetation. Visualize it with a green palette.
  ndvi.updateMask(ndvi.gte(0.2)).visualize(
    min=-1, max=1, palette=['FF0000', '00FF00']
  ),
  # Visualize bare areas with shadow (bare_2 but not bare_1) as gray.
  bare_2.updateMask(bare_2.And(bare_1.Not())).visualize(palette=['AAAAAA']),
  # Visualize the other bare areas as white.
  bare_1.updateMask(bare_1).visualize(palette=['FFFFFF']),
]).mosaic()
m.add_layer(mosaic, {}, 'Visualization mosaic')
m
```

To make a composite which maximizes an arbitrary band in the input, use `imageCollection.qualityMosaic()`. The `qualityMosaic()` method sets each pixel in the composite based on which image in the collection has a maximum value for the specified band. For example, the following code demonstrates making a greenest pixel composite and a recent value composite:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_composite_mosaic#colab-python-sample) More
```
// Define a function that scales and masks Landsat 8 surface reflectance images.
functionprepSrL8(image){
// Develop masks for unwanted pixels (fill, cloud, cloud shadow).
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varsaturationMask=image.select('QA_RADSAT').eq(0);
// Apply the scaling factors to the appropriate bands.
vargetFactorImg=function(factorNames){
varfactorList=image.toDictionary().select(factorNames).values();
returnee.Image.constant(factorList);
};
varscaleImg=getFactorImg([
'REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10']);
varoffsetImg=getFactorImg([
'REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10']);
varscaled=image.select('SR_B.|ST_B10').multiply(scaleImg).add(offsetImg);
// Replace original bands with scaled bands and apply masks.
returnimage.addBands(scaled,null,true)
.updateMask(qaMask).updateMask(saturationMask);
}
// This function masks clouds and adds quality bands to Landsat 8 images.
varaddQualityBands=function(image){
// Normalized difference vegetation index.
varndvi=image.normalizedDifference(['SR_B5','SR_B4']);
// Image timestamp as milliseconds since Unix epoch.
varmillis=ee.Image(image.getNumber('system:time_start'))
.rename('millis').toFloat();
returnprepSrL8(image).addBands([ndvi,millis]);
};
// Load a 2014 Landsat 8 ImageCollection.
// Map the cloud masking and quality band function over the collection.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
.filterDate('2014-06-01','2014-12-31')
.map(addQualityBands);
// Create a cloud-free, most recent value composite.
varrecentValueComposite=collection.qualityMosaic('millis');
// Create a greenest pixel composite.
vargreenestPixelComposite=collection.qualityMosaic('nd');
// Display the results.
Map.setCenter(-122.374,37.8239,12);// San Francisco Bay
varvizParams={bands:['SR_B5','SR_B4','SR_B3'],min:0,max:0.4};
Map.addLayer(recentValueComposite,vizParams,'Recent value composite');
Map.addLayer(greenestPixelComposite,vizParams,'Greenest pixel composite');
// Compare to a cloudy image in the collection.
varcloudy=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140825');
Map.addLayer(cloudy,{bands:['B5','B4','B3'],min:0,max:0.4},'Cloudy');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Define a function that scales and masks Landsat 8 surface reflectance images.
defprep_sr_l8(image):
 # Develop masks for unwanted pixels (fill, cloud, cloud shadow).
 qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0)
 saturation_mask = image.select('QA_RADSAT').eq(0)
 # Helper function to create image from scaling factors.
 defget_factor_img(factor_names):
  factor_list = image.toDictionary().select(factor_names).values()
  return ee.Image.constant(factor_list)
 # Apply the scaling factors to the appropriate bands.
 scale_img = get_factor_img(
   ['REFLECTANCE_MULT_BAND_.|TEMPERATURE_MULT_BAND_ST_B10']
 )
 offset_img = get_factor_img(
   ['REFLECTANCE_ADD_BAND_.|TEMPERATURE_ADD_BAND_ST_B10']
 )
 scaled = image.select('SR_B.|ST_B10').multiply(scale_img).add(offset_img)
 # Replace original bands with scaled bands and apply masks.
 return (
   image.addBands(scaled, None, True)
   .updateMask(qa_mask)
   .updateMask(saturation_mask)
 )

# This function masks clouds and adds quality bands to Landsat 8 images.
defadd_quality_bands(image):
 # Normalized difference vegetation index.
 ndvi = image.normalizedDifference(['SR_B5', 'SR_B4'])
 # Image timestamp as milliseconds since Unix epoch.
 millis = (
   ee.Image(image.getNumber('system:time_start')).rename('millis').toFloat()
 )
 return prep_sr_l8(image).addBands([ndvi, millis])

# Load a 2014 Landsat 8 ImageCollection.
# Map the cloud masking and quality band function over the collection.
collection = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
  .filterDate('2014-06-01', '2014-12-31')
  .map(add_quality_bands)
)
# Create a cloud-free, most recent value composite.
recent_value_composite = collection.qualityMosaic('millis')
# Create a greenest pixel composite.
greenest_pixel_composite = collection.qualityMosaic('nd')
# Display the results.
m = geemap.Map()
m.set_center(-122.374, 37.8239, 12) # San Francisco Bay
viz_params = {'bands': ['SR_B5', 'SR_B4', 'SR_B3'], 'min': 0, 'max': 0.4}
m.add_layer(recent_value_composite, viz_params, 'Recent value composite')
m.add_layer(greenest_pixel_composite, viz_params, 'Greenest pixel composite')
# Compare to a cloudy image in the collection.
cloudy = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140825')
m.add_layer(
  cloudy, {'bands': ['B5', 'B4', 'B3'], 'min': 0, 'max': 0.4}, 'Cloudy'
)
m
```

Use the inspector tool to check pixel values at different locations in the composites. Observe that the `millis` band (timestamp) varies by location, indicating that different pixels come from different times.
