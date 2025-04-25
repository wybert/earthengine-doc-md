 
#  ee.Image.arrayPad 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arraypad#examples)


Pads the array values in each pixel to be a fixed length. The pad value will be appended to each array to extend it to given length along each axis. All bands of the image must be array-valued and have the same dimensions. 
Usage| Returns  
---|---  
`Image.arrayPad(lengths,  _pad_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| Array image to pad.  
`lengths`| List| A list of desired lengths for each axis in the output arrays. Arrays are already as large or larger than the given length will be unchanged along that axis.  
`pad`| Number, default: 0| The value to pad with.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arraypad#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arraypad#colab-python-sample) More
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
// Pad 1D array to length of 5 with value 9.
vararrayImg1Dpad=arrayImg1D.arrayPad([5],9);
print('1D array image padded',sampArrImg(arrayImg1Dpad));
// [0, 1, 2, 9, 9]
// Create a 2D array image.
vararrayImg2D=ee.Image([0,1,2,3,4,5]).toArray()
.arrayReshape(ee.Image([2,3]).toArray(),2);
print('2D 2x3 array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 1, 2],
// [3, 4, 5]]
// Pad 2D array to 0-axis length 3 and 1-axis length 5 with value 9.
vararrayImg2Dpad=arrayImg2D.arrayPad([3,5],9);
print('2D array image padded',sampArrImg(arrayImg2Dpad));
// [[0, 1, 2, 9, 9],
// [3, 4, 5, 9, 9],
// [9, 9, 9, 9, 9]]
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
# Pad 1D array to length of 5 with value 9.
array_img_1d_pad = array_img_1d.arrayPad([5], 9)
print('1D array image padded:', samp_arr_img(array_img_1d_pad).getInfo())
# [0, 1, 2, 9, 9]
# Create a 2D array image.
array_img_2d = ee.Image([0, 1, 2, 3, 4, 5]).toArray().arrayReshape(
  ee.Image([2, 3]).toArray(),
  2
)
print('2D 2x3 array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0, 1, 2],
# [3, 4, 5]]
# Pad 2D array to 0-axis length 3 and 1-axis length 5 with value 9.
array_img_2d_pad = array_img_2d.arrayPad([3, 5], 9)
print('2D array image padded:', samp_arr_img(array_img_2d_pad).getInfo())
# [[0, 1, 2, 9, 9],
# [3, 4, 5, 9, 9],
# [9, 9, 9, 9, 9]]
```

Was this helpful?
