 
#  ee.Image.mask 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-mask#examples)


Gets or sets an image's mask. The output image retains the metadata and footprint of the input image. Pixels where the mask changes from zero to another value will be filled with zeros, or the values closest to zero within the range of the pixel type. **Note:** the version that sets a mask will be deprecated. To set a mask from an image on previously unmasked pixels, use Image.updateMask. To unmask previously masked pixels, use Image.unmask.
Usage| Returns  
---|---  
`Image.mask( _mask_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`mask`| Image, default: null| The mask image. If specified, the input image is copied to the output but given the mask by the values of this image. If this is a single band, it is used for all bands in the input image. If not specified, returns an image created from the mask of the input image, scaled to the range [0:1] (invalid = 0, valid = 1.0).  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-mask#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-mask#colab-python-sample) More
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
// Get masks for all image bands; each band has an independent mask.
// Valid pixels are value 1, invalid are 0.
varmultiBandMaskImg=img.mask();
print('Multi-band mask image',multiBandMaskImg);
Map.addLayer(multiBandMaskImg,null,'Multi-band mask image');
// Get the mask for a single image band.
varsingleBandMaskImg=img.select('B1').mask();
print('Single-band mask image',singleBandMaskImg);
Map.addLayer(singleBandMaskImg,null,'Single-band mask image');
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
# Get masks for all image bands each band has an independent mask.
# Valid pixels are value 1, invalid are 0.
multi_band_mask_img = img.mask()
display('Multi-band mask image', multi_band_mask_img)
m.add_layer(multi_band_mask_img, None, 'Multi-band mask image')
# Get the mask for a single image band.
single_band_mask_img = img.select('B1').mask()
display('Single-band mask image', single_band_mask_img)
m.add_layer(single_band_mask_img, None, 'Single-band mask image')
m
```

