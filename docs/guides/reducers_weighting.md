 
#  Weighted Reductions 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
By default, reducers applied to imagery weight the inputs according to the mask value. This is relevant in the context of fractional pixels created through operations such as `clip()`. Adjust this behavior by calling `unweighted()` on the reducer. Using an unweighted reducer forces all pixels in the region to have the same weight. The following example illustrates how pixel weighting can affect the reducer output:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_weighting#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/reducers_weighting#colab-python-sample) More
```
// Load a Landsat 8 input image.
varimage=ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318');
// Create an arbitrary region.
vargeometry=ee.Geometry.Rectangle(-122.496,37.532,-121.554,37.538);
// Make an NDWI image. It will have one band named 'nd'.
varndwi=image.normalizedDifference(['B3','B5']);
// Compute the weighted mean of the NDWI image clipped to the region.
varweighted=ndwi.clip(geometry)
.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:geometry,
scale:30})
.get('nd');
// Compute the UN-weighted mean of the NDWI image clipped to the region.
varunweighted=ndwi.clip(geometry)
.reduceRegion({
reducer:ee.Reducer.mean().unweighted(),
geometry:geometry,
scale:30})
.get('nd');
// Observe the difference between weighted and unweighted reductions.
print('weighted:',weighted);
print('unweighted',unweighted);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load a Landsat 8 input image.
image = ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20140318')
# Create an arbitrary region.
geometry = ee.Geometry.Rectangle(-122.496, 37.532, -121.554, 37.538)
# Make an NDWI image. It will have one band named 'nd'.
ndwi = image.normalizedDifference(['B3', 'B5'])
# Compute the weighted mean of the NDWI image clipped to the region.
weighted = (
  ndwi.clip(geometry)
  .reduceRegion(reducer=ee.Reducer.mean(), geometry=geometry, scale=30)
  .get('nd')
)
# Compute the UN-weighted mean of the NDWI image clipped to the region.
unweighted = (
  ndwi.clip(geometry)
  .reduceRegion(
    reducer=ee.Reducer.mean().unweighted(), geometry=geometry, scale=30
  )
  .get('nd')
)
# Observe the difference between weighted and unweighted reductions.
display('weighted:', weighted)
display('unweighted', unweighted)
```

The difference in results is due to pixels at the edge of the region receiving a weight of one as a result of calling `unweighted()` on the reducer.
In order to obtain an explicitly weighted output, it is preferable to set the weights explicitly with `splitWeights()` called on the reducer. A reducer modified by `splitWeights()` takes two inputs, where the second input is the weight. The following example illustrates `splitWeights()` by computing the weighted mean Normalized Difference Vegetation Index (NDVI) in a region, with the weights given by cloud score (the cloudier, the lower the weight):
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/reducers_weighting#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/reducers_weighting#colab-python-sample) More
```
// Load an input Landsat 8 image.
varimage=ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_186059_20130419');
// Compute cloud score and reverse it such that the highest
// weight (100) is for the least cloudy pixels.
varcloudWeight=ee.Image(100).subtract(
ee.Algorithms.Landsat.simpleCloudScore(image).select(['cloud']));
// Compute NDVI and add the cloud weight band.
varndvi=image.normalizedDifference(['B5','B4']).addBands(cloudWeight);
// Define an arbitrary region in a cloudy area.
varregion=ee.Geometry.Rectangle(9.9069,0.5981,10.5,0.9757);
// Use a mean reducer.
varreducer=ee.Reducer.mean();
// Compute the unweighted mean.
varunweighted=ndvi.select(['nd']).reduceRegion(reducer,region,30);
// compute mean weighted by cloudiness.
varweighted=ndvi.reduceRegion(reducer.splitWeights(),region,30);
// Observe the difference as a result of weighting by cloudiness.
print('unweighted:',unweighted);
print('weighted:',weighted);
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Load an input Landsat 8 image.
image = ee.Image('LANDSAT/LC08/C02/T1_TOA/LC08_186059_20130419')
# Compute cloud score and reverse it such that the highest
# weight (100) is for the least cloudy pixels.
cloud_weight = ee.Image(100).subtract(
  ee.Algorithms.Landsat.simpleCloudScore(image).select(['cloud'])
)
# Compute NDVI and add the cloud weight band.
ndvi = image.normalizedDifference(['B5', 'B4']).addBands(cloud_weight)
# Define an arbitrary region in a cloudy area.
region = ee.Geometry.Rectangle(9.9069, 0.5981, 10.5, 0.9757)
# Use a mean reducer.
reducer = ee.Reducer.mean()
# Compute the unweighted mean.
unweighted = ndvi.select(['nd']).reduceRegion(reducer, region, 30)
# compute mean weighted by cloudiness.
weighted = ndvi.reduceRegion(reducer.splitWeights(), region, 30)
# Observe the difference as a result of weighting by cloudiness.
display('unweighted:', unweighted)
display('weighted:', weighted)
```

Observe that `cloudWeight` needs to be added as a band prior to calling `reduceRegion()`. The result indicates that the estimated mean NDVI is higher as a result of decreasing the weight of cloudy pixels.
Was this helpful?
