 
#  ee.Image.arrayAccum
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arrayaccum#examples)


Accumulates elements of each array pixel along the given axis, by setting each element of the result array pixel to the reduction of elements in that pixel along the given axis, up to and including the current position on the axis. May be used to make a cumulative sum, a monotonically increasing sequence, etc.
Usage | Returns  
---|---  
`Image.arrayAccum(axis, _reducer_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `input` | Image | Input image.  
`axis` | Integer | Axis along which to perform the cumulative sum.  
`reducer` | Reducer, default: null | Reducer to accumulate values. Default is SUM, to produce the cumulative sum of each vector along the given axis.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayaccum#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayaccum#colab-python-sample) More
```
// A function to print the array for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}

// Create a 1D array image.
vararrayImg1D=ee.Image([1,2,3]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [1, 2, 3]

// Perform accumulation procedures along axes using ee.Reducer functions.
// Here we calculate the cumulative sum along the 0-axis for a 1D array.
varaccumSum1DAx0=arrayImg1D.arrayAccum(0,ee.Reducer.sum());
print('Cumulative sum along 0-axis',sampArrImg(accumSum1DAx0));
// [1, 3, 6]

// Create a 2D 3x3 array image.
vararrayImg2D=ee.Image([1,2,3,4,5,6,7,8,9]).toArray()
.arrayReshape(ee.Image([3,3]).toArray(),2);
print('2D 3x3 array image (pixel)',sampArrImg(arrayImg2D));
// [[1, 2, 3],
//  [4, 5, 6],
//  [7, 8, 9]]

// Calculate the cumulative sum along the 0-axis for a 2D array.
varaccumSum2DAx0=arrayImg2D.arrayAccum(0,ee.Reducer.sum());
print('Cumulative sum along 0-axis',sampArrImg(accumSum2DAx0));
// [[ 1,  2,  3],
//  [ 5,  7,  9],
//  [12, 15, 18]]

// Calculate the cumulative sum along the 1-axis for a 2D array.
varaccumSum2DAx1=arrayImg2D.arrayAccum(1,ee.Reducer.sum());
print('Cumulative sum along 1-axis',sampArrImg(accumSum2DAx1));
// [[1,  3,  6],
//  [4,  9, 15],
//  [7, 15, 24]]
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
array_img_1d = ee.Image([1, 2, 3]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [1, 2, 3]

# Perform accumulation procedures along axes using ee.Reducer functions.
# Here we calculate the cumulative sum along the 0-axis for a 1D array.
accum_sum_1d_ax0 = array_img_1d.arrayAccum(0, ee.Reducer.sum())
print('Cumulative sum along 0-axis:', samp_arr_img(accum_sum_1d_ax0).getInfo())
# [1, 3, 6]

# Create a 2D 3x3 array image.
array_img_2d = ee.Image([1, 2, 3, 4, 5, 6, 7, 8, 9]).toArray().arrayReshape(
    ee.Image([3, 3]).toArray(),
    2)
print('2D 3x3 array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# Calculate the cumulative sum along the 0-axis for a 2D array.
accum_sum_2d_ax0 = array_img_2d.arrayAccum(0, ee.Reducer.sum())
print('Cumulative sum along 0-axis:', samp_arr_img(accum_sum_2d_ax0).getInfo())
# [[ 1,  2,  3],
#  [ 5,  7,  9],
#  [12, 15, 18]]

# Calculate the cumulative sum along the 1-axis for a 2D array.
accum_sum_2d_ax1 = array_img_2d.arrayAccum(1, ee.Reducer.sum())
print('Cumulative sum along 1-axis:', samp_arr_img(accum_sum_2d_ax1).getInfo())
# [[1,  3,  6],
#  [4,  9, 15],
#  [7, 15, 24]]
```

Was this helpful?
