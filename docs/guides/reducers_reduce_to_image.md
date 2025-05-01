 
#  Vector to Raster Conversion 
Stay organized with collections  Save and categorize content based on your preferences. 
Vector to raster conversion in Earth Engine is handled by the `featureCollection.reduceToImage()` method. This method assigns pixels under each feature the value of the specified property. This example uses the counties data to create an image representing the land area of each county:
### Code Editor (JavaScript)
```
// Load a collection of US counties.
varcounties=ee.FeatureCollection('TIGER/2018/Counties');
// Make an image out of the land area attribute.
varlandAreaImg=counties
.filter(ee.Filter.notNull(['ALAND']))
.reduceToImage({
properties:['ALAND'],
reducer:ee.Reducer.first()
});
// Display the county land area image.
Map.setCenter(-99.976,40.38,5);
Map.addLayer(landAreaImg,{
min:3e8,
max:1.5e10,
palette:['FCFDBF','FDAE78','EE605E','B63679','711F81','2C105C']
});
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load a collection of US counties.
counties = ee.FeatureCollection('TIGER/2018/Counties')
# Make an image out of the land area attribute.
land_area_img = counties.filter(ee.Filter.notNull(['ALAND'])).reduceToImage(
  properties=['ALAND'], reducer=ee.Reducer.first()
)
# Display the county land area image.
m = geemap.Map()
m.set_center(-99.976, 40.38, 5)
m.add_layer(
  land_area_img,
  {
    'min': 3e8,
    'max': 1.5e10,
    'palette': ['FCFDBF', 'FDAE78', 'EE605E', 'B63679', '711F81', '2C105C'],
  },
)
m
```

Specify a reducer to indicate how to aggregate properties of overlapping features. In the previous example, since there is no overlap, an `ee.Reducer.first()` is sufficient. As in [this example](https://developers.google.com/earth-engine/guides/reducers_reduce_columns), pre-filter the data to eliminate nulls that can not be turned into an image. The output should look something like Figure 1, which maps a color gradient to county size. Like all image-outputting reducers in Earth Engine, the scale is dynamically set by the output. In this case, the scale corresponds to the zoom level in the Code Editor.
![reduceToImage output](https://developers.google.com/static/earth-engine/images/ReduceToImage_counties.png) Figure 1. The result of `reduceToImage()` using the ‘ALAND’ (land area) property of the 'TIGER/2018/Counties' `FeatureCollection`. 
