 
#  ee.Image.addBands 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-addbands#examples)


Returns an image containing all bands copied from the first input and selected bands from the second input, optionally overwriting bands in the first image with the same name. The new image has the metadata and footprint from the first input image. 
Usage| Returns  
---|---  
`Image.addBands(srcImg,  _names_, _overwrite_)`| Image  
Argument| Type| Details  
---|---|---  
this: `dstImg`| Image| An image into which to copy bands.  
`srcImg`| Image| An image containing bands to copy.  
`names`| List, default: null| Optional list of band names to copy. If names is omitted, all bands from srcImg will be copied over.  
`overwrite`| Boolean, default: false| If true, bands from `srcImg` will override bands with the same names in `dstImg`. Otherwise the new band will be renamed with a numerical suffix (`foo` to `foo_1` unless `foo_1` exists, then `foo_2` unless it exists, etc).  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-addbands#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-addbands#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
print('Original image',img);
// Scale reflectance bands and overwrite the original bands.
varreflBands=img.select('B.*').divide(10000);
img=img.addBands({
srcImg:reflBands,
overwrite:true
});
// Compute and add a single band (NDVI).
varndvi=img.normalizedDifference(['B8','B4']).rename('NDVI');
img=img.addBands(ndvi);
// Compute and add multiple bands (NDWI and NBR).
varndwi=img.normalizedDifference(['B3','B8']).rename('NDWI');
varnbr=img.normalizedDifference(['B8','B12']).rename('NBR');
varnewBands=ee.Image([ndwi,nbr]);
img=img.addBands(newBands);
print('Image with added/modified bands',img);
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
print('Original image:', img.getInfo())
# Scale reflectance bands and overwrite the original bands.
refl_bands = img.select('B.*').divide(10000)
img = img.addBands(srcImg=refl_bands, overwrite=True)
# Compute and add a single band (NDVI).
ndvi = img.normalizedDifference(['B8', 'B4']).rename('NDVI')
img = img.addBands(ndvi)
# Compute and add multiple bands (NDWI and NBR).
ndwi = img.normalizedDifference(['B3', 'B8']).rename('NDWI')
nbr = img.normalizedDifference(['B8', 'B12']).rename('NBR')
new_bands = ee.Image([ndwi, nbr])
img = img.addBands(new_bands)
print('Image with added/modified bands:', img.getInfo())
```

Was this helpful?
