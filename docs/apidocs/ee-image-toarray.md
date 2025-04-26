 
#  ee.Image.toArray 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-toarray#examples)


Concatenates pixels from each band into a single array per pixel. The result will be masked if any input bands are masked. 
Usage| Returns  
---|---  
`Image.toArray( _axis_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| Image of bands to convert to an array per pixel. Bands must have scalar pixels, or array pixels with equal dimensionality.  
`axis`| Integer, default: 0| Axis to concatenate along; must be at least 0 and at most the dimension of the inputs. If the axis equals the dimension of the inputs, the result will have 1 more dimension than the inputs.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-toarray#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-toarray#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// A 3-band image of constants.
varimg=ee.Image([0,1,2]);
print('3-band image',img);
// Convert the 3-band image to an array image. The resulting array image has a
// single band named "array". The "array" band stores the per-pixel band values
// from the input ee.Image as a 1D array.
vararrayImg1D=img.toArray();
print('1D array image',arrayImg1D);
// Sample a single pixel to see its 1D array using the `sampArrImg` function
// defined above. Similar arrays are present for all pixels in a given array
// image; looking at just one helps conceptualize the structure.
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 2]
// Array images can be displayed to the Code Editor map and queried with the
// inspector tool. Per-pixel, the first element in the array is shown.
// Single-band grayscale is used to represent the data. Style parameters `min`
// and `max` are valid. Styling the layer with the Code Editor's layer
// visualization tool is invalid.
Map.addLayer(arrayImg1D,{min:0,max:2},'Image array');
// Create a 2D array image by concatenating the values in a 1D array image
// along the 1-axis using `toArray(1)`. For a 3D array, apply `toArray(2)` to
// the result.
vararrayImg2D=arrayImg1D.toArray(1);
print('2D array image (pixel)',sampArrImg(arrayImg2D));
// [[0],
// [1],
// [2]]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A function to print arrays for a selected pixel in the following examples.
defsamp_arr_img(arr_img):
 point = ee.Geometry.Point([-121, 42])
 return arr_img.sample(point, 500).first().get('array')

# A 3-band image of constants.
img = ee.Image([0, 1, 2])
display('3-band image', img)
# Convert the 3-band image to an array image. The resulting array image has a
# single band named "array". The "array" band stores the per-pixel band values
# from the input ee.Image as a 1D array.
array_img_1_d = img.toArray()
display('1D array image', array_img_1_d)
# Sample a single pixel to see its 1D array using the `samp_arr_img` function
# defined above. Similar arrays are present for all pixels in a given array
# image looking at just one helps conceptualize the structure.
display('1D array image (pixel)', samp_arr_img(array_img_1_d))
# [0, 1, 2]
# Array images can be displayed to the Code Editor map and queried with the
# inspector tool. Per-pixel, the first element in the array is shown.
# Single-band grayscale is used to represent the data. Style parameters `min`
# and `max` are valid. Styling the layer with the Code Editor's layer
# visualization tool is invalid.
m = geemap.Map()
m.add_layer(array_img_1_d, {'min': 0, 'max': 2}, 'Image array')
display(m)
# Create a 2D array image by concatenating the values in a 1D array image
# along the 1-axis using `toArray(1)`. For a 3D array, apply `toArray(2)` to
# the result.
array_img_2_d = array_img_1_d.toArray(1)
display('2D array image (pixel)', samp_arr_img(array_img_2_d))
# [[0],
# [1],
# [2]]
```

