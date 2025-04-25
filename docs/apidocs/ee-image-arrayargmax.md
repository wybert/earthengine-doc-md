 
#  ee.Image.arrayArgmax 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arrayargmax#examples)


Computes the positional indices of the maximum value in image of array values. If there are multiple occurrences of the maximum, the indices reflect the first. 
Usage| Returns  
---|---  
`Image.arrayArgmax()`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayargmax#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayargmax#colab-python-sample) More
```
// A function to print the array for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create a 1D array image.
vararrayImg1D=ee.Image([0,1,5,2,3,4]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 5, 2, 3, 4]
// Get the position of the maximum value in a 1D array.
varmaxValue1D=arrayImg1D.arrayArgmax();
print('Position of the maximum 1D array value',sampArrImg(maxValue1D));
// [2]
// Create a 2D 2x3 array image (reshape the 1D array image).
vararrayImg2D=arrayImg1D.arrayReshape(ee.Image([2,3]).toArray(),2);
print('2D 2x3 array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 1, 5],
// [2, 3, 4]]
// Get the position of the maximum value in a 2D array.
varmaxValue2D=arrayImg2D.arrayArgmax();
print('Position of the maximum 2D array value',sampArrImg(maxValue2D));
// [0, 2]
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
array_img_1d = ee.Image([0, 1, 5, 2, 3, 4]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 5, 2, 3, 4]
# Get the position of the maximum value in a 1D array.
max_value_1d = array_img_1d.arrayArgmax()
print(
  'Position of the maximum 1D array value:',
  samp_arr_img(max_value_1d).getInfo()
  )
# [2]
# Create a 2D 2x3 array image (reshape the 1D array image).
array_img_2d = array_img_1d.arrayReshape(ee.Image([2, 3]).toArray(), 2)
print('2D 2x3 array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0, 1, 5],
# [2, 3, 4]]
# Get the position of the maximum value in a 2D array.
max_value_2d = array_img_2d.arrayArgmax()
print(
  'Position of the maximum 2D array value:',
  samp_arr_img(max_value_2d).getInfo()
)
# [0, 2]
```

Was this helpful?
