 
#  ee.ImageCollection.sort 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-sort#examples)


Sort a collection by the specified property. 
Returns the sorted collection.
Usage| Returns  
---|---  
`ImageCollection.sort(property,  _ascending_)`| Collection  
Argument| Type| Details  
---|---|---  
this: `collection`| Collection| The Collection instance.  
`property`| String| The property to sort by.  
`ascending`| Boolean, optional| Whether to sort in ascending or descending order. The default is true (ascending).  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-sort#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-sort#colab-python-sample) More
```
// A Landsat 8 TOA image collection (2 months of images at a specific point).
varcol=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.Point(-90.70,34.71))
.filterDate('2020-07-01','2020-09-01');
print('Collection',col);
// Sort the collection in ASCENDING order of image cloud cover.
varcolCldSortAsc=col.sort('CLOUD_COVER');
print('Cloud cover ascending',colCldSortAsc);
// Display the image with the least cloud cover.
varvisParams={
bands:['B4','B3','B2'],
min:0.01,
max:0.25
};
Map.setCenter(-90.70,34.71,9);
Map.addLayer(colCldSortAsc.first(),visParams,'Least cloudy');
// Sort the collection in DESCENDING order of image cloud cover.
varcolCldSortDesc=col.sort('CLOUD_COVER',false);
print('Cloud cover descending',colCldSortDesc);
// Display the image with the most cloud cover.
Map.addLayer(colCldSortDesc.first(),visParams,'Most cloudy');
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
)
display('Collection', col)
# Sort the collection in ASCENDING order of image cloud cover.
col_cld_sort_asc = col.sort('CLOUD_COVER')
display('Cloud cover ascending', col_cld_sort_asc)
# Display the image with the least cloud cover.
vis_params = {'bands': ['B4', 'B3', 'B2'], 'min': 0.01, 'max': 0.25}
m = geemap.Map()
m.set_center(-90.70, 34.71, 9)
m.add_layer(col_cld_sort_asc.first(), vis_params, 'Least cloudy')
# Sort the collection in DESCENDING order of image cloud cover.
col_cld_sort_desc = col.sort('CLOUD_COVER', False)
display('Cloud cover descending', col_cld_sort_desc)
# Display the image with the most cloud cover.
m.add_layer(col_cld_sort_desc.first(), vis_params, 'Most cloudy')
m
```

Was this helpful?
