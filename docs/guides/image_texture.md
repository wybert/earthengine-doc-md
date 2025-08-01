 
#  Texture
Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine has several special methods for estimating spatial texture. When the image is discrete valued (not floating point), you can use `image.entropy()` to compute the [entropy](http://en.wikipedia.org/wiki/Entropy_\(information_theory\)) in a neighborhood:
### Code Editor (JavaScript)
```
// Load a high-resolution NAIP image.
varimage=ee.Image('USDA/NAIP/DOQQ/m_3712213_sw_10_1_20140613');

// Zoom to San Francisco, display.
Map.setCenter(-122.466123,37.769833,17);
Map.addLayer(image,{max:255},'image');

// Get the NIR band.
varnir=image.select('N');

// Define a neighborhood with a kernel.
varsquare=ee.Kernel.square({radius:4});

// Compute entropy and display.
varentropy=nir.entropy(square);
Map.addLayer(entropy,
{min:1,max:5,palette:['0000CC','CC0000']},
'entropy');
```

Note that the NIR band is scaled to 8-bits prior to calling `entropy()` since the entropy computation takes discrete valued inputs. The non-zero elements in the kernel specify the neighborhood.
Another way to measure texture is with a gray-level co-occurrence matrix (GLCM). Using the image and kernel from the previous example, compute the GLCM-based contrast as follows: 
### Code Editor (JavaScript)
```
// Compute the gray-level co-occurrence matrix (GLCM), get contrast.
varglcm=nir.glcmTexture({size:4});
varcontrast=glcm.select('N_contrast');
Map.addLayer(contrast,
{min:0,max:1500,palette:['0000CC','CC0000']},
'contrast');
```

Many measures of texture are output by `image.glcm()`. For a complete reference on the outputs, see [Haralick et al. (1973)](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4309314&tag=1) and [Conners et al. (1984)](http://www.sciencedirect.com/science/article/pii/0734189X8490197X).
Local measures of spatial association such as Geary’s C [ (Anselin 1995)](http://onlinelibrary.wiley.com/doi/10.1111/j.1538-4632.1995.tb00338.x/abstract) can be computed in Earth Engine using `image.neighborhoodToBands()`. Using the image from the previous example:
### Code Editor (JavaScript)
```
// Create a list of weights for a 9x9 kernel.
varrow=[1,1,1,1,1,1,1,1,1];
// The center of the kernel is zero.
varcenterRow=[1,1,1,1,0,1,1,1,1];
// Assemble a list of lists: the 9x9 kernel weights as a 2-D matrix.
varrows=[row,row,row,row,centerRow,row,row,row,row];
// Create the kernel from the weights.
// Non-zero weights represent the spatial neighborhood.
varkernel=ee.Kernel.fixed(9,9,rows,-4,-4,false);

// Convert the neighborhood into multiple bands.
varneighs=nir.neighborhoodToBands(kernel);

// Compute local Geary's C, a measure of spatial association.
vargearys=nir.subtract(neighs).pow(2).reduce(ee.Reducer.sum())
.divide(Math.pow(9,2));
Map.addLayer(gearys,
{min:20,max:2500,palette:['0000CC','CC0000']},
"Geary's C");
```

For an example of using neighborhood standard deviation to compute image texture, see the [Statistics of Image Neighborhoods page](https://developers.google.com/earth-engine/guides/reducers_reduce_neighborhood).
