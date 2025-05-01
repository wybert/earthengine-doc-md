 
#  Image Overview 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [ ee.Image constructor ](https://developers.google.com/earth-engine/guides/image_overview#ee.image-constructor)
  * [ Get an ee.Image from an ee.ImageCollection ](https://developers.google.com/earth-engine/guides/image_overview#get-an-ee.image-from-an-ee.imagecollection)
  * [ Images from Cloud GeoTIFFs ](https://developers.google.com/earth-engine/guides/image_overview#images-from-cloud-geotiffs)
  * [ Constant images ](https://developers.google.com/earth-engine/guides/image_overview#constant-images)


[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/guides/linked/generated/image_overview.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/guides/linked/generated/image_overview.ipynb)  
---|---  
As mentioned in the [Get Started](https://developers.google.com/earth-engine/guides/getstarted#earth-engine-data-structures) doc, raster data are represented as `Image` objects in Earth Engine. Images are composed of one or more bands and each band has its own name, data type, scale, mask and projection. Each image has metadata stored as a set of properties.
##  `ee.Image` constructor 
Images can be loaded by pasting an Earth Engine asset ID into the `ee.Image` constructor. You can find image IDs in the [data catalog](https://developers.google.com/earth-engine/datasets). For example, to load [JAXA's ALOS DSM](https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_AW3D30_V3_2): 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_overview#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_overview#colab-python-sample) More
```
varloadedImage=ee.Image('JAXA/ALOS/AW3D30/V2_2');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
loaded_image = ee.Image('JAXA/ALOS/AW3D30/V2_2')
```

Note that finding an image through [the Code Editor search tool](https://developers.google.com/earth-engine/guides/playground#search-tool) is equivalent. When you import the asset, the image construction code is written for you in the [imports section of the Code Editor](https://developers.google.com/earth-engine/guides/playground#imports). You can also use a personal [asset ID](https://developers.google.com/earth-engine/guides/manage_assets#asset_id) as the argument to the `ee.Image` constructor. 
##  Get an `ee.Image` from an `ee.ImageCollection`
The standard way to get an image out of a collection is to filter the collection, with filters in order of decreasing specificity. For example, to get an image out of the [Sentinel-2 surface reflectance collection](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR): 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_overview#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_overview#colab-python-sample) More
```
varfirst=ee.ImageCollection('COPERNICUS/S2_SR')
.filterBounds(ee.Geometry.Point(-70.48,43.3631))
.filterDate('2019-01-01','2019-12-31')
.sort('CLOUDY_PIXEL_PERCENTAGE')
.first();
Map.centerObject(first,11);
Map.addLayer(first,{bands:['B4','B3','B2'],min:0,max:2000},'first');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
first = (
  ee.ImageCollection('COPERNICUS/S2_SR')
  .filterBounds(ee.Geometry.Point(-70.48, 43.3631))
  .filterDate('2019-01-01', '2019-12-31')
  .sort('CLOUDY_PIXEL_PERCENTAGE')
  .first()
)
# Define a map centered on southern Maine.
m = geemap.Map(center=[43.7516, -70.8155], zoom=11)
# Add the image layer to the map and display it.
m.add_layer(
  first, {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 2000}, 'first'
)
display(m)
```

Note that the sort is _after_ the filters. Avoid sorting the entire collection. 
##  Images from Cloud GeoTIFFs 
You can use `ee.Image.loadGeoTIFF()` to load images from [Cloud Optimized GeoTIFFs](https://github.com/cogeotiff/cog-spec/blob/master/spec.md) in [Google Cloud Storage](https://cloud.google.com/storage). For example, the [public Landsat dataset](https://console.cloud.google.com/marketplace/details/usgs-public-data/landast) hosted in Google Cloud contains [this GeoTIFF](https://console.cloud.google.com/storage/browser/_details/gcp-public-data-landsat/LC08/01/001/002/LC08_L1GT_001002_20160817_20170322_01_T2/LC08_L1GT_001002_20160817_20170322_01_T2_B5.TIF), corresponding to band 5 from a Landsat 8 scene. You can load this image from Cloud Storage using `ee.Image.loadGeoTIFF()`: 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_overview#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_overview#colab-python-sample) More
```
varuri='gs://gcp-public-data-landsat/LC08/01/001/002/'+
'LC08_L1GT_001002_20160817_20170322_01_T2/'+
'LC08_L1GT_001002_20160817_20170322_01_T2_B5.TIF';
varcloudImage=ee.Image.loadGeoTIFF(uri);
print(cloudImage);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
uri = (
  'gs://gcp-public-data-landsat/LC08/01/001/002/'
  + 'LC08_L1GT_001002_20160817_20170322_01_T2/'
  + 'LC08_L1GT_001002_20160817_20170322_01_T2_B5.TIF'
)
cloud_image = ee.Image.loadGeoTIFF(uri)
display(cloud_image)
```

Note that if you want to reload a Cloud Optimized GeoTIFF that you [export from Earth Engine to Cloud Storage](https://developers.google.com/earth-engine/guides/exporting#to-cloud-storage), when you do the export, set `cloudOptimized` to **true** as described [here](https://developers.google.com/earth-engine/guides/exporting#configuration-parameters). 
##  Constant images 
In addition to loading images by ID, you can also create images from constants, lists or other suitable Earth Engine objects. The following illustrates methods for creating images, getting band subsets, and manipulating bands:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/image_overview#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/image_overview#colab-python-sample) More
```
// Create a constant image.
varimage1=ee.Image(1);
print(image1);
// Concatenate two images into one multi-band image.
varimage2=ee.Image(2);
varimage3=ee.Image.cat([image1,image2]);
print(image3);
// Create a multi-band image from a list of constants.
varmultiband=ee.Image([1,2,3]);
print(multiband);
// Select and (optionally) rename bands.
varrenamed=multiband.select(
['constant','constant_1','constant_2'],// old names
['band1','band2','band3']// new names
);
print(renamed);
// Add bands to an image.
varimage4=image3.addBands(ee.Image(42));
print(image4);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Create a constant image.
image_1 = ee.Image(1)
display(image_1)
# Concatenate two images into one multi-band image.
image_2 = ee.Image(2)
image_3 = ee.Image.cat([image_1, image_2])
display(image_3)
# Create a multi-band image from a list of constants.
multiband = ee.Image([1, 2, 3])
display(multiband)
# Select and (optionally) rename bands.
renamed = multiband.select(
  ['constant', 'constant_1', 'constant_2'], # old names
  ['band1', 'band2', 'band3'], # new names
)
display(renamed)
# Add bands to an image.
image_4 = image_3.addBands(ee.Image(42))
display(image_4)
```

