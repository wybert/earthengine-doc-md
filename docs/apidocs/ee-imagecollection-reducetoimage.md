 
#  ee.ImageCollection.reduceToImage
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-reducetoimage#examples)


Creates an image from a feature collection by applying a reducer over the selected properties of all the features that intersect each pixel. 
Usage| Returns  
---|---  
`ImageCollection.reduceToImage(properties, reducer)`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| Feature collection to intersect with each output pixel.  
`properties`| List| Properties to select from each feature and pass into the reducer.  
`reducer`| Reducer| A Reducer to combine the properties of each intersecting feature into a final result to store in the pixel.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-reducetoimage#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-reducetoimage#colab-python-sample) More
```
varcol=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.BBox(-124.0,43.2,-116.5,46.3))
.filterDate('2021','2022');
// Image visualization settings.
varvisParams={
bands:['B4','B3','B2'],
min:0.01,
max:0.25
};
Map.addLayer(col.mean(),visParams,'RGB mean');
// Reduce the geometry (footprint) of images in the collection to an image.
// Image property values are applied to the pixels intersecting each
// image's geometry and then a per-pixel reduction is performed according
// to the selected reducer. Here, the image cloud cover property is assigned
// to the pixels intersecting image geometry and then reduced to a single
// image representing the per-pixel mean image cloud cover.
varmeanCloudCover=col.reduceToImage({
properties:['CLOUD_COVER'],
reducer:ee.Reducer.mean()
});
Map.setCenter(-119.87,44.76,6);
Map.addLayer(meanCloudCover,{min:0,max:50},'Cloud cover mean');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
col = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filterBounds(ee.Geometry.BBox(-124.0, 43.2, -116.5, 46.3))
  .filterDate('2021', '2022')
)
# Image visualization settings.
vis_params = {'bands': ['B4', 'B3', 'B2'], 'min': 0.01, 'max': 0.25}
m = geemap.Map()
m.add_layer(col.mean(), vis_params, 'RGB mean')
# Reduce the geometry (footprint) of images in the collection to an image.
# Image property values are applied to the pixels intersecting each
# image's geometry and then a per-pixel reduction is performed according
# to the selected reducer. Here, the image cloud cover property is assigned
# to the pixels intersecting image geometry and then reduced to a single
# image representing the per-pixel mean image cloud cover.
mean_cloud_cover = col.reduceToImage(
  properties=['CLOUD_COVER'], reducer=ee.Reducer.mean()
)
m.set_center(-119.87, 44.76, 6)
m.add_layer(mean_cloud_cover, {'min': 0, 'max': 50}, 'Cloud cover mean')
m
```

