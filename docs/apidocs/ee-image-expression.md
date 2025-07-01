 
#  ee.Image.expression
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-expression#examples)


Evaluates an arithmetic expression on an image, possibly involving additional images. 
The bands of the primary input image are available using the built-in function b(), as b(0) or b('band_name').
Variables in the expression are interpreted as additional image parameters which must be supplied in opt_map. The bands of each such image can be accessed like image.band_name or image[0].
Both b() and image[] allow multiple arguments, to specify multiple bands, such as b(1, 'name', 3). Calling b() with no arguments, or using a variable by itself, returns all bands of the image.
If the result of an expression is a single band, it can be assigned a name using the '=' operator (e.g.: x = a + b).
Returns the image computed by the provided expression.
Usage| Returns  
---|---  
`Image.expression(expression,  _map_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The Image instance.  
`expression`| String| The expression to evaluate.  
`map`| Dictionary, optional| A map of input images available by name.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-expression#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-expression#colab-python-sample) More
```
// The following expressions calculate the normalized difference vegetation
// index (NDVI): (NIR - Red) / (NIR + Red).
// NIR is Landsat 8 L2 band 'SR_B5', the 4th band index.
// Red is Landsat 8 L2 band 'SR_B4', the 3rd band index.
// A Landsat 8 L2 surface reflectance image.
varimg=ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508');
// Visualization parameters for NDVI.
varndviVis={min:0,max:0.5};
// Expression using image band indices.
varbandIndexExp='(b(4) - b(3)) / (b(4) + b(3))';
varbandIndexImg=img.expression(bandIndexExp).rename('NDVI');
Map.setCenter(-122.14,37.38,11);
Map.addLayer(bandIndexImg,ndviVis,'NDVI 1');
// Expression using image band names.
varbandNameExp='(b("SR_B5") - b("SR_B4")) / (b("SR_B5") + b("SR_B4"))';
varbandNameImg=img.expression(bandNameExp).rename('NDVI');
Map.addLayer(bandNameImg,ndviVis,'NDVI 2');
// Expression using named variables.
varnamedVarsExp='(NIR - Red) / (NIR + Red)';
varnamedVarsImg=ee.Image().expression({
expression:namedVarsExp,
map:{
NIR:img.select('SR_B5'),
Red:img.select('SR_B4')
}
}).rename('NDVI');
Map.addLayer(namedVarsImg,ndviVis,'NDVI 3');
// Expression using named variables with image band access by dot notation.
varnamedVarsDotExp='(ls8.SR_B5 - ls8.SR_B4) / (ls8.SR_B5 + ls8.SR_B4)';
varnamedVarsDotImg=ee.Image().expression({
expression:namedVarsDotExp,
map:{ls8:img}
}).rename('NDVI');
Map.addLayer(namedVarsDotImg,ndviVis,'NDVI 4');
// Expressions can use arithmetic operators (+ - * / % **), relational
// operators (== != < > <= >=), logical operators (&& || ! ^), the ternary
// operator (condition ? ifTrue : ifFalse), and a subset of JavaScript Math
// functions. Math functions are called by name directly, they are not accessed
// from the Math object (e.g., sqrt() instead of Math.sqrt()).
varjsMathExp='c = sqrt(pow(a, 2) + pow(b, 2))';
varjsMathImg=ee.Image().expression({
expression:jsMathExp,
map:{
a:ee.Image(5),
b:img.select('SR_B2')
}
});
Map.addLayer(jsMathImg,{min:5000,max:20000},'Hypotenuse',false);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The following expressions calculate the normalized difference vegetation
# index (NDVI): (NIR - Red) / (NIR + Red).
# NIR is Landsat 8 L2 band 'SR_B5', the 4th band index.
# Red is Landsat 8 L2 band 'SR_B4', the 3rd band index.
# A Landsat 8 L2 surface reflectance image.
img = ee.Image('LANDSAT/LC08/C02/T1_L2/LC08_044034_20210508')
# Visualization parameters for NDVI.
ndvi_vis = {'min': 0, 'max': 0.5}
# Expression using image band indices.
band_index_exp = '(b(4) - b(3)) / (b(4) + b(3))'
band_index_img = img.expression(band_index_exp).rename('NDVI')
m = geemap.Map()
m.set_center(-122.14, 37.38, 11)
m.add_layer(band_index_img, ndvi_vis, 'NDVI 1')
# Expression using image band names.
band_name_exp = '(b("SR_B5") - b("SR_B4")) / (b("SR_B5") + b("SR_B4"))'
band_name_img = img.expression(band_name_exp).rename('NDVI')
m.add_layer(band_name_img, ndvi_vis, 'NDVI 2')
# Expression using named variables.
named_vars_exp = '(NIR - Red) / (NIR + Red)'
named_vars_img = (
  ee.Image()
  .expression(
    expression=named_vars_exp,
    opt_map={'NIR': img.select('SR_B5'), 'Red': img.select('SR_B4')},
  )
  .rename('NDVI')
)
m.add_layer(named_vars_img, ndvi_vis, 'NDVI 3')
# Expression using named variables with image band access by dot notation.
named_vars_dot_exp = '(ls8.SR_B5 - ls8.SR_B4) / (ls8.SR_B5 + ls8.SR_B4)'
named_vars_dot_img = (
  ee.Image()
  .expression(expression=named_vars_dot_exp, opt_map={'ls8': img})
  .rename('NDVI')
)
m.add_layer(named_vars_dot_img, ndvi_vis, 'NDVI 4')
# Expressions can use arithmetic operators (+ - * / % **), relational
# operators (== != < > <= >=), logical operators (&& || ! ^), the ternary
# operator (condition ? ifTrue : ifFalse), and a subset of JavaScript Math
# functions. Math functions are called by name directly, they are not accessed
# from the Math object (e.g., sqrt() instead of Math.sqrt()).
js_math_exp = 'c = sqrt(pow(a, 2) + pow(b, 2))'
js_math_img = ee.Image().expression(
  expression=js_math_exp, opt_map={'a': ee.Image(5), 'b': img.select('SR_B2')}
)
m.add_layer(js_math_img, {'min': 5000, 'max': 20000}, 'Hypotenuse', False)
m
```

Was this helpful?
