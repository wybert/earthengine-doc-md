 
#  Spectral transformations 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Pan sharpening](https://developers.google.com/earth-engine/guides/image_transforms#pan-sharpening)
  * [Spectral unmixing](https://developers.google.com/earth-engine/guides/image_transforms#spectral-unmixing)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/image_transforms.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/image_transforms.ipynb)  
---|---  
There are several spectral transformation methods in Earth Engine. These include instance methods on images such as `normalizedDifference()`, `unmix()`, `rgbToHsv()` and `hsvToRgb()`.
## Pan sharpening
Pan sharpening improves the resolution of a multiband image through enhancement provided by a corresponding panchromatic image with finer resolution. The `rgbToHsv()` and `hsvToRgb()` methods are useful for pan sharpening.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_transforms#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_transforms#colab-python-sample) More
```
// Load a Landsat 8 top-of-atmosphere reflectance image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318');
Map.addLayer(
image,
{bands:['B4','B3','B2'],min:0,max:0.25,gamma:[1.1,1.1,1]},
'rgb');
// Convert the RGB bands to the HSV color space.
varhsv=image.select(['B4','B3','B2']).rgbToHsv();
// Swap in the panchromatic band and convert back to RGB.
varsharpened=ee.Image.cat([
hsv.select('hue'),hsv.select('saturation'),image.select('B8')
]).hsvToRgb();
// Display the pan-sharpened result.
Map.setCenter(-122.44829,37.76664,13);
Map.addLayer(sharpened,
{min:0,max:0.25,gamma:[1.3,1.3,1.3]},
'pan-sharpened');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 top-of-atmosphere reflectance image.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318')
# Convert the RGB bands to the HSV color space.
hsv = image.select(['B4', 'B3', 'B2']).rgbToHsv()
# Swap in the panchromatic band and convert back to RGB.
sharpened = ee.Image.cat(
  [hsv.select('hue'), hsv.select('saturation'), image.select('B8')]
).hsvToRgb()
# Define a map centered on San Francisco, California.
map_sharpened = geemap.Map(center=[37.76664, -122.44829], zoom=13)
# Add the image layers to the map and display it.
map_sharpened.add_layer(
  image,
  {
    'bands': ['B4', 'B3', 'B2'],
    'min': 0,
    'max': 0.25,
    'gamma': [1.1, 1.1, 1],
  },
  'rgb',
)
map_sharpened.add_layer(
  sharpened,
  {'min': 0, 'max': 0.25, 'gamma': [1.3, 1.3, 1.3]},
  'pan-sharpened',
)
display(map_sharpened)
```

## Spectral unmixing
Spectral unmixing is implemented in Earth Engine as the `image.unmix()` method. (For more flexible methods, see the [Array Transformations page](https://developers.google.com/earth-engine/guides/arrays_transformations)). The following is an example of unmixing Landsat 5 with predetermined urban, vegetation and water endmembers:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_transforms#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_transforms#colab-python-sample) More
```
// Load a Landsat 5 image and select the bands we want to unmix.
varbands=['B1','B2','B3','B4','B5','B6','B7'];
varimage=ee.Image('LANDSAT/LT05/C02/T1/LT05_044034_20080214')
.select(bands);
Map.setCenter(-122.1899,37.5010,10);// San Francisco Bay
Map.addLayer(image,{bands:['B4','B3','B2'],min:0,max:128},'image');
// Define spectral endmembers.
varurban=[88,42,48,38,86,115,59];
varveg=[50,21,20,35,50,110,23];
varwater=[51,20,14,9,7,116,4];
// Unmix the image.
varfractions=image.unmix([urban,veg,water]);
Map.addLayer(fractions,{},'unmixed');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 5 image and select the bands we want to unmix.
bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
image = ee.Image('LANDSAT/LT05/C02/T1/LT05_044034_20080214').select(bands)
# Define spectral endmembers.
urban = [88, 42, 48, 38, 86, 115, 59]
veg = [50, 21, 20, 35, 50, 110, 23]
water = [51, 20, 14, 9, 7, 116, 4]
# Unmix the image.
fractions = image.unmix([urban, veg, water])
# Define a map centered on San Francisco Bay.
map_fractions = geemap.Map(center=[37.5010, -122.1899], zoom=10)
# Add the image layers to the map and display it.
map_fractions.add_layer(
  image, {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 128}, 'image'
)
map_fractions.add_layer(fractions, None, 'unmixed')
display(map_fractions)
```
![unmixed_sf](https://developers.google.com/static/earth-engine/images/Images_unmixing_sf.png) Figure 1. Landsat 5 imagery unmixed to urban (red), vegetation (green) and water (blue) fractions. San Francisco bay area, California, USA. 
Was this helpful?
