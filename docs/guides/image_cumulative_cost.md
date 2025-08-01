 
#  Cumulative Cost Mapping
Stay organized with collections  Save and categorize content based on your preferences. 
Use `image.cumulativeCost()` to compute a cost map where every pixel contains the total cost of the lowest cost path to the nearest source location. This process is useful in a variety of contexts such as habitat analysis [(Adriaensen et al. 2003)](http://www.sciencedirect.com/science/article/pii/S0169204602002426), watershed delineation [(Melles et al. 2011)](http://www.sciencedirect.com/science/article/pii/S1878029611001691) and image segmentation [(Falcao et al. 2004).](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1261076) Call the cumulative cost function on an image in which each pixel represents the cost per meter to traverse it. Paths are computed through any of a pixel's eight neighbors. Required inputs include a `source` image, in which each non-zero pixel represents a potential source (or start of a path), and a `maxDistance` (in meters) over which to compute paths. The algorithm finds the cumulative cost of all paths less than _maxPixels_ = `maxDistance`/_scale_ in length, where _scale_ is the pixel resolution, or [scale of analysis in Earth Engine](https://developers.google.com/earth-engine/guides/scale).
The following example demonstrates computing least-cost paths across a land cover image:
### Code Editor (JavaScript)
```
// A rectangle representing Bangui, Central African Republic.
vargeometry=ee.Geometry.Rectangle([18.5229,4.3491,18.5833,4.4066]);

// Create a source image where the geometry is 1, everything else is 0.
varsources=ee.Image().toByte().paint(geometry,1);

// Mask the sources image with itself.
sources=sources.selfMask();

// The cost data is generated from classes in ESA/GLOBCOVER.
varcover=ee.Image('ESA/GLOBCOVER_L4_200901_200912_V2_3').select(0);

// Classes 60, 80, 110, 140 have cost 1.
// Classes 40, 90, 120, 130, 170 have cost 2.
// Classes 50, 70, 150, 160 have cost 3.
varbeforeRemap=[60,80,110,140,
40,90,120,130,170,
50,70,150,160];
varafterRemap=[1,1,1,1,
2,2,2,2,2,
3,3,3,3];
varcost=cover.remap(beforeRemap,afterRemap,0);

// Compute the cumulative cost to traverse the land cover.
varcumulativeCost=cost.cumulativeCost({
source:sources,
maxDistance:80*1000// 80 kilometers
});

// Display the results
Map.setCenter(18.71,4.2,9);
Map.addLayer(cover,{},'Globcover');
Map.addLayer(cumulativeCost,{min:0,max:5e4},'accumulated cost');
Map.addLayer(geometry,{color:'FF0000'},'source geometry');
```

The result should look something like Figure 1, in which each output pixel represents the accumulated cost to the nearest source. Note that discontinuities can appear in places where the least cost path to the nearest source exceeds _maxPixels_ in length.
![costMap](https://developers.google.com/static/earth-engine/images/CumulativeCost.png) Figure 1. The cumulative cost to the source pixels, where cost is determined by the land cover categories. Low costs are black, higher costs are white. 
