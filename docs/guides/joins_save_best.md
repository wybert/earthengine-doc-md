 
#  Save-Best Joins 
Stay organized with collections  Save and categorize content based on your preferences. 
To save only the best match for each element in a collection, use an `ee.Join.saveBest()`. The `saveBest()` join functions in an equivalent way to the `saveAll()` join, except for each element in the `primary` collection, it saves the element from the `secondary` collection with the best match. Unmatched elements in the primary collection are dropped. Suppose the intention is to find a meteorological image closest in time to each Landsat image in the `primary` collection. To perform this join, the `ee.Filter` must be redefined for a single join condition (combined filters will not work with `saveBest()` since it is ambiguous how to combine ranks from multiple sub-Filters):
### Code Editor (JavaScript)
```
// Load a primary collection: Landsat imagery.
varprimary=ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
.filterDate('2014-04-01','2014-06-01')
.filterBounds(ee.Geometry.Point(-122.092,37.42));
// Load a secondary collection: GRIDMET meteorological data
vargridmet=ee.ImageCollection('IDAHO_EPSCOR/GRIDMET');
// Define a max difference filter to compare timestamps.
varmaxDiffFilter=ee.Filter.maxDifference({
difference:2*24*60*60*1000,
leftField:'system:time_start',
rightField:'system:time_start'
});
// Define the join.
varsaveBestJoin=ee.Join.saveBest({
matchKey:'bestImage',
measureKey:'timeDiff'
});
// Apply the join.
varlandsatMet=saveBestJoin.apply(primary,gridmet,maxDiffFilter);
// Print the result.
print(landsatMet);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a primary collection: Landsat imagery.
primary = (
  ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA')
  .filterDate('2014-04-01', '2014-06-01')
  .filterBounds(ee.Geometry.Point(-122.092, 37.42))
)
# Load a secondary collection: GRIDMET meteorological data
gridmet = ee.ImageCollection('IDAHO_EPSCOR/GRIDMET')
# Define a max difference filter to compare timestamps.
max_diff_filter = ee.Filter.maxDifference(
  difference=2 * 24 * 60 * 60 * 1000,
  leftField='system:time_start',
  rightField='system:time_start',
)
# Define the join.
save_best_join = ee.Join.saveBest(matchKey='bestImage', measureKey='timeDiff')
# Apply the join.
landsat_met = save_best_join.apply(primary, gridmet, max_diff_filter)
# Print the result.
display(landsat_met)
```

Note that a `saveBest()` join defines the name of the property with which to store the best match (`‘bestImage’`) and the name of the property with which to store the goodness of the match metric (`‘timeDiff’`). Inspection of the results indicates that a matching DAYMET image has been added to the property `bestImage` for each Landsat scene in the `primary` collection. Each of these DAYMET images has the property `timeDiff` indicating the time difference in milliseconds between the DAYMET image and the Landsat image, which will be minimum among the DAYMET images passing the condition in the filter.
