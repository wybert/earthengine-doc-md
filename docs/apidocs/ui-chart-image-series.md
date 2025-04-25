 
#  ui.Chart.image.series 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ui-chart-image-series#examples)


Generates a Chart from an ImageCollection. Plots derived values of each band in a region across images. Usually a time series. 
- X-axis: Image, labeled by xProperty value.
- Y-axis: Band value.
- Series: Band names.
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.series(imageCollection, region,  _reducer_, _scale_, _xProperty_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`imageCollection`| ImageCollection| An ImageCollection with data to be included in the chart.  
`region`| Feature|FeatureCollection|Geometry| The region to reduce.  
`reducer`| Reducer, optional| Reducer that generates the values for the y-axis. Must return a single value. Defaults to ee.Reducer.mean().  
`scale`| Number, optional| Scale to use with the reducer in meters.  
`xProperty`| String, optional| Property to be used as the label for each image on the x-axis. Defaults to 'system:time_start'.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ui-chart-image-series#code-editor-javascript-sample) More
```
// Define a region of pixels to reduce and chart a time series for.
varregion=ee.Geometry.BBox(-121.916,37.130,-121.844,37.076);
// Define an image collection time series to chart, MODIS vegetation indices
// in this case.
varimgCol=ee.ImageCollection('MODIS/006/MOD13A1')
.filter(ee.Filter.date('2015-01-01','2020-01-01'))
.select(['NDVI','EVI']);
// Define the chart and print it to the console.
varchart=ui.Chart.image.series({
imageCollection:imgCol,
region:region,
reducer:ee.Reducer.mean(),
scale:500,
xProperty:'system:time_start'
})
.setSeriesNames(['EVI','NDVI'])
.setOptions({
title:'Average Vegetation Index Value by Date',
hAxis:{title:'Date',titleTextStyle:{italic:false,bold:true}},
vAxis:{
title:'Vegetation index (x1e4)',
titleTextStyle:{italic:false,bold:true}
},
lineWidth:5,
colors:['e37d05','1d6b99'],
curveType:'function'
});
print(chart);
```

