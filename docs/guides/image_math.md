 
#  Mathematical Operations
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Operators](https://developers.google.com/earth-engine/guides/image_math#operators)
  * [Expressions](https://developers.google.com/earth-engine/guides/image_math#expressions)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/image_math.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/image_math.ipynb)  
---|---  
Image math can be performed using operators like `add()` and `subtract()`, but for complex computations with more than a couple of terms, the `expression()` function provides a good alternative. See the following sections for more information on [operators](https://developers.google.com/earth-engine/guides/image_math#operators) and [expressions](https://developers.google.com/earth-engine/guides/image_math#expressions).
## Operators
Math operators perform basic arithmetic operations on image bands. They take two inputs: either two images or one image and a constant term, which is interpreted as a single-band constant image with no masked pixels. Operations are performed per pixel for each band.
As a basic example, consider the task of calculating the Normalized Difference Vegetation Index (NDVI) using VIIRS imagery, where `add()`, `subtract()`, and `divide()` operators are used:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_math#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_math#colab-python-sample) More
```
// Load a VIIRS 8-day surface reflectance composite for May 2024.
varviirs202405=ee.ImageCollection('NASA/VIIRS/002/VNP09H1').filter(
ee.Filter.date('2024-05-01','2024-05-16')).first();
// Compute NDVI.
varndvi202405=viirs202405.select('SurfReflect_I2')
.subtract(viirs202405.select('SurfReflect_I1'))
.divide(viirs202405.select('SurfReflect_I2')
.add(viirs202405.select('SurfReflect_I1')));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a VIIRS 8-day surface reflectance composite for May 2024.
viirs202405 = (
  ee.ImageCollection('NASA/VIIRS/002/VNP09H1')
  .filter(ee.Filter.date('2024-05-01', '2024-05-16'))
  .first()
)
# Compute NDVI.
ndvi202405 = (
  viirs202405.select('SurfReflect_I2')
  .subtract(viirs202405.select('SurfReflect_I1'))
  .divide(
    viirs202405.select('SurfReflect_I2').add(
      viirs202405.select('SurfReflect_I1')
    )
  )
)
```
**Note:** the normalized difference operation is available as a shortcut method: [`normalizedDifference()`](https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference). 
Only the intersection of unmasked pixels between the two inputs are considered and returned as unmasked, all else are masked. In general, if either input has only one band, then it is used against all the bands in the other input. If the inputs have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in the first input's order. The type of the output pixels is the union of the input types.
The following example of multi-band image subtraction demonstrates how bands are matched automatically, resulting in a "change vector" for each pixel for each co-occurring band.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_math#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_math#colab-python-sample) More
```
// Load a VIIRS 8-day surface reflectance composite for September 2024.
varviirs202409=ee.ImageCollection('NASA/VIIRS/002/VNP09H1').filter(
ee.Filter.date('2024-09-01','2024-09-16')).first();
// Compute multi-band difference between the September composite and the
// previously loaded May composite.
vardiff=viirs202409.subtract(ndvi202405);
Map.addLayer(diff,{
bands:['SurfReflect_I1','SurfReflect_I2','SurfReflect_I3'],
min:-1,
max:1
},'difference');
// Compute the squared difference in each band.
varsquaredDifference=diff.pow(2);
Map.addLayer(squaredDifference,{
bands:['SurfReflect_I1','SurfReflect_I2','SurfReflect_I3'],
min:0,
max:0.7
},'squared diff.');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a VIIRS 8-day surface reflectance composite for September 2024.
viirs202409 = (
  ee.ImageCollection('NASA/VIIRS/002/VNP09H1')
  .filter(ee.Filter.date('2024-09-01', '2024-09-16'))
  .first()
)
# Compute multi-band difference between the September composite and the
# previously loaded May composite.
diff = viirs202409.subtract(ndvi202405)
m = geemap.Map()
m.add_layer(
  diff,
  {
    'bands': ['SurfReflect_I1', 'SurfReflect_I2', 'SurfReflect_I3'],
    'min': -1,
    'max': 1,
  },
  'difference',
)
# Compute the squared difference in each band.
squared_difference = diff.pow(2)
m.add_layer(
  squared_difference,
  {
    'bands': ['SurfReflect_I1', 'SurfReflect_I2', 'SurfReflect_I3'],
    'min': 0,
    'max': 0.7,
  },
  'squared diff.',
)
display(m)
```

In the second part of this example, the squared difference is computed using `image.pow(2)`. For the complete list of mathematical operators handling basic arithmetic, trigonometry, exponentiation, rounding, casting, bitwise operations and more, see the [API documentation](https://developers.google.com/earth-engine/apidocs).
## Expressions
To implement more complex mathematical expressions, consider using `image.expression()`, which parses a text representation of a math operation. The following example uses `expression()` to compute the Enhanced Vegetation Index (EVI):
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_math#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_math#colab-python-sample) More
```
// Load a Landsat 8 image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
// Compute the EVI using an expression.
varevi=image.expression(
'2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))',{
'NIR':image.select('B5'),
'RED':image.select('B4'),
'BLUE':image.select('B2')
});
Map.centerObject(image,9);
Map.addLayer(evi,{min:-1,max:1,palette:['a6611a','f5f5f5','4dac26']});
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 image.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
# Compute the EVI using an expression.
evi = image.expression(
  '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))',
  {
    'NIR': image.select('B5'),
    'RED': image.select('B4'),
    'BLUE': image.select('B2'),
  },
)
# Define a map centered on San Francisco Bay.
map_evi = geemap.Map(center=[37.4675, -122.1363], zoom=9)
# Add the image layer to the map and display it.
map_evi.add_layer(
  evi, {'min': -1, 'max': 1, 'palette': ['a6611a', 'f5f5f5', '4dac26']}, 'evi'
)
display(map_evi)
```

Observe that the first argument to `expression()` is the textual representation of the math operation, the second argument is a dictionary where the keys are variable names used in the expression and the values are the image bands to which the variables should be mapped. Bands in the image may be referred to as `b("band name")` or `b(index)`, for example `b(0)`, instead of providing the dictionary. Bands can be defined from images other than the input when using the band map dictionary. Note that `expression()` uses "floor division", which discards the remainder and returns an integer when two integers are divided. For example `10 / 20 = 0`. To change this behavior, multiply one of the operands by `1.0`: `10 * 1.0 / 20 = 0.5`. Only the intersection of unmasked pixels are considered and returned as unmasked when bands from more than one source image are evaluated. Supported expression operators are listed in the following table.
Operators for `expression()` Type | Symbol | Name  
---|---|---  
**Arithmetic** | + - * / % ** | Add, Subtract, Multiply, Divide, Modulus, Exponent  
**Relational** | == != < > <= >= | Equal, Not Equal, Less Than, Greater than, etc.  
**Logical** | && || ! ^ | And, Or, Not, Xor  
**Ternary** | ? : | If then else  
