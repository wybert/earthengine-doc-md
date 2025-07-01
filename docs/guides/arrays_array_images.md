 
#  Arrays and Array Images
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Arrays in Earth Engine are constructed from lists of numbers and lists of lists. The degree of nesting determines the number of dimensions. To get started with a simple, motivated example, consider the following example of an `Array` created from Landsat 8 tasseled cap (TC) coefficients ([Baig et al., 2014](http://dx.doi.org/10.1080/2150704X.2014.915434)):
### Code Editor (JavaScript)
```
// Create an Array of Tasseled Cap coefficients.
varcoefficients=ee.Array([
[0.3029,0.2786,0.4733,0.5599,0.508,0.1872],
[-0.2941,-0.243,-0.5424,0.7276,0.0713,-0.1608],
[0.1511,0.1973,0.3283,0.3407,-0.7117,-0.4559],
[-0.8239,0.0849,0.4396,-0.058,0.2013,-0.2773],
[-0.3294,0.0557,0.1056,0.1855,-0.4349,0.8085],
[0.1079,-0.9023,0.4119,0.0575,-0.0259,0.0252],
]);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create an Array of Tasseled Cap coefficients.
coefficients = ee.Array([
  [0.3029, 0.2786, 0.4733, 0.5599, 0.508, 0.1872],
  [-0.2941, -0.243, -0.5424, 0.7276, 0.0713, -0.1608],
  [0.1511, 0.1973, 0.3283, 0.3407, -0.7117, -0.4559],
  [-0.8239, 0.0849, 0.4396, -0.058, 0.2013, -0.2773],
  [-0.3294, 0.0557, 0.1056, 0.1855, -0.4349, 0.8085],
  [0.1079, -0.9023, 0.4119, 0.0575, -0.0259, 0.0252],
])
```

Confirm that this is a 6x6, 2-D Array using `length()`, which will return the lengths of each axis:
### Code Editor (JavaScript)
```
// Print the dimensions.
print(coefficients.length());//  [6,6]
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Print the dimensions.
display(coefficients.length()) #  [6,6]
```

The following table illustrates the arrangement of the matrix entries along the 0-axis and the 1-axis:
| | 1-axis ->  
---|---|---  
| | **0**| **1**| **2**| **3**| **4**| **5**  
| **0**|  0.3029| 0.2786| 0.4733| 0.5599| 0.508| 0.1872  
| **1**|  -0.2941| -0.243| -0.5424| 0.7276| 0.0713| -0.1608  
**0-axis**| **2**|  0.1511| 0.1973| 0.3283| 0.3407| -0.7117| -0.4559  
| **3**|  -0.8239| 0.0849| 0.4396| -0.058| 0.2013| -0.2773  
| **4**|  -0.3294| 0.0557| 0.1056| 0.1855| -0.4349| 0.8085  
| **5**|  0.1079| -0.9023| 0.4119| 0.0575| -0.0259| 0.0252  
The indices on the left of the table indicate positions along the 0-axis. The n-th element within each list on the 0-axis is in the n-th position along the 1-axis. For example, the entry at coordinate [3,1] of the array is 0.0849. Suppose ‘greenness’ is the TC component of interest. You can get the greenness sub-matrix using `slice()`: 
### Code Editor (JavaScript)
```
// Get the 1x6 greenness slice, display it.
vargreenness=coefficients.slice({axis:0,start:1,end:2,step:1});
print(greenness);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Get the 1x6 greenness slice, display it.
greenness = coefficients.slice(axis=0, start=1, end=2, step=1)
display(greenness)
```

The 2-D greenness matrix should look something like:
```
[[-0.2941,-0.243,-0.5424,0.7276,0.0713,-0.1608]]
  
```

Observe that the `start` and `end` parameters of `slice()` correspond to the 0-axis indices displayed in the table (`start` is inclusive and `end` is exclusive).
##  Array Images 
To get a greenness image, matrix multiply the bands of a Landsat 8 image by the greenness matrix. To do that, first convert the multi-band Landsat image into an “Array Image”, where each pixel is an `Array` of band values. For example:
### Code Editor (JavaScript)
```
// Load a Landsat 8 image, select the bands of interest.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
.select(['B2','B3','B4','B5','B6','B7']);
// Make an Array Image, with a 1-D Array per pixel.
vararrayImage1D=image.toArray();
// Make an Array Image with a 2-D Array per pixel, 6x1.
vararrayImage2D=arrayImage1D.toArray(1);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a Landsat 8 image, select the bands of interest.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318').select(
  ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']
)
# Make an Array Image, with a 1-D Array per pixel.
array_image_1d = image.toArray()
# Make an Array Image with a 2-D Array per pixel, 6x1.
array_image_2d = array_image_1d.toArray(1)
```

In this example, note that `toArray()` converts `image` to an array image in which each pixel is a 1-D vector, the entries of which correspond to the 6 values at the corresponding positions in the bands of `image`. An array image of 1-D vectors created in this manner has no concept of 2-D shape. To perform 2-D only operations such as matrix multiplication, convert it into a 2-D array per-pixel image with `toArray(1)`. In each pixel of the 2-D array image, there is a 6x1 matrix of band values. To see this, consider the following toy example:
### Code Editor (JavaScript)
```
vararray1D=ee.Array([1,2,3]);// [1,2,3]
vararray2D=ee.Array.cat([array1D],1);// [[1],[2],[3]]
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
array_1d = ee.Array([1, 2, 3]) # [1,2,3]
array_2d = ee.Array.cat([array_1d], 1) # [[1],[2],[3]]
```

Observe that the `array1D` vector varies along the 0-axis. The `array2D` matrix does as well, but it’s got an extra dimension. Calling `toArray(1)` on the array image is like calling `cat(bandVector, 1)` on every pixel. Using the 2-D array image, left multiply by an image where each pixel contains a 2-D matrix of greenness coefficients:
### Code Editor (JavaScript)
```
// Do a matrix multiplication: 1x6 times 6x1.
// Cast the greenness Array to an Image prior to multiplication.
vargreennessArrayImage=ee.Image(greenness).matrixMultiply(arrayImage2D);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Do a matrix multiplication: 1x6 times 6x1.
# Cast the greenness Array to an Image prior to multiplication.
greenness_array_image = ee.Image(greenness).matrixMultiply(array_image_2d)
```

The result is a new array image where every pixel is the 1x1 matrix that results from matrix multiplying the 1x6 greenness matrix (left) and the 6x1 band matrix (right). For display purposes, convert to a regular, one-band image with `arrayGet()`:
### Code Editor (JavaScript)
```
// Get the result from the 1x1 array in each pixel of the 2-D array image.
vargreennessImage=greennessArrayImage.arrayGet([0,0]);
// Display the input imagery with the greenness result.
Map.setCenter(-122.3,37.562,10);
Map.addLayer(image,{bands:['B5','B4','B3'],min:0,max:0.5},'image');
Map.addLayer(greennessImage,{min:-0.1,max:0.13},'greenness');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Get the result from the 1x1 array in each pixel of the 2-D array image.
greenness_image = greenness_array_image.arrayGet([0, 0])
# Display the input imagery with the greenness result.
m = geemap.Map()
m.set_center(-122.3, 37.562, 10)
m.add_layer(image, {'bands': ['B5', 'B4', 'B3'], 'min': 0, 'max': 0.5}, 'image')
m.add_layer(greenness_image, {'min': -0.1, 'max': 0.13}, 'greenness')
m
```

Here is a complete example, which uses the entire coefficients array to compute multiple tasseled cap components at once and display the result:
### Code Editor (JavaScript)
```
// Define an Array of Tasseled Cap coefficients.
varcoefficients=ee.Array([
[0.3029,0.2786,0.4733,0.5599,0.508,0.1872],
[-0.2941,-0.243,-0.5424,0.7276,0.0713,-0.1608],
[0.1511,0.1973,0.3283,0.3407,-0.7117,-0.4559],
[-0.8239,0.0849,0.4396,-0.058,0.2013,-0.2773],
[-0.3294,0.0557,0.1056,0.1855,-0.4349,0.8085],
[0.1079,-0.9023,0.4119,0.0575,-0.0259,0.0252],
]);
// Load a Landsat 8 image, select the bands of interest.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
.select(['B2','B3','B4','B5','B6','B7']);
// Make an Array Image, with a 1-D Array per pixel.
vararrayImage1D=image.toArray();
// Make an Array Image with a 2-D Array per pixel, 6x1.
vararrayImage2D=arrayImage1D.toArray(1);
// Do a matrix multiplication: 6x6 times 6x1.
varcomponentsImage=ee.Image(coefficients)
.matrixMultiply(arrayImage2D)
// Get rid of the extra dimensions.
.arrayProject([0])
.arrayFlatten(
[['brightness','greenness','wetness','fourth','fifth','sixth']]);
// Display the first three bands of the result and the input imagery.
varvizParams={
bands:['brightness','greenness','wetness'],
min:-0.1,max:[0.5,0.1,0.1]
};
Map.setCenter(-122.3,37.562,10);
Map.addLayer(image,{bands:['B5','B4','B3'],min:0,max:0.5},'image');
Map.addLayer(componentsImage,vizParams,'components');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Define an Array of Tasseled Cap coefficients.
coefficients = ee.Array([
  [0.3029, 0.2786, 0.4733, 0.5599, 0.508, 0.1872],
  [-0.2941, -0.243, -0.5424, 0.7276, 0.0713, -0.1608],
  [0.1511, 0.1973, 0.3283, 0.3407, -0.7117, -0.4559],
  [-0.8239, 0.0849, 0.4396, -0.058, 0.2013, -0.2773],
  [-0.3294, 0.0557, 0.1056, 0.1855, -0.4349, 0.8085],
  [0.1079, -0.9023, 0.4119, 0.0575, -0.0259, 0.0252],
])
# Load a Landsat 8 image, select the bands of interest.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318').select(
  ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']
)
# Make an Array Image, with a 1-D Array per pixel.
array_image_1d = image.toArray()
# Make an Array Image with a 2-D Array per pixel, 6x1.
array_image_2d = array_image_1d.toArray(1)
# Do a matrix multiplication: 6x6 times 6x1.
components_image = (
  ee.Image(coefficients)
  .matrixMultiply(array_image_2d)
  # Get rid of the extra dimensions.
  .arrayProject([0])
  .arrayFlatten(
    [['brightness', 'greenness', 'wetness', 'fourth', 'fifth', 'sixth']]
  )
)
# Display the first three bands of the result and the input imagery.
viz_params = {
  'bands': ['brightness', 'greenness', 'wetness'],
  'min': -0.1,
  'max': [0.5, 0.1, 0.1],
}
m = geemap.Map()
m.set_center(-122.3, 37.562, 10)
m.add_layer(image, {'bands': ['B5', 'B4', 'B3'], 'min': 0, 'max': 0.5}, 'image')
m.add_layer(components_image, viz_params, 'components')
m
```

Note that when getting bands from an array image, first get rid of the extra dimensions with `project()`, then convert it back to a regular image with `arrayFlatten()`. The output should look something like:
![tasseled cap image](https://developers.google.com/static/earth-engine/images/Arrays_tasseled_cap.png) Figure 1. Tasseled cap components “brightness” (red), “greenness” (green), and “wetness” (blue). 
