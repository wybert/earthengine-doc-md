 
#  ee.Image.sample
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Samples the pixels of an image, returning them as a FeatureCollection. Each feature will have 1 property per band in the input image. Note that the default behavior is to drop features that intersect masked pixels, which result in null-valued properties (see dropNulls argument). 
Usage| Returns  
---|---  
`Image.sample( _region_, _scale_, _projection_, _factor_, _numPixels_, _seed_, _dropNulls_, _tileScale_, _geometries_)`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to sample.  
`region`| Geometry, default: null| The region to sample from. If unspecified, uses the image's whole footprint.  
`scale`| Float, default: null| A nominal scale in meters of the projection to sample in.  
`projection`| Projection, default: null| The projection in which to sample. If unspecified, the projection of the image's first band is used. If specified in addition to scale, rescaled to the specified scale.  
`factor`| Float, default: null| A subsampling factor, within (0, 1]. If specified, 'numPixels' must not be specified. Defaults to no subsampling.  
`numPixels`| Long, default: null| The approximate number of pixels to sample. If specified, 'factor' must not be specified.  
`seed`| Integer, default: 0| A randomization seed to use for subsampling.  
`dropNulls`| Boolean, default: true| Post filter the result to drop features that have null-valued properties.  
`tileScale`| Float, default: 1| A scaling factor used to reduce aggregation tile size; using a larger tileScale (e.g., 2 or 4) may enable computations that run out of memory with the default.  
`geometries`| Boolean, default: false| If true, adds the center of the sampled pixel as the geometry property of the output feature. Otherwise, geometries will be omitted (saving memory).  
## Examples
### Code Editor (JavaScript)
```
// Demonstrate extracting pixels from an image as features with
// ee.Image.sample(), and show how the features are aligned with the pixels.
// An image with one band of elevation data.
varimage=ee.Image('CGIAR/SRTM90_V4');
varVIS_MIN=1620;
varVIS_MAX=1650;
Map.addLayer(image,{min:VIS_MIN,max:VIS_MAX},'SRTM');
// Region to sample.
varregion=ee.Geometry.Polygon(
[[[-110.006,40.002],
[-110.006,39.999],
[-109.995,39.999],
[-109.995,40.002]]],null,false);
// Show region on the map.
Map.setCenter(-110,40,16);
Map.addLayer(ee.FeatureCollection([region]).style({"color":"00FF0022"}));
// Perform sampling; convert image pixels to features.
varsamples=image.sample({
region:region,
// Default (false) is no geometries in the output.
// When set to true, each feature has a Point geometry at the center of the
// image pixel.
geometries:true,
// The scale is not specified, so the resolution of the image will be used,
// and there is a feature for every pixel. If we give a scale parameter, the
// image will be resampled and there will be more or fewer features.
//
// scale: 200,
});
// Visualize sample data using ee.FeatureCollection.style().
varstyled=samples
.map(function(feature){
returnfeature.set('style',{
pointSize:feature.getNumber('elevation').unitScale(VIS_MIN,VIS_MAX)
.multiply(15),
});
})
.style({
color:'000000FF',
fillColor:'00000000',
styleProperty:'style',
neighborhood:6,// increase to correctly draw large points
});
Map.addLayer(styled);
// Each sample feature has a point geometry and a property named 'elevation'
// corresponding to the band named 'elevation' of the image. If there are
// multiple bands they will become multiple properties. This will print:
//
// geometry: Point (-110.01, 40.00)
// properties:
//  elevation: 1639
print(samples.first());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Demonstrate extracting pixels from an image as features with
# ee.Image.sample(), and show how the features are aligned with the pixels.
# An image with one band of elevation data.
image = ee.Image('CGIAR/SRTM90_V4')
vis_min = 1620
vis_max = 1650
m = geemap.Map()
m.add_layer(image, {'min': vis_min, 'max': vis_max}, 'SRTM')
# Region to sample.
region = ee.Geometry.Polygon(
  [[
    [-110.006, 40.002],
    [-110.006, 39.999],
    [-109.995, 39.999],
    [-109.995, 40.002],
  ]],
  None,
  False,
)
# Show region on the map.
m.set_center(-110, 40, 16)
m.add_layer(ee.FeatureCollection([region]).style(color='00FF0022'))
# Perform sampling convert image pixels to features.
samples = image.sample(
  region=region,
  # Default (False) is no geometries in the output.
  # When set to True, each feature has a Point geometry at the center of the
  # image pixel.
  geometries=True,
  # The scale is not specified, so the resolution of the image will be used,
  # and there is a feature for every pixel. If we give a scale parameter, the
  # image will be resampled and there will be more or fewer features.
  #
  # scale=200,
)

defscale_point_size(feature):
 elevation = feature.getNumber('elevation')
 point_size = elevation.unitScale(vis_min, vis_max).multiply(15)
 feature.set('style', {'pointSize': point_size})
 return feature

# Visualize sample data using ee.FeatureCollection.style().
styled = samples.map(scale_point_size).style(
  color='000000FF',
  fillColor='00000000',
  styleProperty='style',
  neighborhood=6, # increase to correctly draw large points
)
m.add_layer(styled)
display(m)
# Each sample feature has a point geometry and a property named 'elevation'
# corresponding to the band named 'elevation' of the image. If there are
# multiple bands they will become multiple properties. This will print:
#
# geometry: Point (-110.01, 40.00)
# properties:
#  elevation: 1639
display(samples.first())
```

