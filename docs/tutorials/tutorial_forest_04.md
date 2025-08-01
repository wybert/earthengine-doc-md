 
#  Introduction to Forest Monitoring for Action (FORMA) data
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
FORMA is a [MODIS](http://modis.gsfc.nasa.gov/about/) based 500 x 500 meter twice-monthly deforestation alerting system for the humid tropical forests. The [FORMA 500 dataset](https://developers.google.com/earth-engine/datasets/catalog/FORMA_FORMA_500m) in Earth Engine is an image with alerts starting in January 2006 and updated monthly. Each alert has a time associated with it in a single band named `alert_date` in units of [epoch seconds](https://en.wikipedia.org/wiki/Unix_time). Filtering FORMA by dates and calculating alerts within areas of interest are two of the most important things you can do with the FORMA dataset.
## Filtering FORMA by Date
To show just those alerts that occur in 2012, find pixels that have times between the first day of 2012 and the first day of 2013, expressed in seconds since midnight, January 1, 1970:
### Code Editor (JavaScript)
```
// Convert dates from milliseconds to seconds.
varstart=ee.Date('2012-01-01').millis().divide(1000);
varend=ee.Date('2013-01-01').millis().divide(1000);

// Load the FORMA 500 dataset.
varforma=ee.Image('FORMA/FORMA_500m');

// Create a binary layer from the dates of interest.
varforma2012=forma.gte(start).and(forma.lte(end));

Map.setCenter(15.87,-0.391,7);
Map.addLayer(
forma2012.mask(forma2012),
{palette:['FF0000']},
'FORMA alerts in 2012'
);
```

In this example, `forma2012` is a binary image containing only those pixels that have times occurring in 2012 (i.e. all other pixels are masked).
## Counting FORMA Alerts in a Region of Interest
[As we did in the previous section](https://developers.google.com/earth-engine/tutorials/tutorial_forest_03#quantifying-forest-change-in-an-area-of-interest) with the Hansen et al. data, we can start by counting the number of FORMA alerts (pixels) in an area of interest. For example, to count the number of alerts in protected areas of the Congo Republic in 2012, build on the previous example as follows:
### Code Editor (JavaScript)
```
// Load country features from Large Scale International Boundary (LSIB) dataset.
varcountries=ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017');

// Subset the Congo Republic feature from countries.
varcongo=ee.Feature(
countries
.filter(ee.Filter.eq('country_na','Rep of the Congo'))
.first()
);

// Subset protected areas to the bounds of the congo feature
// and other criteria. Clip to the intersection with congo.
varprotectedAreas=ee.FeatureCollection('WCMC/WDPA/current/polygons')
.filter(ee.Filter.and(
ee.Filter.bounds(congo.geometry()),
ee.Filter.neq('IUCN_CAT','VI'),
ee.Filter.neq('STATUS','proposed'),
ee.Filter.lt('STATUS_YR',2010)
))
.map(function(feat){
returncongo.intersection(feat);
});

// Display protected areas on the map.
Map.addLayer(
protectedAreas,
{color:'000000'},
'Congo Republic protected areas'
);

// Calculate the number of FORMA pixels in protected
// areas of the Congo Republic, 2012.
varstats=forma2012.reduceRegion({
reducer:ee.Reducer.sum(),
geometry:protectedAreas.geometry(),
scale:500
});
print('Number of FORMA pixels, 2012: ',stats.get('constant'));
```

## Counting FORMA Alerts in Several Regions of Interest
So far, we've been computing statistics in a single region at a time. For computing statistics in multiple regions at once, you can use [`reduceRegions()`](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregions). Again building on the previous example:
### Code Editor (JavaScript)
```
varregionsStats=forma2012.reduceRegions({
collection:protectedAreas,
reducer:ee.Reducer.sum(),
scale:forma2012.projection().nominalScale()
});
print(regionsStats);
```

Examine the object printed to the console and observe that the output of `reduceRegions()` is another `FeatureCollection`. Note that every region in the collection of the Congo Republic protected areas now has an additional property, `sum`, named after the reducer. The value of this property is the output of the reducer, or the number of 2012 alerts in the protected areas.
## Comparing FORMA and Hansen et al. Datasets
To compare the FORMA and Hansen et al. datasets, you can use logical operators. ([Learn more about logical operations](https://developers.google.com/earth-engine/guides/image_relational)). Specifically, we'd like to make an image in which pixels marked by both FORMA and the Hansen et al. data as deforestation are 1 and the rest are zero. This code makes such an image for 2012 and displays it along with other predicted deforestation layers:
### Code Editor (JavaScript)
```
// Convert dates from milliseconds to seconds.
varstart=ee.Date('2012-01-01').millis().divide(1000);
varend=ee.Date('2013-01-01').millis().divide(1000);
varregion=ee.Geometry.Rectangle([-59.81163,-9.43348,-59.27561,-9.22818]);

// Load the FORMA 500 dataset.
varforma=ee.Image('FORMA/FORMA_500m');

// Create a binary layer from the dates of interest.
varforma2012=forma.gte(start).and(forma.lte(end));

// Load Hansen et al. data and get change in 2012.
vargfc=ee.Image('UMD/hansen/global_forest_change_2015');
vargfc12=gfc.select(['lossyear']).eq(12);

// Create an image which is one where the datasets
// both show deforestation and zero elsewhere.
vargfc_forma=gfc12.eq(1).and(forma2012.eq(1));

// Display data on the map.
Map.setCenter(-59.58813,-9.36439,11);
Map.addLayer(forma.updateMask(forma),{palette:'00FF00'},'Forma (green)');
Map.addLayer(gfc12.updateMask(gfc12),{palette:'FF0000'},'Hansen (red)');
Map.addLayer(
gfc_forma.updateMask(gfc_forma),
{palette:'FFFF00'},
'Hansen & FORMA (yellow)'
);
```

This concludes the overview of forest change datasets in Earth Engine. We're looking forward to seeing what you can do with them!
