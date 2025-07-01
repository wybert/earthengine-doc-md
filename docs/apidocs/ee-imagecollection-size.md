 
#  ee.ImageCollection.size
Stay organized with collections  Save and categorize content based on your preferences. 
Returns the number of elements in the collection. Usage| Returns  
---|---  
`ImageCollection.size()`| Integer  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The collection to count.  
## Examples
### Code Editor (JavaScript)
```
// Note: ee.ImageCollection.size may take a lot of time and memory to run,
// since it must generate all of the results in order to count them. Large
// collections and/or complex computations can produce memory limitation
// errors.
// A Landsat 8 TOA image collection (1 year of images at a specific point).
varcol=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.Point(-90.70,34.71))
.filterDate('2020-01-01','2021-01-01');
// Get the number of images in the collection.
print('Number of images',col.size());
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Note: ee.ImageCollection.size may take a lot of time and memory to run,
# since it must generate all of the results in order to count them. Large
# collections and/or complex computations can produce memory limitation
# errors.
# A Landsat 8 TOA image collection (1 year of images at a specific point).
col = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA').filterBounds(
  ee.Geometry.Point(-90.70, 34.71)
  ).filterDate('2020-01-01', '2021-01-01')
# Get the number of images in the collection.
print('Number of images', col.size().getInfo())
```

