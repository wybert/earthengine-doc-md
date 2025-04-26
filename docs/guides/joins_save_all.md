 
#  Save-All Joins 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Saving joins are one way of representing one-to-many relationships in Earth Engine. Unlike an [inner join](https://developers.google.com/earth-engine/guides/joins_inner), a saving join stores matches from the `secondary` collection as a named property of the features in the `primary` collection. To save all such matches, use an `ee.Join.saveAll()`. If there is a one-to-many relationship, a `saveAll()` join stores all matching features as an `ee.List`. Unmatched elements in the `primary` collection are dropped. For example, suppose there is a need to get all MODIS imagery acquired within two days of each Landsat image in a collection. This example uses a `saveAll()` join for that purpose:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/joins_save_all#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/joins_save_all#colab-python-sample) More
```
// Load a primary collection: Landsat imagery.
varprimary=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterDate('2014-04-01','2014-06-01')
.filterBounds(ee.Geometry.Point(-122.092,37.42));
// Load a secondary collection: MODIS imagery.
varmodSecondary=ee.ImageCollection('MODIS/006/MOD09GA')
.filterDate('2014-03-01','2014-07-01');
// Define an allowable time difference: two days in milliseconds.
vartwoDaysMillis=2*24*60*60*1000;
// Create a time filter to define a match as overlapping timestamps.
vartimeFilter=ee.Filter.or(
ee.Filter.maxDifference({
difference:twoDaysMillis,
leftField:'system:time_start',
rightField:'system:time_end'
}),
ee.Filter.maxDifference({
difference:twoDaysMillis,
leftField:'system:time_end',
rightField:'system:time_start'
})
);
// Define the join.
varsaveAllJoin=ee.Join.saveAll({
matchesKey:'terra',
ordering:'system:time_start',
ascending:true
});
// Apply the join.
varlandsatModis=saveAllJoin.apply(primary,modSecondary,timeFilter);
// Display the result.
print('Join.saveAll:',landsatModis);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a primary collection: Landsat imagery.
primary = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filterDate('2014-04-01', '2014-06-01')
  .filterBounds(ee.Geometry.Point(-122.092, 37.42))
)
# Load a secondary collection: MODIS imagery.
mod_secondary = ee.ImageCollection('MODIS/006/MOD09GA').filterDate(
  '2014-03-01', '2014-07-01'
)
# Define an allowable time difference: two days in milliseconds.
two_days_millis = 2 * 24 * 60 * 60 * 1000
# Create a time filter to define a match as overlapping timestamps.
time_filter = ee.Filter.Or(
  ee.Filter.maxDifference(
    difference=two_days_millis,
    leftField='system:time_start',
    rightField='system:time_end',
  ),
  ee.Filter.maxDifference(
    difference=two_days_millis,
    leftField='system:time_end',
    rightField='system:time_start',
  ),
)
# Define the join.
save_all_join = ee.Join.saveAll(
  matchesKey='terra', ordering='system:time_start', ascending=True
)
# Apply the join.
landsat_modis = save_all_join.apply(primary, mod_secondary, time_filter)
# Display the result.
display('Join.saveAll:', landsat_modis)
```

In this example, note that the `secondary` MODIS collection is pre-filtered to be chronologically similar to the `primary` Landsat collection for efficiency. To compare the Landsat acquisition time to the MODIS composite time, which has a daily range, the filter compares the endpoints of the image timestamps. The join is defined with the name of the property used to store the list of matches for each Landsat image (`‘terra’`) and optional parameter to sort the list of matches by the `system:time_start` property
Inspection of the result indicates that images within the primary collection have the added `terra` property which stores a list of the matching MODIS images.
