 
#  ee.Dictionary.toImage
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-dictionary-toimage#examples)


Creates an image of constants from values in a dictionary. The bands of the image are ordered and named according to the names argument. If no names are specified, the bands are sorted alpha-numerically.
Usage | Returns  
---|---  
`Dictionary.toImage(_names_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `dictionary` | Dictionary | The dictionary to convert.  
`names` | List, default: null | The order of the output bands.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-toimage#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-dictionary-toimage#colab-python-sample) More
```
// A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
vardict=ee.Dictionary({
B1:182,
B2:219,
B3:443
});

varselectedKeysImg=dict.toImage(['B1','B2']);
print('Selected keys image band names',selectedKeysImg.bandNames());

varallKeysImg=dict.toImage();
print('All keys image band names',allKeysImg.bandNames());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A dictionary (e.g. results of ee.Image.reduceRegion of an S2 image).
dic = ee.Dictionary({
    'B1': 182,
    'B2': 219,
    'B3': 443
})

selected_keys_img = dic.toImage(['B1', 'B2'])
print('Selected keys image band names:',
      selected_keys_img.bandNames().getInfo())

all_keys_img = dic.toImage()
print('All keys image band names:', all_keys_img.bandNames().getInfo())
```

