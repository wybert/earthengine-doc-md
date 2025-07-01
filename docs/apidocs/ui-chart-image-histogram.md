 
#  ui.Chart.image.histogram
Stay organized with collections  Save and categorize content based on your preferences. 
Generates a Chart from an image. Computes and plots histograms of the values of the bands in the specified region of the image. 
- X-axis: Histogram buckets (of band value).
- Y-axis: Frequency (number of pixels with a band value in the bucket).
Returns a chart.
Usage| Returns  
---|---  
`ui.Chart.image.histogram(image,  _region_, _scale_, _maxBuckets_, _minBucketWidth_, _maxRaw_, _maxPixels_)`| ui.Chart  
Argument| Type| Details  
---|---|---  
`image`| Image| The image to generate a histogram from.  
`region`| Feature|FeatureCollection|Geometry, optional| The region to reduce. If omitted, uses the entire image.  
`scale`| Number, optional| The pixel scale used when applying the histogram reducer, in meters.  
`maxBuckets`| Number, optional| The maximum number of buckets to use when building a histogram; will be rounded up to a power of 2.  
`minBucketWidth`| Number, optional| The minimum histogram bucket width, or null to allow any power of 2.  
`maxRaw`| Number, optional| The number of values to accumulate before building the initial histogram.  
`maxPixels`| Number, optional| If specified, overrides the maximum number of pixels allowed in the histogram reduction. Defaults to 1e6.  
## Examples
### Code Editor (JavaScript)
```
// Define a MODIS surface reflectance composite.
varmodisSr=ee.ImageCollection('MODIS/006/MOD09A1')
.filter(ee.Filter.date('2018-06-01','2018-09-01'))
.select(['sur_refl_b01','sur_refl_b02','sur_refl_b06'])
.mean();
// Define a region to calculate histogram for.
varhistRegion=ee.Geometry.Rectangle([-112.60,40.60,-111.18,41.22]);
// Define the chart and print it to the console.
varchart=
ui.Chart.image.histogram({image:modisSr,region:histRegion,scale:500})
.setSeriesNames(['Red','NIR','SWIR'])
.setOptions({
title:'MODIS SR Reflectance Histogram',
hAxis:{
title:'Reflectance (scaled by 1e4)',
titleTextStyle:{italic:false,bold:true},
},
vAxis:
{title:'Count',titleTextStyle:{italic:false,bold:true}},
colors:['cf513e','1d6b99','f0af07']
});
print(chart);
```

