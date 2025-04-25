 
#  ee.Image.arrayGet 
Stay organized with collections  Save and categorize content based on your preferences. 
For each band, an output band of the same name is created with the value at the given position extracted from the input multidimensional pixel in that band. Usage| Returns  
---|---  
`Image.arrayGet(position)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| Array to get an element from.  
`position`| Image| The coordinates of the element to get. There must be as many scalar bands as there are dimensions in the input image.  
## Examples
### Code Editor (JavaScript)
```
// A function to print the array for a selected pixel in the following examples.
functionsampArrImg(arrImg){
varpoint=ee.Geometry.Point([-121,42]);
returnarrImg.sample(point,500).first().get('array');
}
// Create a 1D array image.
vararrayImg1D=ee.Image([0,1,2,3,4,5]).toArray();
print('1D array image (pixel)',sampArrImg(arrayImg1D));
// [0, 1, 2, 3, 4, 5]
// Get the array value at a given position. Here we target the 4th element.
varposition1D=ee.Image([3]);
varselectedElement1D=arrayImg1D.arrayGet(position1D);
print('Element at position [3] (4th element)',sampArrImg(selectedElement1D));
// [3]
// Create a 2D 2x3 array image (reshape the 1D array image).
vararrayImg2D=arrayImg1D.arrayReshape(ee.Image([2,3]).toArray(),2);
print('2D 2x3 array image (pixel)',sampArrImg(arrayImg2D));
// [[0, 1, 2],
// [3, 4, 5]]
// Get the array element value at axis-0, position 0 and axis-1, position 2.
varposition2D=ee.Image([0,2]);
varselectedElement2D=arrayImg2D.arrayGet(position2D);
print('Element at position [0, 2]',sampArrImg(selectedElement2D));
// 2
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# A function to print the array for a selected pixel in the following examples.
defsamp_arr_img(arr_img):
 point = ee.Geometry.Point([-121, 42])
 return arr_img.sample(point, 500).first().get('array')
# Create a 1D array image.
array_img_1d = ee.Image([0, 1, 2, 3, 4, 5]).toArray()
print('1D array image (pixel):', samp_arr_img(array_img_1d).getInfo())
# [0, 1, 2, 3, 4, 5]
# Get the array value at a given position. Here we target the 4th element.
position_1d = ee.Image([3])
selected_element_1d = array_img_1d.arrayGet(position_1d)
print(
  'Element at position [3] (4th element):',
  samp_arr_img(selected_element_1d).getInfo()
)
# [3]
# Create a 2D 2x3 array image (reshape the 1D array image).
array_img_2d = array_img_1d.arrayReshape(ee.Image([2, 3]).toArray(), 2)
print('2D 2x3 array image (pixel):', samp_arr_img(array_img_2d).getInfo())
# [[0, 1, 2],
# [3, 4, 5]]
# Get the array element value at axis-0, position 0 and axis-1, position 2.
position_2d = ee.Image([0, 2])
selected_element_2d = array_img_2d.arrayGet(position_2d)
print(
  'Element at position [0, 2]:',
  samp_arr_img(selected_element_2d).getInfo()
)
# 2
```

