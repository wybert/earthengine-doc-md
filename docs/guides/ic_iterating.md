 
#  Iterating over an ImageCollection 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Although `map()` applies a function to every image in a collection, the function visits every image in the collection independently. For example, suppose you want to compute a cumulative anomaly (_A t_) at time _t_ from a time series. To obtain a recursively defined series of the form _A t = f(Imaget, At-1)_, mapping won't work because the function (_f_) depends on the previous result (_A t-1_). For example, suppose you want to compute a series of cumulative Normalized Difference Vegetation Index (NDVI) anomaly images relative to a baseline. Let _A 0_ = 0 and _f(Image t, At-1)_ = _Image t + At-1_ where _A t-1_ is the cumulative anomaly up to time _t-1_ and _Image t_ is the anomaly at time _t_. Use `imageCollection.iterate()` to make this recursively defined `ImageCollection`. In the following example, the function `accumulate()` takes two parameters: an image in the collection, and a list of all the previous outputs. With each call to `iterate()`, the anomaly is added to the running sum and the result is added to the list. The final result is passed to the `ImageCollection` constructor to get a new sequence of images:
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/ic_iterating#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/guides/ic_iterating#colab-python-sample) More
```
// Load MODIS EVI imagery.
varcollection=ee.ImageCollection('MODIS/006/MYD13A1').select('EVI');
// Define reference conditions from the first 10 years of data.
varreference=collection.filterDate('2001-01-01','2010-12-31')
// Sort chronologically in descending order.
.sort('system:time_start',false);
// Compute the mean of the first 10 years.
varmean=reference.mean();
// Compute anomalies by subtracting the 2001-2010 mean from each image in a
// collection of 2011-2014 images. Copy the date metadata over to the
// computed anomaly images in the new collection.
varseries=collection.filterDate('2011-01-01','2014-12-31').map(function(image){
returnimage.subtract(mean).set('system:time_start',image.get('system:time_start'));
});
// Display cumulative anomalies.
Map.setCenter(-100.811,40.2,5);
Map.addLayer(series.sum(),
{min:-60000,max:60000,palette:['FF0000','000000','00FF00']},'EVI anomaly');
// Get the timestamp from the most recent image in the reference collection.
vartime0=reference.first().get('system:time_start');
// Use imageCollection.iterate() to make a collection of cumulative anomaly over time.
// The initial value for iterate() is a list of anomaly images already processed.
// The first anomaly image in the list is just 0, with the time0 timestamp.
varfirst=ee.List([
// Rename the first band 'EVI'.
ee.Image(0).set('system:time_start',time0).select([0],['EVI'])
]);
// This is a function to pass to Iterate().
// As anomaly images are computed, add them to the list.
varaccumulate=function(image,list){
// Get the latest cumulative anomaly image from the end of the list with
// get(-1). Since the type of the list argument to the function is unknown,
// it needs to be cast to a List. Since the return type of get() is unknown,
// cast it to Image.
varprevious=ee.Image(ee.List(list).get(-1));
// Add the current anomaly to make a new cumulative anomaly image.
varadded=image.add(previous)
// Propagate metadata to the new image.
.set('system:time_start',image.get('system:time_start'));
// Return the list with the cumulative anomaly inserted.
returnee.List(list).add(added);
};
// Create an ImageCollection of cumulative anomaly images by iterating.
// Since the return type of iterate is unknown, it needs to be cast to a List.
varcumulative=ee.ImageCollection(ee.List(series.iterate(accumulate,first)));
// Predefine the chart titles.
vartitle={
title:'Cumulative EVI anomaly over time',
hAxis:{title:'Time'},
vAxis:{title:'Cumulative EVI anomaly'},
};
// Chart some interesting locations.
varpt1=ee.Geometry.Point(-65.544,-4.894);
print('Amazon rainforest:',
ui.Chart.image.series(
cumulative,pt1,ee.Reducer.first(),500).setOptions(title));
varpt2=ee.Geometry.Point(116.4647,40.1054);
print('Beijing urbanization:',
ui.Chart.image.series(
cumulative,pt2,ee.Reducer.first(),500).setOptions(title));
varpt3=ee.Geometry.Point(-110.3412,34.1982);
print('Arizona forest disturbance and recovery:',
ui.Chart.image.series(
cumulative,pt3,ee.Reducer.first(),500).setOptions(title));
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
importaltairasalt
# Load MODIS EVI imagery.
collection = ee.ImageCollection('MODIS/006/MYD13A1').select('EVI')
# Define reference conditions from the first 10 years of data.
reference = collection.filterDate('2001-01-01', '2010-12-31').sort(
  # Sort chronologically in descending order.
  'system:time_start',
  False,
)
# Compute the mean of the first 10 years.
mean = reference.mean()
# Compute anomalies by subtracting the 2001-2010 mean from each image in a
# collection of 2011-2014 images. Copy the date metadata over to the
# computed anomaly images in the new collection.
series = collection.filterDate('2011-01-01', '2014-12-31').map(
  lambda image: image.subtract(mean).set(
    'system:time_start', image.get('system:time_start')
  )
)
# Display cumulative anomalies.
m = geemap.Map()
m.set_center(-100.811, 40.2, 5)
m.add_layer(
  series.sum(),
  {'min': -60000, 'max': 60000, 'palette': ['FF0000', '000000', '00FF00']},
  'EVI anomaly',
)
display(m)
# Get the timestamp from the most recent image in the reference collection.
time_0 = reference.first().get('system:time_start')
# Use imageCollection.iterate() to make a collection of cumulative anomaly over time.
# The initial value for iterate() is a list of anomaly images already processed.
# The first anomaly image in the list is just 0, with the time_0 timestamp.
first = ee.List([
  # Rename the first band 'EVI'.
  ee.Image(0)
  .set('system:time_start', time_0)
  .select([0], ['EVI'])
])
# This is a function to pass to Iterate().
# As anomaly images are computed, add them to the list.
defaccumulate(image, list):
 # Get the latest cumulative anomaly image from the end of the list with
 # get(-1). Since the type of the list argument to the function is unknown,
 # it needs to be cast to a List. Since the return type of get() is unknown,
 # cast it to Image.
 previous = ee.Image(ee.List(list).get(-1))
 # Add the current anomaly to make a new cumulative anomaly image.
 added = image.add(previous).set(
   # Propagate metadata to the new image.
   'system:time_start',
   image.get('system:time_start'),
 )
 # Return the list with the cumulative anomaly inserted.
 return ee.List(list).add(added)
# Create an ImageCollection of cumulative anomaly images by iterating.
# Since the return type of iterate is unknown, it needs to be cast to a List.
cumulative = ee.ImageCollection(ee.List(series.iterate(accumulate, first)))
# Predefine the chart titles.
title = 'Cumulative EVI anomaly over time'
# Chart some interesting locations.
defdisplay_chart(region, collection):
 reduced = (
   collection.filterBounds(region)
   .sort('system:time_start')
   .map(
     lambda image: ee.Feature(
       None,
       image.reduceRegion(ee.Reducer.first(), region, 500).set(
         'time', image.get('system:time_start')
       ),
     )
   )
 )
 reduced_dataframe = ee.data.computeFeatures(
   {'expression': reduced, 'fileFormat': 'PANDAS_DATAFRAME'}
 )
 alt.Chart(reduced_dataframe).mark_line().encode(
   alt.X('time:T').title('Time'),
   alt.Y('EVI:Q').title('Cumulative EVI anomaly'),
 ).properties(title=title).display()
pt_1 = ee.Geometry.Point(-65.544, -4.894)
display('Amazon rainforest:')
display_chart(pt_1, cumulative)
pt_2 = ee.Geometry.Point(116.4647, 40.1054)
display('Beijing urbanization:')
display_chart(pt_2, cumulative)
pt_3 = ee.Geometry.Point(-110.3412, 34.1982)
display('Arizona forest disturbance and recovery:')
display_chart(pt_3, cumulative)
```

Charting these sequences indicates whether NDVI is stabilizing relative to previous disturbances or whether NDVI is trending to a new state. Learn more about charts in Earth Engine from the [Charts section](https://developers.google.com/earth-engine/guides/charts).
The iterated function is limited in the operations it can perform. Specifically, it can’t modify variables outside the function; it can’t print anything; it can’t use JavaScript ‘if’ or ‘for’ statements. Any results you wish to collect or intermediate information you wish to carry over to the next iteration must be in the function’s return value. You can use `ee.Algorithms.If()` to perform conditional operations. 
