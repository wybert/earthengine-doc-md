 
#  ee.Image.arraySlice
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arrayslice#examples)


Creates a subarray by slicing out each position along the given axis from the 'start' (inclusive) to 'end' (exclusive) by increments of 'step'. The result will have as many dimensions as the input, and the same length in all directions except the slicing axis, where the length will be the number of positions from 'start' to 'end' by 'step' that are in range of the input array's length along 'axis'. This means the result can be length 0 along the given axis if start=end, or if the start or end values are entirely out of range. 
Usage| Returns  
---|---  
`Image.arraySlice( _axis_, _start_, _end_, _step_)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| Input array image.  
`axis`| Integer, default: 0| Axis to subset.  
`start`| Image, default: null| The coordinate of the first slice (inclusive) along 'axis'. Negative numbers are used to position the start of slicing relative to the end of the array, where -1 starts at the last position on the axis, -2 starts at the next to last position, etc. There must one band for start indices, or one band per 'input' band. If this argument is not set or masked at some pixel, then the slice at that pixel will start at index 0.  
`end`| Image, default: null| The coordinate (exclusive) at which to stop taking slices. By default this will be the length of the given axis. Negative numbers are used to position the end of slicing relative to the end of the array, where -1 will exclude the last position, -2 will exclude the last two positions, etc. There must be one band for end indices, or one band per 'input' band. If this argument is not set or masked at some pixel, then the slice at that pixel will end just after the last index.  
`step`| Integer, default: 1| The separation between slices along 'axis'; a slice will be taken at each whole multiple of 'step' from 'start' (inclusive) to 'end' (exclusive). Must be positive.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayslice#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayslice#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create a 1D array image with length 12.
vararrayImg1D=ee.Image([0,1,2,3,4,5,6,7,8,9,10,11]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
// Get the first 3 elements.
print('1D array image first 3 elements (pixel)',
sampArrImg(arrayImg1D.arraySlice(0,0,3)));
// [0, 1, 2]
// Get the last 3 elements.
print('1D array image last 3 elements (pixel)',
sampArrImg(arrayImg1D.arraySlice(0,-3)));
// [9, 10, 11]
// Get elements at index positions 3 through 5 (0-based).
print('1D array image elements at index positions 3 through 5 (pixel)',
sampArrImg(arrayImg1D.arraySlice(0,3,6)));
// [3, 4, 5]
// Get elements at index positions 4 through end (0-based).
print('1D array image elements at index positions 4 through end (pixel)',
sampArrImg(arrayImg1D.arraySlice(0,4)));
// [4, 5, 6, 7, 8, 9, 10, 11]
// Get elements using a step of 3.
print('1D array image elements at a step of 3 (pixel)',
sampArrImg(arrayImg1D.arraySlice(0,0,null,3)));
// [0, 3, 6, 9]
// Create a 2D array image with 3 rows and 4 columns.
vararrayImg2D=arrayImg1D.arrayReshape(ee.Image([3,4]).toArray(),2);
print('2D array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 1, 2, 3],
// [4, 5, 6, 7],
// [8, 9, 10, 11]]
// Get the second row.
print('2D array image second row (pixel)',
sampArrImg(arrayImg2D.arraySlice(0,1,2)));
// [[4, 5, 6, 7]
// Get the second column.
print('2D array image second column (pixel)',
sampArrImg(arrayImg2D.arraySlice(1,1,2)));
// [[1],
// [5],
// [9]]
// Get all columns except the last.
print('2D array image all columns except last (pixel)',
sampArrImg(arrayImg2D.arraySlice(1,0,-1)));
// [[0, 1, 2],
// [4, 5, 6],
// [8, 9, 10]]
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
# Create a 1D array image with length 12.
array_img_1d = ee.Image([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# Get the first 3 elements.
print('1D array image first 3 elements (pixel):',
   samp_arr_img(array_img_1d.arraySlice(0, 0, 3)).getInfo())
# [0, 1, 2]
# Get the last 3 elements.
print('1D array image last 3 elements (pixel):',
   samp_arr_img(array_img_1d.arraySlice(0, -3)).getInfo())
# [9, 10, 11]
# Get elements at index positions 3 through 5 (0-based).
print('1D array image elements at index positions 3 through 5 (pixel):',
   samp_arr_img(array_img_1d.arraySlice(0, 3, 6)).getInfo())
# [3, 4, 5]
# Get elements at index positions 4 through end (0-based).
print('1D array image elements at index positions 4 through end (pixel)',
   samp_arr_img(array_img_1d.arraySlice(0, 4)).getInfo())
# [4, 5, 6, 7, 8, 9, 10, 11]
# Get elements using a step of 3.
print('1D array image elements at a step of 3 (pixel)',
   samp_arr_img(array_img_1d.arraySlice(0, 0, None, 3)).getInfo())
# [0, 3, 6, 9]
# Create a 2D array image with 3 rows and 4 columns.
array_img_2d = array_img_1d.arrayReshape(ee.Image([3, 4]).toArray(), 2)
print('2D array image (pixel)', samp_arr_img(array_img_2d).getInfo())
# [[0, 1, 2, 3],
# [4, 5, 6, 7],
# [8, 9, 10, 11]]
# Get the second row.
print('2D array image second row (pixel):',
   samp_arr_img(array_img_2d.arraySlice(0, 1, 2)).getInfo())
# [[4, 5, 6, 7]
# Get the second column.
print('2D array image second column (pixel):',
   samp_arr_img(array_img_2d.arraySlice(1, 1, 2)).getInfo())
# [[1],
# [5],
# [9]]
# Get all columns except the last.
print('2D array image all columns except last (pixel):',
   samp_arr_img(array_img_2d.arraySlice(1, 0, -1)).getInfo())
# [[0, 1, 2],
# [4, 5, 6],
# [8, 9, 10]]
```

Was this helpful?
