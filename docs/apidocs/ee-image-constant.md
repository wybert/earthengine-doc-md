 
#  ee.Image.constant 
Stay organized with collections  Save and categorize content based on your preferences. 
Generates an image containing a constant value everywhere. Usage| Returns  
---|---  
`ee.Image.constant(value)`| Image  
Argument| Type| Details  
---|---|---  
`value`| Object| The value of the pixels in the constant image. Must be a number or an Array or a list of numbers or Arrays.  
## Examples
### Code Editor (JavaScript)
```
// Create a constant image, where every pixel has bands of the same value.
varimage1=ee.Image.constant(1);
Map.addLayer(image1,null,'1');
// Image (1 band)
// type: Image
// bands: List (1 element)
// 0: "constant", int ∈ [1, 1], EPSG:4326
print(image1);
varimage2=ee.Image(2);
Map.addLayer(image2,null,'2');
// Image (1 band)
// type: Image
// bands: List (1 element)
// 0: "constant", int ∈ [2, 2], EPSG:4326
print(image2);
varπ=ee.Image(Math.PI);
Map.addLayer(π,null,'π');
// Image (1 band)
// type: Image
// bands: List (1 element)
// 0: "constant", double ∈ [3.141592653589793, 3.141592653589793], EPSG:4326
// id: constant
// crs: EPSG:4326
// crs_transform: [1,0,0,0,1,0]
// data_type: double ∈ [3.141592653589793, 3.141592653589793]
print(π);
// Create a multi-band image from a list of constant double integers.
vardoubleIntImage=ee.Image.constant([-1.2,4]);
Map.addLayer(doubleIntImage,null,'double int');
// Image (2 bands)
// type: Image
// bands: List (2 elements)
// 0: "constant_0", double ∈ [-1.2, -1.2], EPSG:4326
// 1: "constant_1", int ∈ [4, 4], EPSG:4326
print(doubleIntImage);
// Create a multi-band image from a list of constants, using hexadecimal
// notation.
varmultiband=ee.Image([0xff,0x88,0x00]);
Map.addLayer(multiband,{min:0,max:0xff},'orange');
// Image (3 bands)
// type: Image
// bands: List (3 elements)
// 0: "constant", int ∈ [255, 255], EPSG:4326
// 1: "constant_1", int ∈ [136, 136], EPSG:4326
// 2: "constant_2", int ∈ [0, 0], EPSG:4326
print(multiband);
```

