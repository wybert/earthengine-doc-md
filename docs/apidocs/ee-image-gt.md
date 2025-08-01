 
#  ee.Image.gt
Stay organized with collections  Save and categorize content based on your preferences. 
Returns 1 if and only if the first value is greater than the second for each matched pair of bands in image1 and image2. If either image1 or image2 has only 1 band, then it is used against all the bands in the other image. If the images have the same number of bands, but not the same names, they're used pairwise in the natural order. The output bands are named for the longer of the two inputs, or if they're equal in length, in image1's order. The type of the output pixels is boolean. Usage | Returns  
---|---  
`Image.gt(image2)` | Image  
Argument | Type | Details  
---|---|---  
this: `image1` | Image | The image from which the left operand bands are taken.  
`image2` | Image | The image from which the right operand bands are taken.  
## Examples
### Code Editor (JavaScript)
```
// Show world oceans in blue and anything higher than the ellipsoid as gray.
// The bedrock layer is generally close to the geoid (sealevel).
varelevation=ee.Image('NOAA/NGDC/ETOPO1').select('bedrock');
varwaterLand=elevation.gt(0.0);
varwaterLandViz={palette:['cadetblue','lightgray']};
Map.addLayer(waterLand,waterLandViz,'water_land');
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Show world oceans in blue and anything higher than the ellipsoid as gray.
# The bedrock layer is generally close to the geoid (sealevel).
elevation = ee.Image('NOAA/NGDC/ETOPO1').select('bedrock')
water_land = elevation.gt(0.0)
water_land_viz = {'palette': ['cadetblue', 'lightgray']}
m = geemap.Map()
m.add_layer(water_land, water_land_viz, 'water_land')
m
```

