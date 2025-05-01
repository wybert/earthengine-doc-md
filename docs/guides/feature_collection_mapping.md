 
#  Mapping over a FeatureCollection 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
To apply the same operation to every `Feature` in a `FeatureCollection`, use `featureCollection.map()`. For example, to add another area attribute to every feature in a watersheds `FeatureCollection`, use:
### Code Editor (JavaScript)
```
// Load watersheds from a data table.
varsheds=ee.FeatureCollection('USGS/WBD/2017/HUC06');
// This function computes the feature's geometry area and adds it as a property.
varaddArea=function(feature){
returnfeature.set({areaHa:feature.geometry().area().divide(100*100)});
};
// Map the area getting function over the FeatureCollection.
varareaAdded=sheds.map(addArea);
// Print the first feature from the collection with the added property.
print('First feature:',areaAdded.first());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load watersheds from a data table.
sheds = ee.FeatureCollection('USGS/WBD/2017/HUC06')
# Map an area calculation function over the FeatureCollection.
area_added = sheds.map(
  lambda feature: feature.set(
    {'areaHa': feature.geometry().area().divide(100 * 100)}
  )
)
# Print the first feature from the collection with the added property.
display('First feature:', area_added.first())
```

In the previous example, note that a new property is set based on a computation with the feature's geometry. Properties can also be set using a computation involving existing properties.
An entirely new `FeatureCollection` can be generated with `map()`. The following example converts the watersheds to centroids:
### Code Editor (JavaScript)
```
// This function creates a new feature from the centroid of the geometry.
vargetCentroid=function(feature){
// Keep this list of properties.
varkeepProperties=['name','huc6','tnmid','areasqkm'];
// Get the centroid of the feature's geometry.
varcentroid=feature.geometry().centroid();
// Return a new Feature, copying properties from the old Feature.
returnee.Feature(centroid).copyProperties(feature,keepProperties);
};
// Map the centroid getting function over the features.
varcentroids=sheds.map(getCentroid);
// Display the results.
Map.addLayer(centroids,{color:'FF0000'},'centroids');
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# This function creates a new feature from the centroid of the geometry.
defget_centroid(feature):
 # Keep this list of properties.
 keep_properties = ['name', 'huc6', 'tnmid', 'areasqkm']
 # Get the centroid of the feature's geometry.
 centroid = feature.geometry().centroid()
 # Return a new Feature, copying properties from the old Feature.
 return ee.Feature(centroid).copyProperties(feature, keep_properties)
# Map the centroid getting function over the features.
centroids = sheds.map(get_centroid)
# Display the results.
m = geemap.Map()
m.set_center(-96.25, 40, 4)
m.add_layer(centroids, {'color': 'FF0000'}, 'centroids')
m
```

Note that only a subset of properties is propagated to the features in the new collection. 
