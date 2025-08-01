 
#  ee.Image.unmask
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-unmask#examples)


Replaces mask and value of the input image with the mask and value of another image at all positions where the input mask is zero. The output image retains the metadata of the input image. By default, the output image also retains the footprint of the input, but setting sameFootprint to false allows to extend the footprint.
Usage | Returns  
---|---  
`Image.unmask(_value_, _sameFootprint_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `input` | Image | Input image.  
`value` | Image, default: null | New value and mask for the masked pixels of the input image. If not specified, defaults to constant zero image which is valid everywhere.  
`sameFootprint` | Boolean, default: true | If true (or unspecified), the output retains the footprint of the input image. If false, the footprint of the output is the union of the input footprint with the footprint of the value image.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-unmask#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-unmask#colab-python-sample) More
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

// Set invalid masked pixels to a new value, e.g. a constant nodata value
// when exporting an image as GeoTIFF.
varimgUnmasked=imgMasked.unmask(32767);
print('Image, unmasked',imgMasked);
Map.addLayer(imgUnmasked,trueColorViz,'Image, unmasked');

// Reset masked pixels to valid, fill with default value 0, input footprint.
varmaskResetFootprint=imgMasked.unmask();
print('Image mask reset, footprint',maskResetFootprint);
Map.addLayer(maskResetFootprint,trueColorViz,'Image mask reset, footprint');

// Reset masked pixels to valid, fill with default value 0, everywhere.
varmaskResetEverywhere=imgMasked.unmask({sameFootprint:false});
print('Image mask reset, everywhere',maskResetEverywhere);
Map.addLayer(maskResetEverywhere,trueColorViz,'Image mask reset, everywhere');

// Fill masked pixels with pixels from a different image.
varfill=ee.Image('COPERNICUS/S2_SR/20200618T184919_20200618T190341_T10SEG');
varimgFilled=imgMasked.unmask(fill);
print('Image, filled',imgFilled);
Map.addLayer(imgFilled,trueColorViz,'Image, filled');
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

# Set invalid masked pixels to a new value, e.g. a constant nodata value
# when exporting an image as GeoTIFF.
img_unmasked = img_masked.unmask(32767)
display('Image, unmasked', img_masked)
m.add_layer(img_unmasked, true_color_viz, 'Image, unmasked')

# Reset masked pixels to valid, fill with default value 0, input footprint.
mask_reset_footprint = img_masked.unmask()
display('Image mask reset, footprint', mask_reset_footprint)
m.add_layer(mask_reset_footprint, true_color_viz, 'Image mask reset, footprint')

# Reset masked pixels to valid, fill with default value 0, everywhere.
mask_reset_everywhere = img_masked.unmask(sameFootprint=False)
display('Image mask reset, everywhere', mask_reset_everywhere)
m.add_layer(
    mask_reset_everywhere, true_color_viz, 'Image mask reset, everywhere'
)

# Fill masked pixels with pixels from a different image.
fill = ee.Image('COPERNICUS/S2_SR/20200618T184919_20200618T190341_T10SEG')
img_filled = img_masked.unmask(fill)
display('Image, filled', img_filled)
m.add_layer(img_filled, true_color_viz, 'Image, filled')
m
```

