 
#  ee.ImageCollection
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection#examples)


- A string: assumed to be the name of a collection,
- A list of images, or anything that can be used to construct an image.
- A single image.
- A computed object - reinterpreted as a collection.
Usage | Returns  
---|---  
`ee.ImageCollection(args)` | ImageCollection  
Argument | Type | Details  
---|---|---  
`args` | ComputedObject|Image|List<Object>|String | The constructor arguments.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection#colab-python-sample) More
```
print('Image collection from a string',
ee.ImageCollection('COPERNICUS/S2_SR').limit(3));

varimg1=ee.Image('COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNK');
varimg2=ee.Image('COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNL');
varimg3=ee.Image('COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNM');
print('Image collection from a list of images',
ee.ImageCollection([img1,img2,img3]));

print('Image collection from a single image',
ee.ImageCollection(img1));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
print('Image collection from a string:',
      ee.ImageCollection('COPERNICUS/S2_SR').limit(3).getInfo())

img1 = ee.Image('COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNK')
img2 = ee.Image('COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNL')
img3 = ee.Image('COPERNICUS/S2_SR/20170328T083601_20170328T084228_T35RNM')
print('Image collection from a list of images:',
      ee.ImageCollection([img1, img2, img3]).getInfo())

print('Image collection from a single image:',
      ee.ImageCollection(img1).getInfo())
```

