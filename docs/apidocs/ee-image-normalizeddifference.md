 
#  ee.Image.normalizedDifference 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference#examples)


Computes the normalized difference between two bands. If the bands to use are not specified, uses the first two bands. The normalized difference is computed as (first − second) / (first + second). Note that the returned image band name is 'nd', the input image properties are not retained in the output image, and a negative pixel value in either input band will cause the output pixel to be masked. To avoid masking negative input values, use `ee.Image.expression()` to compute normalized difference. 
Usage| Returns  
---|---  
`Image.normalizedDifference( _bandNames_)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| The input image.  
`bandNames`| List, default: null| A list of names specifying the bands to use. If not specified, the first and second bands are used.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference#colab-python-sample) More
```
// A Landsat 8 surface reflectance image.
varimg=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508');
// Calculate normalized difference vegetation index: (NIR - Red) / (NIR + Red).
varnirBand='SR_B5';
varredBand='SR_B4';
varndvi=img.normalizedDifference([nirBand,redBand]);
// Display NDVI result on the map.
Map.setCenter(-122.148,37.377,11);
Map.addLayer(ndvi,{min:0,max:0.5},'NDVI');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Landsat 8 surface reflectance image.
img = ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508')
# Calculate normalized difference vegetation index: (NIR - Red) / (NIR + Red).
nir_band = 'SR_B5'
red_band = 'SR_B4'
ndvi = img.normalizedDifference([nir_band, red_band])
# Display NDVI result on the map.
m = geemap.Map()
m.set_center(-122.148, 37.377, 11)
m.add_layer(ndvi, {'min': 0, 'max': 0.5}, 'NDVI')
m
```

Was this helpful?
