 
#  Chart Styling
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Charts produced by the `ui.Chart` module in the Earth Engine Code Editor can be styled using the `.setOptions()` method. The method takes a client-side JavaScript object of configuration options as an input. Configuration options for each chart type are provided in the respective Google Charts documentation under the _Configuration Options_ section, for example: [Line Chart](https://developers.google.com/chart/interactive/docs/gallery/linechart#configuration-options).
## Configuration options example
![](https://developers.google.com/static/earth-engine/images/Charts_style_01.svg)
Here, custom chart styling is applied to the [`ui.Chart.image.doySeries` example](https://developers.google.com/earth-engine/guides/charts_image_collection#uichartimagedoyseries). It provides a guide for how to format a configuration options object and apply it to an `ee.Chart`.
```
// Import the example feature collection and subset the glassland feature.
vargrassland=ee.FeatureCollection('projects/google/charts_feature_example')
.filter(ee.Filter.eq('label','Grassland'));

// Load MODIS vegetation indices data and subset a decade of images.
varvegIndices=ee.ImageCollection('MODIS/006/MOD13A1')
.filter(ee.Filter.date('2010-01-01','2020-01-01'))
.select(['NDVI','EVI']);

**// Set chart style properties.
varchartStyle={
title:'Average Vegetation Index Value by Day of Year for Grassland',
hAxis:{
title:'Day of year',
titleTextStyle:{italic:false,bold:true},
gridlines:{color:'FFFFFF'}
},
vAxis:{
title:'Vegetation index (x1e4)',
titleTextStyle:{italic:false,bold:true},
gridlines:{color:'FFFFFF'},
format:'short',
baselineColor:'FFFFFF'
},
series:{
0:{lineWidth:3,color:'E37D05',pointSize:7},
1:{lineWidth:7,color:'1D6B99',lineDashStyle:[4,4]}
},
chartArea:{backgroundColor:'EBEBEB'}
};**

// Define the chart.
varchart=
ui.Chart.image
.doySeries({
imageCollection:vegIndices,
region:grassland,
regionReducer:ee.Reducer.mean(),
scale:500,
yearReducer:ee.Reducer.mean(),
startDay:1,
endDay:365
})
.setSeriesNames(['EVI','NDVI']);

**// Apply custom style properties to the chart.
chart.setOptions(chartStyle);**

// Print the chart to the console.
print(chart);
```
**Note:** setting individual series properties overrides top-level properties.
## How do I...
The following examples provide JavaScript objects defining only the relevant configuration options to answer the question. Add additional options to the object as needed and pass the result to the `.setOptions()` method of an `ee.Chart`.
### set the chart title?
```
{
title:'The Chart Title'
}
```

### hide the chart title?
```
{
titlePosition:'none'
}
```

### hide the legend?
```
{
legend:{position:'none'}
}
```

### define the axis limits?
```
{
hAxis:{// x-axis
viewWindow:{min:10,max:100}
},
vAxis:{// y-axis
viewWindow:{min:-10,max:50}
}
}
```

### set symbol size and color?
You can set symbol properties for all series using top-level properties, for example:
```
{
colors:['blue'],
pointSize:10,
lineWidth:5,
lineDashStyle:[4,4],
pointShape:'diamond'// 'circle', 'triangle', 'square', 'star', or 'polygon'
}
```

or set properties for selected series:
```
{
series:{
0:{lineWidth:3,color:'yellow',pointSize:7},
2:{lineWidth:7,color:'1D6D99',lineDashStyle:[4,4]}
}
}
```

You can also set colors for individual series by providing a color array that corresponds to the length and order of the series.
```
{
colors:['blue','yellow','red']
}
```

### hide a series from the legend?
```
{
series:{
0:{visibleInLegend:false},// hides the 1st series in the legend
2:{visibleInLegend:false}// hides the 3rd series in the legend
}
}
```

### show points on a line chart?
Show points for all series:
```
{
pointSize:10
}
```

or for individual series:
```
{
series:{
0:{pointSize:10},// shows size 10 points for the 1st line series
2:{pointSize:10}// shows size 10 points for the 3rd line series
}
}
```

### show lines on a point chart?
Show lines for all series:
```
{
lineWidth:10
}
```

or for individual series:
```
{
series:{
0:{lineWidth:10},// shows size 10 lines for the 1st point series
2:{lineWidth:10}// shows size 10 lines for the 3rd point series
}
}
```

### apply log scale to an axis?
```
{
hAxis:{logScale:true},// x-axis
vAxis:{logScale:true}// y-axis
}
```

### apply a smoothing function to a line?
Apply a smoothing function to every line series:
```
{
curveType:'function'
}
```

or individual series:
```
{
series:{
0:{curveType:'function'},// apply smoothing function to 1st line series
2:{curveType:'function'}// apply smoothing function to 3rd line series
}
}
```

### zoom and pan chart axes?
See the `explorer` options for respective Google Chart types. The following will permit zooming and panning on both axes.
```
{
explorer:{}
}
```

Limit panning and zooming to a single axis:
```
{
explorer:{axis:'vertical'}// or 'horizontal'
}
```
**Note:** The explorer only works with continuous axes (such as numbers or dates).
### set point symbol opacity?
```
{
dataOpacity:0.5
}
```
**Note:** line opacity cannot be set.
### rotate axes?
```
{
orientation:'vertical'// or 'horizontal'
}
```

### set text style?
Text styling options are specified according to the following JavaScript object:
```
vartextStyle={
color:'grey',
fontName:'arial',
fontSize:14,
bold:true,
italic:false
}
```

Set x-axis text style:
```
{
hAxis:{
textStyle:textStyle,// tick label text style
titleTextStyle:textStyle// axis title text style
}
}
```

Set y-axis text style:
```
{
vAxis:{
textStyle:textStyle,// tick label text style
titleTextStyle:textStyle// axis title text style
}
}
```

Set legend text style:
```
{
legend:{textStyle:textStyle}
}
```

You can also set font name and size for all text elements:
```
{
fontName:'arial',
fontSize:14
}
```

### set chart background color?
```
{
chartArea:{backgroundColor:'EBEBEB'}
}
```

### set chart grid line color?
```
{
hAxis:{// x-axis
gridlines:{color:'FFFFFF'}
},
vAxis:{// y-axis
gridlines:{color:'FFFFFF'}
}
}
```

### remove grid lines?
```
{
hAxis:{// x-axis
gridlines:{count:0}
},
vAxis:{// y-axis
gridlines:{count:0}
}
}
```

### format axis value labels?
See [this guide](https://developers.google.com/chart/interactive/docs/customizing_axes#number-formats) for the full list of axis value label format options.
```
{
hAxis:{// x-axis
format:'short'// applies the 'short' format option
},
vAxis:{// y-axis
format:'scientific'// applies the 'scientific' format option
}
}
```

### interpolate null y-axis values?
Missing or null y-axis values in a line chart can cause line breaks. Use `interpolateNulls: true` to draw a continuous line.
```
{
interpolateNulls:true
}
```

### add a trend line?
A trend line can be automatically generated for scatter, bar, column, and line charts. See [this page](https://developers.google.com/chart/interactive/docs/gallery/trendlines) for full details.
```
{
trendlines:{
0:{// add a trend line to the 1st series
type:'linear',// or 'polynomial', 'exponential'
color:'green',
lineWidth:5,
opacity:0.2,
visibleInLegend:true,
}
}
}
```

