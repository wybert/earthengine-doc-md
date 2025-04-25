 
#  DataTable Charts 
Stay organized with collections  Save and categorize content based on your preferences. 
The `ui.Chart` function renders charts from a client-side JSON object that follows the same structure as the Google Charts [`DataTable`](https://developers.google.com/chart/interactive/docs/reference#datatable-class), class, but lacks `DataTable` methods and mutability. It is essentially a 2-D table with rows that represent observations and columns that represent observation attributes. It provides a flexible, base interface to charting in Earth Engine. It is a good option when a high degree of chart customization is required.
## `DataTable` schema
There are two ways to define a pseudo-`DataTable` in Earth Engine: a JavaScript 2-D array and a JavaScript literal object. For most applications, constructing a 2-D array will be the simplest approach. In both cases, the table passed to `ui.Chart` must be a client-side object. A manually coded table will be inherently client-side, whereas a computed object will need to be transferred client-side using `evaluate`. Please see the [Client vs. Server](https://developers.google.com/earth-engine/guides/client_server) page for more information on the distinction between server-side and client-side objects.
### JavaScript array
A 2-D `DataTable` is composed of an array of rows and columns. Rows are observations and columns are attributes. The first column defines values for the x-axis, while additional columns define values for y-axis series. The first row is expected to be a column header. The simplest header is a series of column labels, demonstrated in the following array `DataTable` relating population by selected states.
```
vardataTable=[
['State','Population'],
['CA',37253956],
['NY',19378102],
['IL',12830632],
['MI',9883640],
['OR',3831074],
];
```

Optionally, columns can be designated to a role other than defining the domain (x-axis) and data (y-axis series) e.g. annotation, intervals, tooltips, or style. In the following example, the header array is presented as a series of objects, where the role of each column is explicitly defined. Acceptable column roles for each Google Chart type can be found in their respective documentation e.g. [Column Chart data format](https://developers.google.com/chart/interactive/docs/gallery/columnchart#data-format).
```
vardataTable=[
[{role:'domain'},{role:'data'},{role:'annotation'}],
['CA',37253956,'37.2e6'],
['NY',19378102,'19.3e6'],
['IL',12830632,'12.8e6'],
['MI',9883640,'9.8e6'],
['OR',3831074,'3.8e6'],
];
```

Column properties are specified as follows:
Parameter | Type | Definition  
---|---|---  
`type` | _string, recommended_ | Column data type: `'string'`, `'number'`, `'boolean'`, `'date'`, `'datetime'`, or `'timeofday'`.  
`label` | _string, recommended_ | A label for the column, series label in the chart legend.  
`role` | _string, recommended_ | A role for the column (e.g., [roles for Column Chart](https://developers.google.com/chart/interactive/docs/gallery/columnchart#data-format)).  
`pattern` | _string, optional_ | A number (or date) format string specifying how to display the column value.  
### JavaScript object
A `DataTable` can be formatted as a JavaScript literal object where arrays of row and column objects are provided. See this [guide](https://developers.google.com/chart/interactive/docs/reference#format-of-the-constructors-javascript-literal-data-parameter) for instructions on specifying column and row parameters.
```
vardataTable={
cols:[{id:'name',label:'State',type:'string'},
{id:'pop',label:'Population',type:'number'}],
rows:[{c:[{v:'CA'},{v:37253956}]},
{c:[{v:'NY'},{v:19378102}]},
{c:[{v:'IL'},{v:12830632}]},
{c:[{v:'MI'},{v:9883640}]},
{c:[{v:'OR'},{v:3831074}]}]
};
```

## Manual `DataTable` chart
![](https://developers.google.com/static/earth-engine/images/Charts_datatable_01.svg)
Suppose you have a small amount of static data you want to display to a chart. Use either the JavaScript [array](https://developers.google.com/earth-engine/guides/charts_datatable#javascript_array) or [object](https://developers.google.com/earth-engine/guides/charts_datatable#javascript_object) specifications to construct an input to pass to the `ui.Chart` function. Here, selected state populations from the U.S. 2010 census are encoded as a JavaScript array with column header objects that define column properties. Note that the third column is designated to the role of `'annotation'`, which adds the population as an annotation to each observation in the chart.
### Code Editor (JavaScript)
```
// Define a DataTable using a JavaScript array with a column property header.
vardataTable=[
[
{label:'State',role:'domain',type:'string'},
{label:'Population',role:'data',type:'number'},
{label:'Pop. annotation',role:'annotation',type:'string'}
],
['CA',37253956,'37.2e6'],
['NY',19378102,'19.3e6'],
['IL',12830632,'12.8e6'],
['MI',9883640,'9.8e6'],
['OR',3831074,'3.8e6']
];
// Define the chart and print it to the console.
varchart=ui.Chart(dataTable).setChartType('ColumnChart').setOptions({
title:'State Population (US census, 2010)',
legend:{position:'none'},
hAxis:{title:'State',titleTextStyle:{italic:false,bold:true}},
vAxis:{title:'Population',titleTextStyle:{italic:false,bold:true}},
colors:['1d6b99']
});
print(chart);
```

## Computed `DataTable` chart
A `DataTable` array can be created from a 2-D `ee.List` passed from the server to the client via `evaluate`. A common scenario is to convert properties of an `ee.FeatureCollection`, `ee.ImageCollection`, or element-wise reduction of these into a `DataTable`. The strategy applied in the following examples maps a function over an `ee.ImageCollection` that reduces the given element, assembles an `ee.List` from the reduction results, and attaches the list as a property called `'row'` to the returned element. Each element of the new collection has a 1-D `ee.List` that represents a row in a `DataTable`. The `aggregate_array()` function is used to aggregate all of the `'row'` properties into a parent `ee.List` to create a 2-D server-side `ee.List` in the shape required for `DataTable`. A custom column header is concatenated to the table and the result is transferred client-side with `evaluate`, where it is rendered using the `ui.Chart` function.
**Note:** charts printed from within an `evaluate` function will not immediately display the '_Generating chart..._ ' message in the console or `ui.Panel` widget. Wait patiently until the request has executed and the results have been transferred to the client.
### Time series by region
![](https://developers.google.com/static/earth-engine/images/Charts_datatable_02.svg)
This example shows a time series of MODIS-derived NDVI and EVI vegetation indices for a [forested ecoregion](https://developers.google.com/earth-engine/guides/charts_feature#compose-a-question). Each image in the series is reduced by the ecoregion and its results assembled as a `'row'` property that is aggregated into a `DataTable` for passing to the client and charting with `ui.Chart`. Note that this snippet produces the same chart generated by the [`ui.Chart.image.series` chart example](https://developers.google.com/earth-engine/guides/charts_image_collection#uichartimageseries).
### Code Editor (JavaScript)
```
// Import the example feature collection and subset the forest feature.
varforest=ee.FeatureCollection('projects/google/charts_feature_example')
.filter(ee.Filter.eq('label','Forest'));
// Load MODIS vegetation indices data and subset a decade of images.
varvegIndices=ee.ImageCollection('MODIS/061/MOD13A1')
.filter(ee.Filter.date('2010-01-01','2020-01-01'))
.select(['NDVI','EVI']);
// Define a function to format an image timestamp as a JavaScript Date string.
functionformatDate(img){
varmillis=img.date().millis().format();
returnee.String('Date(').cat(millis).cat(')');
}
// Build a feature collection where each feature has a property that represents
// a DataFrame row.
varreductionTable=vegIndices.map(function(img){
// Reduce the image to the mean of pixels intersecting the forest ecoregion.
varstat=img.reduceRegion(
{reducer:ee.Reducer.mean(),geometry:forest,scale:500});
// Extract the reduction results along with the image date.
vardate=formatDate(img);// x-axis values.
varevi=stat.get('EVI');// y-axis series 1 values.
varndvi=stat.get('NDVI');// y-axis series 2 values.
// Make a list of observation attributes to define a row in the DataTable.
varrow=ee.List([date,evi,ndvi]);
// Return the row as a property of an ee.Feature.
returnee.Feature(null,{'row':row});
});
// Aggregate the 'row' property from all features in the new feature collection
// to make a server-side 2-D list (DataTable).
vardataTableServer=reductionTable.aggregate_array('row');
// Define column names and properties for the DataTable. The order should
// correspond to the order in the construction of the 'row' property above.
varcolumnHeader=ee.List([[
{label:'Date',role:'domain',type:'date'},
{label:'EVI',role:'data',type:'number'},
{label:'NDVI',role:'data',type:'number'}
]]);
// Concatenate the column header to the table.
dataTableServer=columnHeader.cat(dataTableServer);
// Use 'evaluate' to transfer the server-side table to the client, define the
// chart and print it to the console.
dataTableServer.evaluate(function(dataTableClient){
varchart=ui.Chart(dataTableClient).setOptions({
title:'Average Vegetation Index Value by Date for Forest',
hAxis:{
title:'Date',
titleTextStyle:{italic:false,bold:true},
},
vAxis:{
title:'Vegetation index (x1e4)',
titleTextStyle:{italic:false,bold:true}
},
lineWidth:5,
colors:['e37d05','1d6b99'],
curveType:'function'
});
print(chart);
});
```

### Interval chart
![](https://developers.google.com/static/earth-engine/images/Charts_datatable_03.svg)
This chart takes advantage of the `DataTable` column `'role'` property to generate an [interval chart](https://developers.google.com/chart/interactive/docs/gallery/intervals). The chart relates the annual NDVI profile and inter-annual variance for a pixel near Monterey, CA. Inter-annual median is presented as a line, while the absolute and interquartile ranges are shown as bands. Table columns representing each interval are assigned as such by setting the `'role'` column property as `'interval'`. Bands are drawn around the median line by setting the `intervals.style` chart property as `'area'`.
### Code Editor (JavaScript)
```
// Define a point to extract an NDVI time series for.
vargeometry=ee.Geometry.Point([-121.679,36.479]);
// Define a band of interest (NDVI), import the MODIS vegetation index dataset,
// and select the band.
varband='NDVI';
varndviCol=ee.ImageCollection('MODIS/006/MOD13Q1').select(band);
// Map over the collection to add a day of year (doy) property to each image.
ndviCol=ndviCol.map(function(img){
vardoy=ee.Date(img.get('system:time_start')).getRelative('day','year');
// Add 8 to day of year number so that the doy label represents the middle of
// the 16-day MODIS NDVI composite.
returnimg.set('doy',ee.Number(doy).add(8));
});
// Join all coincident day of year observations into a set of image collections.
vardistinctDOY=ndviCol.filterDate('2013-01-01','2014-01-01');
varfilter=ee.Filter.equals({leftField:'doy',rightField:'doy'});
varjoin=ee.Join.saveAll('doy_matches');
varjoinCol=ee.ImageCollection(join.apply(distinctDOY,ndviCol,filter));
// Calculate the absolute range, interquartile range, and median for the set
// of images composing each coincident doy observation group. The result is
// an image collection with an image representative per unique doy observation
// with bands that describe the 0, 25, 50, 75, 100 percentiles for the set of
// coincident doy images.
varcomp=ee.ImageCollection(joinCol.map(function(img){
vardoyCol=ee.ImageCollection.fromImages(img.get('doy_matches'));
returndoyCol
.reduce(ee.Reducer.percentile(
[0,25,50,75,100],['p0','p25','p50','p75','p100']))
.set({'doy':img.get('doy')});
}));
// Extract the inter-annual NDVI doy percentile statistics for the
// point of interest per unique doy representative. The result is
// is a feature collection where each feature is a doy representative that
// contains a property (row) describing the respective inter-annual NDVI
// variance, formatted as a list of values.
varreductionTable=comp.map(function(img){
varstats=ee.Dictionary(img.reduceRegion(
{reducer:ee.Reducer.first(),geometry:geometry,scale:250}));
// Order the percentile reduction elements according to how you want columns
// in the DataTable arranged (x-axis values need to be first).
varrow=ee.List([
img.get('doy'),// x-axis, day of year.
stats.get(band+'_p50'),// y-axis, median.
stats.get(band+'_p0'),// y-axis, min interval.
stats.get(band+'_p25'),// y-axis, 1st quartile interval.
stats.get(band+'_p75'),// y-axis, 3rd quartile interval.
stats.get(band+'_p100')// y-axis, max interval.
]);
// Return the row as a property of an ee.Feature.
returnee.Feature(null,{row:row});
});
// Aggregate the 'row' properties to make a server-side 2-D array (DataTable).
vardataTableServer=reductionTable.aggregate_array('row');
// Define column names and properties for the DataTable. The order should
// correspond to the order in the construction of the 'row' property above.
varcolumnHeader=ee.List([[
{label:'Day of year',role:'domain'},
{label:'Median',role:'data'},
{label:'p0',role:'interval'},
{label:'p25',role:'interval'},
{label:'p75',role:'interval'},
{label:'p100',role:'interval'}
]]);
// Concatenate the column header to the table.
dataTableServer=columnHeader.cat(dataTableServer);
// Use 'evaluate' to transfer the server-side table to the client, define the
// chart and print it to the console.
dataTableServer.evaluate(function(dataTableClient){
varchart=ui.Chart(dataTableClient).setChartType('LineChart').setOptions({
title:'Annual NDVI Time Series with Inter-Annual Variance',
intervals:{style:'area'},
hAxis:{
title:'Day of year',
titleTextStyle:{italic:false,bold:true},
},
vAxis:{title:'NDVI (x1e4)',titleTextStyle:{italic:false,bold:true}},
colors:['0f8755'],
legend:{position:'none'}
});
print(chart);
});
```

There are many ways to represent intervals. In the following example, boxes are used instead of bands by changing the `intervals.style` property to `'boxes'` with respective box styling.
```
dataTableServer.evaluate(function(dataTableClient){
varchart=ui.Chart(dataTableClient).setChartType('LineChart').setOptions({
title:'Annual NDVI Time Series with Inter-Annual Variance',
**intervals:{style:'boxes',barWidth:1,boxWidth:1,lineWidth:0},**
hAxis:{
title:'Day of year',
titleTextStyle:{italic:false,bold:true},
},
vAxis:{title:'NDVI (x1e4)',titleTextStyle:{italic:false,bold:true}},
colors:['0f8755'],
legend:{position:'none'}
});
print(chart);
});
```

![](https://developers.google.com/static/earth-engine/images/Charts_datatable_04.svg)
