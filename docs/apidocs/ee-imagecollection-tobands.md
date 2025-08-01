 
#  ee.ImageCollection.toBands
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-tobands#examples)


Converts a collection to a single multi-band image containing all of the bands of every image in the collection. Output bands are named by prefixing the existing band names with the image id from which it came (e.g., 'image1_band1'). Note: The maximum number of bands is 5000.
Usage | Returns  
---|---  
`ImageCollection.toBands()` | Image  
Argument | Type | Details  
---|---|---  
this: `collection` | ImageCollection | The input collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-tobands#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-tobands#colab-python-sample) More
```
// A Landsat 8 TOA image collection (2 months of images at a specific point).
varcol=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.Point(-90.70,34.71))
.filterDate('2020-07-01','2020-09-01')
.select('B[4-5]');// Get NIR and SWIR1 bands only.
print('Collection',col);

// Convert the image collection to a single multi-band image. Note that image ID
// ('system:index') is prepended to band names to delineate the source images.
varimg=col.toBands();
print('Collection to bands',img);

// Band order is determined by collection order. Here, the collection is
// sorted in descending order of the date of observation (reverse of previous).
varbandOrder=col.sort('DATE_ACQUIRED',false).toBands();
print('Customized band order',bandOrder);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A Landsat 8 TOA image collection (2 months of images at a specific point).
col = (
    ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
    .filterBounds(ee.Geometry.Point(-90.70, 34.71))
    .filterDate('2020-07-01', '2020-09-01')
    .select('B[4-5]')
)  # Get NIR and SWIR1 bands only.
print('Collection:', col.getInfo())

# Convert the image collection to a single multi-band image. Note that image ID
# ('system:index') is prepended to band names to delineate the source images.
img = col.toBands()
print('Collection to bands:', img.getInfo())

# Band order is determined by collection order. Here, the collection is
# sorted in descending order of the date of observation (reverse of previous).
band_order = col.sort('DATE_ACQUIRED', False).toBands()
print('Customized band order:', band_order.getInfo())
```

Was this helpful?
