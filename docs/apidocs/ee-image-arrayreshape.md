 
#  ee.Image.arrayReshape
Stay organized with collections  Save and categorize content based on your preferences. 
Converts array bands of an image with equally-shaped, possibly multidimensional pixels to an image of arrays with a new shape. Usage | Returns  
---|---  
`Image.arrayReshape(lengths, dimensions)` | Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image of arrays to reshape.  
`lengths` | Image | A 1-band image specifying the new lengths of each axis of the input image specified as a 1-D array per pixel. There should be 'dimensions' lengths values in each shape' array. If one of the lengths is -1, then the corresponding length for that axis will be computed such that the total size remains constant. In particular, a shape of [-1] flattens into 1-D. At most one component of shape can be -1.  
`dimensions` | Integer | The number of dimensions shared by all output array pixels.  
## Examples
### Code Editor (JavaScript)
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

// Reshape the 1D 6-element array to a 2D 2 (row) x 3 (column) array. Notice
// that elements are filled row by row in the reshaped result.
varreshape2x3=arrayImg1D.arrayReshape(ee.Image([2,3]).toArray(),2);
print('2D 2x3 array image (pixel)',sampArrImg(reshape2x3));
// [[0, 1, 2],
//  [3, 4, 5]]

// Use -1 to auto-determine a dimension length. For example, here we set
// 3 rows and let Earth Engine determine the number of columns needed.
varreshape3x_=arrayImg1D.arrayReshape(ee.Image([3,-1]).toArray(),2);
print('2D 3x? array image (pixel)',sampArrImg(reshape3x_));
// [[0, 1],
//  [2, 3],
//  [4, 5]]

// Flatten a 2D 2x3 array to 1D 6-element array.
varflattened=reshape2x3.arrayReshape(ee.Image([-1]).toArray(),1);
print('2D array flattened to 1D',sampArrImg(flattened));
// [0, 1, 2, 3, 4, 5]
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A function to print arrays for a selected pixel in the following examples.
defsamp_arr_img(arr_img):
  point = ee.Geometry.Point([-121, 42])
  return arr_img.sample(point, 500).first().get('array')

# Create a 1D array image with length 6.
array_img_1d = ee.Image([0, 1, 2, 3, 4, 5]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 2, 3, 4, 5]

# Reshape the 1D 6-element array to a 2D 2 (row) x 3 (column) array. Notice
# that elements are filled row by row in the reshaped result.
reshape2x3 = array_img_1d.arrayReshape(ee.Image([2, 3]).toArray(), 2)
print('2D 2x3 array image (pixel):', samp_arr_img(reshape2x3).getInfo())
# [[0, 1, 2],
#  [3, 4, 5]]

# Use -1 to auto-determine a dimension length. For example, here we set
# 3 rows and let Earth Engine determine the number of columns needed.
reshape3x_ = array_img_1d.arrayReshape(ee.Image([3, -1]).toArray(), 2)
print('2D 3x? array image (pixel):', samp_arr_img(reshape3x_).getInfo())
# [[0, 1],
#  [2, 3],
#  [4, 5]]

# Flatten a 2D 2x3 array to 1D 6-element array.
flattened = reshape2x3.arrayReshape(ee.Image([-1]).toArray(), 1)
print('2D array flattened to 1D:', samp_arr_img(flattened).getInfo())
# [0, 1, 2, 3, 4, 5]
```

