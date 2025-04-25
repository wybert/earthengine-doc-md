 
#  ee.Image 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image#examples)


An object to represent an Earth Engine image. This constructor accepts a variety of arguments: 
- A string: an EarthEngine asset id,
- A string and a number: an EarthEngine asset id and version,
- A number or ee.Array: creates a constant image,
- A list: creates an image out of each list element and combines them into a single image,
- An ee.Image: returns the argument,
- Nothing: results in an empty transparent image.
Usage| Returns  
---|---  
`ee.Image( _args_)`| Image  
Argument| Type| Details  
---|---|---  
`args`| Image|List, optional| Constructor argument.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image#colab-python-sample) More
```
varimage=ee.Image('JAXA/ALOS/AW3D30/V2_2');
Map.setZoom(3);
Map.addLayer(image.select('AVE_DSM'),{min:-1e3,max:5e3},'AVE_DSM');
// Image JAXA/ALOS/AW3D30/V2_2 (3 bands)
// type: Image
// id: JAXA/ALOS/AW3D30/V2_2
// version: 1595337806697615
// bands: List (3 elements)
// properties: Object (21 properties)
print(image);
vartransparent=ee.Image();
Map.addLayer(transparent,null,'transparent',false);
// Image (1 band)
// type: Image
// bands: List (1 element)
// 0: "constant", int ∈ [0, 0], EPSG:4326
print(transparent);
// Create a multi-band image from a list of constants.
varorange=ee.Image([0xff,0x88,0x00]);
Map.addLayer(orange,{min:0,max:0xff},'orange',false);
// Image (3 bands)
// type: Image
// bands: List (3 elements)
// 0: "constant", int ∈ [255, 255], EPSG:4326
// 1: "constant_1", int ∈ [136, 136], EPSG:4326
// 2: "constant_2", int ∈ [0, 0], EPSG:4326
print(orange);
// Create a one band image where each pixel is an array of three values.
varimageOfArray=ee.Image(ee.Array([0x00,0x00,0xff]));
Map.addLayer(imageOfArray,null,'imageOfArray',false);
// Image (1 band)
// type: Image
// bands: List (1 element)
// 0: "constant", unsigned int8, 1 dimension, EPSG:4326
// id: constant
// crs: EPSG:4326
// crs_transform: [1,0,0,0,1,0]
// data_type: unsigned int8, 1 dimension
// type: PixelType
// dimensions: 1
// max: 255
// min: 0
// precision: int
print(imageOfArray);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
image = ee.Image('JAXA/ALOS/AW3D30/V2_2')
m = geemap.Map()
m.zoom = 3
display(m)
m.add_layer(image.select('AVE_DSM'), {'min': -1e3, 'max': 5e3}, 'AVE_DSM')
# Image JAXA/ALOS/AW3D30/V2_2 (3 bands)
# type: Image
# id: JAXA/ALOS/AW3D30/V2_2
# version: 1595337806697615
# 'bands': List (3 elements)
# properties: Object (21 properties)
display(image)
transparent = ee.Image()
m.add_layer(transparent, None, 'transparent', False)
# Image (1 band)
# type: Image
# 'bands': List (1 element)
# 0: "constant", int ∈ [0, 0], EPSG:4326
display(transparent)
# Create a multi-band image from a list of constants.
orange = ee.Image([0xFF, 0x88, 0x00])
m.add_layer(orange, {'min': 0, 'max': 0xFF}, 'orange', False)
# Image (3 bands)
# type: Image
# 'bands': List (3 elements)
# 0: "constant", int ∈ [255, 255], EPSG:4326
# 1: "constant_1", int ∈ [136, 136], EPSG:4326
# 2: "constant_2", int ∈ [0, 0], EPSG:4326
display(orange)
# Create a one band image where each pixel is an array of three values.
image_of_array = ee.Image(ee.Array([0x00, 0x00, 0xFF]))
m.add_layer(image_of_array, None, 'image_of_array', False)
# Image (1 band)
# type: Image
# 'bands': List (1 element)
# 0: "constant", unsigned int8, 1 dimension, EPSG:4326
# id: constant
# crs: EPSG:4326
# crs_transform: [1,0,0,0,1,0]
# data_type: unsigned int8, 1 dimension
# type: PixelType
# dimensions: 1
# 'max': 255
# 'min': 0
# precision: int
display(image_of_array)
```

