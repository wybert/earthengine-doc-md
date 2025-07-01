 
#  ee.Image.arrayDotProduct
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Computes the dot product of each pair of 1-D arrays in the bands of the input images. 
Usage| Returns  
---|---  
`Image.arrayDotProduct(image2)`| Image  
Argument| Type| Details  
---|---|---  
this: `image1`| Image| First array image of 1-D vectors.  
`image2`| Image| Second array image of 1-D vectors.  
## Examples
### Code Editor (JavaScript)
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// A 1D array image.
vararrayImg1Da=ee.Image([0,1,2]).toArray();
print('1D array image A (pixel)',sampArrImg(arrayImg1Da));
// [0, 1, 2]
// A second 1D array image of the same length.
vararrayImg1Db=ee.Image([3,4,5]).toArray();
print('1D array image B (pixel)',sampArrImg(arrayImg1Db));
// [3, 4, 5]
// Calculate the dot product for the two 1D arrays.
vartest=arrayImg1Da.arrayDotProduct(arrayImg1Db);
print('A⋅B = 0(3) + 1(4) + 2(5) = ',sampArrImg(test));
// 14
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
# A 1D array image.
array_img_1d_a = ee.Image([0, 1, 2]).toArray()
print('1D array image A (pixel):', samp_arr_img(array_img_1d_a).getInfo())
# [0, 1, 2]
# A second 1D array image of the same length.
array_img_1d_b = ee.Image([3, 4, 5]).toArray()
print('1D array image B (pixel):', samp_arr_img(array_img_1d_b).getInfo())
# [3, 4, 5]
# Calculate the dot product for the two 1D arrays.
test = array_img_1d_a.arrayDotProduct(array_img_1d_b)
print('A⋅B = 0(3) + 1(4) + 2(5) = ', samp_arr_img(test).getInfo())
# 14
```

