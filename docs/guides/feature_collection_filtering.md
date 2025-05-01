 
#  Filtering a FeatureCollection 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Filtering a `FeatureCollection` is analogous to filtering an `ImageCollection`. (See the [Filtering an ImageCollection section](https://developers.google.com/earth-engine/guides/ic_filtering)). There are the `featureCollection.filterDate()`, and `featureCollection.filterBounds()` convenience methods and the `featureCollection.filter()` method for use with any applicable `ee.Filter`. For example:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/feature_collection_filtering#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/feature_collection_filtering#colab-python-sample) More
```
// Load watersheds from a data table.
varsheds=ee.FeatureCollection('USGS/WBD/2017/HUC06')
// Convert 'areasqkm' property from string to number.
.map(function(feature){
varnum=ee.Number.parse(feature.get('areasqkm'));
returnfeature.set('areasqkm',num);
});
// Define a region roughly covering the continental US.
varcontinentalUS=ee.Geometry.Rectangle(-127.18,19.39,-62.75,51.29);
// Filter the table geographically: only watersheds in the continental US.
varfiltered=sheds.filterBounds(continentalUS);
// Check the number of watersheds after filtering for location.
print('Count after filter:',filtered.size());
// Filter to get only larger continental US watersheds.
varlargeSheds=filtered.filter(ee.Filter.gt('areasqkm',25000));
// Check the number of watersheds after filtering for size and location.
print('Count after filtering by size:',largeSheds.size());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load watersheds from a data table.
sheds = (
  ee.FeatureCollection('USGS/WBD/2017/HUC06')
  # Convert 'areasqkm' property from string to number.
  .map(
    lambda feature: feature.set(
      'areasqkm', ee.Number.parse(feature.get('areasqkm'))
    )
  )
)
# Define a region roughly covering the continental US.
continental_us = ee.Geometry.Rectangle(-127.18, 19.39, -62.75, 51.29)
# Filter the table geographically: only watersheds in the continental US.
filtered = sheds.filterBounds(continental_us)
# Check the number of watersheds after filtering for location.
display('Count after filter:', filtered.size())
# Filter to get only larger continental US watersheds.
large_sheds = filtered.filter(ee.Filter.gt('areasqkm', 25000))
# Check the number of watersheds after filtering for size and location.
display('Count after filtering by size:', large_sheds.size())
```

