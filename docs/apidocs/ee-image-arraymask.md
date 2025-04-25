 
#  ee.Image.arrayMask 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arraymask#examples)


Creates an array image where each array-valued pixel is masked with another array-valued pixel, retaining only the elements where the mask is non-zero. If the mask image has one band it will be applied to all the bands of 'input', otherwise they must have the same number of bands. 
Usage| Returns  
---|---  
`Image.arrayMask(mask)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| Array image to mask.  
`mask`| Image| Array image to mask with.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arraymask#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arraymask#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create a 1D array image with length 6.
vararrayImg1D=ee.Image([0,1,2,4,0,5]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 2, 4, 0, 5]
// Create a mask using a relational operator to mask values greater than 2.
varmask1D=arrayImg1D.lte(2);
print('1D mask for greater than value 2 (pixel)',sampArrImg(mask1D));
// [1, 1, 1, 0, 1, 0]
vararrayImg1DMask=arrayImg1D.arrayMask(mask1D);
print('1D array image mask (pixel)',sampArrImg(arrayImg1DMask));
// [0, 1, 2, 0]
// Self mask the 1D array image. Value zero will be masked out.
vararrayImg1DselfMask=arrayImg1D.arrayMask(arrayImg1D);
print('1D array image self mask (pixel)',sampArrImg(arrayImg1DselfMask));
// [1, 2, 4, 5]
// Create a 2D array image.
vararrayImg2D=arrayImg1D.arrayReshape(ee.Image([2,3]).toArray(),2);
print('2D 2x3 array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 1, 2],
// [4, 0, 5]]
// Slice out a row to use as a column mask.
varrowAsMaskForCols=arrayImg2D.arraySlice(0,1,2);
print('2D mask for cols (pixel)',sampArrImg(rowAsMaskForCols));
// [[4, 0, 5]]
vararrayImg2DMaskCols=arrayImg2D.arrayMask(rowAsMaskForCols);
print('2D array image cols masked (pixel)',sampArrImg(arrayImg2DMaskCols));
// [[0, 2],
// [4, 5]]
// Slice out a column to use as a row mask.
varcolAsMaskForRows=arrayImg2D.arraySlice(1,1,2);
print('2D mask for rows (pixel)',sampArrImg(colAsMaskForRows));
// [[1],
// [0]]
vararrayImg2DMaskRows=arrayImg2D.arrayMask(colAsMaskForRows);
print('2D array image rows masked (pixel)',sampArrImg(arrayImg2DMaskRows));
// [[0, 1, 2]]
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
array_img_1d = ee.Image([0, 1, 2, 4, 0, 5]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 2, 4, 0, 5]
# Create a mask using a relational operator to mask values greater than 2.
mask_1d = array_img_1d.lte(2)
print(
  '1D mask for greater than value 2 (pixel):',
  samp_arr_img(mask_1d).getInfo()
)
# [1, 1, 1, 0, 1, 0]
array_img1d_mask = array_img_1d.arrayMask(mask_1d)
print('1D array image mask (pixel):', samp_arr_img(array_img1d_mask).getInfo())
# [0, 1, 2, 0]
# Self mask the 1D array image. Value zero will be masked out.
array_img_1d_self_mask = array_img_1d.arrayMask(array_img_1d)
print(
  '1D array image self mask (pixel):',
  samp_arr_img(array_img_1d_self_mask).getInfo()
)
# [1, 2, 4, 5]
# Create a 2D array image.
array_img_2d = array_img_1d.arrayReshape(ee.Image([2, 3]).toArray(), 2)
print('2D 2x3 array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0, 1, 2],
# [4, 0, 5]]
# Slice out a row to use as a column mask.
row_as_mask_for_cols = array_img_2d.arraySlice(0, 1, 2)
print('2D mask for cols (pixel):', samp_arr_img(row_as_mask_for_cols).getInfo())
# [[4, 0, 5]]
array_img_2d_mask_cols = array_img_2d.arrayMask(row_as_mask_for_cols);
print(
  '2D array image cols masked (pixel):',
  samp_arr_img(array_img_2d_mask_cols).getInfo()
)
# [[0, 2],
# [4, 5]]
# Slice out a column to use as a row mask.
col_as_mask_for_rows = array_img_2d.arraySlice(1, 1, 2)
print('2D mask for rows (pixel):', samp_arr_img(col_as_mask_for_rows).getInfo())
# [[1],
# [0]]
array_img_2d_mask_rows = array_img_2d.arrayMask(col_as_mask_for_rows)
print(
  '2D array image rows masked (pixel):',
  samp_arr_img(array_img_2d_mask_rows).getInfo()
)
# [[0, 1, 2]]
```

Was this helpful?
