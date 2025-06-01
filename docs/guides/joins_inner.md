 
#  Inner Joins 
Stay organized with collections  Save and categorize content based on your preferences. 
To enumerate all matches between the elements of two collections, use an `ee.Join.inner()`. The output of an inner join is a `FeatureCollection` (even if joining one `ImageCollection` to another `ImageCollection`). Each feature in the output represents a match, where the matching elements are stored in two properties of the feature. For example, `feature.get('primary')` is the element in the primary collection that matches the element from the secondary collection stored in `feature.get('secondary')`. (Different names for these properties can be specified as arguments to `inner()`, but `‘primary’` and `‘secondary’` are the defaults). One-to-many relationships are represented by multiple features in the output. If an element in either collection doesn’t have a match, it is not present in the output.
Join examples using `ImageCollection` inputs apply without modification to `FeatureCollection` inputs. It is also possible to join a `FeatureCollection` to an `ImageCollection` and vice versa. Consider the following toy example of inner join:
### Code Editor (JavaScript)
```
// Create the primary collection.
varprimaryFeatures=ee.FeatureCollection([
ee.Feature(null,{foo:0,label:'a'}),
ee.Feature(null,{foo:1,label:'b'}),
ee.Feature(null,{foo:1,label:'c'}),
ee.Feature(null,{foo:2,label:'d'}),
]);
// Create the secondary collection.
varsecondaryFeatures=ee.FeatureCollection([
ee.Feature(null,{bar:1,label:'e'}),
ee.Feature(null,{bar:1,label:'f'}),
ee.Feature(null,{bar:2,label:'g'}),
ee.Feature(null,{bar:3,label:'h'}),
]);
// Use an equals filter to specify how the collections match.
vartoyFilter=ee.Filter.equals({
leftField:'foo',
rightField:'bar'
});
// Define the join.
varinnerJoin=ee.Join.inner('primary','secondary');
// Apply the join.
vartoyJoin=innerJoin.apply(primaryFeatures,secondaryFeatures,toyFilter);
// Print the result.
print('Inner join toy example:',toyJoin);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Create the primary collection.
primary_features = ee.FeatureCollection([
  ee.Feature(None, {'foo': 0, 'label': 'a'}),
  ee.Feature(None, {'foo': 1, 'label': 'b'}),
  ee.Feature(None, {'foo': 1, 'label': 'c'}),
  ee.Feature(None, {'foo': 2, 'label': 'd'}),
])
# Create the secondary collection.
secondary_features = ee.FeatureCollection([
  ee.Feature(None, {'bar': 1, 'label': 'e'}),
  ee.Feature(None, {'bar': 1, 'label': 'f'}),
  ee.Feature(None, {'bar': 2, 'label': 'g'}),
  ee.Feature(None, {'bar': 3, 'label': 'h'}),
])
# Use an equals filter to specify how the collections match.
toy_filter = ee.Filter.equals(leftField='foo', rightField='bar')
# Define the join.
inner_join = ee.Join.inner('primary', 'secondary')
# Apply the join.
toy_join = inner_join.apply(primary_features, secondary_features, toy_filter)
# Print the result.
display('Inner join toy example:', toy_join)
```

In the previous example, notice that the relationship between the tables is defined in the filter, which indicates that fields `‘foo’` and `‘bar’` are the join fields. An inner join is then specified and applied to the collections. Inspect the output and observe that each possible match is represented as one `Feature`.
For a motivated example, consider joining MODIS `ImageCollection` objects. MODIS quality data are sometimes stored in a separate collection from the image data, so an inner join is convenient for joining the two collections in order to apply the quality data. In this case, the image acquisition times are identical, so an equals filter handles the job of specifying this relationship between the two collections:
### Code Editor (JavaScript)
```
// Make a date filter to get images in this date range.
vardateFilter=ee.Filter.date('2014-01-01','2014-02-01');
// Load a MODIS collection with EVI data.
varmcd43a4=ee.ImageCollection('MODIS/MCD43A4_006_EVI')
.filter(dateFilter);
// Load a MODIS collection with quality data.
varmcd43a2=ee.ImageCollection('MODIS/006/MCD43A2')
.filter(dateFilter);
// Define an inner join.
varinnerJoin=ee.Join.inner();
// Specify an equals filter for image timestamps.
varfilterTimeEq=ee.Filter.equals({
leftField:'system:time_start',
rightField:'system:time_start'
});
// Apply the join.
varinnerJoinedMODIS=innerJoin.apply(mcd43a4,mcd43a2,filterTimeEq);
// Display the join result: a FeatureCollection.
print('Inner join output:',innerJoinedMODIS);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Make a date filter to get images in this date range.
date_filter = ee.Filter.date('2014-01-01', '2014-02-01')
# Load a MODIS collection with EVI data.
mcd43a4 = ee.ImageCollection('MODIS/MCD43A4_006_EVI').filter(date_filter)
# Load a MODIS collection with quality data.
mcd43a2 = ee.ImageCollection('MODIS/006/MCD43A2').filter(date_filter)
# Define an inner join.
inner_join = ee.Join.inner()
# Specify an equals filter for image timestamps.
filter_time_eq = ee.Filter.equals(
  leftField='system:time_start', rightField='system:time_start'
)
# Apply the join.
inner_joined_modis = inner_join.apply(mcd43a4, mcd43a2, filter_time_eq)
# Display the join result: a FeatureCollection.
display('Inner join output:', inner_joined_modis)
```

To make use of the joined images in the output `FeatureCollection`, `map()` a combining function over the output. For example, the matching images can be stacked together such that the quality bands are added to the image data:
### Code Editor (JavaScript)
```
// Map a function to merge the results in the output FeatureCollection.
varjoinedMODIS=innerJoinedMODIS.map(function(feature){
returnee.Image.cat(feature.get('primary'),feature.get('secondary'));
});
// Print the result of merging.
print('Inner join, merged bands:',joinedMODIS);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Map a function to merge the results in the output FeatureCollection.
joined_modis = inner_joined_modis.map(
  lambda feature: ee.Image.cat(
    feature.get('primary'), feature.get('secondary')
  )
)
# Print the result of merging.
display("Inner join, merged 'bands':", joined_modis)
```

Although this function is mapped over a `FeatureCollection`, the result is an `ImageCollection`. Each image in the resultant `ImageCollection` has all the bands of the images in the primary collection (in this example just `‘EVI’`) and all the bands of the matching image in the secondary collection (the quality bands).
