 
#  Coding Best Practices 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Avoid mixing client functions and objects with server functions and objects](https://developers.google.com/earth-engine/guides/best_practices#avoid_mixing_client_functions_and_objects_with_server_functions_and_objects)
  * [Avoid converting to list unnecessarily](https://developers.google.com/earth-engine/guides/best_practices#avoid_converting_to_list_unnecessarily)
  * [Avoid ee.Algorithms.If()](https://developers.google.com/earth-engine/guides/best_practices#avoid_eealgorithmsif)
  * [Avoid reproject()](https://developers.google.com/earth-engine/guides/best_practices#avoid_reproject)
  * [Filter and select() first](https://developers.google.com/earth-engine/guides/best_practices#filter_and_select_first)
  * [Use updateMask() instead of mask()](https://developers.google.com/earth-engine/guides/best_practices#use_updatemask_instead_of_mask)
  * [Combine reducers](https://developers.google.com/earth-engine/guides/best_practices#combine_reducers)
  * [Use Export](https://developers.google.com/earth-engine/guides/best_practices#use_export)
  * [If you don't need to clip, don't use clip()](https://developers.google.com/earth-engine/guides/best_practices#if_you_dont_need_to_clip_dont_use_clip)
  * [If you need to clip with a complex collection, use clipToCollection()](https://developers.google.com/earth-engine/guides/best_practices#if_you_need_to_clip_with_a_complex_collection_use_cliptocollection)
  * [Don't use a complex collection as the region for a reducer](https://developers.google.com/earth-engine/guides/best_practices#dont_use_a_complex_collection_as_the_region_for_a_reducer)
  * [Use a non-zero errorMargin](https://developers.google.com/earth-engine/guides/best_practices#use_a_non-zero_errormargin)
  * [Don't use a ridiculously small scale with reduceToVectors()](https://developers.google.com/earth-engine/guides/best_practices#dont_use_a_ridiculously_small_scale_with_reducetovectors)
  * [Don't use reduceToVectors() with reduceRegions()](https://developers.google.com/earth-engine/guides/best_practices#dont_use_reducetovectors_with_reduceregions)
  * [Use fastDistanceTransform() for neighborhood operations](https://developers.google.com/earth-engine/guides/best_practices#use_fastdistancetransform_for_neighborhood_operations)
  * [Use the optimizations in reduceNeighborhood()](https://developers.google.com/earth-engine/guides/best_practices#use_the_optimizations_in_reduceneighborhood)
  * [Don't sample more data than you need](https://developers.google.com/earth-engine/guides/best_practices#dont_sample_more_data_than_you_need)
  * [Export intermediate results](https://developers.google.com/earth-engine/guides/best_practices#export_intermediate_results)
  * [Join vs. map-filter](https://developers.google.com/earth-engine/guides/best_practices#join_vs_map-filter)
  * [reduceRegion() vs. reduceRegions() vs. for-loop](https://developers.google.com/earth-engine/guides/best_practices#reduceregion_vs_reduceregions_vs_for-loop)
  * [Use forward differencing for neighbors in time](https://developers.google.com/earth-engine/guides/best_practices#use_forward_differencing_for_neighbors_in_time)


This doc describes coding practices that are intended to maximize the chance of success for complex or expensive Earth Engine computations. The methods described here are applicable to both interactive (e.g. Code Editor) and batch (`Export`) computations, though generally long running computations should be run in the batch system.
## Avoid mixing client functions and objects with server functions and objects
Earth Engine server objects are objects with constructors that start with `ee` (e.g. `ee.Image`, `ee.Reducer`) and any methods on such objects are server functions. Any object not constructed in this manner is a client object. Client objects may come from the Code Editor (e.g. `Map`, `Chart`) or the JavaScript language (e.g. `Date`, `Math`, `[]`, `{}`).
To avoid unintended behavior, do not mix client and server functions in your script as discussed [here](https://developers.google.com/earth-engine/guides/debugging#avoid-mixing) and [here](https://developers.google.com/earth-engine/guides/debugging#browser-lock) and [here](https://developers.google.com/earth-engine/guides/debugging#mapped-functions). See [this page](https://developers.google.com/earth-engine/guides/client_server) and/or [this tutorial](https://developers.google.com/earth-engine/guides/tutorial_js_01) for in-depth explanation of client vs. server in Earth Engine. The following example illustrates the dangers of mixing client and server functionality:
Error — this code doesn't work!
```
vartable=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Won't work.
for(vari=0;i<table.size();i++){
print('No!');
}

```

Can you spot the error? Note that `table.size()` is a server method on a server object and can not be used with client-side functionality such as the `<` conditional.
A situation in which you may want to use for-loops is with UI setup, since Code Editor `ui` objects and methods are client-side. ([Learn more about creating user interfaces in Earth Engine](https://developers.google.com/earth-engine/guides/ui)). For example:
Use client functions for UI setup.
```
varpanel=ui.Panel();
for(vari=1;i<8;i++){
panel.widgets().set(i,ui.Button('button '+i))
}
print(panel);

```

Conversely, `map()` is a server function and client functionality won't work inside the function passed to `map()`. For example:
Error — this code doesn't work!
```
vartable=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Error:
varfoobar=table.map(function(f){
print(f);// Can't use a client function here.
// Can't Export, either.
});

```

To do something to every element in a collection, `map()` a function over the collection and `set()` a property:
Use `map()` and `set()`!
```
vartable=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
print(table.first());
// Do something to every element of a collection.
varwithMoreProperties=table.map(function(f){
// Set a property.
returnf.set('area_sq_meters',f.area())
});
print(withMoreProperties.first());

```

You can also `filter()` the collection based on computed or existing properties and `print()` the result. Note that you can not print a collection with more 5000 elements. If you get the "Collection query aborted after accumulating over 5000 elements" error, `filter()` or `limit()` the collection before printing.
## Avoid converting to list unnecessarily
Collections in Earth Engine are processed using optimizations that are broken by converting the collection to a `List` or `Array` type. Unless you _need_ random access to collection elements (i.e. you _need_ to get the i'th element of a collection), use filters on the collection to access individual collection elements. The following example illustrates the difference between type conversion (not recommended) and filtering (recommended) to access an element in a collection:
Don't convert to list unnecessarily!
```
vartable=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Do NOT do this!!
varlist=table.toList(table.size());
print(list.get(13));// User memory limit exceeded.

```

Note that you can easily trigger errors by converting a collection to a list unnecessesarily. The safer way is to use `filter()`:
Use `filter()`!
```
print(table.filter(ee.Filter.eq('country_na', 'Niger')).first());

```

Note that you should [use filters as early as possible in your analysis](https://developers.google.com/earth-engine/guides/best_practices#filter-and-select-first).
## Avoid `ee.Algorithms.If()`
Do not use `ee.Algorithms.If()` to implement branching logic, especially in a mapped function. As the following example illustrates, `ee.Algorithms.If()` can be memory intensive and is not recommended:
Don't use `If()`!
```
vartable=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Do NOT do this!
varveryBad=table.map(function(f){
returnee.Algorithms.If({
condition:ee.String(f.get('country_na')).compareTo('Chad').gt(0),
trueCase:f,// Do something.
falseCase:null// Do something else.
});
},true);
print(veryBad);// User memory limit exceeded.
// If() may evaluate both the true and false cases.

```

Note that the second argument to `map()` is `true`. This means that the mapped function may return nulls and they will be dropped in the resultant collection. That can be useful (without `If()`), but here the easiest solution is to use a filter:
Use `filter()`!
```
print(table.filter(ee.Filter.eq('country_na','Chad')));

```

As shown in [this tutorial](https://developers.google.com/earth-engine/guides/tutorial_js_03#ifelse-conditions), a functional programming approach using filters is the correct way to apply one logic to some elements of a collection and another logic to the other elements of the collection.
## Avoid `reproject()`
Don't use reproject unless absolutely necessary. One reason you might want to use `reproject()` is to force Code Editor computations to happen at a specific scale so you can examine the results at your desired scale of analysis. In the next example, patches of hot pixels are computed and the count of pixels in each patch is computed. Run the example and click on one of the patches. Note that the count of pixels differs between the reprojected data the data that has not been reprojected.
```
varl8sr=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2');
varsf=ee.Geometry.Point([-122.405,37.786]);
Map.centerObject(sf,13);
// A reason to reproject - counting pixels and exploring interactively.
varimage=l8sr.filterBounds(sf)
.filterDate('2019-06-01','2019-12-31')
.first();
image=image.multiply(0.00341802).add(149);// Apply scale factors.
Map.addLayer(image,{bands:['ST_B10'],min:280,max:317},'image');
varhotspots=image.select('ST_B10').gt(317)
.selfMask()
.rename('hotspots');
varobjectSize=hotspots.connectedPixelCount(256);
Map.addLayer(objectSize,{min:1,max:256},'Size No Reproject',false);
// Beware of reproject! Don't zoom out on reprojected data.
varreprojected=objectSize.reproject(hotspots.projection());
Map.addLayer(reprojected,{min:1,max:256},'Size Reproject',false);

```

The reason for the discrepancy is because the [scale of analysis](https://developers.google.com/earth-engine/guides/scale#scale-of-analysis) is set by the Code Editor zoom level. By calling `reproject()` you set the scale of the computation instead of the Code Editor. Use `reproject()` with extreme caution for reasons described in [this doc](https://developers.google.com/earth-engine/guides/projections#reprojecting).
## Filter and `select()` first
In general, filter input collections by time, location and/or metadata prior to doing anything else with the collection. Apply more selective filters before less selective filters. Spatial and/or temporal filters are often more selective. For example, note that `select()` and `filter()` are applied _before_ `map()`:
```
varimages=ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED');
varsf=ee.Geometry.Point([-122.463,37.768]);
// Expensive function to reduce the neighborhood of an image.
varreduceFunction=function(image){
returnimage.reduceNeighborhood({
reducer:ee.Reducer.mean(),
kernel:ee.Kernel.square(4)
});
};
varbands=['B4','B3','B2'];
// Select and filter first!
varreasonableComputation=images
.select(bands)
.filterBounds(sf)
.filterDate('2018-01-01','2019-02-01')
.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',1))
.aside(print)// Useful for debugging.
.map(reduceFunction)
.reduce('mean')
.rename(bands);
varviz={bands:bands,min:0,max:10000};
Map.addLayer(reasonableComputation,viz,'reasonableComputation');

```

## Use `updateMask()` instead of `mask()`
The difference between `updateMask()` and `mask()` is that the former does a logical `and()` of the argument (the new mask) and the existing image mask whereas `mask()` simply replaces the image mask with the argument. The danger of the latter is that you can unmask pixels unintentionally. In this example, the goal is to mask pixels less than or equal to 300 meters elevation. As you can see (zoom out), using `mask()` causes a lot of pixels to become unmasked, pixels that don't belong in the image of interest:
```
varl8sr=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2');
varsf=ee.Geometry.Point([-122.40554461769182,37.786807309873716]);
varaw3d30=ee.Image('JAXA/ALOS/AW3D30_V1_1');
Map.centerObject(sf,7);
varimage=l8sr.filterBounds(sf)
.filterDate('2019-06-01','2019-12-31')
.first();
image=image.multiply(0.0000275).subtract(0.2);// Apply scale factors.
varvis={bands:['SR_B4','SR_B3','SR_B2'],min:0,max:0.3};
Map.addLayer(image,vis,'image',false);
varmask=aw3d30.select('AVE').gt(300);
Map.addLayer(mask,{},'mask',false);
// NO! Don't do this!
varbadMask=image.mask(mask);
Map.addLayer(badMask,vis,'badMask');
vargoodMask=image.updateMask(mask);
Map.addLayer(goodMask,vis,'goodMask',false);

```

## Combine reducers
If you need multiple statistics (e.g. mean and standard deviation) from a single input (e.g. an image region), it is more efficient to combine reducers. For example, to get image statistics, combine reducers as follows:
```
varimage=ee.Image(
'COPERNICUS/S2_HARMONIZED/20150821T111616_20160314T094808_T30UWU');
// Get mean and SD in every band by combining reducers.
varstats=image.reduceRegion({
reducer:ee.Reducer.mean().combine({
reducer2:ee.Reducer.stdDev(),
sharedInputs:true
}),
geometry:ee.Geometry.Rectangle([-2.15,48.55,-1.83,48.72]),
scale:10,
bestEffort:true// Use maxPixels if you care about scale.
});
print(stats);
// Extract means and SDs to images.
varmeansImage=stats.toImage().select('.*_mean');
varsdsImage=stats.toImage().select('.*_stdDev');

```

In this example, note that the mean reducer is combined with the standard deviation reducer and `sharedInputs` is true to enable a single pass through the input pixels. In the output dictionary, the name of the reducer is appended to the band name. To get mean and SD images (for example to normalize the input image), you can turn the values into an image and use regexes to extract means and SDs individually as demonstrated in the example.
## Use `Export`
For computations that result in "User memory limit exceeded" or "Computation timed out" errors in the Code Editor, the same computations may be able to succeed by using `Export`. This is because the timeouts are longer and the allowable memory footprint is larger when running in the batch system (where exports run). (There are other approaches you may want to try first as detailed in the [debugging doc](https://developers.google.com/earth-engine/guides/debugging#scaling_errors)). Continuing the previous example, suppose that dictionary returned an error. You could obtain the results by doing something like:
```
varlink='86836482971a35a5e735a17e93c23272';
Export.table.toDrive({
collection:ee.FeatureCollection([ee.Feature(null,stats)]),
description:'exported_stats_demo_'+link,
fileFormat:'CSV'
});

```

Note that the link is embedded into the asset name, for reproducibility. Also note that if you want to export `toAsset`, you will need to supply a geometry, which can be anything, for example the image centroid, which is small and cheap to compute. (i.e. don't use a complex geometry if you don't need it).
See the debugging page for examples of using `Export` to resolve [Computation timed out](https://developers.google.com/earth-engine/guides/debugging#timed-out) and [Too many concurrent aggregations](https://developers.google.com/earth-engine/guides/debugging#too-many). See [this doc](https://developers.google.com/earth-engine/guides/exporting) for details on exporting in general.
## If you don't need to clip, don't use `clip()`
Using `clip()` unnecessarily will _increase_ computation time. Avoid `clip()` unless it's necessary to your analysis. If you're not sure, don't clip. An example of a bad use of clip:
Don't clip inputs unnecessarily!
```
vartable=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
varl8sr=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2');
varbelgium=table.filter(ee.Filter.eq('country_na','Belgium')).first();
// Do NOT clip unless you need to.
varunnecessaryClip=l8sr
.select('SR_B4')// Good.
.filterBounds(belgium.geometry())// Good.
.filterDate('2019-01-01','2019-04-01')// Good.
.map(function(image){
returnimage.clip(belgium.geometry());// NO! Bad! Not necessary.
})
.median()
.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:belgium.geometry(),
scale:30,
maxPixels:1e10,
});
print(unnecessaryClip);

```

Clipping the input images can be skipped entirely, because the region is specified in the `reduceRegion()` call:
Specify the region for the output!
```
varnoClipNeeded=l8sr
.select('SR_B4')// Good.
.filterBounds(belgium.geometry())// Good.
.filterDate('2019-01-01','2019-12-31')// Good.
.median()
.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:belgium.geometry(),// Geometry is specified here.
scale:30,
maxPixels:1e10,
});
print(noClipNeeded);

```

If this computation times out, `Export` it as in [this example](https://developers.google.com/earth-engine/guides/best_practices#use-export).
## If you need to clip with a complex collection, use `clipToCollection()`
If you really need to clip something, and the geometries you want to use for clipping are in a collection, use `clipToCollection()`:
```
varecoregions=ee.FeatureCollection('RESOLVE/ECOREGIONS/2017');
varimage=ee.Image('JAXA/ALOS/AW3D30_V1_1');
varcomplexCollection=ecoregions
.filter(ee.Filter.eq('BIOME_NAME',
'Tropical & Subtropical Moist Broadleaf Forests'));
Map.addLayer(complexCollection,{},'complexCollection');
varclippedTheRightWay=image.select('AVE')
.clipToCollection(complexCollection);
Map.addLayer(clippedTheRightWay,{},'clippedTheRightWay',false);

```

Do NOT use `featureCollection.geometry()` or `featureCollection.union()` on large and/or complex collections, which can be more memory intensive.
## Don't use a complex collection as the region for a reducer
If you need to do a spatial reduction such that the reducer pools inputs from multiple regions in a `FeatureCollection`, don't supply `featureCollection.geometry()` as the `geometry` input to the reducer. Instead, use `clipToCollection()` and a region large enough to encompass the bounds of the collection. For example:
```
varecoregions=ee.FeatureCollection('RESOLVE/ECOREGIONS/2017');
varimage=ee.Image('JAXA/ALOS/AW3D30_V1_1');
varcomplexCollection=ecoregions
.filter(ee.Filter.eq('BIOME_NAME','Tropical & Subtropical Moist Broadleaf Forests'));
varclippedTheRightWay=image.select('AVE')
.clipToCollection(complexCollection);
Map.addLayer(clippedTheRightWay,{},'clippedTheRightWay');
varreduction=clippedTheRightWay.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:ee.Geometry.Rectangle({
coords:[-179.9,-50,179.9,50],// Almost global.
geodesic:false
}),
scale:30,
maxPixels:1e12
});
print(reduction);// If this times out, export it.

```

## Use a non-zero `errorMargin`
For possibly expensive geometry operations, use the largest error margin possible given the required precision of the computation. The error margin specifies the maximum allowable error (in meters) permitted during operations on geometries (e.g. during reprojection). Specifying a small error margin can result in the need to densify geometries (with coordinates), which can be memory intensive. It's good practice to specify as large an error margin as possible for your computation:
```
varecoregions=ee.FeatureCollection('RESOLVE/ECOREGIONS/2017');
varcomplexCollection=ecoregions.limit(10);
Map.centerObject(complexCollection);
Map.addLayer(complexCollection);
varexpensiveOps=complexCollection.map(function(f){
returnf.buffer(10000,200).bounds(200);
});
Map.addLayer(expensiveOps,{},'expensiveOps');

```

## Don't use a ridiculously small scale with `reduceToVectors()`
If you want to convert a raster to a vector, use an appropriate scale. Specifying a very small scale can substantially increase computation cost. Set scale as high as possible give the required precision. For example, to get polygons representing global land masses:
```
varetopo=ee.Image('NOAA/NGDC/ETOPO1');
// Approximate land boundary.
varbounds=etopo.select(0).gt(-100);
// Non-geodesic polygon.
varalmostGlobal=ee.Geometry.Polygon({
coords:[[-180,-80],[180,-80],[180,80],[-180,80],[-180,-80]],
geodesic:false
});
Map.addLayer(almostGlobal,{},'almostGlobal');
varvectors=bounds.selfMask().reduceToVectors({
reducer:ee.Reducer.countEvery(),
geometry:almostGlobal,
// Set the scale to the maximum possible given
// the required precision of the computation.
scale:50000,
});
Map.addLayer(vectors,{},'vectors');

```

In the previous example, note the use of a non-geodesic polygon for use in global reductions.
## Don't use `reduceToVectors()` with `reduceRegions()`
Don't use a `FeatureCollection` returned by `reduceToVectors()` as an input to `reduceRegions()`. Instead, add the bands you want to reduce before calling `reduceToVectors()`:
```
varetopo=ee.Image('NOAA/NGDC/ETOPO1');
varmod11a1=ee.ImageCollection('MODIS/006/MOD11A1');
// Approximate land boundary.
varbounds=etopo.select(0).gt(-100);
// Non-geodesic polygon.
varalmostGlobal=ee.Geometry.Polygon({
coords:[[-180,-80],[180,-80],[180,80],[-180,80],[-180,-80]],
geodesic:false
});
varlst=mod11a1.first().select(0);
varmeans=bounds.selfMask().addBands(lst).reduceToVectors({
reducer:ee.Reducer.mean(),
geometry:almostGlobal,
scale:1000,
maxPixels:1e10
});
print(means.limit(10));

```

Note that other ways of reducing pixels of one image within zones of another include [reduceConnectedCommponents()](https://developers.google.com/earth-engine/apidocs/ee-image-reduceconnectedcomponents) and/or [grouping reducers](https://developers.google.com/earth-engine/guides/reducers_grouping).
## Use `fastDistanceTransform()` for neighborhood operations
For some convolution operations, `fastDistanceTransform()` may be more efficient than `reduceNeighborhood()` or `convolve()`. For example, to do erosion and/or dilation of binary inputs:
```
varaw3d30=ee.Image('JAXA/ALOS/AW3D30_V1_1');
// Make a simple binary layer from a threshold on elevation.
varmask=aw3d30.select('AVE').gt(300);
Map.setCenter(-122.0703,37.3872,11);
Map.addLayer(mask,{},'mask');
// Distance in pixel units.
vardistance=mask.fastDistanceTransform().sqrt();
// Threshold on distance (three pixels) for a dilation.
vardilation=distance.lt(3);
Map.addLayer(dilation,{},'dilation');
// Do the reverse for an erosion.
varnotDistance=mask.not().fastDistanceTransform().sqrt();
varerosion=notDistance.gt(3);
Map.addLayer(erosion,{},'erosion');

```

## Use the optimizations in `reduceNeighborhood()`
If you need to perform a convolution and can't use `fastDistanceTransform()`, use the optimizations in `reduceNeighborhood()`.
```
varl8raw=ee.ImageCollection('LANDSAT/LC08/C02/T1_RT');
varcomposite=ee.Algorithms.Landsat.simpleComposite(l8raw);
varbands=['B4','B3','B2'];
varoptimizedConvolution=composite.select(bands).reduceNeighborhood({
reducer:ee.Reducer.mean(),
kernel:ee.Kernel.square(3),
optimization:'boxcar'// Suitable optimization for mean.
}).rename(bands);
varviz={bands:bands,min:0,max:72};
Map.setCenter(-122.0703,37.3872,11);
Map.addLayer(composite,viz,'composite');
Map.addLayer(optimizedConvolution,viz,'optimizedConvolution');

```

## Don't sample more data than you need
Resist the urge to increase your training dataset size unnecessarily. Although increasing the amount of training data is an effective machine learning strategy in some circumstances, it can also increase computational cost with no corresponding increase in accuracy. (For an understanding of when to increase training dataset size, see [this reference](https://www.deeplearning.ai/machine-learning-yearning/)). The following example demonstrates how requesting too much training data can result in the dreaded "Computed value is too large" error:
Don't sample too much data!
```
varl8raw=ee.ImageCollection('LANDSAT/LC08/C02/T1_RT');
varcomposite=ee.Algorithms.Landsat.simpleComposite(l8raw);
varlabels=ee.FeatureCollection('projects/google/demo_landcover_labels');
// No! Not necessary. Don't do this:
labels=labels.map(function(f){returnf.buffer(100000,1000);});
varbands=['B2','B3','B4','B5','B6','B7'];
vartraining=composite.select(bands).sampleRegions({
collection:labels,
properties:['landcover'],
scale:30
});
varclassifier=ee.Classifier.smileCart().train({
features:training,
classProperty:'landcover',
inputProperties:bands
});
print(classifier.explain());// Computed value is too large

```

The better approach is to start with a moderate amount of data and tune the hyperparameters of the classifier to determine if you can achieve your desired accuracy:
Tune hyperparameters!
```
varl8raw=ee.ImageCollection('LANDSAT/LC08/C02/T1_RT');
varcomposite=ee.Algorithms.Landsat.simpleComposite(l8raw);
varlabels=ee.FeatureCollection('projects/google/demo_landcover_labels');
// Increase the data a little bit, possibly introducing noise.
labels=labels.map(function(f){returnf.buffer(100,10);});
varbands=['B2','B3','B4','B5','B6','B7'];
vardata=composite.select(bands).sampleRegions({
collection:labels,
properties:['landcover'],
scale:30
});
// Add a column of uniform random numbers called 'random'.
data=data.randomColumn();
// Partition into training and testing.
vartraining=data.filter(ee.Filter.lt('random',0.5));
vartesting=data.filter(ee.Filter.gte('random',0.5));
// Tune the minLeafPopulation parameter.
varminLeafPops=ee.List.sequence(1,10);
varaccuracies=minLeafPops.map(function(p){
varclassifier=ee.Classifier.smileCart({minLeafPopulation:p})
.train({
features:training,
classProperty:'landcover',
inputProperties:bands
});
returntesting
.classify(classifier)
.errorMatrix('landcover','classification')
.accuracy();
});
print(ui.Chart.array.values({
array:ee.Array(accuracies),
axis:0,
xLabels:minLeafPops
}));

```

In this example, the classifier is already very accurate, so there's not much tuning to do. You might want to choose the smallest tree possible (i.e. largest `minLeafPopulation`) that still has the required accuracy.
## `Export` intermediate results
Suppose your objective is to take samples from a relatively complex computed image. It is often more efficient to `Export` the image `toAsset()`, load the exported image, then sample. For example:
```
varimage=ee.Image('UMD/hansen/global_forest_change_2018_v1_6');
vargeometry=ee.Geometry.Polygon(
[[[-76.64069800085349,5.511777325802095],
[-76.64069800085349,-20.483938229362376],
[-35.15632300085349,-20.483938229362376],
[-35.15632300085349,5.511777325802095]]],null,false);
vartestRegion=ee.Geometry.Polygon(
[[[-48.86726050085349,-3.0475996402515717],
[-48.86726050085349,-3.9248707849303295],
[-47.46101050085349,-3.9248707849303295],
[-47.46101050085349,-3.0475996402515717]]],null,false);
// Forest loss in 2016, to stratify a sample.
varloss=image.select('lossyear');
varloss16=loss.eq(16).rename('loss16');
// Scales and masks Landsat 8 surface reflectance images.
functionprepSrL8(image){
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBands=image.select('ST_B.*').multiply(0.00341802).add(149.0);
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBands,null,true)
.updateMask(qaMask);
}
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
.map(prepSrL8);
// Create two annual cloud-free composites.
varcomposite1=collection.filterDate('2015-01-01','2015-12-31').median();
varcomposite2=collection.filterDate('2017-01-01','2017-12-31').median();
// We want a strtatified sample of this stack.
varstack=composite1.addBands(composite2)
.float();// Export the smallest size possible.
// Export the image. This block is commented because the export is complete.
/*
var link = '0b8023b0af6c1b0ac7b5be649b54db06'
var desc = 'Logistic_regression_stack_' + link;
Export.image.toAsset({
 image: stack,
 description: desc,
 assetId: desc,
 region: geometry,
 scale: 30,
 maxPixels: 1e10
})
*/
// Load the exported image.
varexportedStack=ee.Image(
'projects/google/Logistic_regression_stack_0b8023b0af6c1b0ac7b5be649b54db06');
// Take a very small sample first, to debug.
vartestSample=exportedStack.addBands(loss16).stratifiedSample({
numPoints:1,
classBand:'loss16',
region:testRegion,
scale:30,
geometries:true
});
print(testSample);// Check this in the console.
// Take a large sample.
varsample=exportedStack.addBands(loss16).stratifiedSample({
numPoints:10000,
classBand:'loss16',
region:geometry,
scale:30,
});
// Export the large sample...

```

In this example, note that the imagery is exported as float. Don't export at double precision unless absolutely necessary. When doing this export, note that a Code Editor link (obtained immediately prior to export) is embedded in the filename for reproduceability.
Once the export is completed, reload the asset and proceed with sampling from it. Note that a very small sample over a very small test area is run first, for debugging. When that is shown to succeed, take a larger sample and export it. Such large samples typically need to be exported. Do not expect such samples to be available interactively (for example through `print()`) or usable (for example as input to a classifier) without exporting them first.
## Join vs. map-filter
Suppose you want to join collections based on time, location or some metadata property. Generally, this is most efficiently accomplished with a join. The following example does a spatio-temporal join between the Landsat 8 and Sentinel-2 collections:
```
vars2=ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
.filterBounds(ee.Geometry.Point([-2.0205,48.647]));
varl8=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2');
varjoined=ee.Join.saveAll('landsat').apply({
primary:s2,
secondary:l8,
condition:ee.Filter.and(
ee.Filter.maxDifference({
difference:1000*60*60*24,// One day in milliseconds
leftField:'system:time_start',
rightField:'system:time_start',
}),
ee.Filter.intersects({
leftField:'.geo',
rightField:'.geo',
})
)
});
print(joined);

```

Although you should try a join first (`Export` if needed), occasionally a `filter()` within a `map()` can also be effective, particularly for very large collections.
```
vars2=ee.ImageCollection('COPERNICUS/S2_HARMONIZED')
.filterBounds(ee.Geometry.Point([-2.0205,48.647]));
varl8=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2');
varmappedFilter=s2.map(function(image){
vardate=image.date();
varlandsat=l8
.filterBounds(image.geometry())
.filterDate(date.advance(-1,'day'),date.advance(1,'day'));
// Return the input image with matching scenes in a property.
returnimage.set({
landsat:landsat,
size:landsat.size()
});
}).filter(ee.Filter.gt('size',0));
print(mappedFilter);

```

## `reduceRegion()` vs. `reduceRegions()` vs. for-loop
Calling `reduceRegions()` with a very large or complex `FeatureCollection` as input may result in the dreaded "Computed value is too large" error. One potential solution is to map `reduceRegion()` over the `FeatureCollection` instead. Another potential solution is to use a (gasp) for-loop. Although this is strongly discouraged in Earth Engine as described [here](https://developers.google.com/earth-engine/guides/getstarted#mapping-what-to-do-instead-of-a-for-loop), [here](https://developers.google.com/earth-engine/guides/tutorial_js_03#for-loops) and [here](https://developers.google.com/earth-engine/guides/client_server#looping), `reduceRegion()` can be implemented in a for-loop to perform large reductions.
Suppose your objective is to obtain the mean of pixels (or any statistic) in each feature in a `FeatureCollection` for each image in an `ImageCollection`. The following example compares the three approaches previously described:
```
// Table of countries.
varcountriesTable=ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017");
// Time series of images.
varmod13a1=ee.ImageCollection("MODIS/006/MOD13A1");
// MODIS vegetation indices (always use the most recent version).
varband='NDVI';
varimagery=mod13a1.select(band);
// Option 1: reduceRegions()
vartestTable=countriesTable.limit(1);// Do this outside map()s and loops.
vardata=imagery.map(function(image){
returnimage.reduceRegions({
collection:testTable,
reducer:ee.Reducer.mean(),
scale:500
}).map(function(f){
returnf.set({
time:image.date().millis(),
date:image.date().format()
});
});
}).flatten();
print(data.first());
// Option 2: mapped reduceRegion()
vardata=countriesTable.map(function(feature){
returnimagery.map(function(image){
returnee.Feature(feature.geometry().centroid(100),
image.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:feature.geometry(),
scale:500
})).set({
time:image.date().millis(),
date:image.date().format()
}).copyProperties(feature);
});
}).flatten();
print(data.first());
// Option 3: for-loop (WATCH OUT!)
varsize=countriesTable.size();
// print(size); // 312
varcountriesList=countriesTable.toList(1);// Adjust size.
vardata=ee.FeatureCollection([]);// Empty table.
for(varj=0;j<1;j++){// Adjust size.
varfeature=ee.Feature(countriesList.get(j));
// Convert ImageCollection > FeatureCollection
varfc=ee.FeatureCollection(imagery.map(function(image){
returnee.Feature(feature.geometry().centroid(100),
image.reduceRegion({
reducer:ee.Reducer.mean(),
geometry:feature.geometry(),
scale:500
})).set({
time:image.date().millis(),
date:image.date().format()
}).copyProperties(feature);
}));
data=data.merge(fc);
}
print(data.first());

```

Note that the `first()` thing from each collection is printed, for debugging purposes. You should not expect that the complete result will be available interactively: you'll need to `Export`. Also note that for-loops should be used with extreme caution and only as a last resort. Finally, the for-loop requires manually obtaining the size of the input collection and hardcoding that in the appropriate locations. If any of that sounds unclear to you, don't use a for-loop.
## Use forward differencing for neighbors in time
Suppose you have a temporally sorted `ImageCollection` (i.e. a time series) and you want to compare each image to the previous (or next) image. Rather than use `iterate()` for this purpose, it may be more efficient to use an array-based forward differencing. The following example uses this method to de-duplicate the Sentinel-2 collection, where duplicates are defined as images with the same day of year:
```
varsentinel2=ee.ImageCollection('COPERNICUS/S2_HARMONIZED');
varsf=ee.Geometry.Point([-122.47555371521855,37.76884708376152]);
vars2=sentinel2
.filterBounds(sf)
.filterDate('2018-01-01','2019-12-31');
varwithDoys=s2.map(function(image){
varndvi=image.normalizedDifference(['B4','B8']).rename('ndvi');
vardate=image.date();
vardoy=date.getRelative('day','year');
vartime=image.metadata('system:time_start');
vardoyImage=ee.Image(doy)
.rename('doy')
.int();
returnndvi.addBands(doyImage).addBands(time)
.clip(image.geometry());// Appropriate use of clip.
});
vararray=withDoys.toArray();
vartimeAxis=0;
varbandAxis=1;
vardedupe=function(array){
vartime=array.arraySlice(bandAxis,-1);
varsorted=array.arraySort(time);
vardoy=sorted.arraySlice(bandAxis,-2,-1);
varleft=doy.arraySlice(timeAxis,1);
varright=doy.arraySlice(timeAxis,0,-1);
varmask=ee.Image(ee.Array([[1]]))
.arrayCat(left.neq(right),timeAxis);
returnarray.arrayMask(mask);
};
vardeduped=dedupe(array);
// Inspect these outputs to confirm that duplicates have been removed.
print(array.reduceRegion('first',sf,10));
print(deduped.reduceRegion('first',sf,10));

```

Inspect the printed collections to verify that duplicates have been removed.
Was this helpful?
