 
#  ee.ImageCollection.fromImages
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-fromimages#examples)


Returns the image collection containing the given images. 
Usage| Returns  
---|---  
`ee.ImageCollection.fromImages(images)`| ImageCollection  
Argument| Type| Details  
---|---|---  
`images`| List| The images to include in the collection.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-fromimages#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-fromimages#colab-python-sample) More
```
// A series of images.
varimg1=ee.Image(0);
varimg2=ee.Image(1);
varimg3=ee.Image(2);
// Convert the list of images into an image collection.
varcol=ee.ImageCollection.fromImages([img1,img2,img3]);
print('Collection from list of images',col);
// The ee.ImageCollection.fromImages function is intended to coerce the image
// list to a collection when the list is an ambiguous, computed object fetched
// from the properties of a server-side object. For instance, a list
// of images retrieved from a ee.Feature property. Here, we set an image
// list as a property of a feature, retrieve it, and convert it to
// a collection. Notice that the ee.ImageCollection constructor fails to coerce
// the image list to a collection, but ee.ImageCollection.fromImages does.
varfeature=ee.Feature(null).set('img_list',[img1,img2,img3]);
varambiguousImgList=feature.get('img_list');
print('Coerced to collection',ee.ImageCollection.fromImages(ambiguousImgList));
print('NOT coerced to collection',ee.ImageCollection(ambiguousImgList));
// A common use case is coercing an image list from a saveAll join to a
// image collection, like in this example of building a collection of mean
// annual NDVI images from a MODIS collection.
varmodisCol=ee.ImageCollection('MODIS/006/MOD13A2')
.filterDate('2017','2021')
.select('NDVI')
.map(function(img){returnimg.set('year',img.date().get('year'))});
vardistinctYearCol=modisCol.distinct('year');
varjoinedCol=ee.Join.saveAll('img_list').apply({
primary:distinctYearCol,
secondary:modisCol,
condition:ee.Filter.equals({'leftField':'year','rightField':'year'})
});
varannualNdviMean=joinedCol.map(function(img){
returnee.ImageCollection.fromImages(img.get('img_list')).mean()
.copyProperties(img,['year']);
});
print('Mean annual NDVI collection',annualNdviMean);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# A series of images.
img1 = ee.Image(0)
img2 = ee.Image(1)
img3 = ee.Image(2)
# Convert the list of images into an image collection.
col = ee.ImageCollection.fromImages([img1, img2, img3])
print('Collection from list of images:', col.getInfo())
# The ee.ImageCollection.fromImages function is intended to coerce the image
# list to a collection when the list is an ambiguous, computed object fetched
# from the properties of a server-side object. For instance, a list
# of images retrieved from a ee.Feature property. Here, we set an image
# list as a property of a feature, retrieve it, and convert it to
# a collection. Notice that the ee.ImageCollection constructor fails to coerce
# the image list to a collection, but ee.ImageCollection.fromImages does.
feature = ee.Feature(None).set('img_list', [img1, img2, img3])
ambiguous_img_list = feature.get('img_list')
print(
  'Coerced to collection:',
  ee.ImageCollection.fromImages(ambiguous_img_list).getInfo(),
)
print(
  'NOT coerced to collection:',
  ee.ImageCollection(ambiguous_img_list).getInfo(),
)
# A common use case is coercing an image list from a saveAll join to a
# image collection, like in this example of building a collection of mean
# annual NDVI images from a MODIS collection.
modis_col = (
  ee.ImageCollection('MODIS/006/MOD13A2')
  .filterDate('2017', '2021')
  .select('NDVI')
  .map(lambda img: img.set('year', img.date().get('year')))
)
distinct_year_col = modis_col.distinct('year')
joined_col = ee.Join.saveAll('img_list').apply(
  primary=distinct_year_col,
  secondary=modis_col,
  condition=ee.Filter.equals(leftField='year', rightField='year'),
)
annual_ndvi_mean = joined_col.map(
  lambda img: ee.ImageCollection.fromImages(img.get('img_list'))
  .mean()
  .copyProperties(img, ['year'])
)
print('Mean annual NDVI collection:', annual_ndvi_mean.getInfo())
```

Was this helpful?
