 
#  ui.Chart.image.seriesByRegion
Stay organized with collections  Save and categorize content based on your preferences. 
Generates a Chart from an image collection. Extracts and plots the value of the specified band in each region for each image in the collection. Usually a time series. 
- X-axis = Image labeled by xProperty (default: 'system:time_start').
- Y-axis = Reducer output.
- Series = Region labeled by seriesProperty (default: 'system:index').
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.seriesByRegion(imageCollection, regions, reducer,  _band_, _scale_, _xProperty_, _seriesProperty_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`imageCollection`| ImageCollection| An ImageCollection with data to be included in the chart.  
`regions`| Feature|FeatureCollection|Geometry|List| The regions to reduce.  
`reducer`| Reducer| Reducer that generates the value for the y-axis. Must return a single value.  
`band`| Number|String, optional| The band name to reduce using the reducer. Defaults to the first band.  
`scale`| Number, optional| Scale to use with the reducer in meters.  
`xProperty`| String, optional| Property to be used as the label for each image on the x-axis. Defaults to 'system:time_start'.  
`seriesProperty`| String, optional| Property of features in opt_regions to be used for series labels. Defaults to 'system:index'.  
## Examples
### Code Editor (JavaScript)
```
// Define regions of pixels to reduce and chart a time series for.
varregions=ee.FeatureCollection([
ee.Feature(
ee.Geometry.BBox(-121.916,37.130,-121.844,37.076),{label:'Forest'}),
ee.Feature(
ee.Geometry.BBox(-122.438,37.765,-122.396,37.800),{label:'Urban'})
]);
// Define an image collection time series to chart, MODIS vegetation indices
// in this case.
varimgCol=ee.ImageCollection('MODIS/006/MOD13A1')
.filter(ee.Filter.date('2015-01-01','2020-01-01'))
.select(['NDVI','EVI']);
// Define the chart and print it to the console.
varchart=ui.Chart.image.seriesByRegion({
imageCollection:imgCol,
band:'NDVI',
regions:regions,
reducer:ee.Reducer.mean(),
scale:500,
seriesProperty:'label',
xProperty:'system:time_start'
})
.setOptions({
title:'Average NDVI Value by Date',
hAxis:{title:'Date',titleTextStyle:{italic:false,bold:true}},
vAxis:{
title:'NDVI (x1e4)',
titleTextStyle:{italic:false,bold:true}
},
lineWidth:5,
colors:['0f8755','808080'],
});
print(chart);
```

