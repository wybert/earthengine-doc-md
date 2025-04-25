 
#  Statistics of Image Regions 
Stay organized with collections  Save and categorize content based on your preferences. 
To get image statistics in multiple regions stored in a `FeatureCollection`, you can use `image.reduceRegions()` to reduce multiple regions at once. The input to `reduceRegions()` is an `Image` and a `FeatureCollection`. The output is another `FeatureCollection` with the `reduceRegions()` output set as properties on each `Feature`. In this example, means of the Landsat 7 annual composite bands in each feature geometry will be added as properties to the input features:
### Code Editor (JavaScript)
```
// Load input imagery: Landsat 7 5-year composite.
varimage=ee.Image('LANDSAT/LE7_TOA_5YEAR/2008_2012');
// Load a FeatureCollection of counties in Maine.
varmaineCounties=ee.FeatureCollection('TIGER/2016/Counties')
.filter(ee.Filter.eq('STATEFP','23'));
// Add reducer output to the Features in the collection.
varmaineMeansFeatures=image.reduceRegions({
collection:maineCounties,
reducer:ee.Reducer.mean(),
scale:30,
});
// Print the first feature, to illustrate the result.
print(ee.Feature(maineMeansFeatures.first()).select(image.bandNames()));
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load input imagery: Landsat 7 5-year composite.
image = ee.Image('LANDSAT/LE7_TOA_5YEAR/2008_2012')
# Load a FeatureCollection of counties in Maine.
maine_counties = ee.FeatureCollection('TIGER/2016/Counties').filter(
  ee.Filter.eq('STATEFP', '23')
)
# Add reducer output to the Features in the collection.
maine_means_features = image.reduceRegions(
  collection=maine_counties, reducer=ee.Reducer.mean(), scale=30
)
# Print the first feature, to illustrate the result.
display(ee.Feature(maine_means_features.first()).select(image.bandNames()))
```

Observe that new properties, keyed by band name, have been added to the `FeatureCollection` to store the mean of the composite in each `Feature` geometry. As a result, the output of the print statement should look something like:
```
Feature (Polygon, 7 properties)
 type: Feature
 geometry: Polygon, 7864 vertices
 properties: Object (7 properties)
  B1: 24.034822192925134
  B2: 19.40202233717122
  B3: 13.568454303016292
  B4: 63.00423784301736
  B5: 29.142707062821305
  B6_VCID_2: 186.18172376827042
  B7: 12.064469664746415
  
```

