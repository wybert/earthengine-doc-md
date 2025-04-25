 
#  ee.Image.arrayTranspose 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arraytranspose#examples)


Transposes two dimensions of each array pixel. 
Usage| Returns  
---|---  
`Image.arrayTranspose( _axis1_, _axis2_)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| Input image.  
`axis1`| Integer, default: 0| First axis to swap.  
`axis2`| Integer, default: 1| Second axis to swap.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arraytranspose#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arraytranspose#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create a 2D array image.
vararrayImg2D=ee.Image([0,1,2,3,4,5]).toArray().arrayReshape(
ee.Image([2,3]).toArray(),2);
print('2D 2x3 array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 1, 2],
// [3, 4, 5]]
// Swap 0-axis and 1-axis. Input is a 2x3 array, output will be 3x2.
vartransposed=arrayImg2D.arrayTranspose();
print('Transposed (3x2) array image (pixel)',sampArrImg(transposed));
// [[0, 3],
// [1, 4],
// [2, 5]]
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
# Create a 2D array image.
array_img_2d = ee.Image([0, 1, 2, 3, 4, 5]).toArray().arrayReshape(
  ee.Image([2, 3]).toArray(),
  2
)
print('2D 2x3 array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0, 1, 2],
# [3, 4, 5]]
# Swap 0-axis and 1-axis. Input is a 2x3 array, output will be 3x2.
transposed = array_img_2d.arrayTranspose()
print('Transposed (3x2) array image (pixel):',
   samp_arr_img(transposed).getInfo())
# [[0, 3],
# [1, 4],
# [2, 5]]
```

