 
#  ee.Image.arrayReduce
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arrayreduce#examples)


Reduces elements of each array pixel.
Usage | Returns  
---|---  
`Image.arrayReduce(reducer, axes, _fieldAxis_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `input` | Image | Input image.  
`reducer` | Reducer | The reducer to apply.  
`axes` | List | The list of array axes to reduce in each pixel. The output will have a length of 1 in all these axes.  
`fieldAxis` | Integer, default: null | The axis for the reducer's input and output fields. Only required if the reducer has multiple inputs or outputs.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayreduce#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arrayreduce#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}

// Create a 1D array image with length 6.
vararrayImg1D=ee.Image([0,1,2,3,4,5]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 2, 3, 4, 5]

// Sum the elements in the 1D array image.
vararrayImg1Dsum=arrayImg1D.arrayReduce(ee.Reducer.sum(),[0]);
print('1D array image sum (pixel)',sampArrImg(arrayImg1Dsum));
// [15]

// Create a 2D array image with 2 rows and 3 columns.
vararrayImg2D=arrayImg1D.arrayReshape(ee.Image([2,3]).toArray(),2);
print('2D array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 1, 2],
//  [3, 4, 5]]

// Sum 2D array image along 0-axis.
vararrayImg2DsumRow=arrayImg2D.arrayReduce(ee.Reducer.sum(),[0]);
print('2D array image sum rows (pixel)',sampArrImg(arrayImg2DsumRow));
// [[3, 5, 7]]

// Sum 2D array image along 1-axis.
vararrayImg2DsumCol=arrayImg2D.arrayReduce(ee.Reducer.sum(),[1]);
print('2D array image sum columns (pixel)',sampArrImg(arrayImg2DsumCol));
// [[3],
//  [12]]

// Sum 2D array image 0-axis and 1-axis.
vararrayImg2DsumRowCol=arrayImg2D.arrayReduce(ee.Reducer.sum(),[0,1]);
print('2D array image sum columns (pixel)',sampArrImg(arrayImg2DsumRowCol));
// [[15]]

// For reducers that provide several outputs (like minMax and percentile),
// you need to ensure you have a dimension to hold the results. For instance,
// if you want minMax for a 1D array, add a second dimension.
vararrayImg1Dto2D=arrayImg1D.toArray(1);
print('1D array image to 2D',sampArrImg(arrayImg1Dto2D));
// [[0],
//  [1],
//  [2],
//  [3],
//  [4],
//  [5]]

// Calculate min and max for 2D array, use the fieldAxis parameter.
varminMax1D=arrayImg1Dto2D.arrayReduce(ee.Reducer.minMax(),[0],1);
print('1D array image minMax (pixel)',sampArrImg(minMax1D));
// [[0, 5]]

// If your array image is 2D and you want min and max, add a third dimension.
vararrayImg2Dto3D=arrayImg2D.toArray(2);
print('2D array image to 3D',sampArrImg(arrayImg2Dto3D));
// [[[0], [1], [2]],
//  [[3], [4], [5]]]

// Calculate min and max along the 0-axis, store results in 2-axis.
varminMax2D=arrayImg2Dto3D.arrayReduce(ee.Reducer.minMax(),[0],2);
print('2D array image minMax (pixel)',sampArrImg(minMax2D));
// [[[0, 3],
//   [1, 4],
//   [2, 5]]]
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

# Create a 1D array image with length 6.
array_img_1d = ee.Image([0, 1, 2, 3, 4, 5]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 2, 3, 4, 5]

# Sum the elements in the 1D array image.
array_img_1d_sum = array_img_1d.arrayReduce(ee.Reducer.sum(), [0])
print('1D array image sum (pixel):', samp_arr_img(array_img_1d_sum).getInfo())
# [15]

# Create a 2D array image with 2 rows and 3 columns.
array_img_2d = array_img_1d.arrayReshape(ee.Image([2, 3]).toArray(), 2)
print('2D array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0, 1, 2],
#  [3, 4, 5]]

# Sum 2D array image along 0-axis.
array_img_2d_sum_row = array_img_2d.arrayReduce(ee.Reducer.sum(), [0])
print(
    '2D array image sum rows (pixel):',
    samp_arr_img(array_img_2d_sum_row).getInfo()
)
# [[3, 5, 7]]

# Sum 2D array image along 1-axis.
array_img_2d_sum_col = array_img_2d.arrayReduce(ee.Reducer.sum(), [1])
print(
    '2D array image sum columns (pixel):',
    samp_arr_img(array_img_2d_sum_col).getInfo()
)
# [[3],
#  [12]]

# Sum 2D array image 0-axis and 1-axis.
array_img_2d_sum_row_col = array_img_2d.arrayReduce(ee.Reducer.sum(), [0, 1])
print(
    '2D array image sum columns (pixel):',
    samp_arr_img(array_img_2d_sum_row_col).getInfo()
)
# [[15]]

# For reducers that provide several outputs (like minMax and percentile),
# you need to ensure you have a dimension to hold the results. For instance,
# if you want minMax for a 1D array, add a second dimension.
array_img_1d_to_2d = array_img_1d.toArray(1)
print('1D array image to 2D:', samp_arr_img(array_img_1d_to_2d).getInfo())
# [[0],
#  [1],
#  [2],
#  [3],
#  [4],
#  [5]]

# Calculate min and max for 2D array, use the fieldAxis parameter.
min_max_1d = array_img_1d_to_2d.arrayReduce(ee.Reducer.minMax(), [0], 1)
print('1D array image minMax (pixel):', samp_arr_img(min_max_1d).getInfo())
# [[0, 5]]

# If your array image is 2D and you want min and max, add a third dimension.
array_img_2d_to_3d = array_img_2d.toArray(2)
print('2D array image to 3D:', samp_arr_img(array_img_2d_to_3d).getInfo())
# [[[0], [1], [2]],
#  [[3], [4], [5]]]

# Calculate min and max along the 0-axis, store results in 2-axis.
min_max_2d = array_img_2d_to_3d.arrayReduce(ee.Reducer.minMax(), [0], 2)
print('2D array image minMax (pixel):', samp_arr_img(min_max_2d).getInfo())
# [[[0, 3],
#   [1, 4],
#   [2, 5]]]
```

Was this helpful?
