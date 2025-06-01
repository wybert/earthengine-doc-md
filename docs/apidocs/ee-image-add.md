 
#  ee.Image.add 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-add#examples)


Adds the first value to the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is the union of the input types. 
Usage| Returns  
---|---  
`Image.add(image2)`| Image  
Argument| Type| Details  
---|---|---  
this: `image1`| Image| The image from which the left operand bands are taken.  
`image2`| Image| The image from which the right operand bands are taken.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-add#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-add#colab-python-sample) More
```
// A Sentinel-2 surface reflectance image.
varimg=ee.Image('COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
// Subset two image bands and display them on the map.
varswir1=img.select('B11');
varswir2=img.select('B12');
Map.setCenter(-122.276,37.456,12);
Map.addLayer(swir1,{min:0,max:3000},'swir1');
Map.addLayer(swir2,{min:0,max:3000},'swir2');
// The following examples demonstrate ee.Image arithmetic methods using two
// single-band ee.Image inputs.
varaddition=swir1.add(swir2);
Map.addLayer(addition,{min:100,max:6000},'addition');
varsubtraction=swir1.subtract(swir2);
Map.addLayer(subtraction,{min:0,max:1500},'subtraction');
varmultiplication=swir1.multiply(swir2);
Map.addLayer(multiplication,{min:1.9e5,max:9.4e6},'multiplication');
vardivision=swir1.divide(swir2);
Map.addLayer(division,{min:0,max:3},'division');
varremainder=swir1.mod(swir2);
Map.addLayer(remainder,{min:0,max:1500},'remainder');
// If a number input is provided as the second argument, it will automatically
// be promoted to an ee.Image object, a convenient shorthand for constants.
varexponent=swir1.pow(3);
Map.addLayer(exponent,{min:0,max:2e10},'exponent');
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
# Subset two image bands and display them on the map.
swir_1 = img.select('B11')
swir_2 = img.select('B12')
m = geemap.Map()
m.set_center(-122.276, 37.456, 12)
m.add_layer(swir_1, {'min': 0, 'max': 3000}, 'swir_1')
m.add_layer(swir_2, {'min': 0, 'max': 3000}, 'swir_2')
# The following examples demonstrate ee.Image arithmetic methods using two
# single-band ee.Image inputs.
addition = swir_1.add(swir_2)
m.add_layer(addition, {'min': 100, 'max': 6000}, 'addition')
subtraction = swir_1.subtract(swir_2)
m.add_layer(subtraction, {'min': 0, 'max': 1500}, 'subtraction')
multiplication = swir_1.multiply(swir_2)
m.add_layer(multiplication, {'min': 1.9e5, 'max': 9.4e6}, 'multiplication')
division = swir_1.divide(swir_2)
m.add_layer(division, {'min': 0, 'max': 3}, 'division')
remainder = swir_1.mod(swir_2)
m.add_layer(remainder, {'min': 0, 'max': 1500}, 'remainder')
# If a number input is provided as the second argument, it will automatically
# be promoted to an ee.Image object, a convenient shorthand for constants.
exponent = swir_1.pow(3)
m.add_layer(exponent, {'min': 0, 'max': 2e10}, 'exponent')
m
```

