 
#  Spatiotemporal Statistics of Vegetation Indices 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
[ Edit on GitHub ](https://github.com/google/earthengine-community/edit/master/tutorials/spatiotemporal-image-statistics/index.md "Contribute to this article on GitHub.")
[ Report issue ](https://github.com/google/earthengine-community/issues/new?title=Issue%20with%20tutorials/spatiotemporal-image-statistics/index.md&body=Issue%20Description "Report an issue with this article on GitHub.")
[ Page history ](https://github.com/google/earthengine-community/commits/master/tutorials/spatiotemporal-image-statistics/index.md "View changes to this article over time.")
Author(s): [ saumyatas ](https://github.com/saumyatas "View the profile for saumyatas on GitHub")
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
This tutorial demonstrates how to create a comma delimited table of zonal statistics of vegetation indices (NDVI or EVI) over a study area, for a given range of years. 
## Import datasets
### Vegetation index
Google Earth Engine has a range data products that provide time series of vegetation indices. Here, we use the MODIS [Terra Vegetation Indices for 16-days Global 250m](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD13Q1) product (also available at 500m and 1km resolution). After importing, we select the 'EVI' band.
```
vardataset=ee.ImageCollection('MODIS/006/MOD13Q1')
.select('EVI');// or 'NDVI'

```

### Region of interest
A FeatureCollection (or Geometry) is needed to define regions to summarize vegetation index data over. For example, you can use the [Global Administrative Unit Layers (GAUL) dataset](https://developers.google.com/earth-engine/datasets/catalog/FAO_GAUL_2015_level2?hl=en), to extract zonal statistics for administrative regions. The GAUL provides administrative unit boundaries for all countries in the world at three levels. Here, we'll use the districts of Maharashtra, India; we'll get zonal statistics for each district (35 districts).
```
varregions=ee.FeatureCollection('FAO/GAUL/2015/level2')
.filter(ee.Filter.inList('ADM1_NAME',['Maharashtra']));

```

Alternatively, you can select a different FeatureCollection from the [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets) or upload your own ShapeFile by following the instructions in the [Importing Table Data](https://developers.google.com/earth-engine/guides/table_upload) section of the Earth Engine Developer's Guide.
## Defining spatiotemporal reduction parameters
The statistics we're after include spatial and temporal components. Above, we've defined the bounds of the spatial component, now we define the temporal component, i.e. the series of time windows to generate representative composite vegetation index images for. The following variables set the length a time window and the duration of the series.
The variables are set to generate zonal statistics (`spatialReducers`) for image composites constructed from three time periods (`intervalCount`) that start on 2018-01-01 (`startDate`) with each time window being 1 (`interval`) year (`intervalUnit`) reduced by mean (`temporalReducer`). In other words, we'll be generating annual mean vegetation index zonal statistics for years 2018, 2019, and 2020.
```
varstartDate='2018-01-01';// time period of interest beginning date
varinterval=1;// time window length
varintervalUnit='year';// unit of time e.g. 'year', 'month', 'day'
varintervalCount=3;// number of time windows in the series
vartemporalReducer=ee.Reducer.mean();// how to reduce images in time window
// Defines mean, standard deviation, and variance as the zonal statistics.
varspatialReducers=ee.Reducer.mean().combine({
reducer2:ee.Reducer.stdDev(),
sharedInputs:true
}).combine({
reducer2:ee.Reducer.variance(),
sharedInputs:true
});

```

## Calculating spatiotemporal statistics
Now, we'll calculate spatiotemporal vegetation index statistics. Two ways to arrange the statistics table are provided: a long table and a wide table. Depending on your application, one arrangement might be more suitable than the other. The resulting tables are [exported to Google Drive](https://developers.google.com/earth-engine/guides/exporting#to-drive) as a CSV file, but there are multiple [other ways to export](https://developers.google.com/earth-engine/guides/exporting#exporting-tables-and-vector-data), including downloading the CSV file directly using [`getDownloadURL`](https://developers.google.com/earth-engine/apidocs/ee-featurecollection-getdownloadurl).
### Long table
The long table format will have one row per unique combination of region and time window. So in this example, there will be 105 rows (35 districts * 3 time windows). First, a list of 0-based time window indices is constructed, then we map over the time window index list to generate composite images for each time window, and then apply `reduceRegions` to calculate the zonal statistics per region. Finally, the start date of the time window is added as a feature property so the statistics can be tied to a given image composite. The result is a FeatureCollection of FeatureCollections, which must be flattened. The flattened FeatureCollection is then exported to Google Drive as a CSV file.
```
// Get time window index sequence.
varintervals=ee.List.sequence(0,intervalCount-1,interval);
// Map reductions over index sequence to calculate statistics for each interval.
varzonalStatsL=intervals.map(function(i){
// Calculate temporal composite.
varstartRangeL=ee.Date(startDate).advance(i,intervalUnit);
varendRangeL=startRangeL.advance(interval,intervalUnit);
vartemporalStat=dataset.filterDate(startRangeL,endRangeL)
.reduce(temporalReducer);
// Calculate zonal statistics.
varstatsL=temporalStat.reduceRegions({
collection:regions,
reducer:spatialReducers,
scale:dataset.first().projection().nominalScale(),
crs:dataset.first().projection()
});
// Set start date as a feature property.
returnstatsL.map(function(feature){
returnfeature.set({
composite_start:startRangeL.format('YYYY'),// or 'YYYY-MM-dd'
});
});
});
zonalStatsL=ee.FeatureCollection(zonalStatsL).flatten();
print('Spatiotemporal statistics (long)',zonalStatsL);
Export.table.toDrive({
collection:zonalStatsL,
description:'zonal_stats_long',
});

```

### Wide table
The wide table will have one row for each region (35 rows in this case) with a column per unique combination of statistic and time window. The new column names are the concatenation of the statistic and the time window separated by an underscore. The process uses a client-side for loop on the number of time windows, and for each one, zonal statistics are calculated and appended as new properties to the FeatureCollection. An alternative approach is to use Earth Engine's `iterate` function, but a comparison of the approaches' performance was equal, so we've chosen the for loop for improved readability.
```
vartemporalStatW;// defined dynamically for each temporal image composite
varstartRangeW;// defined dynamically for each temporal image composite
varreduce=function(feature){
// Calculate zonal statistics.
varstatsW=temporalStatW.reduceRegion({
reducer:spatialReducers,
geometry:feature.geometry(),
scale:dataset.first().projection().nominalScale(),
crs:dataset.first().projection()
});
// Append date to the statistic label.
varkeys=ee.Dictionary(statsW).keys();
varnewKeys=keys.map(function(key){
returnee.String(key).cat('_')
.cat(startRangeW.format('YYYY'));// or 'YYYY-MM-dd'
});
// Add the statistic properties to the feature.
returnfeature.set(statsW.rename(keys,newKeys));
};
varzonalStatsW=regions;// make a copy of the regions FeatureCollection
// Loop through sequence of intervals to calculate statistics for each.
for(vari=0;i < intervalCount;i++){
varstartRangeW=ee.Date(startDate).advance(i,intervalUnit);
varendRangeW=startRangeW.advance(interval,intervalUnit);
temporalStatW=dataset.filterDate(startRangeW,endRangeW).mean()
.reduce(temporalReducer);
zonalStatsW=zonalStatsW.map(reduce);
}
print('Spatiotemporal statistics (wide)',zonalStatsW);
Export.table.toDrive({
collection:zonalStatsW,
description:'zonal_stats_wide',
});

```

