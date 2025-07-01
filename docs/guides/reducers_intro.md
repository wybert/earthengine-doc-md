 
#  Reducer Overview
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Reducers have inputs and outputs](https://developers.google.com/earth-engine/guides/reducers_intro#reducers-have-inputs-and-outputs)
  * [Reducers use weighted inputs](https://developers.google.com/earth-engine/guides/reducers_intro#reducers-use-weighted-inputs)
  * [Combining reducers](https://developers.google.com/earth-engine/guides/reducers_intro#combining-reducers)


Reducers are the way to aggregate data over time, space, bands, arrays and other data structures in Earth Engine. The `ee.Reducer` class specifies how data is aggregated. The reducers in this class can specify a simple statistic to use for the aggregation (e.g. minimum, maximum, mean, median, standard deviation, etc.), or a more complex summary of the input data (e.g. histogram, linear regression, list). Reductions may occur over time (`imageCollection.reduce()`), space (`image.reduceRegion()`, `image.reduceNeighborhood()`), bands (`image.reduce()`), or the attribute space of a `FeatureCollection` (`featureCollection.reduceColumns()` or `FeatureCollection` methods that start with `aggregate_`). 
## Reducers have inputs and outputs
Reducers take an input dataset and produce a single output. When a single input reducer is applied to a multi-band image, Earth Engine automatically replicates the reducer and applies it separately to each band. As a result, the output image has the same number of bands as the input image; each band in the output is the reduction of pixels from the corresponding band in the input data. Some reducers take tuples of input datasets. These reducers will not be automatically replicated for each band. For example, `ee.Reducer.LinearRegression()` takes multiple predictor datasets (representing independent variables in the regression) in a particular order (see [Regression reducers](https://developers.google.com/earth-engine/guides/reducers_regression)). 
Some reducers produce multiple outputs, for example `ee.Reducer.minMax()`, `ee.Reducer.histogram()` or `ee.Reducer.toList()`. For example: 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_intro#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/reducers_intro#colab-python-sample) More
```
// Load and filter the Sentinel-2 image collection.
varcollection=ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
.filterDate('2016-01-01','2016-12-31')
.filterBounds(ee.Geometry.Point([-81.31,29.90]));
// Reduce the collection.
varextrema=collection.reduce(ee.Reducer.minMax());
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load and filter the Sentinel-2 image collection.
collection = (
  ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
  .filterDate('2016-01-01', '2016-12-31')
  .filterBounds(ee.Geometry.Point([-81.31, 29.90]))
)
# Reduce the collection.
extrema = collection.reduce(ee.Reducer.minMax())
```

This will produce an output with twice the number of bands of the inputs, where band names in the output have '_min' or '_max' appended to the band name. 
The output type should match the computation. For example, a reducer applied to an `ImageCollection` has an `Image` output. Because the output is interpreted as a pixel value, you must use reducers with a numeric output to reduce an `ImageCollection` (reducers like `toList()` or `histogram()` won't work). 
## Reducers use weighted inputs
By default, reductions over pixel values are weighted by their mask, though this behavior can be changed (see the [Weighting section](https://developers.google.com/earth-engine/guides/reducers_weighting)). Pixels with mask equal to 0 will not be used in the reduction. 
## Combining reducers
If your intent is to apply multiple reducers to the same inputs, it's good practice to `combine()` the reducers for efficiency. Specifically, calling `combine()` on a reducer with `sharedInputs` set to `true` will result in only a single pass over the data. For example, to compute the mean and standard deviation of pixels in an image, you could use something like this: 
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_intro#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/reducers_intro#colab-python-sample) More
```
// Load a Landsat 8 image.
varimage=ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318');
// Combine the mean and standard deviation reducers.
varreducers=ee.Reducer.mean().combine({
reducer2:ee.Reducer.stdDev(),
sharedInputs:true
});
// Use the combined reducer to get the mean and SD of the image.
varstats=image.reduceRegion({
reducer:reducers,
bestEffort:true,
});
// Display the dictionary of band means and SDs.
print(stats);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 image.
image = ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318')
# Combine the mean and standard deviation reducers.
reducers = ee.Reducer.mean().combine(
  reducer2=ee.Reducer.stdDev(), sharedInputs=True
)
# Use the combined reducer to get the mean and SD of the image.
stats = image.reduceRegion(reducer=reducers, bestEffort=True)
# Display the dictionary of band means and SDs.
display(stats)
```

In the output, note that the names of the reducers have been appended to the names of the inputs to distinguish the reducer outputs. This behavior also applies to image outputs, which will have the name of the reducer appended to output band names. 
If you are combining reducers using unweighted inputs and reducers using weighted inputs, all weighted inputs must be before all unweighted inputs. 
