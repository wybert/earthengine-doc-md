 
#  ee.ImageCollection.qualityMosaic
Stay organized with collections  Save and categorize content based on your preferences. 
Composites all the images in a collection, using a quality band as a per-pixel ordering function. Usage | Returns  
---|---  
`ImageCollection.qualityMosaic(qualityBand)` | Image  
Argument | Type | Details  
---|---|---  
this: `collection` | ImageCollection | The collection to mosaic.  
`qualityBand` | String | The name of the quality band in the collection.  
## Examples
### Code Editor (JavaScript)
```
// The goal is to generate a best-pixel mosaic from a collection of
// Sentinel-2 images where pixel quality is based on a cloud probability score.
// The qualityMosaic() function selects the image (per-pixel) with the HIGHEST
// quality-band-score to contribute to the resulting mosaic. All bands from the
// selected image (per-pixel) associated with the HIGHEST quality-band-score
// are included in the output.

// A Sentinel-2 SR image collection (2 months of images at a specific point).
varcol=ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
.filterBounds(ee.Geometry.Point(-103.19,40.14))
.filterDate('2020-07-01','2020-09-01');

// Because cloud probability ranges from 0 to 100 percent (low to high), we need
// to invert the MSK_CLDPRB band values so that low cloud probability pixels
// indicate high quality. Here, an inverting function is mapped over the
// image collection, the inverted MSK_CLDPRB band is added as a "quality" band.
col=col.map(function(img){
varcldProb=img.select('MSK_CLDPRB');
varcldProbInv=cldProb.multiply(-1).rename('quality');
returnimg.addBands(cldProbInv);
});

// Image visualization settings.
varvisParams={
bands:['B4','B3','B2'],
min:0,
max:4500
};
Map.setCenter(-103.19,40.14,9);
Map.addLayer(col,visParams,'Collection (for series inspection)',false);

// Generate a best-pixel mosaic from the image collection.
varimg=col.qualityMosaic('quality');
Map.addLayer(img,visParams,'Best-pixel mosaic (by cloud score)');

// To build the worst-pixel mosaic, according to cloud probability, use the
// MSK_CLDPRB band as the quality band (the worst pixels have HIGHEST cloud
// probability score).
varimg=col.qualityMosaic('MSK_CLDPRB');
Map.addLayer(img,visParams,'Worst-pixel mosaic (by cloud score)',false);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# The goal is to generate a best-pixel mosaic from a collection of
# Sentinel-2 images where pixel quality is based on a cloud probability score.
# The qualityMosaic() function selects the image (per-pixel) with the HIGHEST
# quality-band-score to contribute to the resulting mosaic. All bands from the
# selected image (per-pixel) associated with the HIGHEST quality-band-score
# are included in the output.

# A Sentinel-2 SR image collection (2 months of images at a specific point).
col = (
    ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
    .filterBounds(ee.Geometry.Point(-103.19, 40.14))
    .filterDate('2020-07-01', '2020-09-01')
)

# Because cloud probability ranges from 0 to 100 percent (low to high), we need
# to invert the MSK_CLDPRB band values so that low cloud probability pixels
# indicate high quality. Here, an inverting function is mapped over the
# image collection, the inverted MSK_CLDPRB band is added as a "quality" band.
definvertCloudProbabilityBand(img):
  cldProb = img.select('MSK_CLDPRB')
  cldProbInv = cldProb.multiply(-1).rename('quality')
  return img.addBands(cldProbInv)

col = col.map(invertCloudProbabilityBand)

# Image visualization settings.
vis_params = {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 4500}
m = geemap.Map()
m.set_center(-103.19, 40.14, 9)
m.add_layer(col, vis_params, 'Collection (for series inspection)', False)

# Generate a best-pixel mosaic from the image collection.
img = col.qualityMosaic('quality')
m.add_layer(img, vis_params, 'Best-pixel mosaic (by cloud score)')

# To build the worst-pixel mosaic, according to cloud probability, use the
# MSK_CLDPRB band as the quality band (the worst pixels have HIGHEST cloud
# probability score).
img = col.qualityMosaic('MSK_CLDPRB')
m.add_layer(img, vis_params, 'Worst-pixel mosaic (by cloud score)', False)
m
```

