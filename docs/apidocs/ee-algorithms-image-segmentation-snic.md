 
#  ee.Algorithms.Image.Segmentation.SNIC
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-algorithms-image-segmentation-snic#examples)


Superpixel clustering based on SNIC (Simple Non-Iterative Clustering). Outputs a band of cluster IDs and the per-cluster averages for each of the input bands. If the 'seeds' image isn't provided as input, the output will include a 'seeds' band containing the generated seed locations. See: Achanta, Radhakrishna and Susstrunk, Sabine, 'Superpixels and Polygons using Simple Non-Iterative Clustering', CVPR, 2017. 
Usage| Returns  
---|---  
`ee.Algorithms.Image.Segmentation.SNIC(image,  _size_, _compactness_, _connectivity_, _neighborhoodSize_, _seeds_)`| Image  
Argument| Type| Details  
---|---|---  
`image`| Image| The input image for clustering.  
`size`| Integer, default: 5| The superpixel seed location spacing, in pixels. If 'seeds' image is provided, no grid is produced.  
`compactness`| Float, default: 1| Compactness factor. Larger values cause clusters to be more compact (square). Setting this to 0 disables spatial distance weighting.  
`connectivity`| Integer, default: 8| Connectivity. Either 4 or 8.  
`neighborhoodSize`| Integer, default: null| Tile neighborhood size (to avoid tile boundary artifacts). Defaults to 2 * size.  
`seeds`| Image, default: null| If provided, any non-zero valued pixels are used as seed locations. Pixels that touch (as specified by 'connectivity') are considered to belong to the same cluster.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-algorithms-image-segmentation-snic#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-algorithms-image-segmentation-snic#colab-python-sample) More
```
// Note that the compactness and size parameters can have a significant impact
// on the result. They must be adjusted to meet image-specific characteristics
// and patterns, typically through trial. Pixel scale (map zoom level) is also
// important to consider. When exploring interactively through map tile
// visualization, the segmentation result it dependent on zoom level. If you
// need to evaluate the result at a specific scale, call .reproject() on the
// result, but do so with caution because it overrides the default scaling
// behavior that makes tile computation fast and efficient.

// Load a NAIP image for a neighborhood in Las Vegas.
varnaip=ee.Image('USDA/NAIP/DOQQ/m_3611554_sw_11_1_20170613');
// Apply the SNIC algorithm to the image.
varsnic=ee.Algorithms.Image.Segmentation.SNIC({
image:naip,
size:30,
compactness:0.1,
connectivity:8,
});
// Display the original NAIP image as RGB.
// Lock map zoom to maintain the desired scale of the segmentation computation.
Map.setLocked(false,18,18);
Map.setCenter(-115.32053,36.182016,18);
Map.addLayer(naip,null,'NAIP RGB');
// Display the clusters.
Map.addLayer(snic.randomVisualizer(),null,'Clusters');
// Display the RGB cluster means.
varvisParams={
bands:['R_mean','G_mean','B_mean'],
min:0,
max:255
};
Map.addLayer(snic,visParams,'RGB cluster means');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Note that the compactness and size parameters can have a significant impact
# on the result. They must be adjusted to meet image-specific characteristics
# and patterns, typically through trial. Pixel scale (map zoom level) is also
# important to consider. When exploring interactively through map tile
# visualization, the segmentation result it dependent on zoom level. If you
# need to evaluate the result at a specific scale, call .reproject() on the
# result, but do so with caution because it overrides the default scaling
# behavior that makes tile computation fast and efficient.

# Load a NAIP image for a neighborhood in Las Vegas.
naip = ee.Image('USDA/NAIP/DOQQ/m_3611554_sw_11_1_20170613')
# Apply the SNIC algorithm to the image.
snic = ee.Algorithms.Image.Segmentation.SNIC(
  image=naip, size=30, compactness=0.1, connectivity=8
)
# Display the original NAIP image as RGB.
m = geemap.Map()
m.set_center(-115.32053, 36.182016, 18)
m.add_layer(naip, None, 'NAIP RGB')
# Display the clusters.
m.add_layer(snic.randomVisualizer(), None, 'Clusters')
# Display the RGB cluster means.
vis_params = {'bands': ['R_mean', 'G_mean', 'B_mean'], 'min': 0, 'max': 255}
m.add_layer(snic, vis_params, 'RGB cluster means')
m
```

Was this helpful?
