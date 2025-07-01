 
#  ee.FeatureCollection.reduceToImage
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-reducetoimage#examples)


Creates an image from a feature collection by applying a reducer over the selected properties of all the features that intersect each pixel. 
Usage| Returns  
---|---  
`FeatureCollection.reduceToImage(properties, reducer)`| Image  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| Feature collection to intersect with each output pixel.  
`properties`| List| Properties to select from each feature and pass into the reducer.  
`reducer`| Reducer| A Reducer to combine the properties of each intersecting feature into a final result to store in the pixel.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-reducetoimage#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-reducetoimage#colab-python-sample) More
```
// FeatureCollection of power plants in Belgium.
varfc=ee.FeatureCollection('WRI/GPPD/power_plants')
.filter('country_lg == "Belgium"');
// Create an image from features; pixel values are determined from reduction of
// property values of the features intersecting each pixel.
varimage=fc.reduceToImage({
properties:['gwh_estimt'],
reducer:ee.Reducer.sum()
});
// The goal is to sum the electricity generated in 2015 for the power plants
// intersecting 10 km cells and view the result as a map layer.
// ee.FeatureCollection.reduceToImage does not allow the image projection to be
// set because it is waiting on downstream functions that include "crs",
// "scale", and "crsTransform" parameters to define it (e.g., Export.image.*).
// Here, we'll force the projection with ee.Image.reproject so the result can be
// viewed in the map. Note that using small scales with reproject while viewing
// large regions breaks the features that make Earth Engine fast and may result
// in poor performance and/or errors.
image=image.reproject('EPSG:3035',null,10000);
// Display the image on the map.
Map.setCenter(4.3376,50.947,8);
Map.setLocked(true);
Map.addLayer(
image.updateMask(image.gt(0)),
{min:0,max:2000,palette:['yellow','orange','red']},
'Total estimated annual electricity generation, 2015');
Map.addLayer(fc,null,'Belgian power plants');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# FeatureCollection of power plants in Belgium.
fc = ee.FeatureCollection('WRI/GPPD/power_plants').filter(
  'country_lg == "Belgium"'
)
# Create an image from features pixel values are determined from reduction of
# property values of the features intersecting each pixel.
image = fc.reduceToImage(properties=['gwh_estimt'], reducer=ee.Reducer.sum())
# The goal is to sum the electricity generated in 2015 for the power plants
# intersecting 10 km cells and view the result as a map layer.
# ee.FeatureCollection.reduceToImage does not allow the image projection to be
# set because it is waiting on downstream functions that include "crs",
# "scale", and "crsTransform" parameters to define it (e.g., Export.image.*).
# Here, we'll force the projection with ee.Image.reproject so the result can be
# viewed in the map. Note that using small scales with reproject while viewing
# large regions breaks the features that make Earth Engine fast and may result
# in poor performance and/or errors.
image = image.reproject('EPSG:3035', None, 10000)
# Display the image on the map.
m = geemap.Map()
m.set_center(4.3376, 50.947, 8)
m.add_layer(
  image.updateMask(image.gt(0)),
  {'min': 0, 'max': 2000, 'palette': ['yellow', 'orange', 'red']},
  'Total estimated annual electricity generation, 2015',
)
m.add_layer(fc, None, 'Belgian power plants')
m
```

Was this helpful?
