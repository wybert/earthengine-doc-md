 
#  ImageCollection Reductions
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Consider the example of needing to take the median over a time series of images represented by an `ImageCollection`. To reduce an `ImageCollection`, use `imageCollection.reduce()`. This reduces the collection of images to an individual image as illustrated in Figure 1. Specifically, the output is computed pixel-wise, such that each pixel in the output is composed of the median value of all the images in the collection at that location. To get other statistics, such as mean, sum, variance, an arbitrary percentile, etc., the appropriate reducer should be selected and applied. (See the **Docs** tab in the [Code Editor](https://code.earthengine.google.com) for a list of all the reducers currently available). For basic statistics like min, max, mean, etc., `ImageCollection` has shortcut methods like `min()`, `max()`, `mean()`, etc. They function in exactly the same way as calling `reduce()`, except the resultant band names will not have the name of the reducer appended.
![imageCollection.reduce diagram](https://developers.google.com/static/earth-engine/images/Reduce_ImageCollection.png) Figure 1. Illustration of an ee.Reducer applied to an ImageCollection. 
For an example of reducing an `ImageCollection`, consider a collection of Landsat 5 images, filtered by path and row. The following code uses `reduce()` to reduce the collection to one `Image` (here a median reducer is used simply for illustrative purposes):
### Code Editor (JavaScript)
```
// Load an image collection, filtered so it's not too much data.
varcollection=ee.ImageCollection('LANDSAT/LT05/C02/T1')
.filterDate('2008-01-01','2008-12-31')
.filter(ee.Filter.eq('WRS_PATH',44))
.filter(ee.Filter.eq('WRS_ROW',34));
// Compute the median in each band, each pixel.
// Band names are B1_median, B2_median, etc.
varmedian=collection.reduce(ee.Reducer.median());
// The output is an Image. Add it to the map.
varvis_param={bands:['B4_median','B3_median','B2_median'],gamma:1.6};
Map.setCenter(-122.3355,37.7924,9);
Map.addLayer(median,vis_param);
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Load an image collection, filtered so it's not too much data.
collection = (
  ee.ImageCollection('LANDSAT/LT05/C02/T1')
  .filterDate('2008-01-01', '2008-12-31')
  .filter(ee.Filter.eq('WRS_PATH', 44))
  .filter(ee.Filter.eq('WRS_ROW', 34))
)
# Compute the median in each band, each pixel.
# Band names are B1_median, B2_median, etc.
median = collection.reduce(ee.Reducer.median())
# The output is an Image. Add it to the map.
vis_param = {'bands': ['B4_median', 'B3_median', 'B2_median'], 'gamma': 1.6}
m = geemap.Map()
m.set_center(-122.3355, 37.7924, 9)
m.add_layer(median, vis_param)
m
```

This returns a multi-band `Image`, each pixel of which is the median of all unmasked pixels in the `ImageCollection` at that pixel location. Specifically, the reducer has been repeated for each band of the input imagery, meaning that the median is computed independently in each band. Note that the band names have the name of the reducer appended: `'B1_median'`, `'B2_median'`, etc. The output should look something like Figure 2.
For more information about reducing image collections, see the [reducing section of the `ImageCollection` docs](https://developers.google.com/earth-engine/guides/ic_reducing). In particular, note that images produced by reducing an `ImageCollection` [have no projection](https://developers.google.com/earth-engine/guides/ic_reducing#composites-have-no-projection). This means that you should explicitly set the scale on any computations involving computed images output by an `ImageCollection` reduction.
![ImageCollection.reduce output](https://developers.google.com/static/earth-engine/images/Reducer_ImageCollection_median.png) Figure 2. A false color composite of the median of Landsat 5 scenes in 2008. 
