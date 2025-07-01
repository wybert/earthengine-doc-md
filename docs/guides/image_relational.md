 
#  Relational, Conditional, and Boolean Operations
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Relational and boolean operators](https://developers.google.com/earth-engine/guides/image_relational#relational-and-boolean-operators)
  * [Conditional operators](https://developers.google.com/earth-engine/guides/image_relational#conditional-operators)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/image_relational.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/image_relational.ipynb)  
---|---  
`ee.Image` objects have a set of relational, conditional, and boolean methods for constructing decision-making expressions. The results of these methods are useful for limiting analysis to certain pixels or regions through masking, developing classified maps, and value reassignment.
## Relational and boolean operators
**Relational** methods include:
`eq()`, `gt()`, `gte()`, `lt()`, and `lte()`
**Boolean** methods include:
### Code Editor (JavaScript)
`and()`,`or()`, and `not()`
### Colab (Python)
`And()`,`Or()`, and `Not()`
To perform per-pixel comparisons between images, use relational operators. To extract urbanized areas in an image, this example uses relational operators to threshold spectral indices, combining the thresholds with the _and_ operator:
### Code Editor (JavaScript)
```
// Load a Landsat 8 image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
// Create NDVI and NDWI spectral indices.
varndvi=image.normalizedDifference(['B5','B4']);
varndwi=image.normalizedDifference(['B3','B5']);
// Create a binary layer using logical operations.
varbare=ndvi.lt(0.2).and(ndwi.lt(0));
// Mask and display the binary layer.
Map.setCenter(-122.3578,37.7726,12);
Map.setOptions('satellite');
Map.addLayer(bare.selfMask(),{},'bare');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a Landsat 8 image.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
# Create NDVI and NDWI spectral indices.
ndvi = image.normalizedDifference(['B5', 'B4'])
ndwi = image.normalizedDifference(['B3', 'B5'])
# Create a binary layer using logical operations.
bare = ndvi.lt(0.2).And(ndwi.lt(0))
# Define a map centered on San Francisco Bay.
map_bare = geemap.Map(center=[37.7726, -122.3578], zoom=12)
# Add the masked image layer to the map and display it.
map_bare.add_layer(bare.selfMask(), None, 'bare')
display(map_bare)
```

As illustrated by this example, the output of relational and boolean operators is either true (1) or false (0). To mask the 0's, you can mask the resultant binary image with itself using `selfMask()`.
![relational_sf](https://developers.google.com/static/earth-engine/images/Images_relational_sf.png) Low NDVI and low NDWI (white) from Landsat 8, San Francisco, California, USA. 
The binary images that are returned by relational and boolean operators can be used with mathematical operators. This example creates zones of urbanization in a nighttime lights image using relational operators and `add()`:
### Code Editor (JavaScript)
```
// Load a 2012 nightlights image.
varnl2012=ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182012');
varlights=nl2012.select('stable_lights');
// Define arbitrary thresholds on the 6-bit stable lights band.
varzones=lights.gt(30).add(lights.gt(55)).add(lights.gt(62));
// Display the thresholded image as three distinct zones near Paris.
varpalette=['000000','0000FF','00FF00','FF0000'];
Map.setCenter(2.373,48.8683,8);
Map.addLayer(zones,{min:0,max:3,palette:palette},'development zones');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a 2012 nightlights image.
nl_2012 = ee.Image('NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182012')
lights = nl_2012.select('stable_lights')
# Define arbitrary thresholds on the 6-bit stable lights band.
zones = lights.gt(30).add(lights.gt(55)).add(lights.gt(62))
# Define a map centered on Paris, France.
map_zones = geemap.Map(center=[48.8683, 2.373], zoom=8)
# Display the thresholded image as three distinct zones near Paris.
palette = ['000000', '0000FF', '00FF00', 'FF0000']
map_zones.add_layer(
  zones, {'min': 0, 'max': 3, 'palette': palette}, 'development zones'
)
display(map_zones)
```

## Conditional operators
Note that the code in the previous example is equivalent to using a [ternary operator](http://en.wikipedia.org/wiki/%3F:) implemented by `expression()`:
### Code Editor (JavaScript)
```
// Create zones using an expression, display.
varzonesExp=nl2012.expression(
"(b('stable_lights') > 62) ? 3"+
": (b('stable_lights') > 55) ? 2"+
": (b('stable_lights') > 30) ? 1"+
": 0"
);
Map.addLayer(zonesExp,
{min:0,max:3,palette:palette},
'development zones (ternary)');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create zones using an expression, display.
zones_exp = nl_2012.expression(
  "(b('stable_lights') > 62) ? 3 "
  ": (b('stable_lights') > 55) ? 2 "
  ": (b('stable_lights') > 30) ? 1 "
  ': 0'
)
# Define a map centered on Paris, France.
map_zones_exp = geemap.Map(center=[48.8683, 2.373], zoom=8)
# Add the image layer to the map and display it.
map_zones_exp.add_layer(
  zones_exp, {'min': 0, 'max': 3, 'palette': palette}, 'zones exp'
)
display(map_zones_exp)
```

Observe that in the previous expression example, the band of interest is referenced using the `b()` function, rather than a dictionary of variable names. Learn more about image expressions on [this page](https://developers.google.com/earth-engine/guides/image_math#expressions). Using either mathematical operators or an expression will produce the same result.
![conditional_paris](https://developers.google.com/static/earth-engine/images/Images_conditional_nightlights_paris.png) Arbitrary zones of 2012 nightlights imagery for Paris, France. 
Another way to implement conditional operations on images is with the `where()` operator. Consider the need to replace masked pixels with some other data. In the following example, cloudy pixels are replaced by pixels from a cloud-free image using `where()`:
### Code Editor (JavaScript)
```
// Load a cloudy Sentinel-2 image.
varimage=ee.Image(
'COPERNICUS/S2_SR/20210114T185729_20210114T185730_T10SEG');
Map.addLayer(image,
{bands:['B4','B3','B2'],min:0,max:2000},
'original image');
// Load another image to replace the cloudy pixels.
varreplacement=ee.Image(
'COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG');
// Set cloudy pixels (greater than 5% probability) to the other image.
varreplaced=image.where(image.select('MSK_CLDPRB').gt(5),replacement);
// Display the result.
Map.setCenter(-122.3769,37.7349,11);
Map.addLayer(replaced,
{bands:['B4','B3','B2'],min:0,max:2000},
'clouds replaced');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a cloudy Sentinel-2 image.
image = ee.Image('COPERNICUS/S2_SR/20210114T185729_20210114T185730_T10SEG')
# Load another image to replace the cloudy pixels.
replacement = ee.Image(
  'COPERNICUS/S2_SR/20210109T185751_20210109T185931_T10SEG'
)
# Set cloudy pixels (greater than 5% probability) to the other image.
replaced = image.where(image.select('MSK_CLDPRB').gt(5), replacement)
# Define a map centered on San Francisco Bay.
map_replaced = geemap.Map(center=[37.7349, -122.3769], zoom=11)
# Display the images on a map.
vis_params = {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 2000}
map_replaced.add_layer(image, vis_params, 'original image')
map_replaced.add_layer(replaced, vis_params, 'clouds replaced')
display(map_replaced)
```

