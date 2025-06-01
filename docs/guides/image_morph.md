 
#  Morphological Operations 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Earth Engine implements morphological operations as focal operations, specifically `focalMax()`, `focalMin()`, `focalMedian()`, and `focalMode()` instance methods in the `Image` class. (These are shortcuts for the more general `reduceNeighborhood()`, which can input the pixels in a kernel to any reducer with a numeric output. See [this page](https://developers.google.com/earth-engine/guides/reducers_reduce_neighborhood) for more information on reducing neighborhoods). The morphological operators are useful for performing operations such as erosion, dilation, opening and closing. For example, to perform an [opening operation](http://en.wikipedia.org/wiki/Opening_\(morphology\)), use `focalMin()` followed by `focalMax()`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_morph#code-editor-javascript-sample) More
```
// Load a Landsat 8 image, select the NIR band, threshold, display.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
.select(4).gt(0.2);
Map.setCenter(-122.1899,37.5010,13);
Map.addLayer(image,{},'NIR threshold');
// Define a kernel.
varkernel=ee.Kernel.circle({radius:1});
// Perform an erosion followed by a dilation, display.
varopened=image
.focalMin({kernel:kernel,iterations:2})
.focalMax({kernel:kernel,iterations:2});
Map.addLayer(opened,{},'opened');
```

Note that in the previous example, a kernel argument is provided to the morphological operator. The pixels covered by non-zero elements of the kernel are used in the computation. The iterations argument indicates how many times to apply the operator.
