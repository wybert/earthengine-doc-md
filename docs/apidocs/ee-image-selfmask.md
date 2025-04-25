 
#  ee.Image.selfMask 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-selfmask#examples)


Updates an image's mask at all positions where the existing mask is not zero using the value of the image as the new mask value. The output image retains the metadata and footprint of the input image. 
Usage| Returns  
---|---  
`Image.selfMask()`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to mask with itself.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-selfmask#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-selfmask#colab-python-sample) More
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
// Mask the land mask by itself; pixel values equal to 0 (water) become invalid.
varlandMaskMasked=landMask.selfMask();
print('Land mask, masked',landMaskMasked);
Map.addLayer(landMaskMasked,{palette:['gold']},'Land mask, masked');
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
# Mask the land mask by itself pixel values equal to 0 (water) become invalid.
land_mask_masked = land_mask.selfMask()
display('Land mask, masked', land_mask_masked)
m.add_layer(land_mask_masked, {'palette': ['gold']}, 'Land mask, masked')
m
```

Was this helpful?
