 
#  ee.Image.arrayProject 
Stay organized with collections  Save and categorize content based on your preferences. 
Projects the array in each pixel to a lower dimensional space by specifying the axes to retain. Dropped axes must be at most length 1. Usage| Returns  
---|---  
`Image.arrayProject(axes)`| Image  
Argument| Type| Details  
---|---|---  
this: `input`| Image| Input image.  
`axes`| List| The axes to retain. Other axes will be discarded and must be at most length 1.  
## Examples
### Code Editor (JavaScript)
```
// A function to print arrays for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create a 2D array image with the 0-axis having length 6 and the 1-axis
// having length 1.
vararrayImg2D=ee.Image([0,1,2,3,4,5]).toArray().toArray(1);
print('2D array image (pixel)',sampArrImg(arrayImg2D));
// [[0],
// [1],
// [2],
// [3],
// [4],
// [5]]
// Project the 2D array to a 1D array, retain the 0-axis (concatenate elements
// from the 1-axis into the 0-axis).
vararrayImg2Dto1D=arrayImg2D.arrayProject([0]);
print('2D array image (pixel)',sampArrImg(arrayImg2Dto1D));
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
# Create a 2D array image with the 0-axis having length 6 and the 1-axis
# having length 1.
array_img_2d = ee.Image([0, 1, 2, 3, 4, 5]).toArray().toArray(1)
print('2D array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0],
# [1],
# [2],
# [3],
# [4],
# [5]]
# Project the 2D array to a 1D array, retain the 0-axis (concatenate elements
# from the 1-axis into the 0-axis).
array_img_2d_to_1d = array_img_2d.arrayProject([0])
print('2D array image (pixel):', samp_arr_img(array_img_2d_to_1d).getInfo())
# [0, 1, 2, 3, 4, 5]
```

