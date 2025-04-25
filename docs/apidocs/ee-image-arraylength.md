 
#  ee.Image.arrayLength 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arraylength#examples)


Returns the length of each pixel's array along the given axis. 
Usage| Returns  
---|---  
`Image.arrayLength(axis)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| Input image.  
`axis`| Integer| The axis along which to take the length.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arraylength#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arraylength#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// A 3-band image of constants.
varimg=ee.Image([0,1,2]);
print('3-band image',img);
// Convert the 3-band image to a 2D array image.
vararrayImg2D=img.toArray().toArray(1);
print('2D array image (pixel)',sampArrImg(arrayImg2D));
// [[0],
// [1],
// [2]]
// Get the number of dimensions in each pixel's array.
vararrayImg2Ddim=arrayImg2D.arrayDimensions();
print('N dimensions in array',sampArrImg(arrayImg2Ddim));
// 2
// Get the array length per dimension per pixel.
vararrayImg2DdimLen=arrayImg2D.arrayLengths();
print('Array length per dimension',sampArrImg(arrayImg2DdimLen));
// [3, 1]
// Get the array length for 0-axis (rows).
vararrayImg2Daxis0Len=arrayImg2D.arrayLength(0);
print('Array length 0-axis (rows)',sampArrImg(arrayImg2Daxis0Len));
// 3
// Get the array length for 1-axis (columns).
vararrayImg2Daxis1Len=arrayImg2D.arrayLength(1);
print('Array length 1-axis (columns)',sampArrImg(arrayImg2Daxis1Len));
// 1
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
print('3-band image:', img.getInfo())
# Convert the 3-band image to a 2D array image.
array_img_2d = img.toArray().toArray(1)
print('2D array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0],
# [1],
# [2]]
# Get the number of dimensions in each pixel's array.
array_img2d_dim = array_img_2d.arrayDimensions()
print('N dimensions in array:', samp_arr_img(array_img2d_dim).getInfo())
# 2
# Get the array length per dimension per pixel.
array_img_2d_dim_len = array_img_2d.arrayLengths()
print(
  'Array length per dimension:',
  samp_arr_img(array_img_2d_dim_len).getInfo()
)
# [3, 1]
# Get the array length for 0-axis (rows).
array_img2d_axis0_len = array_img_2d.arrayLength(0)
print(
  'Array length 0-axis (rows):',
  samp_arr_img(array_img2d_axis0_len).getInfo()
)
# 3
# Get the array length for 1-axis (columns).
array_img_2d_axis1_len = array_img_2d.arrayLength(1)
print(
  'Array length 1-axis (columns):',
  samp_arr_img(array_img_2d_axis1_len).getInfo()
)
# 1
```

