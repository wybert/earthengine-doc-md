 
#  Simple Joins
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A simple join returns elements from the `primary` collection that match any element in the `secondary` collection according to the match condition in the filter. To perform a simple join, use an `ee.Join.simple()`. This might be useful for finding the common elements among different collections or filtering one collection by another. For example, consider two image collections which (might) have some matching elements, where “matching” is defined by the condition specified in a filter. For example, let matching mean the image IDs are equal. Since the matching images in both collections are the same, use a simple join to discover this set of matching images:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/joins_simple#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/joins_simple#colab-python-sample) More
```
// Load a Landsat 8 image collection at a point of interest.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterBounds(ee.Geometry.Point(-122.09,37.42));

// Define start and end dates with which to filter the collections.
varapril='2014-04-01';
varmay='2014-05-01';
varjune='2014-06-01';
varjuly='2014-07-01';

// The primary collection is Landsat images from April to June.
varprimary=collection.filterDate(april,june);

// The secondary collection is Landsat images from May to July.
varsecondary=collection.filterDate(may,july);

// Use an equals filter to define how the collections match.
varfilter=ee.Filter.equals({
leftField:'system:index',
rightField:'system:index'
});

// Create the join.
varsimpleJoin=ee.Join.simple();

// Apply the join.
varsimpleJoined=simpleJoin.apply(primary,secondary,filter);

// Display the result.
print('Simple join: ',simpleJoined);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 image collection at a point of interest.
collection = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA').filterBounds(
    ee.Geometry.Point(-122.09, 37.42)
)

# Define start and end dates with which to filter the collections.
april = '2014-04-01'
may = '2014-05-01'
june = '2014-06-01'
july = '2014-07-01'

# The primary collection is Landsat images from April to June.
primary = collection.filterDate(april, june)

# The secondary collection is Landsat images from May to July.
secondary = collection.filterDate(may, july)

# Use an equals filter to define how the collections match.
filter = ee.Filter.equals(leftField='system:index', rightField='system:index')

# Create the join.
simple_join = ee.Join.simple()

# Apply the join.
simple_joined = simple_join.apply(primary, secondary, filter)

# Display the result.
display('Simple join:', simple_joined)
```

In the previous example, observe that the collections to join temporally overlap by about a month. Note that when this join is applied, the output will be an `ImageCollection` with only the matching images in the `primary` collection. The output should look something like:
```
Image LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140505 (17 bands)
Image LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140521 (17 bands)

```

This output shows that two images match (as specified in the filter) between the `primary` and `secondary` collections, images at May 5 and May 21.
