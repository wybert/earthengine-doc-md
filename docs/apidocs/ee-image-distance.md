 
#  ee.Image.distance 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-distance#examples)


Computes the distance to the nearest non-zero pixel in each band, using the specified distance kernel. 
Usage| Returns  
---|---  
`Image.distance( _kernel_, _skipMasked_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The input image.  
`kernel`| Kernel, default: null| The distance kernel. One of chebyshev, euclidean, or manhattan.  
`skipMasked`| Boolean, default: true| Mask output pixels if the corresponding input pixel is masked.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-distance#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-distance#colab-python-sample) More
```
// The objective is to determine the per-pixel distance to a target
// feature (pixel value). In this example, the target feature is water in a
// land cover map.
// Import a Dynamic World land cover image and subset the 'label' band.
varlcImg=ee.Image(
'GOOGLE/DYNAMICWORLD/V1/20210726T171859_20210726T172345_T14TQS')
.select('label');
// Create a binary image where the target feature is value 1, all else 0.
// In the Dynamic World map, water is represented as value 0, so we use the
// ee.Image.eq() relational operator to set it to 1.
vartargetImg=lcImg.eq(0);
// Set a max distance from target pixels to consider in the analysis. Pixels
// with distance greater than this value from target pixels will be masked out.
// Here, we are using units of meters, but the distance kernels also accept
// units of pixels.
varmaxDistM=10000;// 10 km
// Calculate distance to target pixels. Several distance kernels are provided.
// Euclidean distance.
vareuclideanKernel=ee.Kernel.euclidean(maxDistM,'meters');
vareuclideanDist=targetImg.distance(euclideanKernel);
varvis={min:0,max:maxDistM};
Map.setCenter(-95.68,46.46,9);
Map.addLayer(euclideanDist,vis,'Euclidean distance to target pixels');
// Manhattan distance.
varmanhattanKernel=ee.Kernel.manhattan(maxDistM,'meters');
varmanhattanDist=targetImg.distance(manhattanKernel);
Map.addLayer(manhattanDist,vis,'Manhattan distance to target pixels',false);
// Chebyshev distance.
varchebyshevKernel=ee.Kernel.chebyshev(maxDistM,'meters');
varchebyshevDist=targetImg.distance(chebyshevKernel);
Map.addLayer(chebyshevDist,vis,'Chebyshev distance to target pixels',false);
// Add the target layer to the map; water is blue, all else masked out.
Map.addLayer(targetImg.mask(targetImg),{palette:'blue'},'Target pixels');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# The objective is to determine the per-pixel distance to a target
# feature (pixel value). In this example, the target feature is water in a
# land cover map.
# Import a Dynamic World land cover image and subset the 'label' band.
lc_img = ee.Image(
  'GOOGLE/DYNAMICWORLD/V1/20210726T171859_20210726T172345_T14TQS'
).select('label')
# Create a binary image where the target feature is value 1, all else 0.
# In the Dynamic World map, water is represented as value 0, so we use the
# ee.Image.eq() relational operator to set it to 1.
target_img = lc_img.eq(0)
# Set a max distance from target pixels to consider in the analysis. Pixels
# with distance greater than this value from target pixels will be masked out.
# Here, we are using units of meters, but the distance kernels also accept
# units of pixels.
max_dist_m = 10000 # 10 km
# Calculate distance to target pixels. Several distance kernels are provided.
# Euclidean distance.
euclidean_kernel = ee.Kernel.euclidean(max_dist_m, 'meters')
euclidean_dist = target_img.distance(euclidean_kernel)
vis = {'min': 0, 'max': max_dist_m}
m = geemap.Map()
m.set_center(-95.68, 46.46, 9)
m.add_layer(euclidean_dist, vis, 'Euclidean distance to target pixels')
# Manhattan distance.
manhattan_kernel = ee.Kernel.manhattan(max_dist_m, 'meters')
manhattan_dist = target_img.distance(manhattan_kernel)
m.add_layer(
  manhattan_dist, vis, 'Manhattan distance to target pixels', False
)
# Chebyshev distance.
chebyshev_kernel = ee.Kernel.chebyshev(max_dist_m, 'meters')
chebyshev_dist = target_img.distance(chebyshev_kernel)
m.add_layer(
  chebyshev_dist, vis, 'Chebyshev distance to target pixels', False
)
# Add the target layer to the map water is blue, all else masked out.
m.add_layer(
  target_img.mask(target_img), {'palette': 'blue'}, 'Target pixels'
)
m
```

Was this helpful?
