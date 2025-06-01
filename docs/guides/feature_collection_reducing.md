 
#  Reducing a FeatureCollection 
Stay organized with collections  Save and categorize content based on your preferences. 
To aggregate data in the properties of a `FeatureCollection`, use `featureCollection.reduceColumns()`. For example, to check the area properties in the watersheds `FeatureCollection`, this code computes the Root Mean Square Error (RMSE) relative to the Earth Engine computed area:
### Code Editor (JavaScript)
```
// Load watersheds from a data table and filter to the continental US.
varsheds=ee.FeatureCollection('USGS/WBD/2017/HUC06')
.filterBounds(ee.Geometry.Rectangle(-127.18,19.39,-62.75,51.29));
// This function computes the squared difference between an area property
// and area computed directly from the feature's geometry.
varareaDiff=function(feature){
// Compute area in sq. km directly from the geometry.
vararea=feature.geometry().area().divide(1000*1000);
// Compute the difference between computed area and the area property.
vardiff=area.subtract(ee.Number.parse(feature.get('areasqkm')));
// Return the feature with the squared difference set to the 'diff' property.
returnfeature.set('diff',diff.pow(2));
};
// Calculate RMSE for population of difference pairs.
varrmse=ee.Number(
// Map the difference function over the collection.
sheds.map(areaDiff)
// Reduce to get the mean squared difference.
.reduceColumns(ee.Reducer.mean(),['diff'])
.get('mean')
)
// Compute the square root of the mean square to get RMSE.
.sqrt();
// Print the result.
print('RMSE=',rmse);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load watersheds from a data table and filter to the continental US.
sheds = ee.FeatureCollection('USGS/WBD/2017/HUC06').filterBounds(
  ee.Geometry.Rectangle(-127.18, 19.39, -62.75, 51.29)
)
# This function computes the squared difference between an area property
# and area computed directly from the feature's geometry.
defarea_diff(feature):
 # Compute area in sq. km directly from the geometry.
 area = feature.geometry().area().divide(1000 * 1000)
 # Compute the difference between computed area and the area property.
 diff = area.subtract(ee.Number.parse(feature.get('areasqkm')))
 # Return the feature with the squared difference set to the 'diff' property.
 return feature.set('diff', diff.pow(2))
# Calculate RMSE for population of difference pairs.
rmse = (
  ee.Number(
    # Map the difference function over the collection.
    sheds.map(area_diff)
    # Reduce to get the mean squared difference.
    .reduceColumns(ee.Reducer.mean(), ['diff']).get('mean')
  )
  # Compute the square root of the mean square to get RMSE.
  .sqrt()
)
# Print the result.
display('RMSE=', rmse)
```

In this example, note that the return value of `reduceColumns()` is a dictionary with key `‘mean’`. To get the mean, cast the result of `dictionary.get()` to a number with `ee.Number()` before trying to call `sqrt()` on it. For more information about ancillary data structures in Earth Engine, see [this tutorial](https://developers.google.com/earth-engine/tutorials/tutorial_js_01).
To overlay features on imagery, use `featureCollection.reduceRegions()`. For example, to compute the volume of precipitation in continental US watersheds, use `reduceRegions()` followed by a `map()`:
### Code Editor (JavaScript)
```
// Load an image of daily precipitation in mm/day.
varprecip=ee.Image(ee.ImageCollection('NASA/ORNL/DAYMET_V3').first());
// Load watersheds from a data table and filter to the continental US.
varsheds=ee.FeatureCollection('USGS/WBD/2017/HUC06')
.filterBounds(ee.Geometry.Rectangle(-127.18,19.39,-62.75,51.29));
// Add the mean of each image as new properties of each feature.
varwithPrecip=precip.reduceRegions(sheds,ee.Reducer.mean())
.filter(ee.Filter.notNull(['prcp']));
// This function computes total rainfall in cubic meters.
varprcpVolume=function(feature){
// Precipitation in mm/day -> meters -> sq. meters.
varvolume=ee.Number(feature.get('prcp'))
.divide(1000).multiply(feature.geometry().area());
returnfeature.set('volume',volume);
};
varhighVolume=withPrecip
// Map the function over the collection.
.map(prcpVolume)
// Sort descending.
.sort('volume',false)
// Get only the 5 highest volume watersheds.
.limit(5)
// Extract the names to a list.
.reduceColumns(ee.Reducer.toList(),['name']).get('list');
// Print the resulting FeatureCollection.
print(highVolume);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load an image of daily precipitation in mm/day.
precip = ee.Image(ee.ImageCollection('NASA/ORNL/DAYMET_V3').first())
# Load watersheds from a data table and filter to the continental US.
sheds = ee.FeatureCollection('USGS/WBD/2017/HUC06').filterBounds(
  ee.Geometry.Rectangle(-127.18, 19.39, -62.75, 51.29)
)
# Add the mean of each image as new properties of each feature.
with_precip = precip.reduceRegions(sheds, ee.Reducer.mean()).filter(
  ee.Filter.notNull(['prcp'])
)

# This function computes total rainfall in cubic meters.
defprcp_volume(feature):
 # Precipitation in mm/day -> meters -> sq. meters.
 volume = (
   ee.Number(feature.get('prcp'))
   .divide(1000)
   .multiply(feature.geometry().area())
 )
 return feature.set('volume', volume)
high_volume = (
  # Map the function over the collection.
  with_precip.map(prcp_volume)
  # Sort descending and get only the 5 highest volume watersheds.
  .sort('volume', False).limit(5)
  # Extract the names to a list.
  .reduceColumns(ee.Reducer.toList(), ['name']).get('list')
)
# Print the resulting FeatureCollection.
display(high_volume)
```

For more information about reducing feature collections, see [Statistics of FeatureCollection Columns](https://developers.google.com/earth-engine/guides/reducers_reduce_columns) and [Vector to Raster Conversion](https://developers.google.com/earth-engine/guides/reducers_reduce_to_image).
