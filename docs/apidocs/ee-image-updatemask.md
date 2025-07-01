 
#  ee.Image.updateMask
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-updatemask#examples)


Updates an image's mask at all positions where the existing mask is not zero. The output image retains the metadata and footprint of the input image. 
Usage| Returns  
---|---  
`Image.updateMask(mask)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| Input image.  
`mask`| Image| New mask for the image, as a floating-point value in the range [0, 1] (invalid = 0, valid = 1). If this image has a single band, it is used for all bands in the input image; otherwise, must have the same number of bands as the input image.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-updatemask#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-updatemask#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
vartrueColorViz={
bands:['B4','B3','B2'],
min:0,
max:2700,
gamma:1.3
};
print('Sentinel-2 image',img);
Map.setCenter(-122.36,37.47,10);
Map.addLayer(img,trueColorViz,'Sentinel-2 image');
// Create a Boolean land mask from the SWIR1 band; water is value 0, land is 1.
varlandMask=img.select('B11').gt(100);
print('Land mask',landMask);
Map.addLayer(landMask,{palette:['blue','lightgreen']},'Land mask');
// Apply the single-band land mask to all image bands; pixel values equal to 0
// in the mask become invalid in the image.
varimgMasked=img.updateMask(landMask);
print('Image, land only',imgMasked);
Map.addLayer(imgMasked,trueColorViz,'Image, land only');
// Masks are band-specific. Here, a multi-band mask image is used to update
// corresponding input image band masks.
varimgBandSubset=img.select(['B4','B3','B2']);
varbandSpecificMasks=imgBandSubset.gt(200);
varimgBandSubsetMasked=imgBandSubset.updateMask(bandSpecificMasks);
print('Multi-band mask image',bandSpecificMasks);
print('Image, variable band masks',imgBandSubsetMasked);
Map.addLayer(bandSpecificMasks,null,'Multi-band mask image');
Map.addLayer(imgBandSubsetMasked,trueColorViz,'Image, variable band masks');
// Note that there is only a single alpha channel for visualization, so when
// the ee.Image is rendered as an RGB image or map tiles, a masked pixel in any
// band will result in transparency for all bands.
// Floating point mask values between 0 and 1 will be used to define opacity
// in visualization via Map.addLayer and ee.Image.visualize.
varlandMaskFloat=landMask.add(0.65);
varimgMaskedFloat=img.updateMask(landMaskFloat);
print('Image, partially transparent',imgMaskedFloat);
Map.addLayer(imgMaskedFloat,trueColorViz,'Image, partially transparent');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Sentinel-2 surface reflectance image.
img = ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG')
true_color_viz = {
  'bands': ['B4', 'B3', 'B2'],
  'min': 0,
  'max': 2700,
  'gamma': 1.3,
}
display('Sentinel-2 image', img)
m = geemap.Map()
m.set_center(-122.36, 37.47, 10)
m.add_layer(img, true_color_viz, 'Sentinel-2 image')
# Create a Boolean land mask from the SWIR1 band water is value 0, land is 1.
land_mask = img.select('B11').gt(100)
display('Land mask', land_mask)
m.add_layer(land_mask, {'palette': ['blue', 'lightgreen']}, 'Land mask')
# Apply the single-band land mask to all image bands pixel values equal to 0
# in the mask become invalid in the image.
img_masked = img.updateMask(land_mask)
display('Image, land only', img_masked)
m.add_layer(img_masked, true_color_viz, 'Image, land only')
# Masks are band-specific. Here, a multi-band mask image is used to update
# corresponding input image band masks.
img_band_subset = img.select(['B4', 'B3', 'B2'])
band_specific_masks = img_band_subset.gt(200)
img_band_subset_masked = img_band_subset.updateMask(band_specific_masks)
display('Multi-band mask image', band_specific_masks)
display('Image, variable band masks', img_band_subset_masked)
m.add_layer(band_specific_masks, None, 'Multi-band mask image')
m.add_layer(
  img_band_subset_masked, true_color_viz, 'Image, variable band masks'
)
# Note that there is only a single alpha channel for visualization, so when
# the ee.Image is rendered as an RGB image or map tiles, a masked pixel in any
# band will result in transparency for all bands.
# Floating point mask values between 0 and 1 will be used to define opacity
# in visualization via m.add_ee_layer and ee.Image.visualize.
land_mask_float = land_mask.add(0.65)
img_masked_float = img.updateMask(land_mask_float)
display('Image, partially transparent', img_masked_float)
m.add_layer(img_masked_float, true_color_viz, 'Image, partially transparent')
m
```

Was this helpful?
