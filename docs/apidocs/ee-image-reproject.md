 
#  ee.Image.reproject 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-image-reproject#examples)


Force an image to be computed in a given projection and resolution. 
Usage| Returns  
---|---  
`Image.reproject(crs,  _crsTransform_, _scale_)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to reproject.  
`crs`| Projection| The CRS to project the image to.  
`crsTransform`| List, default: null| The list of CRS transform values. This is a row-major ordering of the 3x2 transform matrix. This option is mutually exclusive with the scale option, and replaces any transform already on the projection.  
`scale`| Float, default: null| If scale is specified, then the projection is scaled by dividing the specified scale value by the nominal size of a meter in the specified projection. If scale is not specified, then the scale of the given projection will be used.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-image-reproject#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-image-reproject#colab-python-sample) More
```
// Use of ee.Image.reproject is rarely needed and should generally be avoided.
// Defining the projection and scale of analysis should be handled by "scale",
// "crs", and "crsTransform" parameters whenever they are offered by a function.
// It is occasionally useful for forcing computation or visualization at a
// desired scale and projection when alternative methods are not available. In
// this example it is used to compute and visualize terrain slope from a DEM
// composite.
// Calculate mean elevation from two DEM datasets. The resulting composite
// image has a default CRS of WGS84 with 1 degree pixels.
vardem1=ee.Image('NASA/NASADEM_HGT/001').select('elevation');
vardem2=ee.Image('CGIAR/SRTM90_V4').select('elevation');
vardemMean=ee.ImageCollection([dem1,dem2]).mean();
// Display the DEMs on the map, note that they all render as expected.
vardemVisParams={min:500,max:2500};
Map.setCenter(-123.457,47.815,11);
Map.addLayer(dem1,demVisParams,'DEM 1');
Map.addLayer(dem2,demVisParams,'DEM 2');
Map.addLayer(demMean,demVisParams,'DEM composite');
// Calculate terrain slope from the composite DEM (WGS84, 1 degree pixel scale).
vardemCompSlope=ee.Terrain.slope(demMean);
// Because the composite has 1 degree pixel scale, the slope calculation
// is essenstially meaningless and difficult to even display (you may need to
// zoom out to see the individual 1 degree pixels).
Map.addLayer(demCompSlope,{min:0,max:0.3},'Slope');
// We can use ee.Image.reproject to force the slope calculation and display
// the result with a reasonable scale of 30 m on WGS84 CRS, for example.
varslopeScale=ee.Terrain.slope(
demMean.reproject({
crs:'EPSG:4326',
scale:30
})
);
Map.addLayer(slopeScale,{min:0,max:45},'Slope w/ CRS and scale');
// To more precisely control the reprojection, you can use the "crsTransform"
// parameter instead of the "scale" parameter or set the projection according to
// a reference image. For example, here the input composite image for the slope
// function is set to match the grid spacing and alignment of the NASADEM image.
varnasademProj=dem1.projection();
vardemMeanReproj=demMean.reproject(nasademProj);
varslopeRefProj=ee.Terrain.slope(demMeanReproj);
Map.addLayer(slopeRefProj,{min:0,max:45},'Slope w/ reference proj');
print('Reference projection',nasademProj);
print('DEM composite projection',demMeanReproj.projection());
// An alternative method for changing the projection of image composites
// (not accepting the default WGS84 CRS with 1 degree pixel scale) is to
// explicitly set the default projection using ee.Image.setDefaultProjection,
// which will not force resampling, like ee.Image.reproject will.
vardemMeanProj=ee.ImageCollection([dem1,dem2]).mean()
.setDefaultProjection(nasademProj);
varslopeProj=ee.Terrain.slope(demMeanProj);
Map.addLayer(slopeProj,{min:0,max:45},'slope w/ default projection set');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Use of ee.Image.reproject is rarely needed and should generally be avoided.
# Defining the projection and scale of analysis should be handled by "scale",
# "crs", and "crsTransform" parameters whenever they are offered by a function.
# It is occasionally useful for forcing computation or visualization at a
# desired scale and projection when alternative methods are not available. In
# this example it is used to compute and visualize terrain slope from a DEM
# composite.
# Calculate mean elevation from two DEM datasets. The resulting composite
# image has a default CRS of WGS84 with 1 degree pixels.
dem_1 = ee.Image('NASA/NASADEM_HGT/001').select('elevation')
dem_2 = ee.Image('CGIAR/SRTM90_V4').select('elevation')
dem_mean = ee.ImageCollection([dem_1, dem_2]).mean()
# Display the DEMs on the map, note that they all render as expected.
dem_vis_params = {'min': 500, 'max': 2500}
m = geemap.Map()
m.set_center(-123.457, 47.815, 11)
m.add_layer(dem_1, dem_vis_params, 'DEM 1')
m.add_layer(dem_2, dem_vis_params, 'DEM 2')
m.add_layer(dem_mean, dem_vis_params, 'DEM composite')
# Calculate terrain slope from the composite DEM (WGS84, 1 degree pixel scale).
dem_comp_slope = ee.Terrain.slope(dem_mean)
# Because the composite has 1 degree pixel scale, the slope calculation
# is essenstially meaningless and difficult to even display (you may need to
# zoom out to see the individual 1 degree pixels).
m.add_layer(dem_comp_slope, {'min': 0, 'max': 0.3}, 'Slope')
# We can use ee.Image.reproject to force the slope calculation and display
# the result with a reasonable scale of 30 m on WGS84 CRS, for example.
slope_scale = ee.Terrain.slope(dem_mean.reproject(crs='EPSG:4326', scale=30))
m.add_layer(slope_scale, {'min': 0, 'max': 45}, 'Slope w/ CRS and scale')
# To more precisely control the reprojection, you can use the "crsTransform"
# parameter instead of the "scale" parameter or set the projection according to
# a reference image. For example, here the input composite image for the slope
# function is set to match the grid spacing and alignment of the NASADEM image.
nasadem_proj = dem_1.projection()
dem_mean_reproj = dem_mean.reproject(nasadem_proj)
slope_ref_proj = ee.Terrain.slope(dem_mean_reproj)
m.add_layer(slope_ref_proj, {'min': 0, 'max': 45}, 'Slope w/ reference proj')
display('Reference projection', nasadem_proj)
display('DEM composite projection', dem_mean_reproj.projection())
# An alternative method for changing the projection of image composites
# (not accepting the default WGS84 CRS with 1 degree pixel scale) is to
# explicitly set the default projection using ee.Image.setDefaultProjection,
# which will not force resampling, like ee.Image.reproject will.
dem_mean_proj = (
  ee.ImageCollection([dem_1, dem_2]).mean().setDefaultProjection(nasadem_proj)
)
slope_proj = ee.Terrain.slope(dem_mean_proj)
m.add_layer(
  slope_proj, {'min': 0, 'max': 45}, 'slope w/ default projection set'
)
m
```

