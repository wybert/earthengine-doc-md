 
#  Feature and FeatureCollection Charts 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Chart functions](https://developers.google.com/earth-engine/guides/charts_feature#chart_functions)
  * [Example data](https://developers.google.com/earth-engine/guides/charts_feature#example_data)
  * [ui.Chart.feature.byFeature](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturebyfeature)
    * [Column chart](https://developers.google.com/earth-engine/guides/charts_feature#column_chart)
    * [Bar chart](https://developers.google.com/earth-engine/guides/charts_feature#bar_chart)
    * [Stacked column chart](https://developers.google.com/earth-engine/guides/charts_feature#stacked_column_chart)
    * [Scatter chart](https://developers.google.com/earth-engine/guides/charts_feature#scatter_chart)
    * [Combo chart](https://developers.google.com/earth-engine/guides/charts_feature#combo_chart)
  * [ui.Chart.feature.byProperty](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturebyproperty)
    * [Example setup](https://developers.google.com/earth-engine/guides/charts_feature#example_setup)
    * [Column chart](https://developers.google.com/earth-engine/guides/charts_feature#column_chart_2)
    * [Line chart](https://developers.google.com/earth-engine/guides/charts_feature#line_chart)
    * [Area chart](https://developers.google.com/earth-engine/guides/charts_feature#area_chart)
    * [Pie chart](https://developers.google.com/earth-engine/guides/charts_feature#pie_chart)
    * [Donut chart](https://developers.google.com/earth-engine/guides/charts_feature#donut_chart)
  * [ui.Chart.feature.groups](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturegroups)
    * [Column chart](https://developers.google.com/earth-engine/guides/charts_feature#column_chart_3)
  * [ui.Chart.feature.histogram](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturehistogram)


The `ui.Chart.feature` module contains a set of functions for rendering charts from `Feature` and `FeatureCollection` objects. The choice of function determines the arrangement of data in the chart, i.e., what defines x- and y-axis values and what defines the series. Use the following function descriptions and examples to determine the best function and chart type for your purpose.
## Chart functions
Use the following plot diagrams as a visual guide to understand how each function arranges features and their properties in a chart; i.e., what elements define x values, y values, and series.
[**`ui.Chart.feature.byFeature`**](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturebyfeature)
Features are plotted along the x-axis by values of a selected property. Series are defined by a list of property names whose values are plotted along the y-axis.
![](https://developers.google.com/static/earth-engine/images/Charts_feature_by_feature_diagram.svg)
[**`ui.Chart.feature.byProperty`**](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturebyproperty)
Feature properties are plotted along the x-axis by name; values of the given properties are plotted along the y-axis. Series are features labeled by values of a selected property.
![](https://developers.google.com/static/earth-engine/images/Charts_feature_by_property_diagram.svg)
[**`ui.Chart.feature.groups`**](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturegroups)
Features are plotted along the x-axis by values of a selected property. Series are defined by unique values of a given property. Y-axis position is defined by a given property’s value.
![](https://developers.google.com/static/earth-engine/images/Charts_feature_by_group_diagram.svg)
[**`ui.Chart.feature.histogram`**](https://developers.google.com/earth-engine/guides/charts_feature#uichartfeaturehistogram)
Frequency histogram for values of a selected property.
  * **X-axis** : histogram buckets for values of a selected property
  * **Y-axis** : frequency of features qualified for each histogram bucket


## Example data
The following examples rely on a `FeatureCollection` composed of three ecoregion features with properties that describe climate normals.
See how the example data were created
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Define three representative ecoregions in the USA.
vardesert=ee.Feature(
ee.Geometry.Rectangle(-109.21,31.42,-108.3,32.03),
{label:'Desert',value:0});
varforest=ee.Feature(
ee.Geometry.Rectangle(-122.73,43.45,-122.28,43.91),
{label:'Forest',value:1});
vargrassland=ee.Feature(
ee.Geometry.Rectangle(-101.81,41.7,-100.53,42.51),
{label:'Grassland',value:2});
// Combine features into a feature collection.
varecoregions=ee.FeatureCollection([desert,forest,grassland]);
// Load PRISM climate normals image collection; convert images to bands.
varnormClim=ee.ImageCollection('OREGONSTATE/PRISM/Norm81m').toBands();
// Summarize climate normals for each ecoregion feature as a set or properties.
ecoregions=normClim.reduceRegions(
{collection:ecoregions,reducer:ee.Reducer.mean(),scale:5e4});
// Add a property for whether January temperature is warm or not.
ecoregions=ecoregions.map(function(ecoregion){
returnecoregion.set('warm',ee.Number(ecoregion.get('01_tmean')).gt(0));
});
```

## `ui.Chart.feature.byFeature`
### Column chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_01.svg)
Features are plotted along the x-axis, labeled by values of a selected property. Series are represented by adjacent columns defined by a list of property names whose values are plotted along the y-axis.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.byFeature({
features:ecoregions.select('[0-9][0-9]_tmean|label'),
xProperty:'label',
})
.setSeriesNames([
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct',
'Nov','Dec'
])
.setChartType('ColumnChart')
.setOptions({
title:'Average Monthly Temperature by Ecoregion',
hAxis:
{title:'Ecoregion',titleTextStyle:{italic:false,bold:true}},
vAxis:{
title:'Temperature (°C)',
titleTextStyle:{italic:false,bold:true}
},
colors:[
'604791','1d6b99','39a8a7','0f8755','76b349','f0af07',
'e37d05','cf513e','96356f','724173','9c4f97','696969'
]
});
print(chart);
```

### Bar chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_02.svg)
Features are plotted along the y-axis, labeled by values of a selected property. Series are represented by adjacent bars defined by a list of property names whose values are plotted along the x-axis.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.byFeature({
features:ecoregions.select('[0-9][0-9]_tmean|label'),
xProperty:'label',
})
.setSeriesNames([
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct',
'Nov','Dec'
])
.setChartType('BarChart')
.setOptions({
title:'Average Monthly Temperature by Ecoregion',
hAxis:{
title:'Temperature (°C)',
titleTextStyle:{italic:false,bold:true}
},
vAxis:
{title:'Ecoregion',titleTextStyle:{italic:false,bold:true}},
colors:[
'604791','1d6b99','39a8a7','0f8755','76b349','f0af07',
'e37d05','cf513e','96356f','724173','9c4f97','696969'
]
});
print(chart);
```

### Stacked column chart
#### Absolute
![](https://developers.google.com/static/earth-engine/images/Charts_feature_03.svg)
Features are plotted along the x-axis, labeled by values of a selected property. Series are represented by stacked columns defined by a list of property names whose values are plotted along the y-axis as the cumulative series sum.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.byFeature({
features:ecoregions.select('[0-9][0-9]_ppt|label'),
xProperty:'label'
})
.setSeriesNames([
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct',
'Nov','Dec'
])
.setChartType('ColumnChart')
.setOptions({
title:'Average Monthly Precipitation by Ecoregion',
hAxis:
{title:'Ecoregion',titleTextStyle:{italic:false,bold:true}},
vAxis:{
title:'Precipitation (mm)',
titleTextStyle:{italic:false,bold:true}
},
colors:[
'604791','1d6b99','39a8a7','0f8755','76b349','f0af07',
'e37d05','cf513e','96356f','724173','9c4f97','696969'
],
isStacked:'absolute'
});
print(chart);
```

#### Relative
![](https://developers.google.com/static/earth-engine/images/Charts_feature_04.svg)
Features are plotted along the x-axis, labeled by values of a selected property. Series are represented by stacked columns defined by a list of property names whose values are plotted along the y-axis as percent of the summed series.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.byFeature({
features:ecoregions.select('[0-9][0-9]_ppt|label'),
xProperty:'label'
})
.setSeriesNames([
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct',
'Nov','Dec'
])
.setChartType('ColumnChart')
.setOptions({
title:'Average Monthly Precipitation by Ecoregion',
hAxis:
{title:'Ecoregion',titleTextStyle:{italic:false,bold:true}},
vAxis:{
title:'Precipitation (mm)',
titleTextStyle:{italic:false,bold:true}
},
colors:[
'604791','1d6b99','39a8a7','0f8755','76b349','f0af07',
'e37d05','cf513e','96356f','724173','9c4f97','696969'
],
isStacked:'percent'
});
print(chart);
```

### Scatter chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_05.svg)
Features are plotted along the x-axis, labeled by values of a selected property. Series are represented by points defined by a list of property names whose values are plotted along the y-axis.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.byFeature({
features:ecoregions,
xProperty:'label',
yProperties:['01_tmean','07_tmean']
})
.setSeriesNames(['Jan','Jul'])
.setChartType('ScatterChart')
.setOptions({
title:'Average Monthly Temperature by Ecoregion',
hAxis:
{title:'Ecoregion',titleTextStyle:{italic:false,bold:true}},
vAxis:{
title:'Temperature (°C)',
titleTextStyle:{italic:false,bold:true}
},
pointSize:10,
colors:['1d6b99','cf513e'],
});
print(chart);
```

### Combo chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_06.svg)
Features are plotted along the x-axis, labeled by values of a selected property. Series are represented by points and columns defined by a list of property names whose values are plotted along the y-axis. This chart is achieved using [two axes](https://developers.google.com/chart/interactive/docs/gallery/columnchart#dual-y-charts) and series-specific styling.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.byFeature({
features:ecoregions,
xProperty:'label',
yProperties:['06_ppt','06_tmean']
})
.setSeriesNames(['Precipitation','Temperature'])
.setChartType('ColumnChart')
.setOptions({
title:'Average June Temperature and Precipitation by Ecoregion',
series:{
0:{targetAxisIndex:1,type:'bar',color:'1d6b99'},
1:{
targetAxisIndex:0,
type:'line',
lineWidth:0,
pointSize:10,
color:'e37d05'
}
},
hAxis:
{title:'Ecoregion',titleTextStyle:{italic:false,bold:true}},
vAxes:{
0:{
title:'Temperature (°C)',
baseline:0,
titleTextStyle:{italic:false,bold:true,color:'e37d05'}
},
1:{
title:'Precipitation (mm)',
titleTextStyle:{italic:false,bold:true,color:'1d6b99'}
},
},
bar:{groupWidth:'40%'},
});
print(chart);
```

## `ui.Chart.feature.byProperty`
### Example setup
The `ui.Chart.feature.byProperty` function accepts a dictionary that allows you to control the label and order of property names along the x-axis by assigning numerical values to them. The following cartesian grid charts use this option to set month labels and sort month names in chronological order for average monthly precipitation.
### Column chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_07.svg)
Feature properties are plotted along the x-axis, labeled and sorted by a dictionary input; the values of the given properties are plotted along the y-axis. Series are features, represented by columns, labeled by values of a selected property. To convert to a bar chart, use `.setChartType('BarChart')`.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define a dictionary that associates property names with values and labels.
varprecipInfo={
'01_ppt':{v:1,f:'Jan'},
'02_ppt':{v:2,f:'Feb'},
'03_ppt':{v:3,f:'Mar'},
'04_ppt':{v:4,f:'Apr'},
'05_ppt':{v:5,f:'May'},
'06_ppt':{v:6,f:'Jun'},
'07_ppt':{v:7,f:'Jul'},
'08_ppt':{v:8,f:'Aug'},
'09_ppt':{v:9,f:'Sep'},
'10_ppt':{v:10,f:'Oct'},
'11_ppt':{v:11,f:'Nov'},
'12_ppt':{v:12,f:'Dec'}
};
// Organize property information into objects for defining x properties and
// their tick labels.
varxPropValDict={};// Dictionary to codify x-axis property names as values.
varxPropLabels=[];// Holds dictionaries that label codified x-axis values.
for(varkeyinprecipInfo){
xPropValDict[key]=precipInfo[key].v;
xPropLabels.push(precipInfo[key]);
}
// Define the chart and print it to the console.
varchart=ui.Chart.feature
.byProperty({
features:ecoregions,
xProperties:xPropValDict,
seriesProperty:'label'
})
.setChartType('ColumnChart')
.setOptions({
title:'Average Ecoregion Precipitation by Month',
hAxis:{
title:'Month',
titleTextStyle:{italic:false,bold:true},
ticks:xPropLabels
},
vAxis:{
title:'Precipitation (mm)',
titleTextStyle:{italic:false,bold:true}
},
colors:['f0af07','0f8755','76b349'],
});
print(chart);
```

### Line chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_08.svg)
Feature properties are plotted along the x-axis, labeled and sorted by a dictionary input; the values of the given properties are plotted along the y-axis. Series are features, represented by lines, labeled by values of a selected property.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define a dictionary that associates property names with values and labels.
varprecipInfo={
'01_ppt':{v:1,f:'Jan'},
'02_ppt':{v:2,f:'Feb'},
'03_ppt':{v:3,f:'Mar'},
'04_ppt':{v:4,f:'Apr'},
'05_ppt':{v:5,f:'May'},
'06_ppt':{v:6,f:'Jun'},
'07_ppt':{v:7,f:'Jul'},
'08_ppt':{v:8,f:'Aug'},
'09_ppt':{v:9,f:'Sep'},
'10_ppt':{v:10,f:'Oct'},
'11_ppt':{v:11,f:'Nov'},
'12_ppt':{v:12,f:'Dec'}
};
// Organize property information into objects for defining x properties and
// their tick labels.
varxPropValDict={};// Dictionary to codify x-axis property names as values.
varxPropLabels=[];// Holds dictionaries that label codified x-axis values.
for(varkeyinprecipInfo){
xPropValDict[key]=precipInfo[key].v;
xPropLabels.push(precipInfo[key]);
}
// Define the chart and print it to the console.
varchart=ui.Chart.feature
.byProperty({
features:ecoregions,
xProperties:xPropValDict,
seriesProperty:'label'
})
.setChartType('ScatterChart')
.setOptions({
title:'Average Ecoregion Precipitation by Month',
hAxis:{
title:'Month',
titleTextStyle:{italic:false,bold:true},
ticks:xPropLabels
},
vAxis:{
title:'Precipitation (mm)',
titleTextStyle:{italic:false,bold:true}
},
colors:['f0af07','0f8755','76b349'],
lineSize:5,
pointSize:0
});
print(chart);
```

### Area chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_09.svg)
Feature properties are plotted along the x-axis, labeled and sorted by a dictionary input; the values of the given properties are plotted along the y-axis. Series are features, represented by lines and shaded areas, labeled by values of a selected property.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define a dictionary that associates property names with values and labels.
varprecipInfo={
'01_ppt':{v:1,f:'Jan'},
'02_ppt':{v:2,f:'Feb'},
'03_ppt':{v:3,f:'Mar'},
'04_ppt':{v:4,f:'Apr'},
'05_ppt':{v:5,f:'May'},
'06_ppt':{v:6,f:'Jun'},
'07_ppt':{v:7,f:'Jul'},
'08_ppt':{v:8,f:'Aug'},
'09_ppt':{v:9,f:'Sep'},
'10_ppt':{v:10,f:'Oct'},
'11_ppt':{v:11,f:'Nov'},
'12_ppt':{v:12,f:'Dec'}
};
// Organize property information into objects for defining x properties and
// their tick labels.
varxPropValDict={};// Dictionary to codify x-axis property names as values.
varxPropLabels=[];// Holds dictionaries that label codified x-axis values.
for(varkeyinprecipInfo){
xPropValDict[key]=precipInfo[key].v;
xPropLabels.push(precipInfo[key]);
}
// Define the chart and print it to the console.
varchart=ui.Chart.feature
.byProperty({
features:ecoregions,
xProperties:xPropValDict,
seriesProperty:'label'
})
.setChartType('AreaChart')
.setOptions({
title:'Average Ecoregion Precipitation by Month',
hAxis:{
title:'Month',
titleTextStyle:{italic:false,bold:true},
ticks:xPropLabels
},
vAxis:{
title:'Precipitation (mm)',
titleTextStyle:{italic:false,bold:true}
},
colors:['f0af07','0f8755','76b349'],
lineSize:5,
pointSize:0,
curveType:'function'
});
print(chart);
```

### Pie chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_10.svg)
The pie is a feature, each slice is a property label whose value is cast as a percentage of the sum of all values of properties composing the pie.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Subset the forest ecoregion feature and select the monthly precipitation
// properties, rename them as abbreviated months.
varthisForest=ecoregions.filter(ee.Filter.eq('label','Forest'))
.select(Object.keys(precipInfo),[
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
'Sep','Oct','Nov','Dec'
]);
// Define the chart and print it to the console.
varchart=ui.Chart.feature
.byProperty({
features:thisForest,
xProperties:[
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
'Sep','Oct','Nov','Dec'
]
})
.setChartType('PieChart')
.setOptions({
title:'Average Monthly Precipitation for Forest Ecoregion',
colors:[
'604791','1d6b99','39a8a7','0f8755','76b349','f0af07',
'e37d05','cf513e','96356f','724173','9c4f97','696969'
]
});
print(chart);
```

### Donut chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_11.svg)
Convert a pie chart to a donut chart by setting the [`pieHole`](https://developers.google.com/chart/interactive/docs/gallery/piechart#making-a-donut-chart) chart option; numbers between 0.4 and 0.6 will look best on most charts.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Subset the forest ecoregion feature and select the monthly precipitation
// properties, rename them as abbreviated months.
varthisForest=ecoregions.filter(ee.Filter.eq('label','Forest'))
.select(Object.keys(precipInfo),[
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
'Sep','Oct','Nov','Dec'
]);
// Define the chart and print it to the console.
varchart=ui.Chart.feature
.byProperty({
features:thisForest,
xProperties:[
'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
'Sep','Oct','Nov','Dec'
]
})
.setChartType('PieChart')
.setOptions({
title:'Average Monthly Precipitation for Forest Ecoregion',
colors:[
'604791','1d6b99','39a8a7','0f8755','76b349','f0af07',
'e37d05','cf513e','96356f','724173','9c4f97','696969'
],
pieHole:0.4,
});
print(chart);
```

## `ui.Chart.feature.groups`
### Column chart
![](https://developers.google.com/static/earth-engine/images/Charts_feature_12.svg)
Features are plotted along the x-axis, labeled by values of a selected property. Series are represented by columns defined by the set of unique values of a given property. Y-axis position is defined by a given property’s value. This plot can be changed to a scatter plot by setting the chart type as `'ScatterChart'` (`.setChartType('ScatterChart')`). Alternatively, if time is the x-axis variable, you might prefer to use a line chart: `.setChartType('LineChart')`.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Import the example feature collection.
varecoregions=ee.FeatureCollection('projects/google/charts_feature_example');
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.groups({
features:ecoregions,
xProperty:'label',
yProperty:'01_tmean',
seriesProperty:'warm'
})
.setSeriesNames(['Warm','Cold'])
.setChartType('ColumnChart')
.setOptions({
title:'Average January Temperature by Ecoregion',
hAxis:
{title:'Ecoregion',titleTextStyle:{italic:false,bold:true}},
vAxis:{
title:'Jan temp (°C)',
titleTextStyle:{italic:false,bold:true}
},
bar:{groupWidth:'80%'},
colors:['cf513e','1d6b99'],
isStacked:true
});
print(chart);
```

## `ui.Chart.feature.histogram`
![](https://developers.google.com/static/earth-engine/images/Charts_feature_13.svg)
The x-axis is defined by value bins for the range of values of a selected property; the y-axis is the number of elements in the given bin.
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/guides/charts_feature#code-editor-javascript-sample) More
```
// Load PRISM climate normals image collection; convert images to bands.
varnormClim=ee.ImageCollection('OREGONSTATE/PRISM/Norm81m').toBands();
// Make a point sample of climate variables for a region in western USA.
varregion=ee.Geometry.Rectangle(-123.41,40.43,-116.38,45.14);
varclimSamp=normClim.sample(region,5000);
// Define the chart and print it to the console.
varchart=
ui.Chart.feature
.histogram({features:climSamp,property:'07_ppt',maxBuckets:30})
.setOptions({
title:'July Precipitation Distribution for NW USA',
hAxis:{
title:'Precipitation (mm)',
titleTextStyle:{italic:false,bold:true}
},
vAxis:{
title:'Pixel count',
titleTextStyle:{italic:false,bold:true}
},
colors:['1d6b99'],
legend:{position:'none'}
});
print(chart);
```

