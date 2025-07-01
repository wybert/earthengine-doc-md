 
#  Quantifying Forest Change
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Quantifying Forest Change in a Region of Interest](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#quantifying-forest-change-in-a-region-of-interest)
  * [Calculating Pixel Areas](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#calculating-pixel-areas)


Let's start with the calculation needed to create a band that shows pixels where the Hansen et al. data show both loss and gain.
The Hansen et al. dataset has a band whose pixels are 1 where loss occurred and 0 otherwise (`loss`) and a band that is 1 where gain has occurred and a 0 otherwise (`gain`). To create a band where pixels in both the `loss` and the `gain` bands have a 1, you can use the `and()` logical method on images. The `and()` method is called like `image1.and(image2)` and returns an image in which pixels are 1 where both image1 and image2 are 1, and 0 elsewhere:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#code-editor-javascript-sample) More
```
// Load the data and select the bands of interest.
vargfc2014=ee.Image('UMD/hansen/global_forest_change_2015');
varlossImage=gfc2014.select(['loss']);
vargainImage=gfc2014.select(['gain']);
// Use the and() method to create the lossAndGain image.
vargainAndLoss=gainImage.and(lossImage);
// Show the loss and gain image.
Map.addLayer(gainAndLoss.updateMask(gainAndLoss),
{palette:'FF00FF'},'Gain and Loss');
```

The result, zoomed into Arkansas with satellite view, should look something like Figure 1. 
![Loss Arkansas](https://developers.google.com/static/earth-engine/images/Tutorial_hansen_16_loss_arkansas.png) Figure 1. Pixels with forest loss and gain in Arkansas.
Combining this example with the result from the [previous section](https://developers.google.com/earth-engine/tutorials/tutorial_hansen_02#example), it's now possible to recreate the figure from the beginning of the tutorial:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#code-editor-javascript-sample) More
```
// Displaying forest, loss, gain, and pixels where both loss and gain occur.
vargfc2014=ee.Image('UMD/hansen/global_forest_change_2015');
varlossImage=gfc2014.select(['loss']);
vargainImage=gfc2014.select(['gain']);
vartreeCover=gfc2014.select(['treecover2000']);
// Use the and() method to create the lossAndGain image.
vargainAndLoss=gainImage.and(lossImage);
// Add the tree cover layer in green.
Map.addLayer(treeCover.updateMask(treeCover),
{palette:['000000','00FF00'],max:100},'Forest Cover');
// Add the loss layer in red.
Map.addLayer(lossImage.updateMask(lossImage),
{palette:['FF0000']},'Loss');
// Add the gain layer in blue.
Map.addLayer(gainImage.updateMask(gainImage),
{palette:['0000FF']},'Gain');
// Show the loss and gain image.
Map.addLayer(gainAndLoss.updateMask(gainAndLoss),
{palette:'FF00FF'},'Gain and Loss');
```

## Quantifying Forest Change in a Region of Interest
Now that you're more familiar with the bands in the Hansen et al. dataset, we can use concepts learned so far to compute statistics about forest gain and loss in a region of interest. For this we'll need to use vector data (points, lines, and polygons). A vector dataset is represented as a `FeatureCollection` in Earth Engine. (Learn more about [feature collections](https://developers.google.com/earth-engine/guides/feature_collections) and how to [import vector data](https://developers.google.com/earth-engine/guides/table_upload).)
In this section, we'll compare the total amount of forest loss that happened within the Congo Republic in the year 2012 to the amount of forest loss that happened within the country's protected areas at the same time.
[As you learned in the Earth Engine API tutorial](https://developers.google.com/earth-engine/tutorials/tutorial_api_03#image-statistics), the key method for calculating statistics in an image region is `reduceRegion()`. ([Learn more about reducing image regions](https://developers.google.com/earth-engine/guides/reducers_reduce_region).) For example, suppose we want to calculate the number of pixels estimated to represent forest loss during the study period. For that purpose, consider the following code:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#code-editor-javascript-sample) More
```
// Load country features from Large Scale International Boundary (LSIB) dataset.
varcountries=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Subset the Congo Republic feature from countries.
varcongo=countries.filter(ee.Filter.eq('country_na','Rep of the Congo'));
// Get the forest loss image.
vargfc2014=ee.Image('UMD/hansen/global_forest_change_2015');
varlossImage=gfc2014.select(['loss']);
// Sum the values of forest loss pixels in the Congo Republic.
varstats=lossImage.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:congo,
scale:30
});
print(stats);
```

This example uses the `ee.Reducer.sum()` reducer to sum the values of the pixels in `lossImage` within the `congo` feature. Because `lossImage` consists of pixels that have a value of 1 or 0 (for loss or not loss, respectively), the sum of these values is equivalent to the number of pixels of loss in the region.
Unfortunately, running the script as it is results in an error like:
Dictionary (Error) Image.reduceRegion: Too many pixels in the region. Found 383702302, but only 10000000 allowed. 
The default maximum number of pixels in [`reduceRegion()`](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion) is 10 million. This error message indicates that the Congo Republic covers about 383 million Landsat pixels. Luckily, [`reduceRegion()`](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion) takes many parameters, one of which (`maxPixels`) lets you control how many pixels are used in the computation. Specifying this parameter allows the computation to succeed:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#code-editor-javascript-sample) More
```
// Load country features from Large Scale International Boundary (LSIB) dataset.
varcountries=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Subset the Congo Republic feature from countries.
varcongo=countries.filter(ee.Filter.eq('country_na','Rep of the Congo'));
// Get the forest loss image.
vargfc2014=ee.Image('UMD/hansen/global_forest_change_2015');
varlossImage=gfc2014.select(['loss']);
// Sum the values of forest loss pixels in the Congo Republic.
varstats=lossImage.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:congo,
scale:30,
maxPixels:1e9
});
print(stats);
```

By expanding the object printed to the console, observe that the result is 4897933 pixels of forest lost. You can clean up the printout in the console a bit by labeling the output and getting the result of interest from the dictionary returned by `reduceRegion()`:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#code-editor-javascript-sample) More
```
print('pixels representing loss: ',stats.get('loss'));
```

## Calculating Pixel Areas
You're almost ready to answer the question of how much area was lost in the Congo Republic, and how much of that was in protected areas. The remaining part is to convert pixels into actual area. This conversion is important because we don't necessarily know the size of the pixels input to `reduceRegion()`. To help compute areas, Earth Engine has the `ee.Image.pixelArea()` method which generates an image in which the value of each pixel is the pixel's area in square meters. Multiplying the loss image with this area image and then summing over the result gives us a measure of area:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#code-editor-javascript-sample) More
```
// Load country features from Large Scale International Boundary (LSIB) dataset.
varcountries=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Subset the Congo Republic feature from countries.
varcongo=countries.filter(ee.Filter.eq('country_na','Rep of the Congo'));
// Get the forest loss image.
vargfc2014=ee.Image('UMD/hansen/global_forest_change_2015');
varlossImage=gfc2014.select(['loss']);
varareaImage=lossImage.multiply(ee.Image.pixelArea());
// Sum the values of forest loss pixels in the Congo Republic.
varstats=areaImage.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:congo,
scale:30,
maxPixels:1e9
});
print('pixels representing loss: ',stats.get('loss'),'square meters');
```

Now the result is 4,372,575,052 square meters lost over the study period.
You are now ready to answer the question at the start of this section - how much forest area was lost in the Congo Republic in 2012, and how much of that was in protected areas?
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#code-editor-javascript-sample) More
```
// Load country features from Large Scale International Boundary (LSIB) dataset.
varcountries=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Subset the Congo Republic feature from countries.
varcongo=ee.Feature(
countries
.filter(ee.Filter.eq('country_na','Rep of the Congo'))
.first()
);
// Subset protected areas to the bounds of the congo feature
// and other criteria. Clip to the intersection with congo.
varprotectedAreas=ee.FeatureCollection('WCMC/WDPA/current/polygons')
.filter(ee.Filter.and(
ee.Filter.bounds(congo.geometry()),
ee.Filter.neq('IUCN_CAT','VI'),
ee.Filter.neq('STATUS','proposed'),
ee.Filter.lt('STATUS_YR',2010)
))
.map(function(feat){
returncongo.intersection(feat);
});
// Get the loss image.
vargfc2014=ee.Image('UMD/hansen/global_forest_change_2015');
varlossIn2012=gfc2014.select(['lossyear']).eq(12);
varareaImage=lossIn2012.multiply(ee.Image.pixelArea());
// Calculate the area of loss pixels in the Congo Republic.
varstats=areaImage.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:congo.geometry(),
scale:30,
maxPixels:1e9
});
print(
'Area lost in the Congo Republic:',
stats.get('lossyear'),
'square meters'
);
// Calculate the area of loss pixels in the protected areas.
varstats=areaImage.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:protectedAreas.geometry(),
scale:30,
maxPixels:1e9
});
print(
'Area lost in protected areas:',
stats.get('lossyear'),
'square meters'
);
```

The output indicates that of the 348,036,295 square meters of forest lost in the Congo Republic in 2012, 11,880,976 of those were in protected areas, as represented in the [World Database on Protected Areas table](https://developers.google.com/earth-engine/datasets/catalog/WCMC_WDPA_current_polygons).
The only changes between this script and the one just prior are the addition of the protected area information and changing the script from looking at overall loss to looking at loss in 2012. This required two changes. First, there's a new `lossIn2012` image which has a 1 where loss was recorded in 2012, 0 otherwise. Second, because the name of the band is different (`lossyear` instead of `loss`) the property name had to change in the print statement.
In the [next section](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03a), we will explore some advanced methods for computing and charting forest loss for every year, instead of just one year as we did in this section.
