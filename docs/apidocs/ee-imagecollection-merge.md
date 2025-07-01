 
#  ee.ImageCollection.merge
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-merge#examples)


Merges two image collections into one. The result has all the images that were in either collection. 
Usage| Returns  
---|---  
`ImageCollection.merge(collection2)`| ImageCollection  
Argument| Type| Details  
---|---|---  
this: `collection1`| ImageCollection| The first collection to merge.  
`collection2`| ImageCollection| The second collection to merge.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-merge#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-merge#colab-python-sample) More
```
// Sentinel-2 surface reflectance image collection.
varic=ee.ImageCollection('COPERNICUS/S2_SR');
// Filter the images to those that intersect Mount Shasta for 3 months
// in 2019 and 2021 (two image collections).
vargeom=ee.Geometry.Point(-122.196,41.411);
varic2018=ic.filterBounds(geom).filterDate('2019-07-01','2019-10-01');
print('2018 image collection',ic2018);
varic2021=ic.filterBounds(geom).filterDate('2021-07-01','2021-10-01');
print('2021 image collection',ic2021);
// Merge the two image collections.
varicMerged=ic2018.merge(ic2021);
print('Merged image collection',icMerged);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Sentinel-2 surface reflectance image collection.
ic = ee.ImageCollection('COPERNICUS/S2_SR')
# Filter the images to those that intersect Mount Shasta for 3 months
# in 2019 and 2021 (two image collections).
geom = ee.Geometry.Point(-122.196, 41.411)
ic2018 = ic.filterBounds(geom).filterDate('2019-07-01', '2019-10-01')
print('2018 image collection:', ic2018.getInfo())
ic2021 = ic.filterBounds(geom).filterDate('2021-07-01', '2021-10-01')
print('2021 image collection:', ic2021.getInfo())
# Merge the two image collections.
ic_merged = ic2018.merge(ic2021)
print('Merged image collection:', ic_merged.getInfo())
```

Was this helpful?
