 
#  Mapping over an ImageCollection 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
To apply a function to every `Image` in an `ImageCollection` use `imageCollection.map()`. The only argument to `map()` is a function which takes one parameter: an `ee.Image`. For example, the following code adds a timestamp band to every image in the collection.
### Code Editor (JavaScript)
```
// Load a Landsat 8 collection for a single path-row, 2021 images only.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterDate('2021','2022')
.filter(ee.Filter.eq('WRS_PATH',44))
.filter(ee.Filter.eq('WRS_ROW',34));
// This function adds a band representing the image timestamp.
varaddTime=function(image){
returnimage.addBands(image.getNumber('system:time_start'));
};
// Map the function over the collection and display the result.
print(collection.map(addTime));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a Landsat 8 collection for a single path-row, 2021 images only.
collection = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filterDate('2021', '2022')
  .filter(ee.Filter.eq('WRS_PATH', 44))
  .filter(ee.Filter.eq('WRS_ROW', 34))
)

# This function adds a band representing the image timestamp.
defadd_time(image):
 return image.addBands(image.getNumber('system:time_start'))

# Map the function over the collection and display the result.
display(collection.map(add_time))
```

Note that in the predefined function, the `getNumber()` method is used to create a new `Image` from the numerical value of a property. As discussed in the [Reducing](https://developers.google.com/earth-engine/guides/ic_reducing) and [Compositing](https://developers.google.com/earth-engine/guides/ic_composite_mosaic) sections, having the time band is useful for linear modeling of change and for making composites.
The mapped function is limited in the operations it can perform. Specifically, it can't modify variables outside the function; it can't print anything; it can't use JavaScript and Python 'if' or 'for' statements. However, you can use `ee.Algorithms.If()` to perform conditional operations in a mapped function. For example:
### Code Editor (JavaScript)
```
// Load a Landsat 8 collection for a single path-row, 2021 images only.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterDate('2021','2022')
.filter(ee.Filter.eq('WRS_PATH',44))
.filter(ee.Filter.eq('WRS_ROW',34));
// This function uses a conditional statement to return the image if
// the solar elevation > 40 degrees. Otherwise it returns a "zero image".
varconditional=function(image){
returnee.Algorithms.If(ee.Number(image.get('SUN_ELEVATION')).gt(40),
image,
ee.Image(0));
};
// Map the function over the collection and print the result. Expand the
// collection and note that 7 of the 22 images are now "zero images'.
print('Expand this to see the result',collection.map(conditional));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a Landsat 8 collection for a single path-row, 2021 images only.
collection = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filterDate('2021', '2022')
  .filter(ee.Filter.eq('WRS_PATH', 44))
  .filter(ee.Filter.eq('WRS_ROW', 34))
)

# This function uses a conditional statement to return the image if
# the solar elevation > 40 degrees. Otherwise it returns a "zero image".
defconditional(image):
 return ee.Algorithms.If(
   ee.Number(image.get('SUN_ELEVATION')).gt(40), image, ee.Image(0)
 )

# Map the function over the collection and print the result. Expand the
# collection and note that 7 of the 22 images are now "zero images'.
display('Expand this to see the result', collection.map(conditional))
```

Inspect the list of images in the output ImageCollection and note that when the condition evaluated by the `If()` algorithm is true, the output contains a constant image. Although this demonstrates a server-side conditional function ([learn more about client vs. server in Earth Engine](https://developers.google.com/earth-engine/guides/client_server)), avoid `If()` in general and use filters instead.
