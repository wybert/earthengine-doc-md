 
#  Inverted Joins 
Stay organized with collections  Save and categorize content based on your preferences. 
Suppose that the purpose of the join is to retain all images in the `primary` collection that are not in the `secondary` collection. You can perform this type of inverted join using `ee.Join.inverted()`.
### Code Editor (JavaScript)
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
// Define the join.
varinvertedJoin=ee.Join.inverted();
// Apply the join.
varinvertedJoined=invertedJoin.apply(primary,secondary,filter);
// Print the result.
print('Inverted join:',invertedJoined);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
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
# Define the join.
inverted_join = ee.Join.inverted()
# Apply the join.
inverted_joined = inverted_join.apply(primary, secondary, filter)
# Print the result.
display('Inverted join:', inverted_joined)
```

The output should look something like:
```
Image LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140403 (17 bands)
Image LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140419 (17 bands)

```

The inverted join contains the images from April 3 and April 19, indicating the images that are present in the `primary` collection but not in the `secondary` collection.
