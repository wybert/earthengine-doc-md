 
#  ee.Terrain.products 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-terrain-products#examples)


Calculates slope, aspect, and a simple hillshade from a terrain DEM. 
Expects an image containing either a single band of elevation, measured in meters, or if there's more than one band, one named 'elevation'. Adds output bands named 'slope' and 'aspect' measured in degrees plus an unsigned byte output band named 'hillshade' for visualization. All other bands and metadata are copied from the input image. The local gradient is computed using the 4-connected neighbors of each pixel, so missing values will occur around the edges of an image.
Usage| Returns  
---|---  
`ee.Terrain.products(input)`| Image  
Argument| Type| Details  
---|---|---  
`input`| Image| An elevation image, in meters.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-terrain-products#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-terrain-products#colab-python-sample) More
```
// A digital elevation model.
vardem=ee.Image('NASA/NASADEM_HGT/001').select('elevation');
// Calculate slope. Units are degrees, range is [0,90).
varslope=ee.Terrain.slope(dem);
// Calculate aspect. Units are degrees where 0=N, 90=E, 180=S, 270=W.
varaspect=ee.Terrain.aspect(dem);
// Display slope and aspect layers on the map.
Map.setCenter(-123.457,47.815,11);
Map.addLayer(slope,{min:0,max:89.99},'Slope');
Map.addLayer(aspect,{min:0,max:359.99},'Aspect');
// Use the ee.Terrain.products function to calculate slope, aspect, and
// hillshade simultaneously. The output bands are appended to the input image.
// Hillshade is calculated based on illumination azimuth=270, elevation=45.
varterrain=ee.Terrain.products(dem);
print('ee.Terrain.products bands',terrain.bandNames());
Map.addLayer(terrain.select('hillshade'),{min:0,max:255},'Hillshade');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A digital elevation model.
dem = ee.Image('NASA/NASADEM_HGT/001').select('elevation')
# Calculate slope. Units are degrees, range is [0,90).
slope = ee.Terrain.slope(dem)
# Calculate aspect. Units are degrees where 0=N, 90=E, 180=S, 270=W.
aspect = ee.Terrain.aspect(dem)
# Display slope and aspect layers on the map.
m = geemap.Map()
m.set_center(-123.457, 47.815, 11)
m.add_layer(slope, {'min': 0, 'max': 89.99}, 'Slope')
m.add_layer(aspect, {'min': 0, 'max': 359.99}, 'Aspect')
# Use the ee.Terrain.products function to calculate slope, aspect, and
# hillshade simultaneously. The output bands are appended to the input image.
# Hillshade is calculated based on illumination azimuth=270, elevation=45.
terrain = ee.Terrain.products(dem)
display('ee.Terrain.products bands', terrain.bandNames())
m.add_layer(terrain.select('hillshade'), {'min': 0, 'max': 255}, 'Hillshade')
m
```

