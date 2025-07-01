 
#  ee.ImageCollection.toList
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-tolist#examples)


Returns the elements of a collection as a list. 
Usage| Returns  
---|---  
`ImageCollection.toList(count,  _offset_)`| List  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection to fetch.  
`count`| Integer| The maximum number of elements to fetch.  
`offset`| Integer, default: 0| The number of elements to discard from the start. If set, (offset + count) elements will be fetched and the first offset elements will be discarded.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-tolist#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-tolist#colab-python-sample) More
```
// Note: ee.ImageCollection.toList may take a lot of time and memory to run,
// since it must generate all of the results in order to gather them into a
// list. Large collections and/or complex computations can produce memory
// limitation errors.
// A Landsat 8 TOA image collection (1 year of images at a specific point).
varcol=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.Point(-90.70,34.71))
.filterDate('2020-01-01','2021-01-01');
print('Image collection',col);
// Get the first 3 images as a list of images.
varimgListFirst3=col.toList(3);
print('First 3 images',imgListFirst3);
// Get the second 3 images as a list of images (use the offset parameter).
varimgListSecond3=col.toList(3,3);
print('Second 3 images',imgListSecond3);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Note: ee.ImageCollection.toList may take a lot of time and memory to run,
# since it must generate all of the results in order to gather them into a
# list. Large collections and/or complex computations can produce memory
# limitation errors.
# A Landsat 8 TOA image collection (1 year of images at a specific point).
col = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA').filterBounds(
  ee.Geometry.Point(-90.70, 34.71)).filterDate('2020-01-01', '2021-01-01')
print('Image collection:', col.getInfo())
# Get the first 3 images as a list of images.
img_list_first3 = col.toList(3)
print('First 3 images:', img_list_first3.getInfo())
# Get the second 3 images as a list of images (use the offset parameter).
img_list_second3 = col.toList(3, 3)
print('Second 3 images:', img_list_second3.getInfo())
```

Was this helpful?
