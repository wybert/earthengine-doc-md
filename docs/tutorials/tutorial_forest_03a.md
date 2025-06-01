 
#  Charting Yearly Forest Loss 
Stay organized with collections  Save and categorize content based on your preferences. 
## Calculating Yearly Forest Loss
In the previous section you learned how to [calculate total forest area lost](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#calculating-pixel-areas) in the given region of interest using the `reduceRegion` method. Instead of calculating the total loss, it would be helpful to compute the loss for each year. The way to achieve this in Earth Engine is using a [Grouped Reducer](https://developers.google.com/earth-engine/guides/reducers_grouping).
To group output of `reduceRegion()`, you can specify a grouping band that defines groups by integer pixel values. In the following example, we slightly modify the previous code and add the `lossYear` band to the original image. Each pixel in the `lossYear` band contain values from 0 to 14 - indicating the year in which the loss occurred. We also change the reducer to a grouped reducer, specifying the band index of the grouping band (1) so the pixel areas will be summed and grouped according to the value in the `lossYear` band. 
### Code Editor (JavaScript)
```
// Load country boundaries from LSIB.
varcountries=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');
// Get a feature collection with just the Congo feature.
varcongo=countries.filter(ee.Filter.eq('country_co','CF'));
// Get the loss image.
// This dataset is updated yearly, so we get the latest version.
vargfc2017=ee.Image('UMD/hansen/global_forest_change_2017_v1_5');
varlossImage=gfc2017.select(['loss']);
varlossAreaImage=lossImage.multiply(ee.Image.pixelArea());
varlossYear=gfc2017.select(['lossyear']);
varlossByYear=lossAreaImage.addBands(lossYear).reduceRegion({
reducer:ee.Reducer.sum().group({
groupField:1
}),
geometry:congo,
scale:30,
maxPixels:1e9
});
print(lossByYear);
```

Once you run the above code, you will see the yearly forest loss area printed out in a nested list called `groups`. We can format the output a little to make the result a dictionary, with year as the key and loss area as the value. Notice that we are using the `format()` method to convert the year values from 0-14 to 2000-2014.
### Code Editor (JavaScript)
```
varstatsFormatted=ee.List(lossByYear.get('groups'))
.map(function(el){
vard=ee.Dictionary(el);
return[ee.Number(d.get('group')).format("20%02d"),d.get('sum')];
});
varstatsDictionary=ee.Dictionary(statsFormatted.flatten());
print(statsDictionary);
```

## Making a chart
Now that we have yearly loss numbers, we are ready to prepare a chart. We will use the `ui.Chart.array.values()` method. This method takes an array (or list) of input values and an array (or list) of labels for the X-axis. 
### Code Editor (JavaScript)
```
varchart=ui.Chart.array.values({
array:statsDictionary.values(),
axis:0,
xLabels:statsDictionary.keys()
}).setChartType('ColumnChart')
.setOptions({
title:'Yearly Forest Loss',
hAxis:{title:'Year',format:'####'},
vAxis:{title:'Area (square meters)'},
legend:{position:"none"},
lineWidth:1,
pointSize:3
});
print(chart);
```

The result should look like the chart below.
![Tutorial_Hansen_17_chart.png](https://developers.google.com/static/earth-engine/images/Tutorial_hansen_17_chart.png) Figure 1. Chart of Forest Loss by Year 
In the [next section](https://developers.google.com/earth-engine/tutorials/tutorial_forest_04), you'll learn about another deforestation monitoring dataset, [FORMA](https://www.cgdev.org/sites/default/files/1423248_file_Hammer_Kraft_Wheeler_FORMA_FINAL.pdf), and compare it to the Hansen et al. data.
