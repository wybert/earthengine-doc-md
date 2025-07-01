 
#  ee.Image.arrayRepeat
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arrayrepeat#examples)


Repeats each array pixel along the given axis. Each output pixel will have the shape of the input pixel, except length along the repeated axis, which will be multiplied by the number of copies. 
Usage| Returns  
---|---  
`Image.arrayRepeat(axis, copies)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| Image of array pixels to be repeated.  
`axis`| Integer| Axis along which to repeat each pixel's array.  
`copies`| Image| Number of copies of each pixel.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayrepeat#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayrepeat#colab-python-sample) More
```
// A function to print the array for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create a 1D array image.
vararrayImg1D=ee.Image([0,1,2]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 2]
// Repeat a 1D array along the 0-axis 3 times.
varrepeat1DAx0=arrayImg1D.arrayRepeat(0,3);
print('1D array repeated 3 times on 0-axis',sampArrImg(repeat1DAx0));
// [0, 1, 2, 0, 1, 2, 0, 1, 2]
// Repeat a 1D array along the 1-axis 3 times (expands the dimensions).
varrepeat1DAx1=arrayImg1D.arrayRepeat(1,3);
print('1D array repeated 3 times on 1-axis',sampArrImg(repeat1DAx1));
// [[0, 0, 0],
// [1, 1, 1],
// [2, 2, 2]]
// Repeat a 2D array along the 0-axis 2 times.
varrepeat2DAx0=repeat1DAx1.arrayRepeat(0,2);
print('2D array repeated 2 times on 0-axis',sampArrImg(repeat2DAx0));
// [[0, 0, 0],
// [1, 1, 1],
// [2, 2, 2],
// [0, 0, 0],
// [1, 1, 1],
// [2, 2, 2]]
// Repeat a 2D array along the 1-axis 2 times.
varrepeat2DAx1=repeat1DAx1.arrayRepeat(1,2);
print('2D array repeated 2 times on 1-axis',sampArrImg(repeat2DAx1));
// [[0, 0, 0, 0, 0, 0],
// [1, 1, 1, 1, 1, 1],
// [2, 2, 2, 2, 2, 2]]
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A function to print the array for a selected pixel in the following examples.
defsamp_arr_img(arr_img):
 point = ee.Geometry.Point([-121, 42])
 return arr_img.sample(point, 500).first().get('array')
# Create a 1D array image.
array_img_1d = ee.Image([0, 1, 2]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 2]
# Repeat a 1D array along the 0-axis 3 times.
repeat_1d_ax0 = array_img_1d.arrayRepeat(0, 3)
print(
  '1D array repeated 3 times on 0-axis:',
  samp_arr_img(repeat_1d_ax0).getInfo()
)
# [0, 1, 2, 0, 1, 2, 0, 1, 2]
# Repeat a 1D array along the 1-axis 3 times (expands the dimensions).
repeat_1d_ax1 = array_img_1d.arrayRepeat(1, 3)
print(
  '1D array repeated 3 times on 1-axis:',
  samp_arr_img(repeat_1d_ax1).getInfo()
)
# [[0, 0, 0],
# [1, 1, 1],
# [2, 2, 2]]
# Repeat a 2D array along the 0-axis 2 times.
repeat_2d_ax0 = repeat_1d_ax1.arrayRepeat(0, 2)
print(
  '2D array repeated 2 times on 0-axis:',
  samp_arr_img(repeat_2d_ax0).getInfo()
)
# [[0, 0, 0],
# [1, 1, 1],
# [2, 2, 2],
# [0, 0, 0],
# [1, 1, 1],
# [2, 2, 2]]
# Repeat a 2D array along the 1-axis 2 times.
repeat_2d_ax1 = repeat_1d_ax1.arrayRepeat(1, 2)
print(
  '2D array repeated 2 times on 1-axis:',
  samp_arr_img(repeat_2d_ax1).getInfo()
)
# [[0, 0, 0, 0, 0, 0],
# [1, 1, 1, 1, 1, 1],
# [2, 2, 2, 2, 2, 2]]
```

Was this helpful?
