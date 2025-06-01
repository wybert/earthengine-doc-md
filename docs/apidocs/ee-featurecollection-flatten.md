 
#  ee.FeatureCollection.flatten 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-flatten#examples)


Flattens collections of collections. 
Usage| Returns  
---|---  
`FeatureCollection.flatten()`| FeatureCollection  
Argument| Type| Details  
---|---|---  
this: `collection`| FeatureCollection| The input collection of collections.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-flatten#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-flatten#colab-python-sample) More
```
// Counties in New Mexico, USA.
varcounties=ee.FeatureCollection('TIGER/2018/Counties')
.filter('STATEFP == "35"');
// Monthly climate and climatic water balance surfaces for January 2020.
varclimate=ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE')
.filterDate('2020-01','2020-02');
// Calculate mean climate variables for each county per climate surface
// time step. The result is a FeatureCollection of FeatureCollections.
varcountiesClimate=climate.map(function(image){
returnimage.reduceRegions({
collection:counties,
reducer:ee.Reducer.mean(),
scale:5000,
crs:'EPSG:4326'
});
});
// Note that a printed FeatureCollection of FeatureCollections is not
// recursively expanded, you cannot view metadata of the features within the
// nested collections until you isolate a single collection or flatten the
// collections.
print('FeatureCollection of FeatureCollections',countiesClimate);
print('Flattened FeatureCollection of FeatureCollections',
countiesClimate.flatten());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Counties in New Mexico, USA.
counties = ee.FeatureCollection('TIGER/2018/Counties').filter('STATEFP == "35"')
# Monthly climate and climatic water balance surfaces for January 2020.
climate = ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE').filterDate(
  '2020-01', '2020-02')
# Calculate mean climate variables for each county per climate surface
# time step. The result is a FeatureCollection of FeatureCollections.
defreduce_mean(image):
 return image.reduceRegions(**{
   'collection': counties,
   'reducer': ee.Reducer.mean(),
   'scale': 5000,
   'crs': 'EPSG:4326'
   })
counties_climate = climate.map(reduce_mean)
# Note that a printed FeatureCollection of FeatureCollections is not
# recursively expanded, you cannot view metadata of the features within the
# nested collections until you isolate a single collection or flatten the
# collections.
print('FeatureCollection of FeatureCollections:', counties_climate.getInfo())
print('Flattened FeatureCollection of FeatureCollections:',
   counties_climate.flatten().getInfo())
```

Was this helpful?
