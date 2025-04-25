 
#  ee.Image.arrayCat 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-arraycat#examples)


Creates an array image by concatenating each array pixel along the given axis in each band. 
Usage| Returns  
---|---  
`Image.arrayCat(image2, axis)`| Image  
Argument| Type| Details  
---|---|---  
this: `image1`| Image| First array image to concatenate.  
`image2`| Image| Second array image to concatenate.  
`axis`| Integer| Axis to concatenate along.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-arraycat#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-arraycat#colab-python-sample) More
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create two 1D array images.
vararrayImg1Da=ee.Image([0,1,2]).toArray();
print('1D array image (A) (pixel)',sampArrImg(arrayImg1Da));
// [0, 1, 2]
vararrayImg1Db=ee.Image([3,4,5]).toArray();
print('1D array image (B) (pixel)',sampArrImg(arrayImg1Db));
// [3, 4, 5]
// Concatenate 1D array image B to 1D array image A on 0-axis (rows).
vararrayImg1DcatAx0=arrayImg1Da.arrayCat(arrayImg1Db,0);
print('Concatenate 1D array images on 0-axis',sampArrImg(arrayImg1DcatAx0));
// [0, 1, 2, 3, 4, 5]
// Concatenate 1D array image B to 1D array image A on 1-axis (columns).
vararrayImg1DcatAx1=arrayImg1Da.arrayCat(arrayImg1Db,1);
print('Concatenate 1D array images on 1-axis',sampArrImg(arrayImg1DcatAx1));
// [[0, 3],
// [1, 4]
// [2, 5]]
// Create two 2D array images (expand the dimensions of 1D arrays).
vararrayImg2Da=arrayImg1Da.toArray(1);
print('2D array image (A) (pixel)',sampArrImg(arrayImg2Da));
// [[0],
// [1],
// [2]]
vararrayImg2Db=arrayImg1Db.toArray(1);
print('2D array image (B) (pixel)',sampArrImg(arrayImg2Db));
// [[3],
// [4],
// [5]]
// Concatenate 2D array image B to 2D array image A on 0-axis (rows).
vararrayImg2DcatAx0=arrayImg2Da.arrayCat(arrayImg2Db,0);
print('Concatenate 2D array images on 0-axis',sampArrImg(arrayImg2DcatAx0));
// [[0],
// [1],
// [2],
// [3],
// [4],
// [5]]
// Concatenate 2D array image B to 2D array image A on 1-axis (columns).
vararrayImg2DcatAx1=arrayImg2Da.arrayCat(arrayImg2Db,1);
print('Concatenate 2D array images on 1-axis',sampArrImg(arrayImg2DcatAx1));
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
# Create two 1D array images.
array_img_1d_a = ee.Image([0, 1, 2]).toArray()
print('1D array image (A) (pixel):', samp_arr_img(array_img_1d_a).getInfo())
# [0, 1, 2]
array_img_1d_b = ee.Image([3, 4, 5]).toArray()
print('1D array image (B) (pixel):', samp_arr_img(array_img_1d_b).getInfo())
# [3, 4, 5]
# Concatenate 1D array image B to 1D array image A on 0-axis (rows).
array_img_1d_cat_ax0 = array_img_1d_a.arrayCat(array_img_1d_b, 0)
print(
  'Concatenate 1D array images on 0-axis:',
  samp_arr_img(array_img_1d_cat_ax0).getInfo()
)
# [0, 1, 2, 3, 4, 5]
# Concatenate 1D array image B to 1D array image A on 1-axis (columns).
array_img_1d_cat_ax1 = array_img_1d_a.arrayCat(array_img_1d_b, 1)
print(
  'Concatenate 1D array images on 1-axis:',
  samp_arr_img(array_img_1d_cat_ax1).getInfo()
)
# [[0, 3],
# [1, 4]
# [2, 5]]
# Create two 2D array images (expand the dimensions of 1D arrays).
array_img_2d_a = array_img_1d_a.toArray(1)
print('2D array image (A) (pixel):', samp_arr_img(array_img_2d_a).getInfo())
# [[0],
# [1],
# [2]]
array_img_2d_b = array_img_1d_b.toArray(1)
print('2D array image (B) (pixel):', samp_arr_img(array_img_2d_b).getInfo())
# [[3],
# [4],
# [5]]
# Concatenate 2D array image B to 2D array image A on 0-axis (rows).
array_img_2d_cat_ax0 = array_img_2d_a.arrayCat(array_img_2d_b, 0)
print(
  'Concatenate 2D array images on 0-axis:',
  samp_arr_img(array_img_2d_cat_ax0).getInfo()
)
# [[0],
# [1],
# [2],
# [3],
# [4],
# [5]]
# Concatenate 2D array image B to 2D array image A on 1-axis (columns).
array_img_2d_cat_ax1 = array_img_2d_a.arrayCat(array_img_2d_b, 1)
print(
  'Concatenate 2D array images on 1-axis:',
  samp_arr_img(array_img_2d_cat_ax1).getInfo()
)
# [[0, 3],
# [1, 4],
# [2, 5]]
```

